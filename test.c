#include "stdio.h"
#include "stdlib.h"


int f(int x) {
    int y = 0;
    int z = 0;
    y = 2 * x;
    z = y + 1;
    return z / 3;
}
int main() {
    printf ("%d", f(30));
    return 0;
}
