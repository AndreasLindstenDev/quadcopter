# Select multiple faces of a body in FreeCAD
doc_name = "QuadCopter"
body_name = "Body001"

for i in range(1,14):  # 1 to # inclusive
    face_name = f"Pocket012.Face{i}"
    Gui.Selection.addSelection(doc_name, body_name, face_name)








# Select multiple faces of a body in FreeCAD
doc_name = "Unnamed"
body_name = "Body001"

for i in range(1,45):  # 1 to # inclusive
    face_name = f"Pocket012.Face{i}"
    Gui.Selection.addSelection(doc_name, body_name, face_name)