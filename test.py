import unittest
# from mock import *
from character import Mob, Hero, MyEncoder
from item import Item
from librarian import Librarian
import json


class TestCharacter(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCharacter, self).__init__(*args, **kwargs)
        self.hero = Hero("Joe")
        self.villain = Mob("Shmoe")
        self.item_hero = Item(name="Sword of Superiorness", attack_bonus=10, defense_bonus=-1)
        self.item_villain = Item(name="Shield of Losers", attack_bonus=0, defense_bonus=1)

    def test_check_names(self):
        self.assertEqual(self.hero.name, "Joe")
        self.assertEqual(self.villain.name, "Shmoe")

    def test_blank_name_mob(self):
        my_mob = Mob()
        self.assertEqual(type(my_mob.name), str)
        self.assertGreater(len(my_mob.name), 0)

    def test_get_stats(self):
        hero_stats = [{'name': 'Joe'}, {'items': []}, {'attack_strength': 2}, {'defense': 1}, {'health': 100}, {'exp': 0}, {'isMOB': False}, {'persist': True}]
        mob_stats = [{'name': 'Shmoe'}, {'items': []}, {'attack_strength': 2}, {'defense': 1}, {'health': 100}, {'exp': 0}, {'isMOB': True}, {'persist': False}]
        self.assertGreater(len(self.hero.get_stats()),0)
        self.assertGreater(len(self.villain.get_stats()),0)
        #self.assertEqual(self.hero.get_stats(), hero_stats)
        #self.assertEqual(self.villain.get_stats(), mob_stats)

    def test_attack(self):
        self.assertEqual(self.hero.attack(self.villain), 99)
        self.assertEqual(self.hero.attack(self.villain), 98)
        self.assertEqual(self.hero.attack(self.villain), 97)

        # check if item bonuses work
        self.villain.items.append(self.item_villain)
        self.assertEqual(self.hero.attack(self.villain), 97)
        self.hero.items.append(self.item_hero)
        self.assertEqual(self.hero.attack(self.villain), 87)
        # check multiple item bonuses
        self.hero.items.append(self.item_hero)
        self.assertEqual(self.hero.attack(self.villain), 67)
        # validate hero's health hasn't changed
        self.assertEqual(self.hero.health, 100)
        # check out negative defense
        self.assertEqual(self.villain.attack(self.hero), 97)

    def test_heal(self):
        ''' A basic unit test '''
        self.hero.heal(10)
        self.assertEqual(self.hero.health, 110)

    def test_isalive(self):
        hero = Hero(name="Stu")
        self.assertTrue(hero.is_alive())
        hero.health = 0
        self.assertFalse(hero.is_alive())
        hero.health = 100
        self.assertTrue(hero.is_alive())
        hero.take_damage(102)
        self.assertFalse(hero.is_alive())

    def test_check_items(self):
        self.hero.items.append(self.item_hero)
        self.hero.items.append(self.item_hero)
        self.assertEqual(len(self.hero.items), 2)

    def test_librarian(self):
        lib = Librarian()
        my_mob = lib.create_mob()
        self.assertEqual(type(my_mob.name), str)
        self.assertGreater(len(my_mob.name), 0)

    def test_encoding(self):
        my_mob = MyEncoder().encode(Mob())
        self.assertNotEqual(my_mob, " ")
        self.assertEqual(type(json.loads(my_mob)), dict)

    def test_librarian_flask(self):
        my_mob = MyEncoder().encode(Mob())
        test = Mob(my_mob)
        my_name = json.loads(my_mob)['name']
        new_mob = Mob(name=my_name)

    def test_combat(self):
        hero = Hero()
        villain = Mob()
        lib = Librarian()
        winner = lib.combat_time(hero, villain)
        # print "WINNER WINNER", winner, villain.is_alive(), hero.is_alive(), hero.health
        self.assertTrue(hero.is_alive())
        self.assertEqual(hero, winner)

    def test_librarian_create_mob(self):
        lib = Librarian()
        mob = lib.create_mob()
        self.assertTrue(mob)
    def test_hero_creation(self):
        hero = Hero(attack_strength=100)
        self.assertTrue(hero)

if __name__ == '__main__':
    unittest.main()
