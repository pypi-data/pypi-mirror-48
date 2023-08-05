#ifndef NOS_FPRINT_STDTYPE_H
#define NOS_FPRINT_STDTYPE_H

#include <igris/buffer.h>
#include <igris/util/types_extension.h>

namespace nos { class ostream; }

ssize_t nos_fprint(nos::ostream& os, const char* obj, igris::buffer opts);

ssize_t nos_fprint(nos::ostream& os, bool obj, igris::buffer opts);

ssize_t nos_fprint(nos::ostream& os, int8_t obj, igris::buffer opts);
ssize_t nos_fprint(nos::ostream& os, int16_t obj, igris::buffer opts);
ssize_t nos_fprint(nos::ostream& os, int32_t obj, igris::buffer opts);
ssize_t nos_fprint(nos::ostream& os, int64_t obj, igris::buffer opts);

ssize_t nos_fprint(nos::ostream& os, uint8_t obj, igris::buffer opts);
ssize_t nos_fprint(nos::ostream& os, uint16_t obj, igris::buffer opts);
ssize_t nos_fprint(nos::ostream& os, uint32_t obj, igris::buffer opts);
ssize_t nos_fprint(nos::ostream& os, uint64_t obj, igris::buffer opts);

#include <nos/io/ostream.h>

	/*template <> struct fprint_implementation<const char*>
	{
		static ssize_t fprint_to(const char* obj, nos::ostream& out, igris::buffer opts)
		{
			(void) opts;
			return out.write(obj, strlen(obj));
		}
	};

	template <> struct fprint_implementation<int>
	{
		static ssize_t fprint_to(const int& obj, nos::ostream& out, igris::buffer opts)
		{	
			(void) opts;
			return out.print(obj);
		}
	};*/

#endif