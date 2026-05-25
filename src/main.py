import numpy as np
import matplotlib.pyplot as plt
import math

def point_fixe(g, x0, tol = 1e-10, err = 1, k = 0, max = 100, x_vals = None):
    x = x0
    if x_vals is None:
        x_vals = [x0]
    for i in range(max):
        x_new = g(x)
        x_vals.append(x_new)
        if abs(x_new - x) < tol:
            print(f"Convergence reussie en {i+1} iterations.\n")
            return x_new, x_vals
        x = x_new
    print("Iteration max atteinte, pas de convergence !\n")
    return x, x_vals


def erreur_pt_fixe(g, chemin):
    x_liste = np.array(chemin)

    #|x_n+1 - x_n|
    erreur = np.abs(x_liste[1:] - x_liste[:-1])

    #|g(x_n) - x_n|
    x_n = x_liste[:-1]
    residu = np.abs(g(x_n) - x_n)

    plt.figure(figsize=(8, 5))
    plt.plot(erreur, color="red", linestyle="-")
    plt.plot(residu, color="blue", linestyle="--")
    plt.xlabel("Nombre d'iterations (n)")
    plt.ylabel("Erreur")
    plt.yscale('log')
    plt.title("Evolution de l'erreur au cours des itérations")
    plt.grid(True, which="both", linestyle="-.")
    plt.show()

def dichotomie(f, a = 0, b = 1, tol = 1e-6, max_iter = 100, k_bis = 0, errors_bis = []):
    if f(a) * f(b) > 0:
        print("Mauvais encadrement initial")
        return None, None
    else:
        for i in range(max_iter):
            m = (a+b)/2
            errors_bis.append(m)

            if abs(b - a)/2 < tol:
                print(f"Convergence reussie en {i + 1} iterations\n")
                return m, errors_bis
            if f(a) * f(m) <= 0:
                b = m
            else:
                a = m

        print("Iteration max atteinte, pas de convergence !\n")
        return m, errors_bis

def erreur_dichotomie(f, milieux):



def main():
    g1 = lambda x : np.cos(x)
    g2 = lambda x : np.log(2 + x)
    g3 = lambda x : 0.5 * (x + np.cos(x))

    #g1:
    #solution, chemin = point_fixe(g1, 0.5)

    #g2:
    #solution, chemin = point_fixe(g2, 1, err = 2)

    #g3
    """
    solution, chemin = point_fixe(g3, 0.5, tol = 1e-8)
    chemin_float = [float(x) for x in chemin]
    print(f"Point fixe de g : {solution}")
    print(f"chemin : {chemin_float}")
    erreur_pt_fixe(g3, chemin)
    """



if __name__ == "__main__":
    main()