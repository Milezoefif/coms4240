#include "quad.h"
#include <math.h>

double dot(struct point* p1, struct point* p2) {
    return (p1->x * p2->x) + (p1->y * p2->y);
}

double magnitude(struct point* p) {
    return sqrt(pow(p->x, 2) + pow(p->y, 2));
}

void calculate_angles(struct quadrilateral* quad) {
    struct point* points = quad->points;

    for (int i = 0; i < 4; i++) {
        struct point* prev = &points[i];
        struct point* middle = &points[(i + 1) % 4];
        struct point* next = &points[(i + 2) % 4];
        struct point vec1 = (struct point){prev->x - middle->x, prev->y - middle->y};
        struct point vec2 = (struct point){next->x - middle->x, next->y - middle->y};
        quad->angles[i] = acos(dot(&vec1, &vec2) / (magnitude(&vec1) * magnitude(&vec2)));
    }
}