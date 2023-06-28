import routes.note
from routes.note import note
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

app = FastAPI()
app.mount(path = "/static", app = StaticFiles(directory="static"), name="static")  # Taken from FastAPI
# official
# website
app.include_router(note)
