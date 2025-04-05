from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from datetime import datetime
import pycountry
import os
import json


app = FastAPI()



static_folder = os.path.join(os.path.dirname(__file__), "static")
templates_folder = os.path.join(os.path.dirname(__file__), "templates")
app.mount("/static", StaticFiles(directory=static_folder), name="static")
templates = Jinja2Templates(directory=templates_folder)


year = datetime.now().year



@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "year": year,
            
        },
    )


@app.get("/shop", response_class=HTMLResponse)
def shop_swag(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="shop.html",
        context={"year": year},
    )

@app.get("/register", response_class=HTMLResponse)
def register(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={"year": year},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
