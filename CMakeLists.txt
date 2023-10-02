set(CMAKE_CXX_STANDARD 14) #setting C++ 14 standard

project(SingleFrameDetector_dm)

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}" ${CMAKE_MODULE_PATH})
find_package(PkgConfig) #finding pkg-config is a helper tool
# link opencv
find_package(Threads)
find_package(OpenCV REQUIRED)
find_package(CUDA REQUIRED)


#find_package(TensorRT REQUIRED)

#include_directories(${OpenCV_INCLUDE_DIRS})
#include_directories(
#   onnxruntime/include
#)
#link_directories(/media/sd/objectDetection/onnxruntime_jetson_single_object/onnxruntime/lib)

add_executable(${PROJECT_NAME} main.cpp )


# set(PROJECT_LINK_LIBS
# /media/sd/objectDetection/onnxruntime_jetson_single_object/onnxruntime/lib/libjetson-inference.so
# /media/sd/objectDetection/onnxruntime_jetson_single_object/onnxruntime/lib/libjetson-utils.so
# )
#target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS}  ${PROJECT_LINK_LIBS} )


target_include_directories(${PROJECT_NAME} PUBLIC 
${OpenCV_INCLUDE_DIRS} ${CUDA_INCLUDE_DIRS} 
#${TensorRT_INCLUDE_DIRS}
#/usr/include/aarch64-linux-gnu 
/home/ek/install/TensorRT-8.4.1.5/include
)
target_link_libraries( ${PROJECT_NAME} PUBLIC 
${OpenCV_LIBS} ${CUDA_LIBRARIES} ${CMAKE_THREAD_LIBS_INIT} 
#${TensorRT_LIBRARIES}
#/usr/lib/aarch64-linux-gnu
/home/ek/install/TensorRT-8.4.1.5/lib
)