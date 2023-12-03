import graphene


class FakeStoreCartType(graphene.ObjectType):
    id = graphene.ID()
    user_id = graphene.ID()
    date = graphene.String()
    products = graphene.JSONString()  # Assuming rating is a nested object

    def resolve_id(self, info):
        return self.data.get('id', None)

    def resolve_user_id(self, info):
        return self.data.get('userId', None)

    def resolve_date(self, info):
        return self.data.get('date', None)

    def resolve_products(self, info):
        return self.data.get('products', None)
