# Select multiple faces of a body in FreeCAD
doc_name = "QuadCopter"
body_name = "Body001"

for i in range(1,14):  # 1 to # inclusive
    face_name = f"Pocket012.Face{i}"
    Gui.Selection.addSelection(doc_name, body_name, face_name)








# Select multiple faces of a body in FreeCAD
doc_name = "QuadCopter"
body_name = "Body009"

for i in range(1,50):  # 1 to # inclusive
    face_name = f"Pocket045.Face{i}"
    Gui.Selection.addSelection(doc_name, body_name, face_name)