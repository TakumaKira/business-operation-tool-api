import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import DummyJsonQuoteType
from .model import DummyJsonQuoteModel


class DummyJsonQuoteQuery(graphene.ObjectType):
    dummy_json_quotes = graphene.List(DummyJsonQuoteType)
    dummy_json_quote_by_id = graphene.Field(DummyJsonQuoteType, id=graphene.Int(required=True))

    def resolve_dummy_json_quotes(self, info):
        _fetch_and_store_data()
        return list(DummyJsonQuoteModel.objects.all())

    def resolve_dummy_json_quote_by_id(self, info, id):
        _fetch_and_store_data()
        return DummyJsonQuoteModel.objects.filter(id=id).first()


def _fetch_and_store_data():
    fetch_and_store_data(f"{BASE_URL}/quotes", DummyJsonQuoteModel, lambda data: data.get('quotes'))
