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
        tax = ((float(total_pay) / float(produc_value)))**(1.0/float(number_quota))
        print produc_value
    except DBAPIError:
        return Response("Error", content_type="text/plain", status_int=500)
    return {'total_pay' : total_pay, 'tax' : tax}
