cmake_minimum_required(VERSION 3.5 FATAL_ERROR)

project(googletest-download NONE)

include(ExternalProject)

ExternalProject_Add(
        googletest
        SOURCE_DIR "/Users/akhvorov/code/mlimlab/vgram/vgram/cmake-build-debug/core/src/test/cpp/googletest/googletest-src"
        BINARY_DIR "/Users/akhvorov/code/mlimlab/vgram/vgram/cmake-build-debug/core/src/test/cpp/googletest/googletest-build"
        GIT_REPOSITORY
        https://github.com/google/googletest.git
        GIT_TAG
        release-1.8.0
        CONFIGURE_COMMAND ""
        BUILD_COMMAND ""
        INSTALL_COMMAND ""
        TEST_COMMAND ""
)
