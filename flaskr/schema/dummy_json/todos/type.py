import graphene


class DummyJsonTodoType(graphene.ObjectType):
    id = graphene.ID()
    user_id = graphene.ID()
    todo = graphene.String()
    completed = graphene.Boolean()

    def resolve_id(self, info):
        return self.data.get('id', None)

    def resolve_user_id(self, info):
        return self.data.get('userId', None)

    def resolve_todo(self, info):
        return self.data.get('todo', None)

    def resolve_completed(self, info):
        return self.data.get('completed', None)
