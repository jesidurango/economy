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

@view_config(route_name='calculate_values', renderer='json')
def calculateValues(request):
    try:
        produc_value = request.POST.get("txtValorProducto")
        quota_value = request.POST.get("txtCuota")
        number_quota = request.POST.get("txtNumeroCuotas")
        total_pay = float(number_quota) * float(quota_value)
        print request.POST.get("txtCuota")
        print request.POST.get("txtNumeroCuotas")
        print produc_value
        new_value = 1234
    except DBAPIError:
        return Response("Error", content_type="text/plain", status_int=500)
    return {'result': new_value, 'total_pay' : total_pay}
