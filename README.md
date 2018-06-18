# Ciblage de prospect pour DicreditBank

DiscreditBank souhaite cibler de nouveaux clients potentiels, plus particulièrement les jeunes en âge d'ouvrir leur tout premier compte bancaire.

Cependant, elle souhaite cibler les prospects les plus susceptibles d'avoir, plus tard dans leur vie, de hauts revenus.

L'équipe dans laquelle vous travaillez a donc reçu pour mission de créer un modèle permettant de déterminer le revenu potentiel d'une personne.

Ainsi, vous proposez une régression linéaire avec 3 variables :

    - le revenu des parents,
    - le revenu moyen du pays dans lequel habite le prospect,
    - l'indice de Gini calculé sur les revenus des habitants du pays en question. 


## Getting Started (=Avant de commencer)

- Installer requirements 

### Prerequisites (=Pré-requis)

Installer :
- Python 3.5

Et installer les libraires suivantes :
- Jupyter Notebook 5.4.1
- Pandas 0.22.0
- Numpy 1.14.2
- SciPy 1.0.0
- MatplotLib 2.2.2
- Scikit-Learn 0.19.1
- StatsModels 0.9.0

## Arborescense 
Dossier notebook : Contient le programme.
Dossier fichiers_csv : Contient les données utilisées.
Dossier presentation : Contient la présentation pdf et les images associées à cette présentation.
Dossier code : Contient le programme de génération des revenus des parents, le code R des indices de gini provenant de la source additionnelle, le programme de construction des analyses univariée et bivariée.
Dossier documents : Contient les ressources utilisées.

## Running

1. Pour réaliser la modélisation, ouvrez le notebook Jupyter (dossier 'notebook')et faites "run all".

Note : Étant donnée que les echantillons de revenus parents sont générés aléatoirement, il se peut que les résultats des modélisations ne soient pas identiques à ceux visibles dans la présentation. Ils resteront toutefois proches.




## Built With (=Fabriquer avec)

* [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/) - The  web-based application suitable for capturing the whole computation process.
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/) -  It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python
* [Numpy](http://www.numpy.org/) - NumPy is the fundamental package for scientific computing with Python.
*[Matplotlib](https://matplotlib.org/#) - Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.
*[Scipy](https://docs.scipy.org/doc/scipy/reference/index.html) - SciPy (pronounced “Sigh Pie”) is open-source software for mathematics, science, and engineering.
*[Scikit-Learn](http://scikit-learn.org/stable/index.html) - Simple and efficient tools for data mining and data analysis.
*[StatsModels](http://www.statsmodels.org/stable/install.html) - Python module that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration.



## Authors

* **Thibault SCHMIT** - *Initial work* - [Silvock](https://github.com/Silvock)



## License

This project is licensed under the GNU GPL 3.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Olivier Yoo - Mentor OpenClassrooms
