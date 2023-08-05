#ifndef GXX_ARGLIST2_H
#define GXX_ARGLIST2_H

//Структура данных visitable_arglist используется для форматирующей печати.
//Для обработки строки формата все аргументы однотипно записываются с помощью указателей,
//указатели их обработчиков также сохраняются, тем самым осуществляя сохранение типа.
//За подбор обработчиков отвечает класс визитёр (Visitor). Он же ответственен за вызов.
//Таким образом visitable_arglist - это средство разграничения во времени многоаргументного
//вызова и его исполнения.

#include <memory>
#include <utility>
#include <assert.h>
#include <igris/buffer.h>
#include <igris/util/bug.h>

namespace nos
{
	namespace detail
	{
		template<typename T> struct va_remove_cvref
		{
			typedef typename std::remove_volatile <
			typename std::remove_const <
			typename std::remove_reference<T>
			::type >::type >::type type;
		};
		template<typename T> using va_remove_cvref_t = typename va_remove_cvref<T>::type;
	}

	/**
	 *	Класс именованного аргумента.
	 *  Является шаблонным классом, чтобы доставить информацию о типе аргумента
	 *  в конструктор visitable_argument.
	 */
	template<typename T>
	struct argpair
	{
		void* body;
		igris::buffer name;
		constexpr argpair(const igris::buffer& _name, const T& _body) : body((void*)&_body), name(_name) {}
	};

	/**
	 *	Класс имени аргумента, используется как временный объект,
	 *  порождающий объект именованного аргумента argpair. 
	 */
	struct argname
	{
		igris::buffer name;
		constexpr argname(const igris::buffer& _name) : name(_name) {};

		template<typename T>
		constexpr argpair<T> operator= (const T& body)
		{
			return argpair<T>(name, body);
		}
	};

	namespace argument_literal
	{
		static inline argname operator"" _a (const char* name, size_t sz)
		{
			return argname(igris::buffer(name, sz));
		}
	}

	/**
	 *	visitable_argument
	 *	Хранит данные об указатели, имени и точке доступа к визитёру.
	 *	Используется для хранения в упорядоченном массиве информации об аргументах функции.
	 */
	struct visitable_argument
	{
		void* 		ptr;
		igris::buffer name;
		void* 		visit;

		visitable_argument(void* _ptr, const igris::buffer& buf, void* _visit) : 
			ptr(_ptr), name(buf), visit(_visit) {}

		template <typename Visitor, typename Object>
		visitable_argument(const Object& obj, const Visitor& visitor)
			: visitable_argument(
			      (void*) & obj,
			      igris::buffer(),
			      Visitor::template get_visit<detail::va_remove_cvref_t<Object>>())
		{(void)visitor;}

		template <typename Visitor, typename Object>
		visitable_argument(const argpair<Object>& pair, const Visitor& visitor)
			: visitable_argument(
			      pair.body,
			      pair.name,
			      Visitor::template get_visit<detail::va_remove_cvref_t<Object>>())
		{}
	};

	/**
	 *	visitable_arglist
	 *	Предоставляет интерфейс доступа к массиву visitable_argument.
	 *
	 *  @buffer - буфер данных, передаваемый извне для нужд хранения. Должен иметь длину
	 * 	не менее количества аргуметов.
	 */
	class visitable_arglist
	{
		size_t N;
		visitable_argument* arr;

	public:
		visitable_arglist() : N(0), arr(nullptr) {}

		template<size_t M>
		visitable_arglist(visitable_argument(&& arr)[M]) 
			: N(M), arr(arr) 
		{}

		visitable_argument* begin()
		{
			return arr;
		}

		visitable_argument* end()
		{
			return arr + N;
		}

		const visitable_argument& operator[](size_t num) const
		{
			assert(num < N);
			return arr[num];
		}

		const visitable_argument& operator[](igris::buffer str) const
		{
			for (uint8_t i = 0; i < N; ++i)
			{
				if (str == arr[i].name) return arr[i];
			}

			dpr("nos::visitable_arglist: name error: ");
			dprln("on name: "); debug_write(str.data(), str.size()); dprln();
			
			return arr[0]; // -Wreturn-type
		}
	};
}

#endif
