# sample_project for esp

# Usage
## cd esp_sample_project

## git submodule update --init --recursive

## cd esp-idf, ./install.xxx esp32c3, ./export.xxx

## cd /bsp/project

## mkdir build && cd build 

## cmake ../../.. -G Ninja 

## ninja menuconfig

## ninja 

## ninja flash

# config

## According to the esp chip used, set the variable “IDF_TARGFET” in the root CMakeLists.txt to your chip, also some header file in project in "include_directories" need to update.
