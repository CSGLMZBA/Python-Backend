from app.core.firebase import db

class AuthRepository:
    def find_by_usuario(self, usuario: str):
        docs = db.collection("alumnos").where("usuario", "==", usuario).limit(1).stream()

        for doc in docs:
            return {"id": doc.id, **doc.to_dict()}
        return None 