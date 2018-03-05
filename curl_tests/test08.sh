curl -H "Content-Type: application/json" -X POST -d '{
	"user": "nankaond",
	"tests": [{
		"answer": "morá",
		"initialization": "",
		"expression": "\"answer\" is \"modrá\"",
		"hint_false": "Jako první zkus neco modřejšího.",
		"hint_true": "skvěle, v barvách máš pořádek",
		"required": true,
		"tester": "python"
	}, {
                "answer": "zelená",
		"initialization": "",
		"expression": "\"answer\" is \"zelená\"",
		"hint_false": "zelená není ta pravá",
		"hint_true": "výborně, s barvami to umis",
		"required": true,
		"tester": "python"
	}]
}' http://0.0.0.0:5000/test
