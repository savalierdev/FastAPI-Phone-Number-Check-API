from fastapi import FastAPI
from functions import *


app = FastAPI(docs_url='/api/documentation', title="Flarion Development INC.", description="Flarion Development INC. API", version="1.0.0")

@app.get("/")
async def index():
    return {
        "message": "Flarion Development INC.!",
        "status": "API Aktif!",
    }


@app.get("/phone/{phonenumber}/{country}")
async def phone_info(phonenumber: str, country: str):
    phone = Phone()
    phone.set_phone_number(phonenumber)
    phone.set_country_code(country)

    is_number_valid,is_possible_number,number_type,isp=get_phone_info(phone.phonenumber, phone.country_code)
    
    return {
        "phone_number": phone.phonenumber,
        "country_code": phone.country_code,
        "is_number_valid": is_number_valid,
        "is_possible_number": is_possible_number,
        "number_type": number_type,
        "isp": isp
    }