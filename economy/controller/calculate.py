from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

@view_config(route_name='calculate_init', renderer='calculate/calculate.pt')
def calculateInit(request):
    try:
        print "Hi i am here"
    except DBAPIError:
        return Response("Error", content_type='text/plain', status_int=500)
    return {'empty':'empty'}

@view_config(route_name='calculate_values', renderer='calculate/calculate.pt')
def calculateValues(request):
    try:
        produc_value = request.GET.get("txtValorProducto")
        print produc_value
        new_value = 0
    except DBAPIError:
        return Response("Error", content_type="text/plain", status_int=500)
    return {'result': new_value}
