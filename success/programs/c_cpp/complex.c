// C program to show the working
// of complex.h library

#include <complex.h>
#include <stdio.h>

int main(void)
{
	double real = 1.3,
	       imag = 4.9;
	double complex z
	    = CMPLX(real, imag);
	printf(
	    "z = %.1f%+.1fi\n",
	    creal(z), cimag(z));
}

