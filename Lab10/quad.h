#ifndef QUAD_H
#define QUAD_H

struct point {
    double x;
    double y;
};
struct quadrilateral {
    struct point points[4];
    double angles[4];
    double area;
    double perimeter;
};

void calculate_perimeter(struct quadrilateral* quad);

#endif