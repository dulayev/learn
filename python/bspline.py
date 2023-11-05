# UNCOMPLETED attempt to compute B-splines manually, not finished
import bisect
import numpy as np
import matplotlib.pyplot as plt

def bspline_basis(index, degree, u, knot_vector):
    """
    Compute the B-spline basis function N_{index,degree}(u) using the Cox-de Boor recursion formula.

    Parameters:
    - index: index of the basis function
    - degree: degree
    - u: parameter
    - knot_vector: list or array of knot values

    Returns:
    - Value of the basis function N_{index,degree}(u)
    """

    # Base case: degree 0
    if degree == 0:
         # should be <= u <
        return 1.0 if knot_vector[index] <= u <= knot_vector[index+1] else 0.0

    # Recursive case
    term1 = 0.0
    if (knot_vector[index+degree] - knot_vector[index]) != 0:
        term1 = ((u - knot_vector[index]) / (knot_vector[index+degree] - knot_vector[index])) * bspline_basis(index, degree-1, u, knot_vector)

    term2 = 0.0
    if (knot_vector[index+degree+1] - knot_vector[index+1]) != 0:
        term2 = ((knot_vector[index+degree+1] - u) / (knot_vector[index+degree+1] - knot_vector[index+1])) * bspline_basis(index+1, degree-1, u, knot_vector)

    return term1 + term2

# order is a count of points influencing the value
# polynom degree = order - 1
def curve_function(u, order, knot_vector, control_points, weights):
    # choose bisect_right here as B-spline intervals are like [Ki-1, Ki)
    # so search result should give same value for exact position and
    # position which is very close on the right
    span_index = bisect.bisect_right(knot_vector, u)
    if span_index == len(knot_vector):
        span_index -= 1
        assert u == knot_vector[-1] # hit the last item
    num = 0.
    denum = 0.
    for i in range(span_index - order, span_index):
        if i > len(knot_vector) - order - 1:
            continue
        sp_value = bspline_basis(i, order - 1, u, knot_vector)
        num += sp_value * weights[i] * control_points[i]
        denum += sp_value * weights[i]

    # influencing = control_points[i - order: i]
    return num / denum if denum != 0.0 else 0.0

control_points = [1.5]   #[0.64, 0.81, 0.76, 0.79, 0.25, 0.14, 0.79, 0.25, 0.14]
weights = [1.] * len(control_points)
ORDER = 2
knot_vector = [0.0, 0.5, 1.0]
#[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
assert len(knot_vector) == len(control_points) + ORDER

plt.figure(figsize=(10, 6))
u_values = np.linspace(knot_vector[0], knot_vector[-1], 1000)

cf = np.vectorize(lambda u: curve_function(u, ORDER, knot_vector, control_points, weights))
print(type(u_values))
curve_values = cf(u_values)
print(type(curve_values))

plt.plot(u_values, curve_values)
plt.show()
