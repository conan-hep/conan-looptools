      program test_looptools
      implicit none

#include "looptools.h"

      call ltini
      print *, B0(1000D0, 50D0, 80D0)

      call ltexi
      end program test_looptools
