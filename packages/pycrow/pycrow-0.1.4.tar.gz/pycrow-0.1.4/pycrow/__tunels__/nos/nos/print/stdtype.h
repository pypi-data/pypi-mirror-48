#ifndef NOS_PRINT_STDTYPE_H
#define NOS_PRINT_STDTYPE_H

#include <stdlib.h>
#include <stdint.h>
#include <igris/buffer.h>
#include <igris/util/types_extension.h>

#include <string>

namespace nos { class ostream; }

ssize_t nos_print(nos::ostream& out, const char* str);
ssize_t nos_print(nos::ostream& out, bool str);

ssize_t nos_print(nos::ostream& out, int8_t str);
ssize_t nos_print(nos::ostream& out, int16_t str);
ssize_t nos_print(nos::ostream& out, int32_t str);
ssize_t nos_print(nos::ostream& out, int64_t str);

ssize_t nos_print(nos::ostream& out, uint8_t str);
ssize_t nos_print(nos::ostream& out, uint16_t str);
ssize_t nos_print(nos::ostream& out, uint32_t str);
ssize_t nos_print(nos::ostream& out, uint64_t str);

ssize_t nos_print(nos::ostream& out, float str);
ssize_t nos_print(nos::ostream& out, double str);

ssize_t nos_print(nos::ostream& out, igris::buffer buf);

static inline
ssize_t nos_print(nos::ostream& out, const std::string& str) 
{
	return nos_print(out, igris::buffer(str));
}

#include <nos/print.h>
#include <vector>
#include <array>
#include <list>

namespace nos
{
	template <> struct print_implementation<const char *>
	{
		static ssize_t print_to(nos::ostream& out, const char* const obj)
		{
			return nos_print(out, obj);
		}
	};

	template <typename T> struct print_implementation<T*>
	{
		static ssize_t print_to(nos::ostream& out, const T* obj)
		{
			return nos::printptr_to(out, obj);
		}
	};

	template <typename T> struct print_implementation<std::vector<T>>
	{
		static ssize_t print_to(nos::ostream& out, const std::vector<T>& obj)
		{
			return nos::print_list_to<std::vector<T>>(out, obj);
		}
	};

	template <typename T> struct print_implementation<std::list<T>>
	{
		static ssize_t print_to(nos::ostream& out, const std::list<T>& obj)
		{
			return nos::print_list_to<std::list<T>>(out, obj);
		}
	};

	template <typename T, size_t M> struct print_implementation<std::array<T,M>>
	{
		static ssize_t print_to(nos::ostream& out, const std::array<T,M>& obj)
		{
			return nos::print_list_to<std::array<T,M>>(out, obj);
		}
	};
}

#endif