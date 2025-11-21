from fastapi import FastAPI



app = FastAPI()


@app.get("/")
def index():
    return {"message": "hi"}

@app.get("/about")
def index():
    return {"message": "page aboute me"}

@app.get("/student/{name}/familia/{surname}")
def index(name: str, surname):
    return {"message": name + " " + surname}


@app.get("/ikkinchi")
def ikkinchi (s, a=None):
    if a:
        return {"s": s, "a": a }
    return {"s": s}
        
       
   



