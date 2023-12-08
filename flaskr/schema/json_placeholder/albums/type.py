import graphene


class JsonPlaceholderAlbumType(graphene.ObjectType):
    id = graphene.ID()
    user_id = graphene.ID()
    title = graphene.String()

    def resolve_id(self, info):
        return self.data.get('id', None)

    def resolve_user_id(self, info):
        return self.data.get('userId', None)

    def resolve_title(self, info):
        return self.data.get('title', None)
