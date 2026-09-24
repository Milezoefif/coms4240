#include "quad.h"
#include <math.h>

void calculate_area(struct quadrilateral* quad) {
    struct point* p1 = &quad->points[0];
    struct point* p2 = &quad->points[1];
    struct point* p3 = &quad->points[2];
    struct point* p4 = &quad->points[3];
    double area = 0.5 * fabs(((p1->x * p2->y) + (p2->x * p3->y) + (p3->x * p4->y) + (p4->x * p1->y)) - 
                        ((p1->y * p2->x) + (p2->y * p3->x) + (p3->y * p4->x) + (p4->y * p1->x)));
    quad->area = area;
}