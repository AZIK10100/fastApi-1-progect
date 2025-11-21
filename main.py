from fastapi import FastAPI



app = FastAPI()

mevalar =['olma','anor', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore, qui aliquid? Aspernatur sit atque perferendis. Pariatur, quos dolorum a deserunt ipsum totam recusandae. Dolore ab labore placeat. Nihil, illo rem.']



@app.get("/")
def index():
    return {"mevalar_list": mevalar}

@app.post("/")
def meva_yaratish(meva_nomi):
    global mevalar
    mevalar.append (meva_nomi)
    return {"message":  "mave yaratiladi."}
        
       
@app.put('/{mevalar}/{yangi_nom})')
def ozgartirish(meva_nomi: str, yangi_nom: str):
    global mevalar
    try:
        meva_id = mevalar.index(meva_nomi)
        mevalar[meva_id] = yangi_nom
    except:
        return {"error": "bunday meva nomi yoq"}
    return {"xabar": "meva nomi ozgardi"}


@app.put('/{mevalar}')
def ozgartirish(meva_nomi: str):
    global mevalar
    try:
       mevalar.remove(meva_nomi)
    except:
        return {"error": "bunday meva nomi yoq"}
    return {"xabar": "meva nomi ozgardi"}


