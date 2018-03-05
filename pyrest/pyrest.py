#!flask/bin/python
# -*- coding: utf-8 -*-

#Author: Ondřej Naňka

import sys
import flask
import sympy
from flask import Flask, jsonify, request, abort, json
from sympy import symbols, sympify, simplify, SympifyError, Function
from sympy.logic.boolalg import BooleanTrue, BooleanFalse
from tester import *
from raven.contrib.flask import Sentry
from jsonschema import validate

import logging

schema = {
    "type": "object",
    "properties": {
         "question": {"type": "string"},
         "user": {"type": "string"},
         "tests": {"type": "array",
                   "items": {
                         "type": "object",
                         "properties": {
                              "initialization": {"type": "string"},
                              "expression": {"type": "string"},
                              "hint_false": {"type": "string"},
                              "hint_true": {"type": "string"},
                              "required": {"type": "boolean"},
                              "tester": {"type": "string"}
                         },
                         "required": ["initialization", "expression",
                                     "hint_false", "hint_true",
                                     "required", "tester"]
                    }


                   }
            },
         "required": ["question", "user", "tests"]
}
'''
         "initialization": {"type": "string"},
         "expression": {"type": "string"},
         "hint_false": {"type": "string"},
         "hint_true": {"type": "string"},
         "required": {"type": "string"},
         "tester": {"type": "string"},
'''
count_malformedjson = 0


ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s][%(asctime)s][PID:%(process)d] - %(message)s')
ch.setFormatter(formatter)
app = Flask(__name__)
app.logger.handlers = []
app.logger.addHandler(ch)
sentry = Sentry(app)


@app.route('/status', methods=['GET'])
def get_tasks():
    app.logger.info('Returning status')
    return jsonify({'count_total': Question.count_total, 'count_error': Question.count_error, 'count_timeout': Question.count_timeout, 'version_flask': flask.__version__, 'version_sympy': sympy.__version__})


@app.route('/test', methods=['POST'])
def test_symbolic_equality():
    #validate json against a schema
    app.logger.info('Validating JSON')
    if not request.json:
        Question.count_error += 1
        app.logger.info('JSON invalid')
        return json.dumps({'error': 'Recieved data is not in valid JSON format.'}, ensure_ascii=False).encode('utf8'), 201
    try:
        validate(request.json, schema)
    except:
        app.logger.info('JSON does not match JSONschema')
        return json.dumps({'error': 'Recieved data is not in valid JSON format.'}, ensure_ascii=False).encode('utf8'), 201
    app.logger.info('JSON for user %s validated', request.json['user'])
    #create a question object
    question = Question(request.json['question'], request.json['user'], request.json['tests'])
    app.logger.info('Request for user %s is going to be processed', request.json['user'])
    #compute results
    testresult = question.eval_tests()
    # return jsonify(dictionary), 201, ensures ascii
    dictionary = {'result': testresult, 'hint': question.hint}
    if not question.error == "":
        app.logger.info('Error in request for user %s', request.json['user'])
        return json.dumps({'error': question.error}, ensure_ascii=False).encode('utf8'), 201

    else:
        app.logger.info('Success in question from user %s', request.json['user'])
        return json.dumps(dictionary, ensure_ascii=False).encode('utf8'), 201

if __name__ == '__main__':
    app.logger.info('Starting module')
    app.run(host='0.0.0.0')
