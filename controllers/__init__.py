from fastapi import APIRouter

import controllers.auth
import controllers.protected

router = APIRouter(prefix="/api")

router.include_router(controllers.auth.router)
router.include_router(controllers.protected.router)
