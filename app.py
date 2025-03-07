from fastapi import FastAPI,Depends, HTTPException
from fastapi.security import APIKeyHeader,APIKeyQuery, APIKeyCookie
from pydantic import BaseModel
from functions import *
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(docs_url='/api/documentation', title="Flarion Development INC.", description="Flarion Development INC. API", version="1.0.0")

header = APIKeyHeader(name="X-API-Key", auto_error=False)


def get_api_key(x_api_key: str = Depends(header)) -> str:
    if x_api_key == "fake-super-secret":
        return x_api_key
    else:
        raise HTTPException(
            status_code=403,
            detail="Invalid API Key. Please provide a valid X-API-Key header."
        )

origins = [
    "http://localhost:8000",
]


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def index():
    return {
        "message": "Flarion Development INC.!",
        "status": "API Aktif!",
    }


@app.get("/phone/{phonenumber}/{country}")
async def phone_info(phonenumber: str, country: str, api_key: str = Depends(get_api_key)):
    phone = Phone()
    phone.set_phone_number(phonenumber)
    phone.set_country_code(country)

    response = get_phone_info(phone.phonenumber, phone.country_code)
    return response


@app.get("/phone/{phonenumber}")
async def without_country_phone_info(phonenumber: str, api_key: str = Depends(get_api_key)):
    phone = Phone()
    phone.set_phone_number(phonenumber)
    response = dummy_get_phone_info(phone.phonenumber)
    return response