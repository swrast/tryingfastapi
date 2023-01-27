from fastapi import APIRouter, Depends

from lib.auth import AuthDependency, UserMetadata

router = APIRouter(prefix="/protected")


@router.get("/user", dependencies=[Depends(AuthDependency())])
async def user():
    return "ok"


@router.get("/all")
async def _all(data: UserMetadata = Depends(AuthDependency())):
    return data
