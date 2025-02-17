#include "box.h"
#include "vector.h"

Box::Box(const Vector &c, Texture *t, double ya, double pi, double ro,
         double tx, double ty)
    : Plane(c, t, ya, pi, ro, tx, ty) {}
Box::Box(const Vector &c, Texture *t, double ya, double pi, double ro,
         double tx)
    : Plane(c, t, ya, pi, ro, tx, tx) {}

double Box::getIntersection(Ray ray) {
  double time = Plane::getIntersection(ray);
  if (time == inf) {
    return time;
  }

  double denom = COMPUTE_DENOM(right, up, vect);
  Vector C = ray.point + ray.vector * time - center;
  double x = COMPUTE_X(up, vect, C, denom);
  if (x > textureX / 2 || x < -textureX / 2) {
    return inf;
  }
  double y = COMPUTE_Y(right, vect, C, denom);
  if (y > textureY / 2 || y < -textureY / 2) {
    return inf;
  }
  return time;
}

bool Box::getLightIntersection(Ray ray, double *fill) {
  const double t = ray.vector.dot(vect);
  const double norm = vect.dot(ray.point) + d;
  const double r = -norm / t;
  if (r <= 0. || r >= 1.) {
    return false;
  }

  double denom = COMPUTE_DENOM(right, up, vect);
  Vector C = ray.point + ray.vector * r - center;
  double x = COMPUTE_X(up, vect, C, denom);
  if (x > textureX / 2 || x < -textureX / 2) {
    return false;
  }
  double y = COMPUTE_Y(right, vect, C, denom);
  if (y > textureY / 2 || y < -textureY / 2) {
    return false;
  }

  if (texture->opacity > 1 - 1E-6) {
    return true;
  }
  unsigned char temp[4];
  double amb, op, ref;
  texture->getColor(temp, &amb, &op, &ref, fix(x / textureX - .5),
                    fix(y / textureY - .5));
  if (op > 1 - 1E-6) {
    return true;
  }
  fill[0] *= temp[0] / 255.;
  fill[1] *= temp[1] / 255.;
  fill[2] *= temp[2] / 255.;
  return false;
}
