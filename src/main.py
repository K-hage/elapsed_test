from fastapi import FastAPI, HTTPException
from src.routers import router as test_router

app = FastAPI(
    title='Elapsed Test'
)

app.include_router(test_router)


@app.get('/{path:path}', include_in_schema=False)
async def get_any(path: str):
    raise HTTPException(status_code=404, detail='Страница не найдена')
