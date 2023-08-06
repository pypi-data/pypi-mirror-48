#ifndef NOS_FPRINT_SPEC_H
#define NOS_FPRINT_SPEC_H

#include <igris/util/numconvert.h>

namespace nos
{
	enum class alignment
	{
		left, right, center
	};

	enum class text_case
	{
		upper, lower, none
	};

	struct basic_spec
	{
		alignment align = alignment::left;
		text_case tcase = text_case::none;
		int width = 0;
		char fill = ' ';

		char* analyze(char* ptr)
		{
			if (isdigit(*ptr))
			{
				width = atou32(ptr, 10, &ptr);
				return ptr;
			}

			switch (*ptr)
			{
				case '<':
					align = alignment::left;
					break;

				case '>':
					align = alignment::right;
					break;

				case '^':
					align = alignment::center;
					break;

				case 'f':
					fill = *++ptr;
					break;
			}
			return ++ptr;
		}
	};

	struct integer_spec : public basic_spec
	{
		integer_spec(igris::buffer opts) 
		{
			char* ptr = opts.begin();
			char* end = opts.end();
			while(ptr != end)
			{
				ptr = analyze(ptr);
			}
		}
	};

	struct float_spec : public basic_spec
	{
		float_spec(igris::buffer opts) 
		{
			char* ptr = opts.begin();
			char* end = opts.end();
			while(ptr != end)
			{
				ptr = analyze(ptr);
			}
		}
	};

	struct text_spec : public basic_spec
	{
		text_spec(igris::buffer opts) 
		{
			char* ptr = opts.begin();
			char* end = opts.end();
			while(ptr != end)
			{
				ptr = analyze(ptr);
			}
		}
	};
}

#endif