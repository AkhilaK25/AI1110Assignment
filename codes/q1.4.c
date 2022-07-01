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
printf("mean of U = %lf\n",mean("uni.dat"));
printf("variance of U = %lf\n",variance("uni.dat"));
return 0;
}

