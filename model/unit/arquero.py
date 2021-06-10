from model.unit.unit import Unit

class Arquero(Unit):
	def __init__(self):
		super().__init__()
		self._force_points = 10
		self._training_force_points = 7
		self._training_price = 20

	def is_arquero(self):
		return True

	def ready_to_transform(self):
		return self._spent_training_price >= 40