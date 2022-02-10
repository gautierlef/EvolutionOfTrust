# EvolutionOfTrust
Règles :

On génère une population de taille [populationSize] avec des comportements aléatoires en fonction de [nbTurn].\
On fait s'affronter tous les individus 1 à 1 dans un tournoi à [nbTurn] tours par adversaire :\
Les 3 meilleurs et pires individus sont affichés à l'issus du tournoi ainsi que les tendances comportementales.\
A la fin de celui ci la population se reproduit, les individus se reproduisent aléatoirement avec d'autres
individus, les stratégies de l'enfant seront hérités à [crossoverRate] % du parent ayant gagner le plus de pièces
durant le tournoi.\
Pour chaque élément de sa stratégie, l'enfant a un taux de [mutationRate] de faire évoluer un élément de sa
stratégie, si le pourcentage de mutation atteint 0.5, les stratégies sont complétements aléatoires (à éviter donc).\
On recommence le processus pour [period] générations.

Règles du tournoi

Les 2 individus coopérent :               Les 2 individus gagnent [cooperation] pièces chacun.\
1 individu coopére, 1 individu triche :   Le tricheur gagne [steal] pièces et le coopératif gagne 'stolen' pièces.
Les 2 individus trichent :                Les 2 individus gagnent [statu_quo] pièces chacun.