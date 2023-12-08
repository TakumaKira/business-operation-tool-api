import graphene


class FakeStoreProductType(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    price = graphene.Float()
    description = graphene.String()
    category = graphene.String()
    image = graphene.String()
    rating = graphene.JSONString()  # Assuming rating is a nested object

    def resolve_id(self, info):
        return self.data.get('id', None)

    def resolve_title(self, info):
        return self.data.get('title', None)

    def resolve_price(self, info):
        return self.data.get('price', None)

    def resolve_description(self, info):
        return self.data.get('description', None)

    def resolve_category(self, info):
        return self.data.get('category', None)

    def resolve_image(self, info):
        return self.data.get('image', None)

    def resolve_rating(self, info):
        return self.data.get('rating', None)
