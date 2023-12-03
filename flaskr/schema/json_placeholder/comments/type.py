import graphene


class JsonPlaceholderCommentType(graphene.ObjectType):
    id = graphene.ID()
    post_id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    body = graphene.String()

    def resolve_post_id(self, info):
        return self.data.get('postId', None)

    def resolve_name(self, info):
        return self.data.get('name', None)

    def resolve_email(self, info):
        return self.data.get('email', None)

    def resolve_body(self, info):
        return self.data.get('body', None)
