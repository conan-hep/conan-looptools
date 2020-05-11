#include <stdio.h>
#include "clooptools.h"

int main()
{
   ltini();

   ComplexType b0 = B0(1000., 50., 80.);
   ComplexType c0 = C0(0., 1., 3., 10., 20., 30.);

   printf("%e + %e*I\n", Re(b0), Im(b0));
   printf("%e + %e*I\n", Re(c0), Im(c0));

   ltexi();

   return 0;
}
