# from django.shortcuts import render
# from inmuebleslist_app.models import Inmueble
# from django.http import JsonResponse

# # Create your views here.
# def inmueble_list(request):
#     inmuebles = Inmueble.objects.all()

#     data = {
#         'inmuebles': list(inmuebles.values())
#     }

#     return JsonResponse(data)

# def inmuble_detalle(request, pk):
#     inmuble = Inmueble.objects.get(pk=pk)

#     data = {
#         'direccion': inmuble.direccion,
#         'pais': inmuble.pais,
#         'imagen': inmuble.imagen,
#         'active': inmuble.active,
#         'descripcion': inmuble.descripcion,
#     }

#     return JsonResponse(data)