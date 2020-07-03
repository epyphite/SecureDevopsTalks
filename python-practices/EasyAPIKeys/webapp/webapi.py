import markdown
import os
import shelve

# Import the framework
from flask import Flask, g, request,jsonify
from flask_restful import Resource, Api, reqparse



# Create an instance of Flask
app = Flask(__name__)
# Create the API
api = Api(app)



class TestRoute(Resource):
    def get(self):
        try:
            api_key = request.headers['apikey']
        except Exception as e:
            return {'message': 'Not Authorized', 'status':"FAIL"}

        if api_key != app.config['APIKEY']:
            return {'message': 'Bad Token', 'status':"FAIL"}
        else:
            return {'message': 'Success', 'status':"OK"}

    def post(self):
        try:
            api_key = request.headers['apikey']
        except Exception as e:
            return {'message': 'Not Authorized', 'status':"FAIL"}

        if api_key != app.config['APIKEY']:
            return {'message': 'Bad Token', 'status':"FAIL"}
        else:        
            json_data = request.get_json(force=True)
            return {'message': 'Success', 'status':"OK"}



@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


api.add_resource(TestRoute, '/test')
