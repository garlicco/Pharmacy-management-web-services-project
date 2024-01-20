from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db, Base

def main():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


app = FastAPI()



@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return {"status":"success"}
    

class Meds(BaseModel):
    name: str
    type: str

try:
    conn = psycopg2.connect(host='localhost',database='MedecineAPI', 
                            user='postgres', password='0000',
                            cursor_factory=RealDictCursor)
    cursor=conn.cursor()    
    print("Database connection sucessful")
except Exception as error:
    print("Connection to database failed")
    print("Error was: ", error)


@app.get("/meds")
def get_meds():
    cursor.execute("""SELECT * FROM meds""")
    meds= cursor.fetchall()
    return {"data": meds}

@app.post("/addmeds", status_code=status.HTTP_201_CREATED) #lezem l status tji 201 f post operation
def add_meds(new_med: Meds):
    print(new_med.name)
    return {"data":"new med"}
#name str, type str, dosage nbr, frequency nbr

