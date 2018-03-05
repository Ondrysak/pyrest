#timeout test
curl -H "Content-Type: application/json" -X POST -d '{
	"question": "Zadej prvocislo vetsi nez 100.",
	"user": "nankaond",
	"tests": [{
		"answer": "5045656156165156561616161556156156165156165165156781984981",
		"initialization": "",
		"expression": "factorint(answer)==0",
		"hint_false": "x",
		"hint_true": "x",
		"required": true,
		"tester": "sympy"
	}]
}' http://0.0.0.0:5000/test
