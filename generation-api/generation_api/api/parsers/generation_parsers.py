from flask_restx import reqparse, inputs

generation_parser = reqparse.RequestParser()
generation_parser.add_argument('message', type=str, required=True, help='Message')