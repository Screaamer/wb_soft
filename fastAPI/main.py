from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# пример роута (маршрута)
@app.get("/")
def read_root():
    return FileResponse('index.html')