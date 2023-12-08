from flask import Flask
from flask_graphql.graphqlview import GraphQLView
from .database import init_db
from .schema import schema


def create_app():
    app = Flask(__name__)
    app.debug = True

    app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))

    init_db()

    return app
