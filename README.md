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

```
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

