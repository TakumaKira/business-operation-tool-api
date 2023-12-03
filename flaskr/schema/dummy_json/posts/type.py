import graphene


class DummyJsonPostType(graphene.ObjectType):
    id = graphene.ID()
    user_id = graphene.ID()
    title = graphene.String()
    body = graphene.String()
    tags = graphene.JSONString()
    reactions = graphene.Int()

    def resolve_id(self, info):
        return self.data.get('id', None)

    def resolve_user_id(self, info):
        return self.data.get('userId', None)

    def resolve_title(self, info):
        return self.data.get('title', None)

    def resolve_body(self, info):
        return self.data.get('body', None)

    def resolve_tags(self, info):
        return self.data.get('tags', None)

    def resolve_reactions(self, info):
        return self.data.get('reactions', None)
