import firebase_admin
from firebase_admin import credentials, firestore
import os

if not firebase_admin._apps:
    project_id = os.getenv("FIREBASE_PROJECT_ID")
    client_email = os.getenv("FIREBASE_CLIENT_EMAIL")
    private_key = os.getenv("FIREBASE_PRIVATE_KEY")
    auth_uri = os.getenv("FIREBASE_AUTH_URI")
    token_uri = os.getenv("FIREBASE_TOKEN_URI")
    
    cred = credentials.Certificate({
        "type": "service_account",
        "project_id": project_id,
        "client_email": client_email,
        "private_key": private_key.replace("\\n", "\n"),
        "auth_uri": auth_uri,
        "token_uri": token_uri
    })
    firebase_admin.initialize_app(cred)
db = firestore.client()