from django.http import JsonResponse
from .models import Product, Manufacturer

def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())} #"id", "name"
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {
            "product": {
                "name": product.name,
                "description": product.description,
                "manufacturer": product.manufacturer.name,
                "price": product.price,
                "quantity": product.quantity,
                "shipping_cost": product.shipping_cost,
                "photo": product.photo.url
            }
        }
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "status": "ERROR",
                "message": "Product not found!!!"
            }
        }, status=404)
    return response

def manufacturer_list(request):
    manufacturer_list = Manufacturer.objects.filter(active=True)
    data = {"manufacturer_list": list(manufacturer_list.values())}
    response = JsonResponse(data)
    return response

def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_product = manufacturer.products.all()


        data = {
            "manufacturer": {
                "id": pk,
                "name": manufacturer.name,
                "location": manufacturer.location,
                "active": manufacturer.active,
                "products": list(manufacturer_product.values())
            }
        }
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "status": "ERROR",
                "message": "Manufacturer not found!!!"
            }
        }, status=404)
    return response