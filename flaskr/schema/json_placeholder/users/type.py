import graphene


class JsonPlaceholderUserType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    username = graphene.String()
    email = graphene.String()
    address = graphene.JSONString()  # Assuming rating is a nested object
    phone = graphene.String()
    website = graphene.String()
    company = graphene.JSONString()

    def resolve_id(self, info):
        return self.data.get('id', None)

    def resolve_name(self, info):
        return self.data.get('name', None)

    def resolve_username(self, info):
        return self.data.get('username', None)

    def resolve_email(self, info):
        return self.data.get('email', None)

    def resolve_address(self, info):
        return self.data.get('address', None)

    def resolve_phone(self, info):
        return self.data.get('phone', None)

    def resolve_website(self, info):
        return self.data.get('website', None)

    def resolve_company(self, info):
        return self.data.get('company', None)
