#ifndef NOS_IO_ISTREAM_H
#define NOS_IO_ISTREAM_H

#include <nos/input.h>
#include <stdlib.h>
#include <string>

#include <igris/util/types_extension.h>

namespace nos
{
	class istream
	{
	public:

		std::string readline();/*
		{
			std::string ret;
			char c;

			while (1)
			{
				read(&c, 1);
				switch (c)
				{
					case '\r': break;
					case '\n': return ret;
					default: ret += c;
				}
			}
		}*/

		int ignore() { char c; int readed = read(&c,1); return readed; }
		int ignore(int i) { int j = i; while(j--) ignore(); return i; }

		int read_until(char* buf, size_t buflen, char delim) 
		{
			return nos::read_until(*this, buf, buflen, delim);
		}

		int read_paired(char* buf, size_t buflen, char a, char b, bool ignore=true) 
		{
			return nos::read_paired(*this, buf, buflen, a, b, ignore);
		}

		virtual ssize_t read(void* ptr, size_t sz) = 0;
	};
}

#endif