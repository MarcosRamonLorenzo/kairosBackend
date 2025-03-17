from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from datetime import datetime


class NotFoundException(Exception):
    def __init__(self, detail: str):
        self.detail = detail

async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status_code": 404,
            "message": f"{exc.detail} not found",
            "error_code": "not_found",
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            },
    )


class GlobalException(Exception):
    def __init__(self):
        self


def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "An unexpected error occurred",
            "error_code": "INTERNAL_SERVER_ERROR",
            "details": "Internal server error", 
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),  
            "path": request.url.path,
        },
    )