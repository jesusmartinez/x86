section .text: ;;to compile nasm -f elf64 test.asm THEN ld -o runme test.o
  global _start

getNumber1:
  push rbp
  mov rbp, rsp
  sub rsp, 0x10        ; make espace of 10 bytes
  mov dword [rsp], 0x0 ; Set value 0 in SP
  cmp edx, dword [rsp] ; Compare SP against parameter in register D
  je iszero            ; is equal to 0 ? then jump to iszero function
  add edx, 2           ; otherwise add two to register D
  leave
  ret
iszero: 
  mov dword [rsp], 0x1 ; Set value 1 in SP
  mov edx, dword [rsp] ; Set it in register D
  leave
  ret
getNumber2:
  push rbp
  mov rbp, rsp
  sub rsp, 0x10        ; make espace of 10 bytes
  mov dword [rsp], 0x0 ; Set value 0 in SP
  cmp edx, dword [rsp] ; Compare SP against parameter in register D
  jg gthanzero         ; is > 0 ? then jump to gthanzero function
  xor edx, edx         ; otherwise set register D to 0
  leave
  ret
gthanzero: 
  mov dword [rsp], 0x1 ; Set value 1 in SP
  sub edx, dword [rsp] ; Subtract 1 to Register D
  leave
  ret
sum:
  push rbp
  mov rbp, rsp
  sub rsp, 0x10        ; make espace of 10 bytes
  mov dword [rsp], eax ; Sum Reg A
  add dword [rsp], ebx ; plus Reg B
  mov edx, dword [esp] ; Store it in Reg D
  leave
  ret
  
_start:
  push rbp
  mov rbp, rsp
  sub rsp, 0x10        ; make espace of 10 bytes
  mov dword [rsp], 0xe ; Store integer 14
  mov edx, dword [rsp] 
  call getNumber1      ; call first function to get first number
  mov dword [rsp], edx ; store it 
  mov eax, dword [rsp] ; register A
  call getNumber2      ; call first function to get first number
  mov dword [rsp], edx ; store it 
  mov ebx, dword [rsp] ; register B
  call sum             ; call sum
  mov dword [rsp], edx ; result is stored in the register D
  mov eax, dword [rsp] ; move it to register A
  xor rdi, rdi         ; clear register 
  mov eax, 0x3c
  syscall