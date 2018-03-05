siege --reps 10 --concurrent=63 --content-type="application/json" 'http://0.0.0.0:5000/test POST {
	"question": "Zadej prvocislo vetsi nez 100.",
	"user": "nankaond",
	"tests": [{
		"answer": "90",
		"initialization": "",
		"expression": "answer > 100",
		"hint_false": "Zkuste se zamyslet jak spolehlivě poznat, že číslo je větší než 100.",
		"hint_true": "Skvěle, číslo je větší než 100. ",
		"required": true,
		"tester": "python"
	}, {
                "answer": "90",
		"initialization": "",
		"expression": "isprime(answer)",
		"hint_false": "V tom jak poznat prvočíslo by jste snad už měli mít jasno.",
		"hint_true": "Výborně, zadal jste prvočíslo",
		"required": true,
		"tester": "sympy"
	}]
}'

siege --reps 10 --concurrent=63 --content-type="application/json" 'http://0.0.0.0:5000/test POST {
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
}'
