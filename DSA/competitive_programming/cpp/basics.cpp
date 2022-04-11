#include <iostream> // importing modules in c 
#include <limits.h> // importing module for finding the limits of each datatype

// using namespace std; -> namespace determines the scope of functions, this helps to use, cout without this we would've to use std::cout

int main(){
	std::cout << "Hello world" << std::endl;

	// datatypes
	int x = 0; // cpp is a statically typed language so you should intialise every variable with the type

	std::cout << 'Short(short)' << sizeof(short) << std::endl; // short = 2 bytes
	std::cout << 'Integer(int)' << sizeof(int) << std::endl; // int = 4 bytes
	std::cout << 'Long(long)' << sizeof(long) << std::endl; // long = minimum 4 could have more bytes

	// 2 bytes can store a maximum integer value of 65535
	// by default variables store signed values on both sides of the number system from 0 so 65535/2
	unsigned short s = 65535; // you can explicitly ask it to store only unsigned values which would allow the variable to store a max of 65535

	std::cout << 'Float' << sizeof(float) << std::endl; // stores 7 decimals
	std::cout << 'Double' << sizeof(double) << std::endl; // stores 15 decimals

	char c = 'a'; // each character takes 1 bytes or 8 bits

	std::string s = 'Hello world'; // string is just an array of characters

	bool b = true; // bool needs only 1 bit to store a value, you can set it to 1 or 0

	// arithmetic operators +-*/%
	int a = 10, b = 20;
	std::cout << a+b << std::endl; // it should give you 30

	// assignment operators
	int a = 20; // = is an assignment operator
	a++; // increments a by 1

	// comparison operators ==, !=, <, >, <=, >=
	int a = 10, b = 20;
	std::cout << (a<b) << std::endl; // 0

	// logical operators &&, ||, !
	int a = 10, b = 20;
	std::cout << ((a<b)&&(a>5)) << std::endl; // 1

	// bitwise operators &, | 

	// user inputs
	std::cout << 'Please enter your name';
	std::string name;
	std::cin >> 'Your name is ' >> name << std::endl;

	return 0;
}
