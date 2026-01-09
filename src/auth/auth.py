from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/basicAuth")
def base_auth(credentials: Annotated[HTTPBasicCredentials, Depends]):
    pass