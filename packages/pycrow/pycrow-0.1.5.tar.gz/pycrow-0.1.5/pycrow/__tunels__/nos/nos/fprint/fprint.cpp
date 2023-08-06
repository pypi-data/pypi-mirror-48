#include <nos/print.h>
#include <nos/io/ostream.h>

#include <nos/util/arglist.h>
#include <nos/fprint/visitor.h>

namespace nos
{
	ssize_t fprint(const char* arg)
	{
		return print(arg);
	}

	ssize_t fprintln(const char* arg)
	{
		return println(arg);
	}

	ssize_t fprint_to(nos::ostream& out, const char* arg)
	{
		return print_to(out, arg);
	}

	ssize_t fprintln_to(nos::ostream& out, const char* arg)
	{
		return println_to(out, arg);
	}

	static ssize_t fprint_format_argument(nos::ostream& out, const char*& fmt, const nos::visitable_arglist& list, uint8_t argnum)
	{
		ssize_t ret;
		char* pend;
		assert(*fmt == '{');
		fmt++;

		const visitable_argument* varg = nullptr;

		if (isalpha(*fmt))
		{
			const char* count_ptr = fmt;
			int len = 0;

			while (isalpha(*count_ptr++)) len++;

			varg = &list[igris::buffer(fmt, len)];
		}
		else if (isdigit(*fmt))
		{
			varg = &list[atou32(fmt, 10, &pend)];
		}
		else
		{
			varg = &list[argnum];
		}

		while (*fmt != '}' && *fmt != ':' && *fmt != 0) fmt++;

		switch (*fmt)
		{
			case '}':
				ret = nos::format_visitor::visit(*varg, out, igris::buffer());
				break;

			case ':':
				++fmt;
				ret = nos::format_visitor::visit(*varg, out, igris::buffer(fmt, strchr(fmt, '}') - fmt));
				break;

			case 0	:
				return -1;

			default:
				dprln("nos::format_error");
				return -1;
		}

		while (*fmt != '}' && *fmt != 0) fmt++;

		fmt++;
		return ret;
	}

	ssize_t fprint_impl(nos::ostream& out, const char* fmt, const visitable_arglist& args)
	{
		uint8_t argnum = 0;
		const char* fmtptr = fmt;
		ssize_t ret = 0;

		while (*fmtptr != 0)
		{
			if (*fmtptr == '{')
			{
				ret += fprint_format_argument(out, fmtptr, args, argnum);
				argnum++;
			}
			else
			{
				auto strttxt = fmtptr;

				while (*fmtptr != 0 && *fmtptr != '{') fmtptr++;

				ret += out.write(strttxt, fmtptr - strttxt);
			}
		}

		return ret;
	}
}