#ifndef NOS_IO_STD_ADAPTER_H
#define NOS_IO_STD_ADAPTER_H

namespace nos {

	template <class C>
	class streambuf_adapter : public std::basic_streambuf<C>
	{
	private:
		typedef typename std::basic_streambuf<C>::int_type int_type;
		typedef typename std::basic_streambuf<C>::traits_type traits_type;
	
		nos::ostream& out;
	
	public:
		adapterbuf(nos::ostream& _out) : out(_out) {}
	
	protected:
		int_type overflow(int_type ch = traits_type::eof()) override
		{
			if (!traits_type::eq_int_type(ch, traits_type::eof()))
				out.putchar(ch);
			return ch;
		}
	
		std::streamsize xsputn(const C *s, std::streamsize count) override
		{
			out.write(s, count);
			return count;
		}
	};

}

#endif