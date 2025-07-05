from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from endpoints.page_endpoints import router as router_page
from endpoints.processing_endpoints import router as router_processing


app = FastAPI()
app.include_router(router_page)
app.include_router(router_processing)
app.mount("/app/static", StaticFiles(directory="app/static"), name="static")


if __name__ == "__main__":
    uvicorn.run('main:app', port=1111)