import graphene


class DummyJsonCommentType(graphene.ObjectType):
    id = graphene.ID()
    post_id = graphene.ID()
    body = graphene.String()
    user = graphene.JSONString()

    def resolve_id(self, info):
        return self.data.get('id', None)

    def resolve_post_id(self, info):
        return self.data.get('postId', None)

    def resolve_body(self, info):
        return self.data.get('body', None)

    def resolve_user(self, info):
        return self.data.get('user', None)
