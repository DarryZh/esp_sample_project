# sample_project for esp32

# Usage
## cd esp_sample_project

## git submodule init

## git submodule update --recursice

## cd esp-idf

## if you're windows user, do .\install.bat esp32c3. else if you're linux user, do ./install.sh esp32c3

## if you're windows user, do .\export.bat. else if you're linux user, do . ./export.sh

## cd ../bsp/project

## mkdir build && cd build 

## cmake ../../.. -G Ninja 

## ninja menuconfig

## ninja 

## ninja flash

# config

## According to the esp chip used, set the variable “IDF_TARGFET” in the root CMakeLists.txt to your chip, also some header file in project in "include_directories" need to update.
