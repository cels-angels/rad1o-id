INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_RAD1O_ID rad1o_id)

FIND_PATH(
    RAD1O_ID_INCLUDE_DIRS
    NAMES rad1o_id/api.h
    HINTS $ENV{RAD1O_ID_DIR}/include
        ${PC_RAD1O_ID_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    RAD1O_ID_LIBRARIES
    NAMES gnuradio-rad1o_id
    HINTS $ENV{RAD1O_ID_DIR}/lib
        ${PC_RAD1O_ID_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(RAD1O_ID DEFAULT_MSG RAD1O_ID_LIBRARIES RAD1O_ID_INCLUDE_DIRS)
MARK_AS_ADVANCED(RAD1O_ID_LIBRARIES RAD1O_ID_INCLUDE_DIRS)

