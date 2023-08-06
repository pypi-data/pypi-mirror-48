#include <nos/print/print.h>
#include <nos/io/ostream.h>

ssize_t nos::putchar_to(nos::ostream& o, char c)
{
	return o.write(&c, 1);
}

ssize_t nos::write_to(nos::ostream& out, const void* buf, size_t sz)
{
	return out.write(buf, sz);
}

ssize_t nos::writeln_to(nos::ostream& out, const void* buf, size_t sz)
{
	ssize_t ret = 0;
	ret += out.write(buf, sz);
	ret += out.println();
	return ret;
}

ssize_t nos::println_to(nos::ostream& o)
{
	return o.write("\r\n", 2);
}

ssize_t nos::println()
{
	return nos::current_ostream->write("\r\n", 2);
}

ssize_t nos::print_dump_to(nos::ostream& out, const void *mem, size_t len, unsigned int columns)
{
	size_t ret = 0;
	unsigned int i, j;

	for (i = 0; i < len + ((len % columns) ? (columns - len % columns) : 0); i++)
	{
		// print offset
		if (i % columns == 0)
		{
			ret += out.write("0x", 2);
			ret += out.printptr((void*)((char*)mem + i));
			ret += out.putchar(':');
		}

		// print hex data
		if (i < len)
		{
			ret += out.printhex(((char*)mem)[i]);
			ret += out.putchar(' ');
		}
		else
		{
			// end of block, just aligning for ASCII dump
			ret += out.write("   ", 3);
		}

		// print ASCII dump
		if (i % columns == (columns - 1))
		{
			for (j = i - (columns - 1); j <= i; j++)
			{
				if (j >= len)
				{
					// end of block, not really printing
					ret += out.putchar(' ');
				}
				else if (isprint(((char*)mem)[j]))
				{
					// printable char
					ret += out.putchar((char)0xFF & ((char*)mem)[j]);
				}
				else
				{
					// other char
					ret += out.putchar('.');
				}
			}

			ret += out.println();
		}
	}

	return ret;
}

ssize_t nos::print_dump(const void* ptr, size_t sz, unsigned int columns)
{
	return nos::print_dump_to(*nos::current_ostream, ptr, sz, columns);
}

ssize_t nos::print_dump(igris::buffer buf, unsigned int columns)
{
	return nos::print_dump_to(*nos::current_ostream, buf.data(), buf.size(), columns);
}

ssize_t nos::putchar(char c)
{
	return putchar_to(*nos::current_ostream, c);
}

ssize_t nos::write(const void* buf, size_t sz)
{
	return nos::write_to(*nos::current_ostream, buf, sz);
}

ssize_t nos::writeln(const void* buf, size_t sz)
{
	return nos::writeln_to(*nos::current_ostream, buf, sz);
}
