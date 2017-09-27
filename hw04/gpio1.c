#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <signal.h>
#include "beaglebone_gpio.h"
#define  GPIO3_START_ADDR 0x481ae000
#define GPIO3_END_ADDR 0x481b0000
#define GPIO3_SIZE (GPIO0_END_ADDR - GPIO0_START_ADDR)

int main(int argc, char *argv[]){
	volatile void *gpio_addr;
	volatile void *gpio_addr3;
	volatile unsigned int *gpio_datain_addr;
	volatile unsigned int *gpio_datain_addr3;
	volatile unsigned int *gpio_setdataout_addr;
	volatile unsigned int *gpio_cleardataout_addr;
	volatile unsigned int *gpio_oe_addr;
	int fd = open("/dev/mem", O_RDWR);
	gpio_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
	gpio_addr3 = mmap(0, GPIO3_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO3_START_ADDR);
//set up gpio addresses

	gpio_setdataout_addr   = gpio_addr + GPIO_SETDATAOUT;
	gpio_cleardataout_addr = gpio_addr + GPIO_CLEARDATAOUT;
	gpio_datain_addr       = gpio_addr + GPIO_DATAIN;
	gpio_oe_addr           = gpio_addr + GPIO_OE;

        gpio_datain_addr3       = gpio_addr3 + GPIO_DATAIN;


	while (1){
//shift 25 bit to the right to see if the button is 1 or 0; if 1, since gpio25 is pulldown
//then turn it on  initially
		if(*gpio_datain_addr>>25 &1 ==1){
			*gpio_setdataout_addr   =USR3;
		}
		else{
			*gpio_cleardataout_addr =USR3;
		}
//shift 17 bit to the right to see if the button is 1 or 0; if 1, since gpio17 is pulldown
//then turn it off  initially

		if(*gpio_datain_addr3>>17 &1==1){
			*gpio_cleardataout_addr =USR2;
		}
		else{
                      *gpio_setdataout_addr =USR2;
		}
	}
}
