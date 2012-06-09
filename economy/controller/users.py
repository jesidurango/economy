import datetime
import transaction
from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from economy.models import (
    DBSession,
    User,
)

@view_config(route_name='user_init', renderer='master/user.jinja2')
def calculateInit(request):
    try:
        print "Hi i am here"
    except DBAPIError:
        return Response("Error", content_type='text/plain', status_int=500)
    return {'empty':'empty'}

@view_config(route_name='user_save', renderer='json')
def save(request):
    result = {"result" : "el ususario se guardo correctamente"}
    try:
        userName = request.POST.get("txtUserName")
        password = request.POST.get("txtPassword")
        with transaction.manager:
            user = User( userName, password, datetime.datetime.now() )
            DBSession.add(user)
    except DBAPIError:
        return Response("Error", content_type='text/plain', status_int=500)
    return result

