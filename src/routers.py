from time import monotonic

from fastapi import APIRouter

from src.schemas import TestResponse
from src.utils import work

router = APIRouter(
    prefix='',
    tags=['Test']
)


@router.get('/test', response_model=TestResponse)
async def handler() -> TestResponse:
    ts1 = monotonic()
    await work()
    ts2 = monotonic()
    return TestResponse(elapsed=ts2 - ts1)
