from dotenv import load_dotenv
load_dotenv()
from app.main import app
import uvicorn
import os


port = int(os.getenv("PORT", 3050))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)