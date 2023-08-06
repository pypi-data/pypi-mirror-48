#ifndef GXX_IO_OBUFFER_H
#define GXX_IO_OBUFFER_H

#include <nos/io/iostream.h>

namespace nos {
		class ostorage : public nos::ostream {
		public:
			virtual int room() = 0;
			//virtual void set_empty_callback(nos::delegate<void> dlg) {};
		};

		class istorage : public nos::istream {
		public:
			virtual int avail() = 0;
		};

		class iostorage : public nos::ostorage, public nos::istorage {}; 
}

#endif