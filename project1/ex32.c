// Tp compile 32 bits
// $ gcc -m32 bin_name source_code.c

int f1(int p1) {
  return p1 - 1;
}

int main() {
  int x = 10;
  int y = f1(x);
  return y;
}

