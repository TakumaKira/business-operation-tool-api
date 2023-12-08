import graphene


class JsonPlaceholderPhotoType(graphene.ObjectType):
    id = graphene.ID()
    album_id = graphene.ID()
    title = graphene.String()
    url = graphene.String()
    thumbnail_url = graphene.String()

    def resolve_id(self, info):
        return self.data.get('id', None)

    def resolve_album_id(self, info):
        return self.data.get('albumId', None)

    def resolve_title(self, info):
        return self.data.get('title', None)

    def resolve_url(self, info):
        return self.data.get('url', None)

    def resolve_thumbnail_url(self, info):
        return self.data.get('thumbnailUrl', None)
