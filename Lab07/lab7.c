#include <stdio.h>
#include <math.h>

// n!
long long factorial(int n) {
    if (n < 0) {
        printf("Input value must be non-negative\n");
        return -1;
    }
    int product = 1;
    for (int i = 2; i <= n; i++) {
        product *= i;
    }
    return product;
}

// e^x
double exponent(double x) {
    return exp(x);
}

// ln(x)
double logarithm(double x) {
    return log(x);
}

int main(void) {
    int n;
    double x;

    printf("Input value for n: ");
    scanf("%d", &n);
    printf("Input value for x: ");
    scanf("%lf", &x);

    printf("%d!: %lld\n", n, factorial(n));
    printf("e^%lf: %f\n", x, exponent(x));
    printf("ln(%f): %f\n", x, logarithm(x));

    return 0;
}