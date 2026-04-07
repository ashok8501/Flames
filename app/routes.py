from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.models import FlamesInput
from app.flames_logic import calculate_flames
from app.database import collection

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# UI Page
@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# API (JSON)
@router.post("/flames")
def get_flames(data: FlamesInput):
    result = calculate_flames(data.name1, data.name2)

    collection.insert_one({
        "name1": data.name1,
        "name2": data.name2,
        "result": result
    })

    return {"result": result}


# Form Submission
@router.post("/submit", response_class=HTMLResponse)
def submit(request: Request, name1: str = Form(...), name2: str = Form(...)):
    result = calculate_flames(name1, name2)

    collection.insert_one({
        "name1": name1,
        "name2": name2,
        "result": result
    })

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": result}
    )