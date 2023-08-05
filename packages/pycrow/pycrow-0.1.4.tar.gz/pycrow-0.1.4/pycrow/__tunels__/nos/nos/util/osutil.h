#ifndef nos_OSUTIL_FDOPS_H
#define nos_OSUTIL_FDOPS_H

namespace nos {
	namespace osutil {
		int nonblock(int fd, bool en);
		int nodelay(int fd, bool en);
	}
}

#endif