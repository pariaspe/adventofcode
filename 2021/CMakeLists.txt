cmake_minimum_required(VERSION 3.5.0)
project(AOC VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Werror")

set(SOURCE_FILES
    1/src/main.cpp
    2/src/main.cpp
    3/src/main.cpp
    4/src/main.cpp
    5/src/main.cpp
    6/src/main.cpp
)

foreach(sourcefile ${SOURCE_FILES})
    string( REPLACE "/src/main.cpp" "" test ${sourcefile} )
    string( REPLACE "/" "-" execname ${test} )

    add_executable(${execname} ${sourcefile})
endforeach(sourcefile ${SOURCE_FILES})

