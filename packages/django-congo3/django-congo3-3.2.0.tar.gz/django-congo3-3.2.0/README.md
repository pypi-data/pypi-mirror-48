# Congo 3

Biblioteka Congo 3 została stworzona przez [Integree Bussines Solutions](https://www.integree.eu). Paczka zawiera szereg przydatnych rozwiązań, które usprawniają i przyspieszają tworzenie aplikacji webowych w Django 2.x pod Python 3.x.

## Instalacja biblioteki Congo 3 w innym projekcie

Bibliotekę można pobrać bezpośrednio ze strony https://gitlab.com/integree/congo3/-/archive/master/congo3-master.zip. Po rozpakowaniu ZIP'a wykonaj polecenie:

```
python setup.py install
```

Możesz też zainstalować bibliotekę w trybie developerskim, tj. jako symlink:

```
python setup.py develop
```

Aby zainstalować bibliotekę bezpośrednio z repozytorium, wykonaj polecenie:

```
pip install git+https://gitlab.com/integree/congo3.git
```

lub, jeśli chcesz zainstalować branch, wykonaj polecenie:

```
pip install git+https://gitlab.com/integree/congo3.git@branch_name
```

## Instalacja i rozwój projektu Congo 3

### Przygotowanie środowiska developerskiego

Aby w ogóle rozpocząć pracę z projektem, musisz przygotować sobie środowisko programistyczne. Upewnij się, że zainstalowałeś i **poprawnie skonfigurowałeś** wszystkie poniższe programy i/lub narzędzia.

- Python 3.6 x86
- Visual C++ Build Tools 2015
- MySQL 5.7 x64
- MySQL Connector/C 6.1 x86
- Git for Windows
- GTK
- GetText
- Ruby & Compass
- Node & Bower
- virtualenv
- virtualenvwrapper-win

### Pobranie projektu

Uruchom konsolę i przejdź do katalogu roboczego, np. `D:\serwer\www`, utwórz katalog dla projektu i sklonuj do niego repozytorium:

```
cd \serwer\www
mkdir congo3
git clone https://gitlab.com/integree/congo3.git congo3
```

### Przygotowanie środowiska virtualenv

Upewnij się, że zmienna środowiskowa `WORKON_HOME` wskazuje na katalog domowy virtualenv'a, tj. katalog, w którym leżą wszystkie środowiska wirtualne, np. `D:\serwer\envs`.

```
set WORKON_HOME
```

Stwórz nowe środowisko wirtualne:

```
c:\Python36\python.exe -m venv "%WORKON_HOME%\congo3"
workon congo3
```

Upewnij się, że na pewno pracujesz na Pythonie w wersji 3.6.x:

```
python -V
```

Wykonaj upgrade pip'a i upewnij się, że masz wersję >= 18:

```
python -m pip install --upgrade pip
pip -V
```

Przejdź do katalogu projektu, np. `D:\serwer\www\congo3` i ustaw jako domyślny dla środowiska:

```
cd \serwer\www\congo3
setprojectdir .
```

Zainstaluj requirements'y:

```
pip install -r env\requirements.txt
```

### Inicjacja bazy danych

Zainicjuj bazę danych:

```
mysql -h localhost -u root -p -e "source env\init.sql"
```

Gdy baza danych jest skonfigurowana, możesz uruchomić migracje:

```
migrate.bat
```

### Tłumaczenia

Wygneruj i skompiluj tłumaczenia:

```
makemessages.bat
compilemessages.bat
```

### Pliki statyczne

Przed pierwszym uruchomieniem należy pobrać Bowerem biblioteki JavaScript'owe i skompilować Compassem pliki Sass:

```
bower.bat
watch.bat
```

## Developerski serwer HTTP

Wygląda na to, że doszedłeś do końca. Sprawdź, czy nic nie popierdaczyłeś...

```
runserver.bat
```

## Autorzy

Made with love by [Integree Bussines Solutions](https://www.integree.eu) - Warsaw, Poland