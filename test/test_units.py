import unittest
from model.unit.piquero import Piquero
from model.unit.arquero import Arquero
from model.unit.caballero import Caballero

class TestUnits(unittest.TestCase):
	#### CONSTRUCTOR
    def test_piquero_constructor(self):
    	piquero = Piquero()
    	self.assertEqual(piquero.get_force_points() , 5)
    	self.assertEqual(piquero.get_training_force_points() , 3)
    	self.assertEqual(piquero.get_training_price() , 10)
    	self.assertEqual(piquero.get_spent_training_price() , 0)

    def test_arquero_constructor(self):
    	arquero = Arquero()
    	self.assertEqual(arquero.get_force_points() , 10)
    	self.assertEqual(arquero.get_training_force_points() , 7)
    	self.assertEqual(arquero.get_training_price() , 20)
    	self.assertEqual(arquero.get_spent_training_price() , 0)

    def test_caballero_constructor(self):
    	caballero = Caballero()
    	self.assertEqual(caballero.get_force_points() , 20)
    	self.assertEqual(caballero.get_training_force_points() , 10)
    	self.assertEqual(caballero.get_training_price() , 30)
    	self.assertEqual(caballero.get_spent_training_price() , 0)

    #### UNIT TRAINING
    def test_train_piquero(self):
    	army_cash_register = [1000]
    	piquero = Piquero()
    	piquero.train(army_cash_register)
    	self.assertEqual(army_cash_register[0] , 990)
    	self.assertEqual(piquero.get_force_points() , 8)
    	self.assertEqual(piquero.get_spent_training_price() , 10)

    def test_train_arquero(self):
    	army_cash_register = [1000]
    	arquero = Arquero()
    	arquero.train(army_cash_register)
    	self.assertEqual(army_cash_register[0] , 980)
    	self.assertEqual(arquero.get_force_points() , 17)
    	self.assertEqual(arquero.get_spent_training_price() , 20)

    def test_train_caballero(self):
    	army_cash_register = [1000]
    	arquero = Caballero()
    	arquero.train(army_cash_register)
    	self.assertEqual(army_cash_register[0] , 970)
    	self.assertEqual(arquero.get_force_points() , 30)
    	self.assertEqual(arquero.get_spent_training_price() , 30)