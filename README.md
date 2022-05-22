This Project 2 thought me:

- Assembler
  - The different elements: 
    - Stack Pointer
    - Base Pointer
    - Memory Address
    - x86 and x64 architecture
    - Registers
    - Calling conventions
   
- C: BOF using unsafe functions gets, printf, malloc:
  - We can control Stack Pointer
  - Or can execute code loaded into memory
  - Pass parameters that make the execution flow to be guided to win funnctions

- Python
  - pwn library to pass and tailor inputs to binary
  - Be able to analyze binary characteristics:
    - Flaws and Security: PIE, RELRO, NX, Symbols, Canary
    - Read GOT, PLT, Symbols and strings contained in binary
  - Create Shellcode
  - Inspect and Debug code in conjunction with radare2, which honestly this was a huge time saver.
    I consider this the skill that I was able to learn and learn a few tricks by heart. 

- Radare2
  - Debug assembler and inspect code
  - Be able to closely watch memory, program execution and registers. 
  - At first this was not totaly strange to me, however little by little I gained confidence on:
    - how to read assembler code
    - how to predict the execution by just looking at the values of the registers and memory
    - how to distinguish Memory Stack from printable data and how it looks
    - following calling conventions
  - Print data from memory and registers 
  - Seach for symbols
  - Go to memory locations and navigate the stack at any time
  - Still there are plenty of features very powerful

- Rabin2
  - Analyze the importance of symbols to differenciate those that are relevant to the binary at first glance
  - Read Strings and get to know which are potentially needed for pawns

- ROPgadget
  - I was surprised about this feature of controlling execution 
  - It seems this feature is enought to control almost anything

- Checksec helped to review what security flaws contains the binary

Thanks a lot Professor, this was honestly one of the best courses I've taken in my whole life, every video lecture and problem you exaplained
was mind blowing to me. Since it was years since I last used Assembler this lecture answered many questions to me as a developer, it
helped me as a reminder why software security is so important and how easy is to mess with so little.

I'm highly satisfied with this class, thanks again for this incredible knowledge you shared with us.
Jesus Martinez.