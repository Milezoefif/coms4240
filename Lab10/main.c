#include "quad.h"
#include <stdio.h>

int main(void) {
    struct quadrilateral quad;
    quad.points[0] = (struct point){0, 0};
    quad.points[1] = (struct point){0, 0};
    quad.points[2] = (struct point){0, 0};
    quad.points[3] = (struct point){0, 0};
    for (int i = 0; i < 4; i++) {
        double x;
        printf("Point %d, X: ", i + 1);
        scanf("%lf", &x);
        quad.points[i].x = x;

        double y;
        printf("Point %d, Y: ", i + 1);
        scanf("%lf", &y);
        quad.points[i].y = y;
    }

    calculate_perimeter(&quad);
    calculate_area(&quad);
    calculate_angles(&quad);
    printf("perimeter: %lf\n", quad.perimeter);
    printf("area: %lf\n", quad.area);
    printf("angles (in radians): %lf, %lf, %lf, %lf\n", quad.angles[0], quad.angles[1], quad.angles[2], quad.angles[3]);
    return 0;
}