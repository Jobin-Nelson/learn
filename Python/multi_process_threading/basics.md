# Process
Process are instances of a program (e.g. edge browser)

**Pros**
- Takes advantage of multiple CPU's and cores
- Seperate memory spaces -> memory is not shared between process
- Great for CPU bound processing
- New process is started independently from other process
- Processes are interruptable/ killable
- One GIL (Global interpreter lock) for each process -> avoids GIL limitaion

**Cons**
- Heavyweight
- Starting a process is slower than starting a thread
- More memory
- IPC (Inter process communication) is complicated

# Threads
An entity within a process that can be scheduled aka lightweight process. A process can spawn multiple threads

**Pros**
- All threads within a process share the same memory
- Lightweight
- Starting a thread	is faster than starting a process
- Great for I/O bound tasks

**Cons**
- Threading is limited by GIL -> only one thread at a time
- No effect for CPU bound tasks
- Not interruptable/ killable
- Careful with race conditions -> two or more threads want to modify same variable

# Global interpreter lock (GIL)
A lock that allows only one thread at a time to execute in python. It is needed in CPython because memory management is not thread-safe

**Avoid**
- Use multiprocessing
- Use a different, free-threaded Python implementation (Jython, IronPython)
- Use Python as a wrapper for third-party libraries (C/C++) -> numpy, scipy
