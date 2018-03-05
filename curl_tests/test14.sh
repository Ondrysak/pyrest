curl -H "Content-Type: application/json" -X POST -d '{
	"question": "Zadej velke cislo.",
	"user": "nankaond",
	"tests": [{
		"answer": "10",
		"initialization": "",
		"expression": "9**9**9**9 == 0",
		"hint_false": "takhle ne",
		"hint_true": "to by slo",
		"required": true,
		"tester": "python"
	}]
}' http://0.0.0.0:5000/test
