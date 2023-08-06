#ifndef nos_DATAGRAMM_SOCKET_H
#define nos_DATAGRAMM_SOCKET_H

#include <nos/inet/socket.h>
#include <nos/print.h>

#include <unistd.h>
#include <fcntl.h>

#ifndef __WIN64__
#	include <netinet/in.h>
#	include <netinet/tcp.h>
#	include <arpa/inet.h>
#endif
//#include <errno.h>

namespace nos { 
	namespace inet {
		struct datagramm_socket : public inet::socket {
			datagramm_socket(int domain, int type, int proto);
			ssize_t sendto(nos::inet::hostaddr haddr, uint16_t port, const char* data, size_t size);
			ssize_t ne_sendto(uint32_t addr, uint16_t port, const char* data, size_t size);
			ssize_t recvfrom(char* data, size_t maxsize, nos::inet::netaddr* inaddr);
		};
	
		struct udp_socket : public datagramm_socket {
			udp_socket();
			udp_socket(nos::inet::hostaddr addr, uint16_t port);
			int bind(nos::inet::hostaddr addr, uint16_t port);
		};

		struct rdm_socket : public datagramm_socket {
			rdm_socket();
			rdm_socket(nos::inet::hostaddr addr, uint16_t port);
		};
	}
}

#endif
