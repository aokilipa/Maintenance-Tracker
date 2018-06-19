from flask import Blueprint,jsonify
from flask_restful import Api
from resources.Hello import Hello
from resources.requests import (RequestResource, Request,ApproveRequest,DisapproveRequest,
                                ResolveRequest,GetAllRequest)
from resources.user import UserResource, User

from resources.auth.user_auth import (UserSignup, UserLogin, UserLogoutAccess, UserLogoutRefresh, 
                                    UserSignup, TokenRefresh, AllUsers)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

#Route
api.add_resource(Hello, '/','/Hello')
api.add_resource(RequestResource, '/users/requests','/users/requests/', endpoint ="requests")
api.add_resource(Request, '/users/requests/<int:req_id>','/users/requests/<int:req_id>/', endpoint ="request" )
api.add_resource(UserResource, '/users','/users/')
api.add_resource(User, '/users/<int:uid>','/users/<int:uid>/')

#authentication endpoints
api.add_resource(UserSignup, '/auth/signup', '/auth/signup/')
api.add_resource(UserLogin, '/auth/login')
api.add_resource(UserLogoutAccess, '/auth/logout/access')
api.add_resource(UserLogoutRefresh, '/auth/logout/refresh')
api.add_resource(TokenRefresh, '/auth/token/refresh')
api.add_resource(AllUsers, '/users')

#Admin functions
api.add_resource(GetAllRequest,'/requests/','/requests')
api.add_resource(ApproveRequest, '/requests/<int:req_id>/approve')
api.add_resource(DisapproveRequest, '/requests/<int:req_id>/disapprove')
api.add_resource(ResolveRequest, '/requests/<int:req_id>/resolve')
