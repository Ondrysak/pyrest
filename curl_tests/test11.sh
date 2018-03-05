curl -H "Content-Type: application/json" -X POST -d '{
	"question": "Polynom s limitou v nule rovne dvema",
	"user": "nankaond",
	"tests": [{
		"answer": "2+x**2+x**8",
		"initialization": "a, b, c, x, y = symbols(\"a b c x y\", real=True)",
		"expression": "limit(answer, x, 0)==2",
		"hint_false": "Opravdu si myslite ze to je spravne?",
		"hint_true": "Skvěle to je krasny polynom.",
		"required": true,
		"tester": "sympy"
	}]
}' http://0.0.0.0:5000/test

