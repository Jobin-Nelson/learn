# Threading VS Multiprocessing

## Threading
- A new thread is spawned within the existing process
- Starting a thread is faster than starting a process
- Memory is shared between all threads
- Mutexes often necessary to control
- One GIL (Global Interpreter Lock) for all threads

## Multiprocessing
- A new process is started independent from the first process
- Starting a process is slower than starting a thread
- Mutexes is not necessary (unless threading in the new process)
- One GIL (Global Interpreter Lock) for each process
