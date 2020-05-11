      program test_looptools
      implicit none

#include "looptools.h"

      call ltini
      print *, B0(1000D0, 50D0, 80D0)
      print *, C0(0D0, 1D0, 3D0, 10D0, 20D0, 30D0)
      print *, C0i(cc0, 0D0, 1D0, 3D0, 10D0, 20D0, 30D0)

      call ltexi
      end program test_looptools
