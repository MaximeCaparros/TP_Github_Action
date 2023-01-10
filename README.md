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

Exemple de résultat :

![img.png](img.png)