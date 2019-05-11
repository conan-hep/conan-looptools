#include <iostream>
#include "clooptools.h"

int main()
{
   ltini();
   std::cout << B0(1000., 50., 80.) << std::endl;
   ltexi();

   return 0;
}
