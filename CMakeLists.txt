cmake_minimum_required(VERSION 3.16)

set(IDF_TARGET "esp32c3")

include($ENV{IDF_PATH}/tools/cmake/project.cmake)

set(COMPONENTS 
    cxx 
    pthread
    newlib 
    freertos 
    esp_hw_support 
    heap 
    soc 
    hal 
    esp_rom 
    esp_common 
    esp_system
    spi_flash
    riscv
    espcoredump
    driver
    esptool_py
    log
    partition_table
)

list(APPEND EXTRA_COMPONENT_DIRS "${CMAKE_CURRENT_LIST_DIR}/bsp/project/components")
set(sdkconfig "${CMAKE_CURRENT_LIST_DIR}/bsp/project/sdkconfig")

project(sample_project)

include_directories(
    ${CONFIG_DIR}
    ${PROJECT_SOURCE_DIR}/bsp/project/components/esp_rom/include
    ${PROJECT_SOURCE_DIR}/bsp/project/components/esp_rom/include/esp32c3
    ${PROJECT_SOURCE_DIR}/bsp/project/components/esp_system/include
    ${PROJECT_SOURCE_DIR}/bsp/project/components/esp_common/include
    ${PROJECT_SOURCE_DIR}/bsp/project/components/heap/include
    ${PROJECT_SOURCE_DIR}/bsp/project/components/hal/include
    ${PROJECT_SOURCE_DIR}/bsp/project/components/newlib/platform_include
    ${PROJECT_SOURCE_DIR}/bsp/project/components/riscv/include
    ${PROJECT_SOURCE_DIR}/bsp/project/components/soc/esp32c3/include
    ${PROJECT_SOURCE_DIR}/bsp/project/components/esp_hw_support/include
    ${PROJECT_SOURCE_DIR}/bsp/project/components/driver/include
    ${PROJECT_SOURCE_DIR}/bsp/project/components/freertos/FreeRTOS-Kernel/include
    ${PROJECT_SOURCE_DIR}/bsp/project/components/freertos/esp_additions/include/freertos
    ${PROJECT_SOURCE_DIR}/bsp/project/components/freertos/FreeRTOS-Kernel/portable/riscv/include
    ${PROJECT_SOURCE_DIR}/bsp/project/components/freertos/config/include/freertos
    ${PROJECT_SOURCE_DIR}/bsp/project/components/freertos/config/riscv/include

    ${PROJECT_SOURCE_DIR}/bsp/board
)
link_directories(
    .
    ${CMAKE_CURRENT_LIST_DIR}/bsp/project
    ${CMAKE_CURRENT_LIST_DIR}/bsp/board
)
target_link_libraries(${PROJECT_NAME}.elf PRIVATE 
    -Wl,--start-group
    app_main
    -Wl,--end-group
)

add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/bsp/project)
add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/bsp/board)
