from datetime import datetime, timedelta
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from .auth import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    Token,
    User,
    authenticate_user,
    create_access_token,
    fake_users_db,
    get_current_active_user,
)

router = APIRouter(tags=["login"])


class LoginForm(BaseModel):
    username: str
    password: str
    remember_me: bool = False


# Model for login response
class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: User


@router.post("/login", response_model=LoginResponse)
async def login(form_data: LoginForm, response: Response):
    """
    User login endpoint that authenticates and creates a session
    """
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Set token expiration based on remember_me option
    if form_data.remember_me:
        expires_delta = timedelta(days=30)  # Longer session for remember_me
    else:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Create access token
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=expires_delta
    )

    # Set cookie for persistent session
    cookie_max_age = (
        int(expires_delta.total_seconds()) if form_data.remember_me else None
    )
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,
        secure=True,  # Set to True in production with HTTPS
        samesite="lax",
        max_age=cookie_max_age,
    )

    # Return the user info along with the token
    user_data = {
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "disabled": user.disabled,
    }

    return {"access_token": access_token, "token_type": "bearer", "user": user_data}


@router.post("/logout")
async def logout(response: Response):
    """
    Logout endpoint that clears the session cookie
    """
    response.delete_cookie(key="access_token")
    return {"message": "Successfully logged out"}


@router.get("/session", response_model=User)
async def get_session(current_user: User = Depends(get_current_active_user)):
    """
    Get the current user's session information
    """
    return current_user


# Optional: Auto-login with cookie
@router.get("/auto-login", response_model=User)
async def auto_login(current_user: User = Depends(get_current_active_user)):
    """
    Endpoint for automatic login using the session cookie
    """
    return current_user
