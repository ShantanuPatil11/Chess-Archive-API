from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import engine, Base

from app.routes.import_routes import router as import_router
from app.routes.game_routes import router as game_router
from app.routes.analytics_routes import router as analytics_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Chess Archive API"
)

app.include_router(import_router)
app.include_router(game_router)
app.include_router(analytics_router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def api_home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html"
    )


@app.get("/viewer")
def viewer(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )