#include <stdio.h>
int main(void)
{
	int j,k,p,q,m,n,l,o;
	m=2;
	n=m;
	j=n++;
	k=+n;
	l+=n;
	//o++=n;
	p=m--;
	q=--m;
	printf("m=2,n=2\nj=n++ %d \nk=+n %d\np=m-- %d\nq=--m %d\nl+=n %d",j,k,p,q,l);

	return 0;
}