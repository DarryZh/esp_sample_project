cmake_minimum_required(VERSION 3.16)

aux_source_directory(. SRC_LIST)

add_library(app_main STATIC ${SRC_LIST})
# add_dependencies(app_main idf::cxx idf::newlib idf::freertos idf::esp_hw_support idf::heap idf::log idf::soc idf::hal idf::esp_rom idf::esp_common idf::esp_system )
# add_dependencies(app_main test_main)

#target_include_directories(app_main PRIVATE 
#    ${PROJECT_SOURCE_DIR}/test/include
#)
