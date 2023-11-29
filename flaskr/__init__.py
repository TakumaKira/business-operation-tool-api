from flask import Flask
from flask_graphql.graphqlview import GraphQLView
from .schema import schema


def create_app():
    app = Flask(__name__)

    app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))

    return app
