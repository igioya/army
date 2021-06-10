import abc

class Unit:
	def __init__(self):
		self._spent_training_price = 0

	def get_force_points(self):
		return self._force_points

	def get_training_force_points(self):
		return self._training_force_points

	def set_force_points(self, force_points):
		self._force_points = force_points

	def get_training_price(self):
		return self._training_price

	def get_spent_training_price(self):
		return self._spent_training_price

	def set_spent_training_price(self, spent_training_price):
		self._spent_training_price = spent_training_price

	@abc.abstractmethod
	def train(self, army_cash_register):
		army_cash_register[0] -= self._training_price #Debit from cash_register
		self._spent_training_price += self._training_price #Increment spent price (to manage transform)
		self._force_points += self._training_force_points

	def is_piquero(self):
		return False

	def is_arquero(self):
		return False

	def is_caballero(self):
		return False