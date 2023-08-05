#include <nos/io/stdfile.h>
#include <nos/util/init_priority.h>

namespace nos {
	nos::file NOS_PRIORITY_INITIALIZATION_SUPER cout(stdout);
	nos::file NOS_PRIORITY_INITIALIZATION_SUPER cerr(stderr);
	nos::file NOS_PRIORITY_INITIALIZATION_SUPER cin(stdin);
}
