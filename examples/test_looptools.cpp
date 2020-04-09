#include <iostream>
#include "clooptools.h"

int main()
{
   ltini();
   std::cout << B0(1000., 50., 80.) << std::endl;
   std::cout << C0(0., 1., 3., 10., 20., 30.) << std::endl;
   ltexi();

   return 0;
}
