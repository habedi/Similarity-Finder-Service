import json

from flask import request, jsonify, Response


class SimilarityFinder(object):

    def __init__(self, flaskapp):
        self.app = flaskapp

    def run(self, host, port, debug, use_reloader, threaded):
        """
        Starts the task server
        :param host: host ip to bind
        :param port: host port to bind
        :param debug: if 'True' shows the stacktrace on error to browser
        :param use_reloader: if 'True' reloads the new code on its change
        :param threaded: if 'True' server makes a new thread to answer each request
        :return: None
        """

        @self.app.route('/api/1/hash64/calculate', methods=['POST'])
        def hash64_calculate():
            try:
                json.loads(request.data)
            except Exception as err:
                pass
            else:
                hash_calculator = Hash64()
                hash_calculator.string_to_64hash("OH!")

        self.app.run(host=host, port=port, debug=debug,
                     use_reloader=use_reloader, threaded=threaded)
