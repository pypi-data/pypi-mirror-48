#ifndef nos_INETADDR_H
#define nos_INETADDR_H

#include <ctype.h>
#include <nos/print.h>
#include <nos/util/string.h>

namespace nos {
	class hostaddr {
	public:
		uint32_t addr;
		hostaddr() : addr(0) {}
		hostaddr(uint32_t addr_) : addr(addr_) {}
		
		hostaddr(const char* str) {
			if (isdigit(*str)) {
				nos::strvec nums = nos::split(str, '.');
				addr =
					atoi(nums[0].c_str()) << 24 |
					atoi(nums[1].c_str()) << 16 |
					atoi(nums[2].c_str()) << 8 |
					atoi(nums[3].c_str());
			}
		}

		hostaddr(const std::string& str) : hostaddr(str.c_str()) {}

		size_t print_to(nos::ostream& o) const {
			return o.printhex(addr);
		}

		size_t fprint_to(nos::ostream& o, nos::buffer opts) const {
			return o.printhex(addr);
		}
		
		bool operator == (const hostaddr& oth) const {
			return oth.addr == addr;
		}
	};

	namespace inet {
		static constexpr const char* localhost = "127.0.0.1"; 
		using hostaddr = nos::hostaddr;

		struct netaddr {
			hostaddr addr;
			int32_t port;
			netaddr(uint32_t addr_, uint16_t port_) 
				: addr(addr_), port(port_) {}

			netaddr(nos::inet::hostaddr addr_, uint16_t port_) 
				: addr(addr_), port(port_) {}

			netaddr() = default;
			
			ssize_t print_to(nos::ostream& o) const {
				return nos::fprint_to(o, "(h:{},p:{})", addr, port);
			}

			bool operator==(const netaddr& oth) const {
				return oth.addr == addr && oth.port == port;
			}
		};
	}
}

namespace std {
	template<> 
	class hash<nos::inet::hostaddr> {
	public:
		size_t operator()(const nos::inet::hostaddr &s) const {
			return std::hash<int32_t>()(s.addr);
		}
	};

	template<> 
	class hash<nos::inet::netaddr> {
	public:
		size_t operator()(const nos::inet::netaddr &s) const {
			size_t h1 = std::hash<nos::inet::hostaddr>()(s.addr);
			size_t h2 = std::hash<int32_t>()(s.port);
			return h1 ^ ( h2 << 1 );
		}
	};
}

#endif
