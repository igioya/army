from model.unit.piquero import Piquero
from model.unit.arquero import Arquero
from model.unit.caballero import Caballero
from model.battle import Battle

class Army:
    def __init__(self, piqueros_count, arqueros_count, caballeros_count):
        self._piqueros = []
        self._arqueros = []
        self._caballeros = []
        self._battles = []
        self._army_cash_register = [1000]
        # Init units_list by count
        [self._piqueros.append(Piquero()) for x in range(piqueros_count)]
        [self._arqueros.append(Arquero()) for x in range(arqueros_count)]
        [self._caballeros.append(Caballero()) for x in range(caballeros_count)]

    def get_piqueros(self):
        return self._piqueros

    def get_arqueros(self):
        return self._arqueros

    def get_caballeros(self):
        return self._caballeros

    def train_piqueros(self):
        self._train_units(self._piqueros, Arquero, self._arqueros)

    def train_arqueros(self):
        self._train_units(self._arqueros, Caballero, self._caballeros)

    def get_army_cash_register(self):
        return self._army_cash_register

    def set_army_cash_register(self, cash_register):
        self._army_cash_register = cash_register

    def get_battles(self):
        return self._battles

    def total_force_points(self):
        all_units = self._piqueros + self._arqueros + self._caballeros
        return sum(map(lambda unit: unit.get_force_points(), all_units))

    def recieve_attack(self, attacker_army):
        new_battle = Battle()

        if self.total_force_points() == attacker_army.total_force_points():  # TIE
            win = None
            loser = None

            self._delete_smaller_unit(self)
            self._delete_smaller_unit(attacker_army)

            new_battle.set_win(win)
            new_battle.set_loser(loser)

            self._battles.append(new_battle)
            attacker_army.get_battles().append(new_battle)

        else:
            if self.total_force_points() > attacker_army.total_force_points():  # SELF WIN
                win = self
                loser = attacker_army
            else:  # ATTECKER WIN
                win = attacker_army
                loser = self

            self._delete_biggest_units(loser)
            win.set_army_cash_register([win.get_army_cash_register()[0] + 100])
            new_battle.set_win(win)
            new_battle.set_loser(loser)
            win.get_battles().append(new_battle)
            loser.get_battles().append(new_battle)

        return win

    def _delete_smaller_unit(self, army):
        self._delete_unit(1, False, army)

    def _delete_biggest_units(self, army):
        self._delete_unit(2, True, army)

    def _delete_unit(self, head, reverse, army):
        all_units = army.get_piqueros() + army.get_arqueros() + army.get_caballeros()
        all_units.sort(key=lambda unit: unit.get_force_points(), reverse=reverse)
        to_delete = all_units[:head]
        for unit in to_delete:
            if unit.is_piquero():
                army.get_piqueros().remove(unit)
            elif unit.is_arquero():
                army.get_arqueros().remove(unit)
            elif unit.is_caballero():
                army.get_caballeros().remove(unit)

    def _train_units(self, units_list, next_unit_class, next_unit_list):
        # Train
        unit_to_transform = []
        for unit in units_list:
            unit.train(self._army_cash_register)
            if unit.ready_to_transform():
                unit_to_transform.append(unit)

        # Transform
        for unit in unit_to_transform:
            units_list.remove(unit)
            new_next_unit = next_unit_class()
            next_unit_list.append(new_next_unit)