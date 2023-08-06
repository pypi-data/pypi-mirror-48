#ifndef NOS_IO_SOCKET2_H
#define NOS_IO_SOCKET2_H

#include <nos/inet/hostaddr.h>
#include <string.h>

namespace nos { 
	namespace inet {
		struct socket {
			int fd;

			bool good() {
				return fd >= 0;
			}

			socket() = default;
			socket(const socket& oth) = default;
			socket(socket&& oth) = default;
			socket& operator=(const socket& oth) = default;
			socket& operator=(socket&& oth) = default;

			ssize_t send(const void* data, size_t size, int flags);
			ssize_t recv(char* data, size_t size, int flags);

			int init(int domain, int type, int proto); //posix ::socket
			int bind(const hostaddr& haddr, uint16_t port, int family);
			int connect(const hostaddr& haddr, uint16_t port, int family);
			int clean();
			int listen(int conn);

			int nodelay(bool en);
			int nonblock(bool en);
			int reusing(bool en);
			
			int close();
		};
	}
}

#endif
