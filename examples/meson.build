project('test_meson', 'cpp')

dep_libgfortran = meson.get_compiler('cpp').find_library('gfortran')

executable('test_meson', ['test_looptools.cpp'],
           dependencies: [dependency('LoopTools'), dep_libgfortran])
