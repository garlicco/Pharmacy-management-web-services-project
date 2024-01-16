from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")  #path operation
async def root(): #async used for api calls or something that takes some time
    return {"message": "hello world xx"}

@app.get("/meds")
def get_meds():
    return {"data":"this is the list of meds"}

@app.post("/addmeds")
def add_meds(payLoad: dict= Body(...)):
    print(payLoad)
    return {"new_med":f"name {payLoad['name']}, type: {payLoad['type']}"}