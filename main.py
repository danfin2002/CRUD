from fastapi import FastAPI
from crud import router as crud_router
import uvicorn

app = FastAPI()
app.include_router(crud_router)


if __name__ == "__main__":
      uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
      #uvicorn.run("main:app", reload=True)