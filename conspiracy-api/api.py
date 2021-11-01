from flask import Flask
from flask_graphql import GraphQLView
import graphene
from schema.query.question_query import QuestionQuery

app = Flask(__name__)
app.debug = True

schema = graphene.Schema(query=QuestionQuery)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    pass

if __name__ == '__main__':
    app.run()