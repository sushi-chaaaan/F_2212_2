from fastapi import FastAPI

from api.routers import feed

app = FastAPI()
app.include_router(feed.router)


@app.get("/")
async def root():
    return {"message": "root OK"}


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}


def export_yaml():
    import yaml

    openapi_schema = app.openapi()
    with open("openapi.yaml", "w") as f:
        yaml.dump(openapi_schema, f)


def main():
    import uvicorn

    # export_yaml()

    uvicorn.run("api.main:app", host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
