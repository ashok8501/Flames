from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse

from app.flames_logic import calculate_flames
from app.database import collection

router = APIRouter()


# Home Page (loads HTML file)
@router.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()


# Result Page
@router.post("/submit", response_class=HTMLResponse)
def submit(name1: str = Form(...), name2: str = Form(...)):
    result = calculate_flames(name1, name2)

    # Save data
    collection.insert_one({
        "name1": name1,
        "name2": name2,
        "result": result
    })

    # Emojis
    emojis = {
        "Friends": "😄",
        "Love": "❤️",
        "Affection": "🥰",
        "Marriage": "💍",
        "Enemies": "💀",
        "Siblings": "👫"
    }

    # Telugu fun lines
    telugu_lines = {
        "Friends": "Meeru best friends ra 😄",
        "Love": "Idi love kadhu ra… pure love ❤️",
        "Affection": "Chala caring undi mee madhya 🥰",
        "Marriage": "Pelli fix ayyindi 💍😂",
        "Enemies": "Idhi danger zone 💀",
        "Siblings": "Brother sister vibes 😂"
    }

    emoji = emojis.get(result, "✨")
    line = telugu_lines.get(result, "Super combo 🔥")

    return f"""<!DOCTYPE html>
<html>
<head>
    <title>Result</title>

    <style>
        body {{
            font-family: Arial;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #667eea, #764ba2);
            text-align: center;
        }}

        .box {{
            background: white;
            color: black;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
            animation: fadeIn 0.8s ease-in-out;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: scale(0.8); }}
            to {{ opacity: 1; transform: scale(1); }}
        }}

        .emoji {{
            font-size: 45px;
        }}

        h2 {{
            margin: 10px 0;
        }}

        p {{
            margin: 8px 0;
        }}

        a {{
            display: inline-block;
            margin-top: 15px;
            text-decoration: none;
            background: #ff4b5c;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
        }}

        a:hover {{
            background: #e63b4c;
        }}
    </style>
</head>

<body>

    <div class="box">
        <div class="emoji">{emoji}</div>
        <h2>{result}</h2>
        <p><b>{line}</b></p>
        <p>{name1} ❤️ {name2}</p>
        <a href="/">Malli Try Chey 😄</a>
    </div>

</body>
</html>
"""