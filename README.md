Práce je v podobě python balíčku.
Pro spuštění práce v Docker kontejneru je potřeba nainstalovaný Docker Engine, po jeho instalaci lze využít přiložený src/impl/Makefile.

make build

	sestavení image

make container

	spuštění jednoho kontejneru s instancí služby

make health

	spuštění jednho kontejneru s instancí služby s využítím healthcheck

make swarmhealth

	spuštění dvou replik containeru pomocí docker swarm, je potřeba stroj zapojit do swarmu pomocí "docker swarm init"

make local 

	instalace spuštění modulu bez využití Dockeru 

make documentation

	spuštění serveru s dokumentací na portu 1234, je nutno mít nainstalovaný pydoc

make documentation
	
	spuštění jednotkových testů, je nutno mít nainstalovaný pytest

curl_tests

	obsahuje scripty, které testují fungování modulu pomocí příkazu curl 

siege_tests

	obsahuje scripty, které testují modulu pomocí nástroje siege, je potřeba nainstalovaný siege

load_estimate

	obsahuje zdrojové kódy v podobě ipynb, pro interaktivní procházení dat z MARAST v podobě histogramu
	k otevření je potřeba použít příkaz "ipython notebook", je tedy nutné mít nainstalovaný ipython


--------------------------------
Doporučený postup pro seznámení se s touto prací je následující:

1. nainstalujeme Docker Engine dle některého ze zde uvedených způsobů https://docs.docker.com/engine/installation/#server

2. sestavíme a spustíme kontejner pomocí "make container"

3. prohlédneme si obsah složky curl_tests, obsahuje sadu několika skriptů, které simulují interakci MARASTu s modulem

