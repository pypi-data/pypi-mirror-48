#include <nos/util/osutil.h>

#ifndef _MSC_VER
#include <unistd.h>
#include <fcntl.h>

int nos::osutil::nonblock(int fd, bool en) {
   if (fd < 0) return -1;
   int flags = fcntl(fd, F_GETFL, 0);
   if (flags < 0) return -1;
   flags = en ? (flags|O_NONBLOCK) : (flags&~O_NONBLOCK);
   return fcntl(fd, F_SETFL, flags) == 0;
}
#endif