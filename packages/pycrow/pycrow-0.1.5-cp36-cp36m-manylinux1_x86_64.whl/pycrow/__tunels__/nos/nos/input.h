#ifndef NOS_INPUT_H
#define NOS_INPUT_H

#include <string>
#include <stdlib.h>

namespace nos 
{
	class istream;
	extern istream* current_istream;

	std::string readline();	
	int read_until(nos::istream& is, char* buf, size_t buflen, char delim);
	int read_paired(nos::istream& is, char* buf, size_t buflen, char a, char b, bool ignore=true);
}

#include <nos/io/istream.h>

namespace nos
{
	std::string readline();/*
	{
		return current_istream->readline();
	}*/

}

#endif