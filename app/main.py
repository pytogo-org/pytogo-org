from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# from api.auth import router as auth_router



from database  import (
    get_all_events,
    get_swags,
    get_teams_members,
    get_event_by_id,
    get_parteners,
    get_heros,
    galleries,
)
from datetime import datetime
import pycountry
import os
import json


app = FastAPI()
# app.include_router(auth_router, tags=["authentication"])


static_folder = os.path.join(os.path.dirname(__file__), "static")
templates_folder = os.path.join(os.path.dirname(__file__), "templates")
app.mount("/static", StaticFiles(directory=static_folder), name="static")
templates = Jinja2Templates(directory=templates_folder)
teams_members = get_teams_members()

year = datetime.now().year

flags = [
    pycountry.countries.get(alpha_2="US").flag,
    pycountry.countries.get(alpha_2="TG").flag,
]

languages = [
    {"name": "English", "code": "En", "flag": flags[0]},
    {"name": "French", "code": "Fr", "flag": flags[1]},
]


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"year": year, "languages": languages, "teams": teams_members, "partners": get_parteners(), "heros": get_heros() },
    )


@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={"year": year, "languages": languages},
    )


@app.get("/events")
def events(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="events.html",
        context={"year": year, "languages": languages},
    )

@app.get("/coc")
def coc(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="coc.html",
        context={"year": year, "languages": languages},
    )

@app.get("/mission_vision")
def mission_vision(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="mission_vision.html",
        context={"year": year, "languages": languages},
    )

@app.get("/shop", response_class=HTMLResponse)
def shop_swag(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="shop.html",
        context={"year": year, "languages": languages},
    )

@app.get("/gallery")
def gallery(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="gallery.html",
        context={"year": year, "languages": languages, "galleries": galleries},
    )

@app.get("/galleries")
def gallery_dash(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="gallery-dash.html",
        context={"year": year, "languages": languages},
    )

@app.get("/blogs")
def blog(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="blog.html",
        context={"year": year, "languages": languages},
    )

@app.get("/api/shop/swags", response_class=JSONResponse)
def swags(request: Request):
   
    return get_swags()

@app.get("/api/events", response_class=JSONResponse)
async def get_events(request: Request):
    return get_all_events()

@app.get("/api/events/{eventId}", response_class=JSONResponse)
async def get_event(eventId: int):
    return get_event_by_id(eventId)



@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context={"year": year, "languages": languages},
    )

@app.get("/admin", response_class=HTMLResponse)
def admin(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="admin.html",
        context={"year": year, "languages": languages},
    )

@app.get("/add-event", response_class=HTMLResponse)
def add_event(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="add-event.html",
        context={"year": year, "languages": languages},
    )

@app.get("/members")
def members(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="members.html",
        context={"year": year, "languages": languages},
    )

@app.get("/signup", response_class=HTMLResponse)
def signup(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="signup.html",
        context={"year": year, "languages": languages},
    )

@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"year": year, "languages": languages},
    )




if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
