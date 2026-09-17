#include <math.h>
#include <stdio.h>

#define E 2.718281828459

long long factorial(int n) {
    if (n < 0) {
        printf("Input must be non-negative\n");
        return -1;
    }
    if (n == 0) {
        return 1;
    }
    return factorial(n - 1) * n;
}

double exponent(double x) {
    int degrees = 20;
    int x_0 = round(x);
    double z = x - x_0;

    double c = 1.0;
    for (int d = 1; d < degrees; d++) {
        c += pow(z, d) / factorial(d);
    }
    return pow(E, x_0) * c;
}

int main(void) {
    double points[51];
    for (int i = 0; i < 51; i++) {
        double x = i * 0.02;
        points[i] = exponent(x);
    }

    FILE* out_file;
    remove("data.txt");
    out_file = fopen("data.txt", "a");
    for (int i = 0; i < 51; i++) {
        fprintf(out_file, "%lf,", points[i]);
    }
}