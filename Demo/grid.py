from DebugVisualizer import GridVisualizer

# Create a GridVisualizer instance
viz = GridVisualizer()

grid = []

for i in range(10):
    row = []
    for j in range(10):
        value = i + j
        row.append(value)

    grid.append(row)
    viz.visualize(grid)
