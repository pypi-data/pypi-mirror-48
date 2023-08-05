#include <nos/fprint/stdtype.h>
#include <nos/fprint/spec.h>

ssize_t nos_fprint(nos::ostream& os, const char* text, int size, const nos::basic_spec& spec)
{
	int ret = 0;

	int pre_fill_len = 0;
	char post_fill_len = 0;

	int difflen = spec.width - size;

	if (difflen > 0)
	{
		switch (spec.align)
		{
			case nos::alignment::left:
				post_fill_len = difflen;
				break;

			case nos::alignment::right:
				pre_fill_len = difflen;
				break;

			case nos::alignment::center:
				pre_fill_len = difflen / 2;
				post_fill_len = difflen / 2;

				if (difflen % 2) pre_fill_len++;

				break;
		}
	}

	if (pre_fill_len)
	{
		ret += os.fill(spec.fill, pre_fill_len);
	}


	if (spec.tcase == nos::text_case::upper)
	{
		ret += os.write_lower(text, size);
	}
	else if (spec.tcase == nos::text_case::lower)
	{
		ret += os.write_upper(text, size);
	} 
	else
	{
		ret += os.write(text, size);
	}

	if (post_fill_len)
	{
		ret += os.fill(spec.fill, post_fill_len);
	}

	return ret;
}

ssize_t nos_fprint_integer_impl(nos::ostream& os, char* buf, size_t len, const nos::integer_spec& spec) {
	return nos_fprint(os, buf, len, spec);
}

ssize_t nos_fprint(nos::ostream& os, const char* text, const nos::basic_spec& spec) 
{
	return nos_fprint(os, text, strlen(text), spec);
}

ssize_t nos_fprint(nos::ostream& os, const char* obj, igris::buffer opts)
{
	nos::text_spec spec(opts);
	return nos_fprint(os, obj, strlen(obj), spec);
}

ssize_t nos_fprint(nos::ostream& os, bool obj, igris::buffer opts) 
{
	return nos_fprint(os, obj ? "true" : "false", opts);
}

ssize_t nos_fprint(nos::ostream& os, int8_t obj, igris::buffer opts) { return nos_fprint(os, (int32_t)obj, opts); }
ssize_t nos_fprint(nos::ostream& os, int16_t obj, igris::buffer opts) { return nos_fprint(os, (int32_t)obj, opts); }
ssize_t nos_fprint(nos::ostream& os, int32_t obj, igris::buffer opts) 
{
	nos::integer_spec spec(opts);
	char buf[32];
	char * end = i32toa(obj, buf, 10);
	return nos_fprint_integer_impl(os, buf, end - buf, spec);
}

ssize_t nos_fprint(nos::ostream& os, int64_t obj, igris::buffer opts)
{
	nos::integer_spec spec(opts);
	char buf[64];
	char * end = i64toa(obj, buf, 10);
	return nos_fprint_integer_impl(os, buf, end - buf, spec);
}

ssize_t nos_fprint(nos::ostream& os, uint8_t obj, igris::buffer opts) { return nos_fprint(os, (uint32_t)obj, opts); }
ssize_t nos_fprint(nos::ostream& os, uint16_t obj, igris::buffer opts) { return nos_fprint(os, (uint32_t)obj, opts); }
ssize_t nos_fprint(nos::ostream& os, uint32_t obj, igris::buffer opts)
{
	nos::integer_spec spec(opts);
	char buf[32];
	char * end = u32toa(obj, buf, 10);
	return nos_fprint_integer_impl(os, buf, end - buf, spec);
}

ssize_t nos_fprint(nos::ostream& os, uint64_t obj, igris::buffer opts)
{
	nos::integer_spec spec(opts);
	char buf[64];
	char * end = u64toa(obj, buf, 10);
	return nos_fprint_integer_impl(os, buf, end - buf, spec);
}