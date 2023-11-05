# example how to use geomdl library to compute NURBS
from geomdl import NURBS
from geomdl.visualization import VisMPL

# Create a NURBS curve instance
crv = NURBS.Curve()

# Set evaluation delta (curve sampling for visualization)
crv.delta = 0.01

# Set up the NURBS curve
crv.degree = 2
crv.ctrlpts = [[1.0, -2.0], [2.0, 3.0], [3.0, -1.]]
crv.knotvector = [0, 0, 0, 1, 1, 1]
crv.weights = None #[1, 1, 1]
# Plot the curve using the default Matplotlib-based visualization component
crv.vis = VisMPL.VisCurve2D()
crv.render()
