#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const int Nmax = 5;
    int N = -1;
    printf("Provide input N (1 - 5): ");
    scanf("%d", &N);

    if (N < 0 || N > Nmax) {
        printf("Error: N must be in range 0 - 5\n");
        exit(1);
    }

    double coef[N + 1];
    for (int i = 0; i <= N; i++) {
        printf("Set coefficient for x^%d: ", i);
        scanf("%lf", &coef[i]);
    }

    const int num_points = 21;
    double x_values[num_points];

    // x values ranging from -1 to 1
    for (int i = 0; i < num_points; i++) {
        x_values[i] = -1 + i * (2.0 / (1.0 * (num_points - 1)));
    }

    double y_values[num_points];

    for (int i = 0; i < num_points; i++) {
        const double x = x_values[i];
        double phi;
        y_values[i] = coef[0];
        switch(N) {
            case 5:
               phi = (16 * pow(x, 5)) - (20 * pow(x, 3)) + (5 * x);
               y_values[i] += coef[5] * phi;
            case 4:
               phi = (8 * pow(x, 4)) - (8 * pow(x, 2)) + 1;
               y_values[i] += coef[4] * phi;
            case 3:
               phi = (4 * pow(x, 3)) - (3 * x);
               y_values[i] += coef[3] * phi;
            case 2:
               phi = (2 * pow(x, 2)) - 1;
               y_values[i] += coef[2] * phi;
            case 1:
               phi = x;
               y_values[i] += coef[1] * phi;
            case 0:
               break;
            default:
                printf("\nError\n");
                exit(1);
        }

        FILE* output_file;
        remove("poly.data");
        fopen("poly.data", "w");
        fprintf(output_file, "%d\n", num_points);
        for (int i = 0; i < num_points; i++) {
            fprintf(output_file, "%lf,%lf\n", x_values[i], y_values[i]);
        }

        system("python3 plot_poly.py");
        return 0;
    }

}