CMAKE_MINIMUM_REQUIRED(VERSION 3.0)
PROJECT(byteat)
ADD_EXECUTABLE(byteat byteat.c)
INSTALL(TARGETS byteat DESTINATION bin)
