# EvolutionOfTrust
Règles :
On génère une population de taille [populationSize] avec des comportements aléatoires en fonction de [nbTurn].\
On fait s'affronter tous les individus 1 à 1 dans un tournoi à [nbTurn] tours par adversaire :\
A l'issue du tournoi, les individus gagnent leur fond caché en pièces. Ces fonds ne sont pas réinitialisé entre
les générations, c'est à dire que l'enfant d'un individu gardera les fond cachés de son parent.\
Les 3 meilleurs et pires individus sont affichés à l'issue du tournoi ainsi que les tendances comportementales.\
A la fin de celui ci la population se reproduit, les individus se reproduisent aléatoirement avec d'autres\
individus, les stratégies de l'enfant seront hérités à [crossoverRate] % du parent ayant gagner le plus de pièces
à l'issu du tournoi.\
Pour chaque élément de sa stratégie, l'enfant a un taux de [mutationRate] de faire évoluer un élément de sa
stratégie, si le pourcentage de mutation atteint 0.5, les stratégies sont complétements aléatoires (à éviter donc).\
On remet à le compte de pièce des enfants mais pas les fonds cachés hérité du parent.\
On recommence le processus pour [period] générations.

Règles du tournoi :\
Les 2 individus coopérent :       Les 2 individus gagnent [cooperation] pièces chacun.\
Les 2 individus trichent :        Les 2 individus gagnent [statu_quo] pièces chacun.\
Les 2 individus investissent :    Les 2 individus investissent ajoutant [hideMoney] à leur fond caché et gagne
[investment] pièces.\
1 individu coopére, 1 individu triche :   Le tricheur gagne [steal] pièces et le coopératif gagne [stolen] pièces.\
1 individu coopére, 1 individu investie : Le coopératif gagne [cooperation] pièces et l'investisseur investie.\
1 individu triche, 1 individu investie :    Le tricheur gagne [steal] pièces et l'investisseur investie.