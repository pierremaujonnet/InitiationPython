{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Différentes méthodes pour calculer une somme\n",
    "\n",
    "Dans ce notebook, nous allons explorer différentes façons de calculer la somme $S_n=\\sum_{k=0}^{n}(2k+1)$.\n",
    "\n",
    "## 1. Méthode avec une boucle `for`\n",
    "\n",
    "Commençons par implémenter la méthode la plus directe en utilisant une boucle `for`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "def S_a(n):\n",
    "    somme = 0\n",
    "    for k in range(n + 1):  # On va de 0 à n inclus\n",
    "        somme = somme + (2*k + 1)\n",
    "    return somme\n",
    "\n",
    "# Test de la fonction\n",
    "print(f\"S_0 = {S_a(0)}\")\n",
    "print(f\"S_1 = {S_a(1)}\")\n",
    "print(f\"S_2 = {S_a(2)}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Méthode avec une boucle `while`\n",
    "\n",
    "On peut aussi utiliser une boucle `while`. Voici deux approches différentes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "def S_b(n):\n",
    "    somme = 0\n",
    "    k = 0\n",
    "    while k <= n:\n",
    "        somme = somme + (2*k + 1)\n",
    "        k = k + 1\n",
    "    return somme\n",
    "\n",
    "def S_c(n):\n",
    "    somme = 0\n",
    "    while n >= 0:\n",
    "        somme = somme + (2*n + 1)\n",
    "        n = n - 1\n",
    "    return somme\n",
    "\n",
    "# Test des fonctions\n",
    "print(\"Avec S_b :\")\n",
    "print(f\"S_2 = {S_b(2)}\")\n",
    "print(\"\\nAvec S_c :\")\n",
    "print(f\"S_2 = {S_c(2)}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Recherche d'un seuil\n",
    "\n",
    "Trouvons maintenant la plus petite valeur de n telle que $S_n \\geq 5000$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "def seuil():\n",
    "    n = 0\n",
    "    somme = 1  # S_0 = 1\n",
    "    while somme < 5000:\n",
    "        n = n + 1\n",
    "        somme = somme + (2*n + 1)\n",
    "    return n\n",
    "\n",
    "print(f\"La plus petite valeur de n telle que S_n ≥ 5000 est : {seuil()}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Calcul de valeurs particulières\n",
    "\n",
    "Calculons maintenant $S_{10}$, $S_{99}$ et $S_{999}$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "print(f\"S_10 = {S_a(10)}\")\n",
    "print(f\"S_99 = {S_a(99)}\")\n",
    "print(f\"S_999 = {S_a(999)}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Conjecture\n",
    "\n",
    "Pour aider à conjecturer une formule, créons une fonction qui compare nos résultats avec $(n+1)^2$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "def compare_avec_conjecture(n):\n",
    "    sn = S_a(n)\n",
    "    conjecture = (n + 1) ** 2\n",
    "    print(f\"Pour n = {n}:\")\n",
    "    print(f\"S_n = {sn}\")\n",
    "    print(f\"(n+1)² = {conjecture}\")\n",
    "\n",
    "# Testons pour quelques valeurs\n",
    "for n in [0, 1, 2, 3, 4, 5]:\n",
    "    compare_avec_conjecture(n)\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercices proposés\n",
    "\n",
    "1. Modifiez la fonction `S_a` pour calculer la somme $\\sum_{k=0}^{n}(3k+2)$\n",
    "2. Créez une nouvelle fonction qui calcule $\\sum_{k=1}^{n}k^2$\n",
    "3. Pour quelle valeur de n la somme $\\sum_{k=0}^{n}(2k+1)$ dépasse-t-elle 10000 ?"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.8"
  }
 }
}