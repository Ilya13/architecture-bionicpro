from functools import lru_cache

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from keycloak import KeycloakError, KeycloakOpenID
from decouple import config


API_KEYCLOAK_URL = config("API_KEYCLOAK_URL")
API_KEYCLOAK_REALM = config("API_KEYCLOAK_REALM")
API_KEYCLOAK_CLIENT_ID = config("API_KEYCLOAK_CLIENT_ID")
API_KEYCLOAK_CLIENT_SECRET = config("API_KEYCLOAK_CLIENT_SECRET")


@lru_cache(maxsize=1, typed=True)
def get_keycloak_client() -> KeycloakOpenID:
    return KeycloakOpenID(
        server_url=API_KEYCLOAK_URL,
        client_id=API_KEYCLOAK_CLIENT_ID,
        realm_name=API_KEYCLOAK_REALM,
        client_secret_key=API_KEYCLOAK_CLIENT_SECRET,
    )


def keycloak_auth(
    jwt_auth: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
    keycloak_client=Depends(get_keycloak_client),
):
    if not keycloak_client:
        return
    if not (jwt_auth):
        raise HTTPException(status_code=401, detail='Not authenticated')
    try:
        if jwt_auth and jwt_auth.scheme == 'Bearer':
            return keycloak_client.decode_token(jwt_auth.credentials)
    except KeycloakError as e:
        raise HTTPException(
            status_code=401,
            detail='Unable to validate credentials or token. ' + str(e),
        )


class RoleChecker:  
  def __init__(self, allowed_roles):  
    self.allowed_roles = allowed_roles  
  
  def __call__(self, user=Depends(keycloak_auth)): 
    for role in self.allowed_roles:
        if role in user["realm_access"]["roles"]:
            return True
    raise HTTPException(status_code=401, detail="You don't have enough permissions")