#This is the ReadMe.md file
This homework is about testing gpio speed using three different ways.
1. using python: The file is called gpio_speed under hw07 directory. It uses GPIO.setup to setup input and output for the program.
It maps the input and output and triggers the interrupt by gpio.add_event_detect function.
2. using mmap: This file is called gpioThru.c under hw07/mmap directory. It uses mmap to map the memoery locatoin of the input and output.
3. Kernel module: This file is called gpio_test.c under hw07/exploringbb/extras/kernal/gpio_test directory. It triggers the interrupt in kernel mode.
To run it, the user should first run sudo insmod gpio_test.ko to add the module into kernel.
The test results are as displayed in a file called results.
