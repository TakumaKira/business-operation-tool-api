import graphene


class DummyJsonProductType(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    price = graphene.Float()
    discount_percentage = graphene.Float()
    rating = graphene.Float()
    stock = graphene.Int()
    brand = graphene.String()
    category = graphene.String()
    thumbnail = graphene.String()
    images = graphene.JSONString()

    def resolve_id(self, info):
        return self.data.get('id', None)

    def resolve_title(self, info):
        return self.data.get('title', None)

    def resolve_description(self, info):
        return self.data.get('description', None)

    def resolve_price(self, info):
        return self.data.get('price', None)

    def resolve_discount_percentage(self, info):
        return self.data.get('discountPercentage', None)

    def resolve_rating(self, info):
        return self.data.get('rating', None)

    def resolve_stock(self, info):
        return self.data.get('stock', None)

    def resolve_brand(self, info):
        return self.data.get('brand', None)

    def resolve_thumbnail(self, info):
        return self.data.get('thumbnail', None)

    def resolve_images(self, info):
        return self.data.get('images', None)
