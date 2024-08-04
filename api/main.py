import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

# redirect root to /docs
# remove from swagger docs

@app.get("/", include_in_schema=False)
def redirect_root():
    return RedirectResponse("/docs")



@app.get("/hello")
def index():
    return {"details": "Hello, World!"}

def __main__():
    uvicorn.run(app, host="0.0.0.0", port=8000)