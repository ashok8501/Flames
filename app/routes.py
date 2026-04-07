from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse

from app.flames_logic import calculate_flames
from app.database import collection

router = APIRouter()


# Home page
@router.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>FLAMES Game</title>
        </head>
        <body>
            <h1>🔥 FLAMES Game</h1>

            <form action="/submit" method="post">
                <input type="text" name="name1" placeholder="Your Name" required><br><br>
                <input type="text" name="name2" placeholder="Partner Name" required><br><br>
                <button type="submit">Check</button>
            </form>
        </body>
    </html>
    """


# Handle form
@router.post("/submit", response_class=HTMLResponse)
def submit(name1: str = Form(...), name2: str = Form(...)):
    result = calculate_flames(name1, name2)

    collection.insert_one({
        "name1": name1,
        "name2": name2,
        "result": result
    })

    return f"""
    <html>
        <body>
            <h2>Result: {result}</h2>
            <a href="/">Try Again</a>
        </body>
    </html>
    """