import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import DummyJsonQuoteType
from .model import DummyJsonQuoteModel


class DummyJsonQuoteQuery(graphene.ObjectType):
    dummy_json_quotes = graphene.List(DummyJsonQuoteType)

    def resolve_dummy_json_quotes(self, info):
        fetch_and_store_data(f"{BASE_URL}/quotes", DummyJsonQuoteModel, lambda data: data.get('quotes'))
        return list(DummyJsonQuoteModel.objects.all())
