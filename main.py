from flask import Flask
from flask_graphql import GraphQLView
from app.database import init_db
from app.schema import schema

app = Flask(__name__)

# GraphQL route
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

# Entry point
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5001)
