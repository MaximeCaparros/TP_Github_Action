# TP_Github_Action


#### 2. Tester un premier workflow Github :

Pour pouvoir créer un worklow il faut d'abord créer les dossiers ` .github\ ` et ` .github\workflow\ `.
Ensuite on ajoute dans le dossier workflow les .yml ou il faut dedans mettre les travaux Github Actions.

Exemple de fichier .yml :

```
name: GitHub Actions Demo
on: [push]
jobs:
    Explore-GitHub-Actions:
        runs-on: ubuntu-latest
        steps:
            - run: echo "🎉 The job was automatically triggered by a ${{ github.event_name }} event."
            - run: echo "🐧 This job is now running on a ${{ runner.os }} server hosted by GitHub!"
            - run: echo "🔎 The name of your branch is ${{ github.ref }} and your repository is ${{ github.repository }}."
            - name: Check out repository code
            uses: actions/checkout@v3
            - run: echo "💡 The ${{ github.repository }} repository has been cloned to the runner."
            - run: echo "🖥️ The workflow is now ready to test your code on the runner."
            - name: List files in the repository
            run: |
            ls ${{ github.workspace }}
            - run: echo "🍏 This job's status is ${{ job.status }}."

```

Le resultat se trouve dans l'onglet Action et ensuite le workflow que vous voulez voir.


#### 3. Création d'un test UNITEST python

Voici le fichier main.py qu'on va utiliser pour les tests :

```
import unittest

class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(1, 2)
        self.assertEqual(result, 3)

```
Dans le fichier main.py on peut voir la methode addition qui est testé par test_addition.

#### 4. Workflow permettant de lancer les test python

Voici le workflow qui va lancer les tests :

```
name: GitHub Actions Demo
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3
  
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Test with pytest
        run: |
          pip install pytest
          pip install pytest-cov
          pytest test/main.py
```

On set-up en premier la version de python pui on installe pytest qui va nous permettre de lancer les tests dans notre main.py.
Et enfin on lance les test avec `pytest test/main.py`.

#### 5. Création d'une fonction soustraction avec son test

fichier main.py :

```python 3
import unittest

class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b
    def soustraction(a, b):
        return a - b

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(1, 2)
        self.assertEqual(result, 3)
    def test_soustraction(self):
        result = SimpleMath.soustraction(4, 2)
        self.assertEqual(result, 2)


```

On peut voir la fonction soustraction et test_soustraction ajouté.

Dans le workflow on peut voir que les deux test sont passé :

```sh
============================= test session starts ==============================
platform linux -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/runner/work/TP_Github_Action/TP_Github_Action
plugins: cov-4.0.0
collected 2 items

test/main.py ..                                                          [100%]

============================== 2 passed in 0.02s ===============================
```

#### 6. Ajout de pylint dans le Workflow

Voici l'ajout de pylint dans le workflow: 

```yml
      - name: Analyse avec pylint
        run: |
          pip install pylint
          find . -name '*.py' -exec pylint {} \;
```

On installe pylint puis on cherche tout les fichiers `*.py` et on lance pylint sur ces fichiers.

Execution dans le workflow :
```sh
************* Module main
test/main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
test/main.py:3:0: C0115: Missing class docstring (missing-class-docstring)
test/main.py:5:4: C0116: Missing function or method docstring (missing-function-docstring)
test/main.py:5:17: C0103: Argument name "a" doesn't conform to snake_case naming style (invalid-name)
test/main.py:5:20: C0103: Argument name "b" doesn't conform to snake_case naming style (invalid-name)
test/main.py:7:4: C0116: Missing function or method docstring (missing-function-docstring)
test/main.py:7:21: C0103: Argument name "a" doesn't conform to snake_case naming style (invalid-name)
test/main.py:7:24: C0103: Argument name "b" doesn't conform to snake_case naming style (invalid-name)
test/main.py:7:4: E0213: Method 'soustraction' should have "self" as first argument (no-self-argument)
test/main.py:10:0: C0115: Missing class docstring (missing-class-docstring)
test/main.py:11:4: C0116: Missing function or method docstring (missing-function-docstring)
test/main.py:14:4: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 0.00/10

```
0/10 :(

7. Docker


On créer un Dockerfile a la racine :

```Dockerfile
# Container image that runs your code
FROM alpine:3.10

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
```

Ce dockerfile va utiliser l'image alpine:3.10 en utilisant entrypoint.sh qui est un script permettant de faire un hello-world :

entrypoint.sh

```sh
#!/bin/sh -l

pip install pytest
pip install pytest-cov
pytest test/main.py
```


On va créer ensuite un workflow testDocker.yml :

```yml
on: [push]

jobs:
  hello_world_job:
    runs:
  	using: 'docker'
  	image: 'Dockerfile'
        
```

Ce workflow va permettre de build l'image dans DockerFile.



