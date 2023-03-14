#include <stdio.h>

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#include "test_main.h"

void app_main(void)
{
	printf("Helloworld!\n");

	test_main();
}
