# Напишите функцию, которая вычисляет векторное произведение в 3-мерном пространстве.

from supporting.vector import Vector

def vector_product(a: Vector, b: Vector):
    c = Vector((a.y * b.z - a.z * b.y),
               (a.z * b.x - a.x * b.z),
               (a.x * b.y - a.y * b.x))

    return c