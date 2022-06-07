from fastapi import HTTPException

def err_response(status_code, message):
    raise HTTPException(
        status_code=status_code,
        detail={"message": message},
    )