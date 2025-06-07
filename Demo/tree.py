# trees can be visualized with both TreeVisualizer and GraphVisualizer classes. 

from DebugVisualizer import TreeVisualizer
# from DebugVisualizer import GraphVisualiser

viz = TreeVisualizer()
# viz = GraphVisualizer()

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, value):
        child = TreeNode(value)
        self.children.append(child)
        return child

# Create a file system tree
root = TreeNode("C:")
viz.visualize(root)

# First level
documents = root.add_child("Documents")
viz.visualize(root)

downloads = root.add_child("Downloads")
viz.visualize(root)

pictures = root.add_child("Pictures")
viz.visualize(root)

# Second level - Documents
documents.add_child("Resume.pdf")
viz.visualize(root)

documents.add_child("Report.docx")
viz.visualize(root)

work = documents.add_child("Work")
viz.visualize(root)

# Third level - Work folder
work.add_child("Project1.xlsx")
viz.visualize(root)

work.add_child("Meeting_notes.txt")
viz.visualize(root)

# Second level - Pictures
pictures.add_child("Vacation.jpg")
viz.visualize(root)

pictures.add_child("Family.png")
viz.visualize(root)

