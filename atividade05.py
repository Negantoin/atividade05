# Digite uma metragem e veja isso em cm e mm:
metro = float(input("Insira uma metragem (Um número que represente n metros): "))
centimetro = metro *100
milimetro = metro *1000
import time
time.sleep(1)
print(metro, "metros é igual a: ", centimetro, "centímetros!")
print(metro, "metros é igual a: ", milimetro, "milimetros!")