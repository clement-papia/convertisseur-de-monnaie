import requests

def convertir_devise(montant, dev_initiale, dev_finale):
    url = "https://exchangeratesapi.io" + dev_initiale
    donnees = requests.get(url).json()
    taux_change = donnees['rates'][dev_finale]
    conversion = montant * taux_change
    return conversion

montant = float(input('Entrez le montant à convertir: '))
dev_initiale = input('Entrez la devise initiale: ')
dev_finale = input('Entrez la devise finale: ')

resultat = convertir_devise(montant, dev_initiale, dev_finale)

print(str(montant) + ' ' + dev_initiale + ' = ' + str(resultat) + ' ' + dev_finale)