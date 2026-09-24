#include "quad.h"

int main(void) {
    struct quadrilateral quad;
    quad.points[0] = (struct point){0, 0};
    quad.points[1] = (struct point){0, 0};
    quad.points[2] = (struct point){0, 0};
    quad.points[3] = (struct point){0, 0};
    for (int i = 0; i < 4; i++) {
        double x;
        printf("Point #%d, X: ", i);
        scanf("%lf", x);
        quad.points[i].x = x;

        double y;
        printf("Point #%d, Y: ", i);
        scanf("%lf", y);
        quad.points[i].y = y;
    }

    calculate_perimeter(&quad);
    return 0;
}