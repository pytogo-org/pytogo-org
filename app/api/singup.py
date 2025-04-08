from typing import Optional

from fastapi import APIRouter, HTTPException, Response, status
from pydantic import BaseModel, EmailStr, validator

from app.api.auth import (
    User,
    UserCreate,
    create_access_token,
    fake_users_db,
    get_password_hash,
)

router = APIRouter(tags=["signup"])


class SignupResponse(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    message: str


class SignupForm(BaseModel):
    username: str
    email: EmailStr
    password: str
    password_confirm: str
    full_name: Optional[str] = None

    @validator("username")
    def username_must_be_valid(cls, v):
        if len(v) < 3:
            raise ValueError("Username must be at least 3 characters")
        if not v.isalnum():
            raise ValueError("Username must contain only alphanumeric characters")
        return v

    @validator("password")
    def password_must_be_strong(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        return v

    @validator("password_confirm")
    def passwords_match(cls, v, values):
        if "password" in values and v != values["password"]:
            raise ValueError("Passwords do not match")
        return v


@router.post(
    "/signup", response_model=SignupResponse, status_code=status.HTTP_201_CREATED
)
async def signup(form_data: SignupForm, response: Response):
    """
    Register a new user and optionally create a session
    """
    # Check if username already exists
    if form_data.username in fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )

    # Check if email already exists
    for user in fake_users_db.values():
        if user.get("email") == form_data.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

    # Create user with hashed password
    hashed_password = get_password_hash(form_data.password)

    user_dict = {
        "username": form_data.username,
        "email": form_data.email,
        "full_name": form_data.full_name,
        "hashed_password": hashed_password,
        "disabled": False,
    }

    fake_users_db[form_data.username] = user_dict

    # Generate access token (for automatic login)
    access_token = create_access_token(data={"sub": form_data.username})

    # Set cookie for automatic session (optional)
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,
        secure=True,  # Set to True in production with HTTPS
        samesite="lax",
    )

    return {
        "username": form_data.username,
        "email": form_data.email,
        "full_name": form_data.full_name,
        "message": "User successfully registered",
    }


@router.get("/check-username/{username}")
async def check_username_availability(username: str):
    """
    Check if a username is available (for frontend validation)
    """
    if username in fake_users_db:
        return {"available": False}
    return {"available": True}


@router.get("/check-email/{email}")
async def check_email_availability(email: str):
    """
    Check if an email is available (for frontend validation)
    """
    for user in fake_users_db.values():
        if user.get("email") == email:
            return {"available": False}
    return {"available": True}
