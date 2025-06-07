from DebugVisualizer import PlotlyTableVisualizer

# Create a PlotlyTableVisualizer instance
viz = PlotlyTableVisualizer()

# Define heeader and values
header = ["Product", "Q1 Sales", "Q2 Sales"]

values = [
    ["Product A", "Product B", "Product C"],
    [341319, 281489, 294786],
    [448916, 391872, 389124]
]

viz.visualize(header, values)
