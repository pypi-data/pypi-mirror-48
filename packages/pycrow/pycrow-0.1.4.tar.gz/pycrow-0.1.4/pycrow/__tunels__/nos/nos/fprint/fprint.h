#ifndef NOS_FPRINT_FPRINT_H
#define NOS_FPRINT_FPRINT_H

#include <utility>
#include <nos/fprint/visitor.h>
#include <nos/print/print.h>
#include <nos/io/string_writer.h>

#include <igris/util/numconvert.h>

namespace nos
{
	ssize_t fprint_impl(nos::ostream& out, const char* fmt, const visitable_arglist& args);

	template<typename ... Args>
	ssize_t fprint_to(nos::ostream& out, const char* fmt, const Args& ... args)
	{
		return fprint_impl(out, fmt,
		    visitable_arglist ({ 
		    	visitable_argument(args, 
		    	nos::format_visitor()) 
		    	... 
		    })
		);
	}

	template<typename ... Args>
	ssize_t fprint(const char* fmt, const Args& ... args)
	{
		return nos::fprint_to(*current_ostream, fmt,  args ...);
	}

	template<typename ... Args>
	ssize_t fprintln(const Args& ... args)
	{
		size_t ret = 0;
		ret += fprint_to(*current_ostream, args ...);
		ret += println();
		return ret;
	}

	template<typename ... Args>
	ssize_t fprintln_to(nos::ostream& out, const Args& ... args)
	{
		size_t ret = 0;
		ret += fprint_to(out, args ...);
		ret += println();
		return ret;
	}

	ssize_t fprint(const char* arg);

	ssize_t fprintln(const char* arg);

	ssize_t fprint_to(nos::ostream& out, const char* arg);

	ssize_t fprintln_to(nos::ostream& out, const char* arg);

	template<typename ... Args>
	std::string format(const char* fmt, const Args& ... args)
	{
		std::string ret;
		nos::string_writer writer(ret);
		nos::fprint_to(writer, fmt, args ...);
		return ret;
	}
}

#endif