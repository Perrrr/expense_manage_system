import jwt
from typing import Dict
from app import config 

def token_response(token : str):
    return{
        "access token" : token
    }
    
def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, config.JWT_SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except:
        return {}

def signJWT(user_id: str) -> Dict[str, str]:
    token = jwt.encode(user_id, config.JWT_SECRET_KEY, alogorithm=["HS256"])
    return token_response(token)
