#ifndef nos_INET_TCP_SERVER_H
#define nos_INET_TCP_SERVER_H

#include <nos/inet/tcp_socket.h>

namespace nos {
	namespace inet {
		struct tcp_server : public inet::socket {
			tcp_server() = default;

			//tcp_server(int port);
			tcp_server(const nos::inet::hostaddr& addr, uint16_t port, int conn = 10);
            //void listen(int port, int conn = 10);

            int init();
			int bind(const nos::hostaddr& addr, uint16_t port);
            int listen();
            int listen(int conn);

            inet::tcp_socket accept();
		};
	}
}

#endif
