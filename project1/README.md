The following Algorithm is implemented for the setup32.asm and setup64.asm assembler programs


getNumber2(arg1):
  if (arg1 > 0)
     return arg1 - 1
  else
     return 0

getNumber1(arg1):
  if (arg1 == 0)
     return 1
  else
     return arg1 + 2
sum(arg1, arg2):
  return a + b

main:
  x = 14
  a = getNumber1(x)  // 16
  b = getNumber2(a)  // 15
  result = sum(a, b) // 31
  return result