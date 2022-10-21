from fastapi import FastAPI

from api.routers import feed, update

app = FastAPI()
app.include_router(feed.router)
app.include_router(update.router)


@app.get("/")
async def root():
    return {"message": "root OK"}


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}


def main():
    import uvicorn

    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
