import unittest
from model.army import Army

class TestArmy(unittest.TestCase):
    #### CONSTRUCTOR
    def test_army_constructor(self):
        army = Army(20, 10, 5)
        self.assertEqual(army.get_piqueros().__len__(), 20)
        self.assertEqual(army.get_arqueros().__len__(), 10)
        self.assertEqual(army.get_caballeros().__len__(), 5)

    #### TRANSFORM
    def test_transform_piquero(self):
        army = Army(1, 0, 0)
        army.train_piqueros()
        army.train_piqueros()
        army.train_piqueros()
        self.assertEqual(army.get_piqueros().__len__(), 0)
        self.assertEqual(army.get_arqueros().__len__(), 1)
        self.assertEqual(army.get_caballeros().__len__(), 0)

    def test_transform_arquero(self):
        army = Army(1, 0, 0)
        army.train_piqueros()
        army.train_piqueros()
        army.train_piqueros()

        army.train_arqueros()
        army.train_arqueros()

        self.assertEqual(army.get_piqueros().__len__(), 0)
        self.assertEqual(army.get_arqueros().__len__(), 0)
        self.assertEqual(army.get_caballeros().__len__(), 1)

    #### BATTLE
    def test_battle_is_saved_in_both(self):
        army1 = Army(25, 15, 8)
        army2 = Army(20, 20, 8)

        army_win = army1.recieve_attack(army2)

        self.assertEqual(1, army1.get_battles().__len__())
        self.assertEqual(1, army2.get_battles().__len__())

        self.assertEqual(army2, army1.get_battles()[0].get_win())
        self.assertEqual(army2, army2.get_battles()[0].get_win())

        self.assertEqual(army1, army1.get_battles()[0].get_loser())
        self.assertEqual(army1, army2.get_battles()[0].get_loser())

    def test_tied_battle_is_saved_in_both_as_None(self):
        army1 = Army(2, 2, 2)
        army2 = Army(2, 2, 2)

        army_win = army1.recieve_attack(army2)

        self.assertEqual(1, army1.get_battles().__len__())
        self.assertEqual(1, army2.get_battles().__len__())

        self.assertEqual(None, army1.get_battles()[0].get_win())
        self.assertEqual(None, army2.get_battles()[0].get_win())

        self.assertEqual(None, army1.get_battles()[0].get_loser())
        self.assertEqual(None, army2.get_battles()[0].get_loser())

    def test_battle_win(self):
        army1 = Army(25, 15, 8)
        army2 = Army(20, 20, 8)

        army_win = army1.recieve_attack(army2)

        self.assertEqual(army2, army_win)
        self.assertEqual([1100], army_win.get_army_cash_register())
        self.assertEqual(6, army1.get_caballeros().__len__())

    ## LOSER
    def test_battle_with_onecaballero_and_twoarqueros(self):
        army1 = Army(25, 15, 8)
        army2 = Army(0, 2, 1)

        army1.recieve_attack(army2)

        self.assertEqual(0, army2.get_caballeros().__len__())
        self.assertEqual(1, army2.get_arqueros().__len__())

    def test_battle_without_caballeros_but_onearquero_and_two_piqueros(self):
        army1 = Army(25, 15, 8)
        army2 = Army(2, 1, 0)

        army1.recieve_attack(army2)

        self.assertEqual(0, army2.get_arqueros().__len__())
        self.assertEqual(1, army2.get_piqueros().__len__())

    def test_battle_without_caballeros_without_arqueros_and_two_piqueros(self):
        army1 = Army(25, 15, 8)
        army2 = Army(2, 0, 0)

        army1.recieve_attack(army2)

        self.assertEqual(0, army2.get_piqueros().__len__())

    def test_battle_without_caballeros_without_arqueros_and_one_piquero(self):
        army1 = Army(25, 15, 8)
        army2 = Army(1, 0, 0)

        army1.recieve_attack(army2)

        self.assertEqual(0, army2.get_piqueros().__len__())

    ## TIE
    def test_tie_battle_both_armies_lose_one_smaller_unit_piquero(self):
        army1 = Army(2, 2, 2)
        army2 = Army(2, 2, 2)

        army_win = army1.recieve_attack(army2)

        self.assertEqual(1, army1.get_piqueros().__len__())
        self.assertEqual(1, army2.get_piqueros().__len__())
        self.assertEqual(None, army_win)

    def test_tie_battle_both_armies_lose_one_smaller_unit_arquero(self):
        army1 = Army(0, 2, 2)
        army2 = Army(0, 2, 2)

        army_win = army1.recieve_attack(army2)

        self.assertEqual(1, army1.get_arqueros().__len__())
        self.assertEqual(1, army2.get_arqueros().__len__())
        self.assertEqual(None, army_win)

    def test_tie_battle_both_armies_lose_one_smaller_unit_caballero(self):
        army1 = Army(0, 0, 2)
        army2 = Army(0, 0, 2)

        army_win = army1.recieve_attack(army2)

        self.assertEqual(1, army1.get_caballeros().__len__())
        self.assertEqual(1, army2.get_caballeros().__len__())
        self.assertEqual(None, army_win)