
#include <stdio.h>
#include <string.h>

int main(int ac, char **av)
{
	unsigned char buf[] = 0;
	int (*func)();
	func = (int(*)())buf;
	(int)(*func)();
}
