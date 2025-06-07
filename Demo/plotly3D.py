from DebugVisualizer import Plotly3DVisualizer
import math

# Create a Plotly3DVisualizer instance
viz = Plotly3DVisualizer()

# Generate a 3D surface (z = sin(x) + sin(y))
x = []
y = []
z = []

for i in range(10):
    for j in range(10):
        x.append(i)
        y.append(j)
        z.append(math.sin(i) + math.sin(j))

# Visualize as a 3D mesh
viz.visualize(x, y, z)
