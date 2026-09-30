from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"request": request})

@router.post("/generate")
async def generate(request: Request, story: str = Form("")):
    return templates.TemplateResponse(request, "result.html", {"request": request, "story": story})

@router.get("/success")
async def success(request: Request):
    return templates.TemplateResponse(request, "success.html", {"request": request})