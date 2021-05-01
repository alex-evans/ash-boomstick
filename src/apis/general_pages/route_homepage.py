
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')
general_page_router = APIRouter()


@general_page_router.get('/')
async def home(request: Request):
    return templates.TemplateResponse('general_pages/homepage.html', {'request': request})
