# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dummy_generator import get_dummy_data


app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict it later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/files")
def get_files():
    return get_dummy_data(100)
