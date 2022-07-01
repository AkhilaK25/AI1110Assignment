#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"
double variance(char *s)
{
return (sqrmean(s)-mean(s)*mean(s));
}

int  main(void) //main function begins
{
printf("mean of X = %lf\n",mean("gau.dat"));
printf("variance of X = %lf\n",variance("gau.dat"));
return 0;
}
