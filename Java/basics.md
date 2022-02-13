# Java
- Java is a compiled language so there's a middle step in between writing the code and executing it
- The byte code file or class file returned after compiling the java file can be run on any OS, hence it is platform independant
- Highly object oriented language, all of the functionality is gonna be defined inside classes
- Visibility controls with `public` and `private` keywords

## Datatypes
- byte -> 8 bit [-128 to 127]
- short -> 16 bit [-32,768 to 32767]
- int -> 32 bit [-2^31 to 2^31 -1]
- long -> 64 bit [-2^63 to 2^63 -1]
- float -> 32 bit 
- double -> 64 bit
- boolean -> true, false
- char -> 16 bit [\u0000 or 0 to \uffff or 65,535]

## Keywords
abstract, assert, boolean, break, byte, case, catch, char, class, const, continue, default, do, double, else, enum, exports, extends, final, finally, float, goto, if, implements, import, instanceof, int, interface, long, module, native, new, open, opens, package, private, protected, provides, public, requires, return, short, static, strictfp, super, switch, synchronized, this, throw, throws, to, transient, transitive, try, uses, void, volatilve, while, with

## Identifiers
- any variable names you declare in your program
- cannot start with number, contain space, have +, -, &

## Constants
- final variables
- not mutable

## Special Symbols
[] () {} ; * =

## Operators
arithmatic, comparison, logical, bitwise, etc

## Collections
- **TreeSet**: elements are unique, follows tree hierarchy
- **ArrayList**: 0 indexed list with fixed length
- **Vector**: like arraylist but synchronized, they are thread safe and is a legacy class
- **LinkedList**: sequential list which can only be accessed by going through them linearly
- **Stack**: same as stack in python, last in first out [LIFO]
- **PriorityQueue**: same as deque in python, first in first out [FIFO]
- **Hashset**: elements are unique, unsorted
- **Hashtable**: synchronized representation of hashmap, it is thread safe
- **HashMap**: has key value pairs, much like dictionaries in python
- **Hashtree**: like hashmap but sorted
- **LinkedHashmap**: stores the values as linked list