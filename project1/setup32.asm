section .text:
  global _start ;;to compile nasm -f elf t32.asm THEN ld -m elf_i386 -s -o run32 t32.o

getNumber1:
  push ebp
  mov ebp, esp
  sub esp, 0x10        ; make espace of 10 bytes
  mov dword [esp], 0x0 ; Set value 0 in SP
  cmp edx, dword [esp] ; Compare SP against parameter in register D
  je iszero            ; is equal to 0 ? then jump to iszero function
  add edx, 2           ; otherwise add two to register D
  leave
  ret
iszero: 
  mov dword [esp], 0x1 ; Set value 1 in SP
  mov edx, dword [esp] ; Set it in register D 
  leave
  ret
  
getNumber2:
  push ebp
  mov ebp, esp
  sub esp, 0x10        ; make espace of 10 bytes
  mov dword [esp], 0x0 ; Set value 0 in SP
  cmp edx, dword [esp] ; Compare SP against parameter in register D
  jg gthanzero         ; is > 0 ? then jump to gthanzero function
  xor edx, edx         ; otherwise set register D to 0
  leave
  ret
gthanzero: 
  mov dword [esp], 0x1 ; Set value 1 in SP
  sub edx, dword [esp] ; Subtract 1 to Register D 
  leave
  ret
sum:
  push ebp
  mov ebp, esp
  sub esp, 0x10        ; make espace of 10 bytes
  mov dword [esp], eax ; Sum Reg A
  add dword [esp], ebx ; plus Reg B
  mov edx, dword [esp] ; Store it in Reg D
  leave
  ret
  
_start:
  push ebp
  mov ebp, esp
  sub esp, 0x10        ; make espace of 10 bytes
  mov dword [esp], 0xe ; Store integer 14
  mov edx, dword [esp] 
  call getNumber1      ; call first function to get first number
  mov dword [esp], edx ; store it 
  mov eax, dword [esp] ; register A
  call getNumber2      ; call first function to get first number
  mov dword [esp], edx ; store it 
  mov ebx, dword [esp] ; register B
  call sum             ; call sum
  mov dword [esp], edx ; result is stored in the register D
  mov eax, dword [esp] ; move it to register A
  xor ebx, ebx         ; clear register B
  mov eax, 0x01
  int 0x80