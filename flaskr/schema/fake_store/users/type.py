import graphene


class FakeStoreUserType(graphene.ObjectType):
    id = graphene.ID()
    address = graphene.JSONString()  # Assuming rating is a nested object
    email = graphene.String()
    username = graphene.String()
    # password = graphene.String() # Should not retrieve password
    name = graphene.JSONString()  # Assuming rating is a nested object
    phone = graphene.String()

    def resolve_id(self, info):
        return self.data.get('id', None)

    def resolve_address(self, info):
        return self.data.get('address', None)

    def resolve_email(self, info):
        return self.data.get('email', None)

    def resolve_username(self, info):
        return self.data.get('username', None)

    # def resolve_password(self, info):
    #     return self.data.get('password', None)

    def resolve_name(self, info):
        return self.data.get('name', None)

    def resolve_phone(self, info):
        return self.data.get('phone', None)
