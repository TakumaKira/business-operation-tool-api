import graphene


class DummyJsonUserType(graphene.ObjectType):
    id = graphene.ID()
    first_name = graphene.String()
    last_name = graphene.String()
    maiden_name = graphene.String()
    age = graphene.Int()
    gender = graphene.String()
    email = graphene.String()
    phone = graphene.String()
    username = graphene.String()
    # password = graphene.String() # Should not retrieve password
    birth_date = graphene.String()
    image = graphene.String()
    blood_group = graphene.String()
    height = graphene.Float()
    weight = graphene.Float()
    eye_color = graphene.String()
    hair = graphene.JSONString()
    domain = graphene.String()
    ip = graphene.String()
    address = graphene.JSONString()  # Assuming rating is a nested object
    mac_address = graphene.String()
    university = graphene.String()
    bank = graphene.JSONString()
    company = graphene.JSONString()
    ein = graphene.String()
    ssn = graphene.String()
    user_agent = graphene.String()

    def resolve_id(self, info):
        return self.data.get('id', None)

    def resolve_first_name(self, info):
        return self.data.get('firstName', None)

    def resolve_last_name(self, info):
        return self.data.get('lastName', None)

    def resolve_maiden_name(self, info):
        return self.data.get('maidenName', None)

    def resolve_age(self, info):
        return self.data.get('age', None)

    def resolve_gender(self, info):
        return self.data.get('gender', None)

    def resolve_email(self, info):
        return self.data.get('email', None)

    def resolve_phone(self, info):
        return self.data.get('phone', None)

    def resolve_username(self, info):
        return self.data.get('username', None)

    # def resolve_password(self, info):
    #     return self.data.get('password', None)

    def resolve_birth_date(self, info):
        return self.data.get('birthDate', None)

    def resolve_image(self, info):
        return self.data.get('image', None)

    def resolve_blood_group(self, info):
        return self.data.get('bloodGroup', None)

    def resolve_height(self, info):
        return self.data.get('height', None)

    def resolve_weight(self, info):
        return self.data.get('weight', None)

    def resolve_eye_color(self, info):
        return self.data.get('eyeColor', None)

    def resolve_hair(self, info):
        return self.data.get('hair', None)

    def resolve_domain(self, info):
        return self.data.get('domain', None)

    def resolve_ip(self, info):
        return self.data.get('ip', None)

    def resolve_address(self, info):
        return self.data.get('address', None)

    def resolve_mac_address(self, info):
        return self.data.get('macAddress', None)

    def resolve_university(self, info):
        return self.data.get('university', None)

    def resolve_bank(self, info):
        return self.data.get('bank', None)

    def resolve_company(self, info):
        return self.data.get('company', None)

    def resolve_ein(self, info):
        return self.data.get('ein', None)

    def resolve_ssn(self, info):
        return self.data.get('ssn', None)

    def resolve_user_agent(self, info):
        return self.data.get('userAgent', None)
