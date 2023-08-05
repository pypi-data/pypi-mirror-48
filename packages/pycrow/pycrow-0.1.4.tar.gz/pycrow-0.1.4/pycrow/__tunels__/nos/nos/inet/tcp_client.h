#ifndef NOS_INET_TCPCLIENT_H
#define NOS_INET_TCPCLIENT_H

#include <nos/io/iostream.h>
#include <nos/inet/socket.h>
#include <stdio.h>

#include <netinet/in.h>
#include <netinet/tcp.h>
#include <arpa/inet.h>


namespace nos
{
	namespace inet
	{
		struct tcp_client : public nos::inet::socket, public nos::iostream
		{
			hostaddr addr;
			int port;

			bool connected;

			tcp_client(const hostaddr& addr, int port) : addr(addr), port(port) {}

			bool is_connected() { return connected; }
			bool is_disconnected() { return !connected; }

			int connect() 
			{
				socket::init(AF_INET, SOCK_STREAM, IPPROTO_TCP);
				return socket::connect(addr, port, PF_INET);
			}

			int disconnect() 
			{
				return socket::close();
			}

			ssize_t write(const void* data, size_t size) override 
			{
				int ret = socket::send(data, size, 0);
				if (ret == -1) connected = false;
				return ret;
			}

			ssize_t read(void* data, size_t size) override 
			{
				int ret = socket::recv((char*)data, size, 0);
				if (ret == -1) connected = false;
				return ret;
			}
		};
	}
}

#endif
