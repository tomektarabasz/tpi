from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime as Datetime
import json
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str
    temperature: str
    pressure:str

class ItemWithTime():
    def __init__(self):
        self.time = Datetime.now().strftime()
        super(Item, self).__init__()
    def __init__(self,item:Item):
        self.name = item.name
        self.temperature = item.temperature
        self.pressure = item.pressure
        self.time = Datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
    name: str
    temperature: str
    pressure: str
    time: Datetime
    
    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/temp")
async def tt(item:Item):
    result = ItemWithTime(item)
    tt =result.json()
    with open('vol/data.txt', 'a') as f:
        f.write(result.json())
        f.write("\n")
    return item.json()
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)