import scipy.stats as st
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

"""Il faut mettre la taille de l'échantillon dans la variable "size" 
et le nombre de quantiles (100 si on n'a pas regroupé, sinon 10 ou 20,
 en fonction)"""
def generate_salaries(size, p):
    log_p_sal = st.norm(0, 1).rvs(size=size)
    residuals = st.norm(0, 1).rvs(size=size)
    return np.exp(p * log_p_sal + residuals), np.exp(log_p_sal)


def quantiles(l, nb_quantiles):
    orig = l
    size = len(l)
    l = l.copy()
    l.sort()
    quantiles = np.round(np.arange(1, nb_quantiles + 1, nb_quantiles / size) - 0.5 + 1. / size)
    q_dict = {a: int(b) for a, b in zip(l, quantiles)}
    return [q_dict[elem] for elem in orig]


def quantiles_dataframe(child_salaries, parent_salaries,nb_quantiles):
    qcs = quantiles(child_salaries, nb_quantiles)
    qps = quantiles(parent_salaries, nb_quantiles)
    cols = ["child_salary", "child_quantile", "parent_salary", "parent_quantile"]
    data = pd.DataFrame([a for a in zip(child_salaries, qcs, parent_salaries, qps)], columns=cols)
    data = data.groupby(["child_quantile", "parent_quantile"]).apply(lambda df: pd.Series({'nb': len(df)}))
    data = data.reset_index()
    return data


def parent_quantile_proba(q, data, nb_quantiles):
    probas = data[data.child_quantile == q]
    total = probas.nb.sum()
    nb_quantiles = len(data.child_quantile.unique())
    result = []
    for pq in range(1, 1 + nb_quantiles):
        if pq in probas.parent_quantile.values:
            result += list(probas[probas.parent_quantile == pq]["nb"].values / total)
        else:
            result += [0]
    return result


def proba_matrice_from_dataframe(data, nb_quantiles):
    mat = []
    for q in np.arange(nb_quantiles) + 1:
        mat += [parent_quantile_proba(q, data, nb_quantiles)]
    return np.array(mat)


def plot_proba_matrice(mat, nb_quantiles,p):
    mat_t = mat.T
    plt.figure(figsize=(10,10))
    done = np.array([0] * nb_quantiles)
    for i, parent_quantile in enumerate(mat_t):
        plt.bar(np.arange(nb_quantiles) + 1, parent_quantile, width=0.95, bottom=done, label=str(i + 1) + "e")
        done = done + np.array(parent_quantile)

    plt.axis([.5, nb_quantiles * 1.3, 0, 1])
    plt.title("p=" + str(p))
    
    plt.legend()
    plt.xlabel("quantile enfant")
    plt.ylabel("probabilité du quantile parent")
    plt.show()


if __name__ == "__main__":
    size = 10000
    nb_quantiles = 20
#le main est pas passé:
if __name__ == "__main__":
    size = 10000
    nb_quantiles = 20
    for p in [0.1, 0.5, 0.9]:
        child_salaries, parent_salaries = generate_salaries(size, p)
        data = quantiles_dataframe(child_salaries, parent_salaries)
        proba_matrice = proba_matrice_from_dataframe(data, nb_quantiles)
        plot_proba_matrice(proba_matrice, nb_quantiles)

    parent_quantile_proba(3, data, nb_quantiles)
