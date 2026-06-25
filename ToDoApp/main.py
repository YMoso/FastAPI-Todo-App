from fastapi import FastAPI, Request
from .models import Base
from .database import engine
from .routers import auth, todos, admin, users
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="ToDoApp/static"), name="static")

templates = Jinja2Templates(directory="ToDoApp/templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "user": None})


@app.get("/healthy")
def healthy_check():
    return {"status": "healthy"}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)