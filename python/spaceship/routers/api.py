import numpy
from fastapi import APIRouter

router = APIRouter()

@router.get('/matrix')
def matrix() -> dict:
    matrix_a = numpy.random.rand(10, 10)
    matrix_b = numpy.random.rand(10, 10)
    product = numpy.dot(matrix_a, matrix_b)

    result = {
        "matrix_a": matrix_a.tolist(),
        "matrix_b": matrix_b.tolist(),
        "product": product.tolist()
    }

    return result
