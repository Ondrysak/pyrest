curl -H "Content-Type: application/json" -X POST -d '{
	"question": "Zadej prvocislo vetsi nez 100.",
	"user": "nankaond",
	"tests": [{
		"answer": "103",
		"initialization": "",
		"expression": "answer > 100",
		"hint_false": "Zkuste se zamyslet jak spolehlivě poznat, že číslo je větší než 100.",
		"hint_true": "Skvěle, číslo je větší než 100. ",
		"required": true,
		"tester": "python"
	}, {
                "answer": "103",
		"initialization": "",
		"expression": "isprime(answer)",
		"hint_false": "V tom jak poznat prvočíslo by jste snad už měli mít jasno.",
		"hint_true": "Výborně, zadal jste prvočíslo",
		"required": true,
		"tester": "sympy"
	}]
}' http://0.0.0.0:5000/test
