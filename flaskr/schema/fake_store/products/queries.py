import graphene
import requests
from .type import FakeStoreProductType
from .model import FakeStoreProductModel


class FakeStoreProductQuery(graphene.ObjectType):
    fake_store_products = graphene.List(FakeStoreProductType)

    def resolve_fake_store_products(self, info):
        if FakeStoreProductModel.objects.count() == 0:
            print("Get Products data from Fake Store API")
            response = requests.get("https://fakestoreapi.com/products")
            products = response.json()

            for product_data in products:
                product = FakeStoreProductModel(data=product_data)
                product.save()

        return list(FakeStoreProductModel.objects.all())
