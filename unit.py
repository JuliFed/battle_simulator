import random


class Unit:
	def __init__(self):
		self.health = 100
		self.recharge = random.randrange(100, 2000)		

		
class	Soldier(Unit):
	def __init__(self):
		self.experience = 0
	
	""" 
		Вероятность успеха атаки
	"""
	@property
	def attack_probability(self):
		# 0.5 * (1 + health/100) * random(50 + experience, 100) / 100
		return 0.5 * (1 + self.health/100) * random.randrange(50+self.experience, 100) / 100
	
	
	""" 
		Сумма нанесенного урона
	"""
	@property
	def damage(self):
		# 0.05 + experience / 100
		return 0.05 + self.experience / 100
	
	
	
