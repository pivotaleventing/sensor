from fastapi import FastAPI
from uvicorn import run


app = FastAPI()

@app.get('/', response_model=dict)
async def index() -> dict:
    return {'msg': 'Hello, Google Cloud Run!')


if __name__ == '__main__':
    run(app=app, host='', port=8080)
