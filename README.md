# sample_project for esp32

# Usage
## if you're ubuntu user must do this, if you're windows user, skip this step
sudo apt-get install git wget flex bison gperf python3 python3-venv python3-setuptools cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0

## git clone https://github.com/DarryZh/esp_sample_project

## cd esp_sample_project

## git submodule update --init

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
