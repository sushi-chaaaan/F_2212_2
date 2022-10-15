from fastapi import APIRouter

router = APIRouter()


@router.get("/update")
async def return_update_feed():
    pass
