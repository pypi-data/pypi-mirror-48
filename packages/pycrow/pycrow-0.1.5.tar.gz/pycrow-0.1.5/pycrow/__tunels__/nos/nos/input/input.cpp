#include <nos/input.h>
#include <nos/io/istream.h>

int nos::read_until(nos::istream& is, char* buf, size_t buflen, char delim)
{
	char c;
	int count = 0;
	char* last = buf + buflen - 1;

	while (buf != last)
	{
		int readed = is.read(&c, 1);

		if (readed < 0) 
		{
			return readed;
		}

		if (readed == 0)
		{
			*buf = 0;
			return count;
		}

		if (c == delim)
		{
			*buf = 0;
			return count;
		}

		*buf++ = c;
		count++;
	}

	*buf = 0;
	return count;
}


int nos::read_paired(nos::istream& is, char* buf, size_t buflen, char a, char b, bool ignore)
{
	char c;
	int count = 0;
	char* last = buf + buflen - 1;

	int paircount = 0;

	if (ignore) 
		do {
			int ret = is.read(&c, 1);
			if (ret <= 0) return ret;
		} while(c != a);
	else {
		is.read(&c, 1);
		if (c != a) return -1;
	} 


	paircount = 1;
	*buf++ = c;
	count++;

	while (paircount != 0 && buf != last)
	{
		int readed = is.read(&c, 1);

		if (readed <= 0)
		{
			*buf = 0;
			return count;
		}

		if (c == a) 
		{
			++paircount;
		}

		if (c == b)
		{
			if (--paircount == 0) 
			{
				*buf++ = c;
				count++;
				*buf = 0;
				return count;
			}
		}

		*buf++ = c;
		count++;
	}

	*buf = 0;
	return count;
}