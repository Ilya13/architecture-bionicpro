class APIException(Exception):
    message: str = 'API Error'
    status_code: int = 400
