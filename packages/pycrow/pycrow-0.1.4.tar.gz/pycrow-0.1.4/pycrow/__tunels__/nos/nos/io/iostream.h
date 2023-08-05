#ifndef NOS_IO_IOSTREAM_H
#define NOS_IO_IOSTREAM_H

#include <nos/io/ostream.h>
#include <nos/io/istream.h>

namespace nos {
	class iostream : public ostream, public istream {};
}

#endif