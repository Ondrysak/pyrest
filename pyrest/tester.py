# -*- coding: utf-8 -*-
import sys
import stopit
import os
from sympy import *
import logging
import re

logger = logging.getLogger('tester')
logger.setLevel(logging.DEBUG)

#reload(sys)  
#sys.setdefaultencoding('utf8')
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('[%(levelname)s][%(asctime)s][PID:%(process)d] - %(message)s')

ch.setFormatter(formatter)
# add the handlers to the logger

logger.addHandler(ch)

if "MAXLEN" in os.environ:
    MAXLEN = float(os.environ['MAXLEN'])
else:
    MAXLEN = 500

if "TIMEOUT" in os.environ:
    TIMEOUT = float(os.environ['TIMEOUT'])
else:
    TIMEOUT = 5

#enabled characters
if "WHITELIST" in os.environ:
    pattern= re.compile(r'^[' + re.escape(os.environ['WHITELIST']) + r']*$')
else:
    WHITELIST = "^ěščřžýáíéóúůďťňĎŇŤŠČŘŽÝÁÍÉÚŮABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789*+.,()<>=/ {}-"
    pattern= re.compile(r'^[' + re.escape(WHITELIST) + r']*$')
#disable exponentiation of numbers
exp_pattern = re.compile(r'[\d]+\*\*[\d]+')
exec_pattern = re.compile(r'(import|os|eval|system|exec)')
class Question:
    "Queston encapsulates tests and its results"
    count_total = 0
    count_timeout = 0
    count_error = 0

    def __init__(self, question, user, tests):
        """
        Construct a new 'Question' object.

        :param question: question that the user answered
        :param tests: tests for evaluation
        :return: returns nothing
        """
        self.question = question
        self.user = user
        self.tests = tests
        self.hint = ""
        self.error = ""
        self.status = True
        Question.count_total += 1

    def eval_tests(self):
        """
        Create tester object from tests and evaluate them 
        :return: returns True or False as a result of tests evaluation
        """
        logger.debug('Starting to evaluate tests')
        for test in self.tests:
            logger.debug('Testing if %s matches the whitelist' % repr(test['answer']))
            try:
                encoded=test['answer'].encode('utf8')
            except:
                encoded=test['answer']
            matching=pattern.match(encoded)
            if not matching:
                self.error += "Blacklisted characters in answer"
                self.status = False
                Question.count_error += 1
                logger.debug('Fail %s does not match the whitelist' % repr(test['answer']))
                break
            if exp_pattern.match(encoded):
                self.error += "Number exponentiation is not allowed"
                self.status = False
                Question.count_error += 1
                logger.debug('Fail %s is not allowed' % repr(test['answer']))    
                break
            if exec_pattern.match(encoded):
                self.error += "Some disallowed tokens found"
                self.status = False
                Question.count_error += 1
                logger.debug('Fail %s is not allowed' % repr(test['answer']))
                break
            logger.debug('OK %s matches the whitelist' % repr(test['answer']))
            #first init
            if test['initialization'] == '':
                test['initialization'] = self.tests[0]['initialization']
            tester = Tester(test['answer'], test['initialization'], test['expression'], test['hint_false'], test['hint_true'], test['required'], test['tester'])
            #time limit implementime timeout
            try:
                with stopit.ThreadingTimeout(TIMEOUT, swallow_exc=False) as to_ctx_mgr:
                    assert to_ctx_mgr.state == to_ctx_mgr.EXECUTING
                    result = tester.test()
                    if result is True:
                        self.hint += tester.hint_true
                    else:
                        self.hint += tester.hint_false
                        if test["required"]:
                            self.status = False
                            break
            except stopit.utils.TimeoutException:
                self.error += "Vyprsel cas"
                self.status = False
                Question.count_timeout += 1
                break
            except MemoryError:
                self.error += "Operace prekrocila limit pameti"
                self.status = False
                Question.count_error += 1
                break
            except:
                self.error += "Chyba pri zpracovani odpovedi"
                self.status = False
                Question.count_error += 1
                break
        logger.debug('Tests evaluated')
        return self.status


class Tester:
    """
    Tester encapsulates a test, their evaluation and creation of returned hint
    """
    def __init__(self, answer, initialization, expression, hint_false, hint_true, required, tester):
        """
        Construct a new 'Question' object.

        :param answer: users answer 
        :param initialization: initialization of variables etc
        :param answer: users answer 
        :param expression: expression to test
        :param hint_false: hint for false result
        :param hint_true: hint for true result
        :param required: if true failing means false result
        :param tester: tester to be used
        :return: returns nothing
        """
        self.answer = answer
        self.initialization = initialization
        self.expression = expression
        self.hint_false = hint_false
        self.hint_true = hint_true
        self.required = required
        self.tester = tester

    @classmethod
    def subs(self, answer):
        new_answer = answer
        new_answer = new_answer.replace('^', '**')
        new_answer = new_answer.replace('{', 'FiniteSet(')
        new_answer = new_answer.replace('}', ')')
        return new_answer

    def test(self):
        # length constraint
        if len(self.answer) > MAXLEN:
            return False
        # empty string
        if self.answer == "":
            return False
        result = False
        if not self.initialization == "":
            exec(self.initialization)
        if self.tester == 'sympy':
            answer = eval(Tester.subs(self.answer))
            result = eval(Tester.subs(self.expression))
        elif self.tester == 'python':
            result = eval(Tester.subs(self.expression.replace('answer', self.answer)))
        else:
            result = False
        if not result:
            return False
        else:
            return True
