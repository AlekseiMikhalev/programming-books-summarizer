from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from users.models.request.users import SignupReq, UserReq, UserStatus, UserDetails
from users.models.data.users import Signup, Login, User
from users.services.signup import UserSignupService
from users.services.login import UserLoginService
from users.services.users import UserService

from uuid import uuid4
from json import loads

router = APIRouter()


@router.post('/users/signup')
def signup_users(signup: Signup):
    account: Signup = Signup(user_id=signup.user_id, username=signup.username,
                             password=signup.password, sign_id=uuid4().int)
    signup_service = UserSignupService()
    result = signup_service.add_signup(account)
    if result == True:
        return jsonable_encoder(account)
    else:
        return JSONResponse(content={
            'message': 'insertion problem encountered'
        }, status_code=500)


@router.get('/account/signup/approved')
def approved_signup(sign_id: int):
    signup_service: UserSignupService = UserSignupService()
    account = signup_service.get_signup(sign_id)
    if not account == None:
        login = Login(user_id=account.sign_id, user_id=account.user_id, username=account.username, password=account.password)
        login_service: UserLoginService = UserLoginService()
        login_service.add_user_login(login)
        signup_service.delete_signup(sign_id)
        return jsonable_encoder(account)
    else:
        return JSONResponse(content={
            'message': 'signup account does not exist'
        }, status_code=500)


@router.post('/login/account')
def login_app(username: str, password: str):
    login_service: UserLoginService = UserLoginService()
    login = login_service.get_user_login(username)
    if login.password == password:
        return jsonable_encoder(login)
    else:
        return JSONResponse(content={
            'message': 'login account does not exist'
        }, status_code=500)


@router.post('/login/password/change')
def change_password(user_id: int, newpass: str):
    login_service: UserLoginService = UserLoginService()
    result = login_service.update_login_password(user_id, newpass)
    if result:
        return JSONResponse(content={
            'message': 'password changed successfully'
        }, status_code=201)
    else:
        return JSONResponse(content={
            'message': 'change password error'
        }, status_code=500)


@router.post('/profile/add')
def create_profile(profile: UserReq):
    user = User(user_id=profile.user_id, fname=profile.fname,
                lname=profile.lname, status=profile.status)
    user_service: UserService = UserService()
    result = user_service.add_user(user)
    if result:
        return jsonable_encoder(user)
    else:
        return JSONResponse(content={
            'message': 'user profile not created'
        }, status_code=500)


@router.patch('/profile/update')
def update_profile(user_id: int, profile_details: UserDetails):
    profile_dict = profile_details.dict(exclude_unset=True)
    user_service: UserService = UserService()
    result = user_service.update_user(user_id, profile_dict)
    if result:
        return JSONResponse(content={
            'message': 'profile updated successfully'
        }, status_code=500)
    else:
        return JSONResponse(content={
            'message': 'update profile error'
        }, status_code=500)


@router.get('/profile/list/all')
def list_users():
    user_service: UserService = UserService()
    user_list = user_service.list_users()
    return jsonable_encoder(user_list)
