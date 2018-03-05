curl -H "Content-Type: application/json" -X POST -d '{
	"question": "Mas se?",
	"user": "nankaond",
	"tests": [{
		"answer": "modrá&;",
		"initialization": "",
		"expression": "\"answer\" is \"modrá\"",
		"hint_false": "zelená není ta pravá ",
		"hint_true": "skvěle, to je ono ",
		"required": true,
		"tester": "python"
	}, {
                "answer": "zelená",
		"initialization": "",
		"expression": "\"answer\" is \"zelená\"",
		"hint_false": "zelená není ta pravá ",
		"hint_true": "výtečně, v barvách máš pořádek",
		"required": true,
		"tester": "python"
	}]
}' http://0.0.0.0:5000/test
