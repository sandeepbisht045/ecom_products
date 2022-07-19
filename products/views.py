########################################## Project Import ######################################################################

from PIL import Image
import os
from ecom_products.settings import BASE_DIR
from .serializers import ProductSerializer,UpdateProductSerializer
from . models import Product
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


########################################## Project Import ######################################################################



# ADD PRODUCTS TO THE DATABASE
class AddProduct(APIView):
    def post(self,request,format=None):
        req=request.data
        if not req["name"] or not req['details'] or not req['price'] or not req['image']:
            return Response({"message":'fields cannot be empty','status':status.HTTP_400_BAD_REQUEST})

        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":'Product added  Successfully','status':status.HTTP_201_CREATED})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   

# FETCH PEODUCTS FROM THE DATABASE
class GetProduct(APIView):
    def get(self,request,format=None):
        product_id=request.GET.get('id')
        if product_id:
            data_=Product.objects.filter(id=product_id).first()
            if not data_:
                return Response({'data':{},'message':"product id is invalid",'status':status.HTTP_400_BAD_REQUEST})
            serializer=ProductSerializer(data_)

        else:
            data_=Product.objects.all()
            serializer=ProductSerializer(data_,many=True)
        
        return Response({'data':serializer.data,"message":'Product fetched  Successfully','status':status.HTTP_200_OK})


# UPDATE PRODUCT TO THE DATABASE
class UpdateProduct(APIView):
    def put(self,request,format=None):
        req=request.data
        print(req.get("id"))
        try:
            id_object=Product.objects.get(id=req['id'])
        except:
            return Response({'message':'product id is invalid',"status":status.HTTP_400_BAD_REQUEST})

        serializer=UpdateProductSerializer(id_object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":'Product updated  Successfully','status':status.HTTP_200_OK})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# DELETE PRODUCTS FROM THE DATABASE
class DeleteProduct(APIView):
    def delete(self,request,format=None):
        req=request.data
        if not req['id']:
            return Response({'message':'please provide product id',"status":status.HTTP_400_BAD_REQUEST})
        product_ids=req['id'].split(",")

        invalid_prod_ids=[]
        for prod_id in product_ids:
            try:
                prod_id_object=Product.objects.get(id=prod_id)

                if os.path.exists(f'{BASE_DIR}/media/{prod_id_object.image}'):
                    os.remove(f'{BASE_DIR}/media/{prod_id_object.image}')
                prod_id_object.delete()
            
            except:
                invalid_prod_ids.append(prod_id)
        if invalid_prod_ids:
            return Response({'invalid product ids':invalid_prod_ids,"message":'Product deleted  Successfully','status':status.HTTP_200_OK})

        return Response({"message":'Product deleted  Successfully','status':status.HTTP_200_OK})
  