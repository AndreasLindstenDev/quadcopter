# Select multiple faces of a body in FreeCAD
doc_name = "QuadCopter"
body_name = "Body001"

for i in range(1, 62):  # 1 to 49 inclusive
    face_name = f"Pocket012.Face{i}"
    Gui.Selection.addSelection(doc_name, body_name, face_name)