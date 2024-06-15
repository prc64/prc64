import dice
from time import sleep

def roll(amount:int, sides:int):
	return dice.roll(f'{amount}d{sides}')

for idx, result in enumerate(roll(5, 6)):
	print(f'Nuevo mensaje: Lanzamiento {idx+1} numero obtenido {result}')
	sleep(5)

