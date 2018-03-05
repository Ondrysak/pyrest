# -*- coding: utf-8 -*-
from tester import *


def checkit_stringcomp():
    question1 = Question('modrá nebo červená?', "nankaond", [{
      "answer": "morá",
      "initialization": "",
      "expression": "\"answer\" == \"modrá\"",
      "hint_false": "Jako první zkus neco modřejšího.",
      "hint_true": "skvěle, v barvách máš pořádek",
      "required": True,
      "tester": "python"
    }, {
      "answer": "zelená",
      "initialization": "",
      "expression": "\"answer\" == \"zelená\"",
      "hint_false": "zelená není ta pravá",
      "hint_true": "výborně, s barvami to umis",
      "required": True,
      "tester": "python"
    }])
    assert question1.eval_tests() is False

    question2 = Question('modrá nebo červená?', "nankaond", [{
      "answer": "modrá",
      "initialization": "",
      "expression": "\"answer\" == \"modrá\"",
      "hint_false": "Jako první zkus neco modřejšího.",
      "hint_true": "skvěle, v barvách máš pořádek",
      "required": True,
      "tester": "python"
    }, {
      "answer": "zelená",
      "initialization": "",
      "expression": "\"answer\" == \"zelená\"",
      "hint_false": "zelená není ta pravá",
      "hint_true": "výborně, s barvami to umis",
      "required": True,
      "tester": "python"
    }])
    assert question2.eval_tests() is True

def checkit_whitelist():
    question1 = Question('modrá nebo červená?', "nankaond", [{
      "answer": "&&",
      "initialization": "",
      "expression": "\"answer\" is \"&&\"",
      "hint_false": "Jako první zkus neco modřejšího.",
      "hint_true": "skvěle, v barvách máš pořádek",
      "required": True,
      "tester": "python"
    }, {
      "answer": "$$",
      "initialization": "",
      "expression": "\"answer\" is \"$$\"",
      "hint_false": "zelená není ta pravá",
      "hint_true": "výborně, s barvami to umis",
      "required": True,
      "tester": "python"
    }])
    assert question1.eval_tests() is False

def checkit_primenumber():
    question1 = Question("Zadej prvocislo vetsi nez 100.", "nankaond", [{
      "answer": "103",
      "initialization": "",
      "expression": "answer > 100",
      "hint_false": "Zkuste se zamyslet jak spolehlivě poznat, že číslo je větší než 100.",
      "hint_true": "Skvěle, číslo je větší než 100. ",
      "required": True,
      "tester": "python"
    }, {
      "answer": "103",
      "initialization": "",
      "expression": "isprime(answer)",
      "hint_false": "V tom jak poznat prvočíslo by jste snad už měli mít jasno.",
      "hint_true": "Výborně, zadal jste prvočíslo",
      "required": True,
      "tester": "sympy"
    }])
    assert question1.eval_tests() is True

    question2 = Question("Zadej prvocislo vetsi nez 100.", "nankaond", [{
      "answer": "90",
      "initialization": "",
      "expression": "answer > 100",
      "hint_false": "Zkuste se zamyslet jak spolehlivě poznat, že číslo je větší než 100.",
      "hint_true": "Skvěle, číslo je větší než 100. ",
      "required": True,
      "tester": "python"
    }, {
      "answer": "90",
      "initialization": "",
      "expression": "isprime(answer)",
      "hint_false": "V tom jak poznat prvočíslo by jste snad už měli mít jasno.",
      "hint_true": "Výborně, zadal jste prvočíslo",
      "required": True,
      "tester": "sympy"
    }])
    assert question2.eval_tests() is False

    question3 = Question("Zadej prvocislo vetsi nez 100.", "nankaond", [{
      "answer": "105",
      "initialization": "",
      "expression": "answer > 100",
      "hint_false": "Zkuste se zamyslet jak spolehlivě poznat, že číslo je větší než 100.",
      "hint_true": "Skvěle, číslo je větší než 100. ",
      "required": True,
      "tester": "python"
    }, {
      "answer": "105",
      "initialization": "",
      "expression": "isprime(answer)",
      "hint_false": "V tom jak poznat prvočíslo by jste snad už měli mít jasno.",
      "hint_true": "Výborně, zadal jste prvočíslo",
      "required": True,
      "tester": "sympy"
    }])
    assert question3.eval_tests() is False


def checkit_init():
    question1 = Question("Zadejte x", "nankaond", [{
      "answer": "2+x**2+x**8",
      "initialization": "a, b, c, x, y = symbols('a b c x y', real=True)",
      "expression": "limit(answer, x, 0)==2",
      "hint_false": "x",
      "hint_true": "x",
      "required": True,
      "tester": "sympy"
    }])
    assert question1.eval_tests() is True

    question2 = Question("Zadejte x", "nankaond", [{
      "answer": "3+x**2+x**8",
      "initialization": "a, b, c, x, y = symbols('a b c x y', real=True)",
      "expression": "limit(answer, x, 0)==2",
      "hint_false": "x",
      "hint_true": "x",
      "required": True,
      "tester": "sympy"
    }])
    assert question2.eval_tests() is False


def checkit_algebra():
    question1 = Question("Přijme výrazy totožné s $(a+b)^2$.", "kalvotom", [{
      "answer": "a**2 + 2*a*b + b**2",
      "initialization": "a,b = symbols('a,b')",
      "expression": "simplify(answer - (a+b)^2) == 0",
      "hint_false": "Ne",
      "hint_true": "Ano",
      "required": True,
      "tester": "sympy"
      }])
    assert question1.eval_tests() is True and question1.hint == "Ano"

    question2 = Question("Přijme výrazy totožné s $(a+b)^2$.", "kalvotom", [{
      "answer": "(a+b)**2",
      "initialization": "a,b = symbols('a,b')",
      "expression": "answer - (a+b)**2 == 0",
      "hint_false": "Ne",
      "hint_true": "Ano",
      "required": True,
      "tester": "sympy"
      }])
    assert question2.eval_tests() is True and question1.hint == "Ano"


def checkit_substitutions():
    question1 = Question("Přepisuje ^ na **.", "kalvotom", [{
      "answer": "a^b",
      "initialization": "a,b = symbols('a,b')",
      "expression": "answer == a**b",
      "hint_false": "Ne",
      "hint_true": "Ano",
      "required": True,
      "tester": "sympy"
      }])
    assert question1.eval_tests() is True and question1.hint == "Ano"

    question1 = Question("Přepisuje složené závorky na FiniteSet.", "kalvotom", [{
      "answer": "{a, b}",
      "initialization": "a,b = symbols('a, b')",
      "expression": "answer == FiniteSet(a, b)",  # z nějakého důvodu sympify
      "hint_false": "Ne",                        # vytvoří pouze Pythonovský set
      "hint_true": "Ano",                        # nefunguje ani:
      "required": True,                          # FiniteSet(*list(answer))
      "tester": "sympy"
      }])
    assert question1.eval_tests() is True and question1.hint == "Ano"


def checkit_timeout():
    question1 = Question("Zadej prvocislo vetsi nez 100.", "nankaond", [{
      "answer": "5045656156165156561616161556156156165156165165156781984981",
      "initialization": "",
      "expression": "factorint(answer) == 0",
      "hint_false": "x",
      "hint_true": "x",
      "required": True,
      "tester": "sympy"
    }])
    assert question1.eval_tests() is False and question1.error == "Vyprsel cas"



def checkit_required():
    question1 = Question("Zadej prvocislo vetsi nez 100.", "nankaond", [{
      "answer": "105",
      "initialization": "",
      "expression": "answer > 100",
      "hint_false": "Zkuste se zamyslet jak spolehlivě poznat, že číslo je větší než 100.",
      "hint_true": "Skvěle, číslo je větší než 100. ",
      "required": True,
      "tester": "python"
    }, {
      "answer": "105",
      "initialization": "",
      "expression": "isprime(answer)",
      "hint_false": "V tom jak poznat prvočíslo by jste snad už měli mít jasno.",
      "hint_true": "Výborně, zadal jste prvočíslo",
      "required": False,
      "tester": "sympy"
    }])
    assert question1.eval_tests() is True