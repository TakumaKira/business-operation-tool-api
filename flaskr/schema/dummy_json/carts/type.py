import graphene


class DummyJsonCartType(graphene.ObjectType):
    id = graphene.ID()
    user_id = graphene.ID()
    products = graphene.JSONString()
    total = graphene.Int()
    discounted_total = graphene.Int()
    total_products = graphene.Int()
    total_quantity = graphene.Int()

    def resolve_id(self, info):
        return self.data.get('id', None)

    def resolve_user_id(self, info):
        return self.data.get('userId', None)

    def resolve_products(self, info):
        return self.data.get('products', None)

    def resolve_total(self, info):
        return self.data.get('total', None)

    def resolve_discounted_total(self, info):
        return self.data.get('discountedTotal', None)

    def resolve_total_products(self, info):
        return self.data.get('totalProducts', None)

    def resolve_total_quantity(self, info):
        return self.data.get('totalQuantity', None)
