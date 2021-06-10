from model.unit.unit import Unit

class Caballero(Unit):
	def __init__(self):
		super().__init__()
		self._force_points = 20
		self._training_force_points = 10
		self._training_price = 30

	def is_caballero(self):
		return True

	def ready_to_transform(self):
		return False