import random
from datetime import datetime
random.seed(datetime.now())

# Règles :
# On génère une population de taille [populationSize] avec des comportements aléatoires en fonction de [nbTurn].
# On fait s'affronter tous les individus 1 à 1 dans un tournoi à [nbTurn] tours par adversaire :
# Les 3 meilleurs et pires individus sont affichés à l'issus du tournoi ainsi que les tendances comportementales.
# A la fin de celui ci la population se reproduit, les individus se reproduisent aléatoirement avec d'autres
# individus, les stratégies de l'enfant seront hérités à [crossoverRate] % du parent ayant gagner le plus de pièces
# durant le tournoi.
# Pour chaque élément de sa stratégie, l'enfant a un taux de [mutationRate] de faire évoluer un élément de sa
# stratégie, si le pourcentage de mutation atteint 0.5, les stratégies sont complétements aléatoires (à éviter donc).
# On recommence le processus pour [period] générations.

# Règles du tournoi
# Les 2 individus coopérent :               Les 2 individus gagnent [cooperation] pièces chacun.
# 1 individu coopére, 1 individu triche :   Le tricheur gagne [steal] pièces et le coopératif gagne [stolen] pièces.
# Les 2 individus trichent :                Les 2 individus gagnent [statu_quo] pièces chacun.

# Ajuster ces valeurs favorisera plus ou moins certains comportements.
# Valeur par défaut : 2, 3, -1, -2, 1, 4
cooperation = 2
steal = 3
stolen = -1
statu_quo = -2
investment = 1  # Non implémenté
given = 4       # Non implémenté

# Valeur par défaut : 50, 20, 10, 0.9, 0.02
populationSize = 50
period = 20
nbTurn = 10
crossoverRate = 0.9
mutationRate = 0.02


# Génération de la population
def generatePopulation():
    newPopulation = []
    for i in range(populationSize):
        individual = {
            "id": 1000 + i,
            "coins": 0,
            "hiddenMoney": 0,
            "style": "Hasard",
            "strategy": []
        }
        for j in range(nbTurn):
            individual["strategy"].append(random.randint(0, 1))
        newPopulation.append(individual)
        setStyle(newPopulation)
    return newPopulation


# Organisation du tournoi
def tournament(population):
    for leftIndividual in population:
        for rightIndividual in population:
            if leftIndividual != rightIndividual:
                for i in range(nbTurn):
                    # Les 2 individus coopérent
                    if leftIndividual["strategy"][i] == 0 and rightIndividual["strategy"][i] == 0:
                        leftIndividual["coins"] += cooperation
                        rightIndividual["coins"] += cooperation
                    # L'individu de gauche triche, l'individu de droite coopère
                    elif leftIndividual["strategy"][i] == 1 and rightIndividual["strategy"][i] == 0:
                        leftIndividual["coins"] += steal
                        rightIndividual["coins"] += stolen
                    # L'individu de gauche coopère, l'individu de droite triche
                    elif leftIndividual["strategy"][i] == 0 and rightIndividual["strategy"][i] == 1:
                        leftIndividual["coins"] += stolen
                        rightIndividual["coins"] += steal
                    # Les 2 individus trichent
                    elif leftIndividual["strategy"][i] == 1 and rightIndividual["strategy"][i] == 1:
                        leftIndividual["coins"] += statu_quo
                        rightIndividual["coins"] += statu_quo
                    elif leftIndividual["strategy"][i] == 0 and rightIndividual["strategy"][i] == 2:
                        leftIndividual["coins"] += given
                        rightIndividual["hiddenMoney"] += investment
                    elif leftIndividual["strategy"][i] == 2 and rightIndividual["strategy"][i] == 0:
                        leftIndividual["hiddenMoney"] += investment
                        rightIndividual["coins"] += given
                    elif leftIndividual["strategy"][i] == 1 and rightIndividual["strategy"][i] == 2:
                        leftIndividual["coins"] += given
                        rightIndividual["hiddenMoney"] += investment
                    elif leftIndividual["strategy"][i] == 2 and rightIndividual["strategy"][i] == 1:
                        leftIndividual["hiddenMoney"] += investment
                        rightIndividual["coins"] += given
                    else:
                        leftIndividual["hiddenMoney"] += investment
                        rightIndividual["hiddenMoney"] += investment
    population = sorted(population, key=lambda d: d['coins'], reverse=True)
    return population


# Reproduction de la population
def reproducePopulation(population):
    for individual in population:
        indexPartner = -1
        while indexPartner == -1 or individual == population[indexPartner]:
            indexPartner = random.randint(0, populationSize - 1)
        partner = population[indexPartner]
        for i in range(nbTurn):
            if individual["coins"] < partner["coins"]:
                if random.uniform(0, 1) < crossoverRate:
                    individual["strategy"][i] = partner["strategy"][i]
            if random.uniform(0, 1) < mutationRate:
                if individual["strategy"][i] == 0:
                    individual["strategy"][i] = 1
                else:
                    individual["strategy"][i] = 0
                '''if individual["strategy"][i] == 0:
                    individual["strategy"][i] = random.randint(1, 2)
                elif individual["strategy"][i] == 1:
                    if random.randint(0, 1) == 0:
                        individual["strategy"][i] = 0
                    else:
                        individual["strategy"][i] = 2
                else:
                    individual["strategy"][i] = random.randint(0, 1)'''
    setStyle(population)


# Affichage de la population
def showPopulation(population):
    for individual in population:
        print(individual)


# Modifie le comportement des individus de la population
def setStyle(population):
    for individual in population:
        individual["coins"] = 0 + individual["hiddenMoney"]
        nbCooperations = individual["strategy"].count(0)
        nbTricheries = individual["strategy"].count(1)
        nbInvestment = individual["strategy"].count(2)
        individual["cooperations"] = nbCooperations
        individual["tricheries"] = nbTricheries
        individual["investisment"] = nbInvestment
        if nbCooperations > nbTricheries and nbCooperations > nbInvestment:
            individual["style"] = "Coopératif"
        elif nbTricheries > nbCooperations and nbTricheries > nbInvestment:
            individual["style"] = "Arnaqueur!"
        elif nbInvestment > nbCooperations and nbInvestment > nbTricheries:
            individual["style"] = "Long-terme"
        else:
            individual["style"] = "Equilibré!"


# Affichage des données comportementales de la population
def showRatio(population):
    nbCooperatif = 0
    nbInvestisseur = 0
    for individual in population:
        if individual["style"] == "Coopératif":
            nbCooperatif += 1
        elif individual["style"] == "Investisseur":
            nbInvestisseur += 1
    print("\nNombre d'individus principalement coopératifs : " + nbCooperatif.__str__()
          + "\nNombre d'individus principalement investisseurs      : " + nbInvestisseur.__str__()
          + "\nNombre d'individu principalement arnaqueurs   : " + (populationSize - nbInvestisseur - nbCooperatif).__str__() + "\n")


population = generatePopulation()
showRatio(population)
for i in range(period):
    population = tournament(population)
    # print("Résultats tournoi :")
    # showPopulation()
    print(population[0])
    print(population[1])
    print(population[2])
    print(population[47])
    print(population[48])
    print(population[49])
    reproducePopulation(population)
    # print("Reproduction :")
    # showPopulation(population)
    showRatio(population)
