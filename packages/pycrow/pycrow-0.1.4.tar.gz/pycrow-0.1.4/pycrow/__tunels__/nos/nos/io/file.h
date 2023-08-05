#ifndef NOS_IO_FSTREAM_H
#define NOS_IO_FSTREAM_H

#include <nos/io/iostream.h>

namespace nos {

	class file : public nos::iostream
	{
	private:
		FILE* filp;

	public:
		file(FILE* f) : filp(f) {}
		file() : filp(nullptr) {}
		file(const char * path, const char * mode) 
		{
			open(path, mode);
		}

		ssize_t write(const void* ptr, size_t sz) override
		{
			return fwrite(ptr, sizeof(char), sz, filp);
		}

		ssize_t read(void* ptr, size_t sz) override
		{
			return fread(ptr, sizeof(char), sz, filp);
		}

		bool good() { return filp != nullptr; }

		int open(const char * path, const char * mode) 
		{
			filp = fopen(path, mode);
			return 0;
		}

		virtual int flush()
		{
			return fflush(filp);
		}
	};

}

#endif