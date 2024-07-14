from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Rooman", "World2": "Ayan Amir"}

@app.get("/developer/")
def developer_details():
    return {"Name": "Amir Hanif", "Institute": "PIAIC"}