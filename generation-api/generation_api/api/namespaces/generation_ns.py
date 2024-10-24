from flask_restx import Resource

from generation_api.api.v1 import api
from generation_api.core import cache, limiter
from generation_api.utils import handle400error, handle404error, handle500error

from generation_api.api.parsers.generation_parsers import generation_parser
from generation_api.model.openai_gpt import OpenAIGpt
import json


model = OpenAIGpt()
generation_ns = api.namespace('generation', description='Generation namespace')

@generation_ns.route('/emoji')
class ExampleClass(Resource):

        @limiter.limit('1000000/hour')
        @cache.cached(timeout=1, query_string=True)

        def post(self):
            """
            Example endpoint
            """

            global model

            try:
                params = generation_parser.parse_args()
            except:
                return handle400error(generation_ns, 'Malformed request. Please, check the request at /v1')

            try:
                output = model.emoji(message=params['message'])
                return {'message': output}
            except Exception as e:
                return handle500error(generation_ns, e)

@generation_ns.route('/format')
class ExampleClass(Resource):

        @limiter.limit('1000000/hour')
        @cache.cached(timeout=1, query_string=True)

        def post(self):
            """
            Example endpoint
            """

            global model

            try:
                params = generation_parser.parse_args()
            except:
                return handle400error(generation_ns, 'Malformed request. Please, check the request at /v1')

            try:
                output = model.format_message(message=params['message'])
                return {'message': output}
            except Exception as e:
                return handle500error(generation_ns, e)

@generation_ns.route('/empathy')
class ExampleClass(Resource):

        @limiter.limit('1000000/hour')
        @cache.cached(timeout=1, query_string=True)

        def post(self):
            """
            Example endpoint
            """

            global model

            try:
                params = generation_parser.parse_args()
            except:
                return handle400error(generation_ns, 'Malformed request. Please, check the request at /v1')

            try:
                output = model.empathy(message=params['message'])
                return {'message': output}
            except Exception as e:
                return handle500error(generation_ns, e)

@generation_ns.route('/absurdity')
class ExampleClass(Resource):

        @limiter.limit('1000000/hour')
        @cache.cached(timeout=1, query_string=True)

        def post(self):
            """
            Example endpoint
            """

            global model

            try:
                params = generation_parser.parse_args()
            except:
                return handle400error(generation_ns, 'Malformed request. Please, check the request at /v1')

            try:
                output = model.absurdity(subject=params['message'])
                return {'message': output}
            except Exception as e:
                return handle500error(generation_ns, e)


@generation_ns.route('/absurdity_final')
class ExampleClass(Resource):

        @limiter.limit('1000000/hour')
        @cache.cached(timeout=1, query_string=True)

        def post(self):
            """
            Example endpoint
            """

            global model

            try:
                params = generation_parser.parse_args()
            except:
                return handle400error(generation_ns, 'Malformed request. Please, check the request at /v1')

            try:
                output = model.absurdity_final(subject=params['message'])
                return {'message': output}
            except Exception as e:
                return handle500error(generation_ns, e)


@generation_ns.route('/course')
class ExampleClass(Resource):

        @limiter.limit('1000000/hour')
        @cache.cached(timeout=1, query_string=True)

        def post(self):
            """
            Example endpoint
            """

            global model

            try:
                params = generation_parser.parse_args()
            except:
                return handle400error(generation_ns, 'Malformed request. Please, check the request at /v1')

            try:
                output = model.course(message=params['message'])
                return {'message': output}
            except Exception as e:
                return handle500error(generation_ns, e)