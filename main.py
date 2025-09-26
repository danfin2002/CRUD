from fastapi import FastAPI
from crud import router as crud_router
import uvicorn

app = FastAPI()
app.include_router(crud_router)



if __name__ == "__main__":
     uvicorn.run("main:app", reload=True)