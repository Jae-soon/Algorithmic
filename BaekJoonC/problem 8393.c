#include <stdio.h>

int main() {
    int num;
    int rst = 0;
    scanf("%d", &num);

    for (int i = 1; i <= num; i++) {
        rst += i;
    }

    printf("%d\n", rst);

    return 0;
}