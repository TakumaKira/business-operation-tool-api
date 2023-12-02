import graphene


class FakeStoreCartType(graphene.ObjectType):
    user_id = graphene.Int()
    date = graphene.String()
    products = graphene.JSONString()  # Assuming rating is a nested object

    def resolve_user_id(self, info):
        return self.data.get('userId', None)

    def resolve_date(self, info):
        return self.data.get('date', None)

    def resolve_products(self, info):
        return self.data.get('products', None)
