from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import  FileResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()


templates = Jinja2Templates(directory="templates")
favicon_path = 'favicon.png'


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index2.html", {"request": request})


@app.get("/gallery")
async def contact(request: Request):
    return templates.TemplateResponse("gallery.html", {"request": request})


@app.get("/contact")
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})


@app.get("/aboutme")
async def aboutme(request: Request):
    return templates.TemplateResponse("aboutme.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

