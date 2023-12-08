import graphene


class JsonPlaceholderTodoType(graphene.ObjectType):
    id = graphene.ID()
    user_id = graphene.ID()
    title = graphene.String()
    completed = graphene.Boolean()

    def resolve_id(self, info):
        return self.data.get('id', None)

    def resolve_user_id(self, info):
        return self.data.get('userId', None)

    def resolve_title(self, info):
        return self.data.get('title', None)

    def resolve_completed(self, info):
        return self.data.get('completed', None)
