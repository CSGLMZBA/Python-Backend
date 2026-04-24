from app.core.firebase import db
from firebase_admin import firestore
class AlumnosRepository:
    def get_all(self):
        alumnos = db.collection("alumnos").where("activo", "==", True).get()
        return [{
            "id": al.id,
            **al.to_dict()
        } for al in alumnos]
    
    def create(self, data):
        ref = db.collection("alumnos").document()
        ref.set(data)
        return ref.id
    
    def update(self, id, data):
        db.collection("alumnos").document(id).update(data)

    def delete(self, id):
        db.colllection("alumnos").document(id).update({
            "activo": False,
            "updatedAt": firestore.SERVER_TIMESTAMP})