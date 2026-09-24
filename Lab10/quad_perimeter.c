#include "quad.h"
#include <math.h>

double distance(struct point* p1, struct point* p2) {
    return sqrt(pow(p2->x - p1->x, 2) + pow(p2->y - p1->y, 2));
}

void calculate_perimeter(struct quadrilateral* quad) {
    struct point* points = quad->points;
    float perimeter = 0;

    for (int i = 0; i < 4; i++) {
        struct point* p1 = &points[i];
        // Gets next point to compare distance with overflow back to 0 when i = 3
        struct point* p2 = &points[(i + 1) % 4];

        perimeter += distance(p1, p2);
    }
    return perimeter;
}