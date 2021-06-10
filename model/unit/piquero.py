from model.unit.unit import Unit

class Piquero(Unit):
	def __init__(self):
		super().__init__()
		self._force_points = 5
		self._training_force_points = 3
		self._training_price = 10

	def is_piquero(self):
		return True

	def ready_to_transform(self):
		return self._spent_training_price >= 30