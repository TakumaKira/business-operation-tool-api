import graphene


class DummyJsonQuoteType(graphene.ObjectType):
    id = graphene.ID()
    quote = graphene.String()
    author = graphene.String()

    def resolve_id(self, info):
        return self.data.get('id', None)

    def resolve_quote(self, info):
        return self.data.get('quote', None)

    def resolve_author(self, info):
        return self.data.get('author', None)
