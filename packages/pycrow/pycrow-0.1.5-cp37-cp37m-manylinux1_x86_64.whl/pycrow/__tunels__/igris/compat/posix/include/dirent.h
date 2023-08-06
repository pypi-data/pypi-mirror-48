/**
 *
 * @date 23.11.2012
 * @author Alexander Kalmuk
 */

#ifndef DIRENT_H_
#define DIRENT_H_

#include <sys/types.h>
#include <sys/cdefs.h>

__BEGIN_DECLS

#define DIRENT_DNAME_LEN 40

struct dirent {
	ino_t  d_ino;                    /* File serial number. */
	char   d_name[DIRENT_DNAME_LEN]; /* Name of entry. */

	/*only for linux compatible */
	off_t          d_off;       /* not an offset; see NOTES */
	unsigned short d_reclen;    /* length of this record */
	unsigned char  d_type;      /* type of file; not supported
	                            by all filesystem types */
};

typedef struct DIR_struct DIR;


extern int            closedir(DIR *);

extern DIR           *opendir(const char *);

extern struct dirent *readdir(DIR *);

extern int            readdir_r(DIR *, struct dirent *, struct dirent **);

extern void           rewinddir(DIR *dirp);

__END_DECLS

#endif /* DIRENT_H_ */
