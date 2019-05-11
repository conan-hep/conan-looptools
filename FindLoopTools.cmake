find_library(LoopTools_LIBRARY NAMES ${CONAN_LIBS_LOOPTOOLS} PATHS ${CONAN_LIB_DIRS_LOOPTOOLS})
find_path(LoopTools_INCLUDE_DIRS NAMES looptools.h PATHS ${CONAN_INCLUDE_DIRS_LOOPTOOLS})

set(LoopTools_FOUND TRUE)
set(LoopTools_INCLUDE_DIRS ${LoopTools_INCLUDE_DIR})
set(LoopTools_LIBRARIES ${LoopTools_LIBRARY})
mark_as_advanced(LoopTools_LIBRARY LoopTools_INCLUDE_DIR)

if(LoopTools_FOUND AND NOT TARGET LoopTools::LoopTools)
  add_library(LoopTools::LoopTools UNKNOWN IMPORTED)
  set_target_properties(LoopTools::LoopTools PROPERTIES
    IMPORTED_LOCATION "${LoopTools_LIBRARIES}"
    INTERFACE_INCLUDE_DIRECTORIES "${LoopTools_INCLUDE_DIRS}"
  )
endif()
