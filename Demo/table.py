from DebugVisualizer import TableVisualizer

# Create a TableVisualizer instance
viz = TableVisualizer()

students = [
    {"id": 1, "name": "Alice", "math": 95, "science": 88, "history": 92},
    {"id": 2, "name": "Bob", "math": 82, "science": 90, "history": 85},
]
viz.visualize(students)
   
students.extend([
    {"id": 3, "name": "Charlie", "math": 78, "science": 85, "history": 88},
    {"id": 4, "name": "David", "math": 92, "science": 75, "history": 80},
    {"id": 5, "name": "Eve", "math": 85, "science": 82, "history": 87},
])
viz.visualize(students)

students.append({"id": 6, "name": "Frank", "math": 88, "science": 82, "history": 90})
viz.visualize(students)
