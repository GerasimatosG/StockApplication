from fastapi import FastAPI
from controllers.itemController import router


app = FastAPI()

app.include_router(router)

# uvicorn main:app --port 8040 --reload
