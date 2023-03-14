# sample_project for esp

# Usage
## add submodule espidf to root dir (/)

## cd esp-idf, install.xxx target, export.xxx

## cd /bsp/project

## mkdir build && cd build 

## cmake ../../.. -G Ninja 

## ninja 

## ninja flash

# config

## According to the esp chip used, set the variable “IDF_TARGFET” in the root CMakeLists.txt to your chip, also some header file in project in "include_directories" need to update;
