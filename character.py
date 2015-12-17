#import item
import random, uuid

from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Character(object):
    def __init__(self, name, attack_strength=2, defense=1, health=100, items=None, exp=0):
        self.name = name
        self.attack_strength = attack_strength
        self.defense = defense
        self.health = health
        self.items = items
        self.id = uuid.uuid1
        if self.items is None:
            self.items = []
        self.isMOB = False
        self.persist = True
        if not self.isMOB:
            self.exp = exp
    # @property
    # def health(self):
    #     return self.__health
    # @health.setter
    # def health(self, health):
    #     if health < 0:
    #         self.__health = 0
    #     else:
    #         self.__health = health

    def __call__(self, *args, **kwargs):
        return Character(self['name'])

    def __iter__(self):
        return self

    def get_stats(self):
        char_stats = []
        for attr, value in self.__dict__.iteritems():
            # if not attr.startswith('_') or self.isMOB:
            char_stats.append({attr: value})
        return char_stats

    def gain_exp(self, xp):
        if not self.isMOB:
            self.exp += xp
        return self.exp

    def is_alive(self):
        return (self.health > 0)

    def heal(self, hp):
        # TODO: check if is a valid number
        # Lock down property
        self.health = self.health + hp
        return self.health

    def take_damage(self, damage):
        defense_strength = self.defense
        for i in self.items:
            defense_strength += i.defense_bonus
        # print "name: {2} - defenseStrength: {0} - damage:{1}".format(defense_strength,damage,self.name)
        if (defense_strength - damage) < 0:
            self.health += (defense_strength - damage)
        if self.health < 0:
            self.health = 0
        print "{0}'s health is now {1}".format(self.name, self.health)
        return self.health

    def attack(self, villain):
        print "{0} is attacking {1}".format(self.name, villain.name)
        if not self.is_alive():
            print "{0} is dead. Blerg.".format(self.name)
            return 0
        attack_strength = self.attack_strength
        # print attack_strength
        for i in self.items:
            attack_strength += i.attack_bonus
        # print "name: {1} - attackStrength: {0}".format(attack_strength, self.name)
        return villain.take_damage(attack_strength)


class Mob(Character):
    def __init__(self, name=None, *args, **kwargs):
        evil_names = ['wicked', 'bad', 'wrong', 'immoral', 'sinful', 'foul', 'vile', 'dishonorable', 'corrupt', 'iniquitous', 'depraved', 'reprobate', 'villainous', 'nefarious', 'vicious', 'malicious', 'malevolent', 'sinister', 'demonic', 'devilish', 'diabolical', 'fiendish', 'dark','monstrous', 'shocking', 'despicable', 'atrocious', 'heinous', 'odious', 'contemptible', 'horrible', 'execrable']
        first_names = ['Narcisa', 'Ryan', 'Cinthia', 'Sharla', 'Paulette', 'Venice', 'Valentina', 'Andria', 'Linn', 'Evelyn', 'Catherin', 'Tien', 'Mariette', 'Windy', 'Neta', 'Johnette', 'Jacquline', 'Tomeka', 'Tamela', 'Noah']
        if name is None:
            evil_name = [random.choice(evil_names).title(), random.choice(first_names).title()]
            name = " ".join(evil_name)
        super(Mob, self).__init__(name=name, *args, **kwargs)
        self.isMOB = True
        self.exp = 0
        self.persist = False

class Hero(Character):
    def __init__(self, name=None, *args, **kwargs):
        hero_names = ['Courageous', 'Responsible', 'Dedicated', 'Compassionate', 'Selfless', 'Valorous', 'Trustworthy', 'Intelligent', 'Disciplined', 'Charismatic', 'Loyal', 'Kind', 'Caring', 'Strong', 'Determined', 'Ingenious', 'Faithful', 'Generous', 'Inspiring', 'Noble', 'Relentless', 'Fearless', 'Valiant', 'Strong', 'Moral', 'Wise', 'Daring', 'Clever', 'Humble', 'Bold', 'Virtuous', 'Honorable', 'Sincere']
        first_names = ['Christene', 'Adan', 'Reva', 'Luise', 'Jasper', 'Ehtel', 'Katheleen', 'Babara', 'Earline', 'Rebecca', 'Christena', 'Billye', 'Darrell', 'Talisha', 'Kali', 'Rolando', 'Rufina', 'Rigoberto', 'Silvana', 'Suk']
        if name is None:
            hero_name = [random.choice(hero_names).title(), random.choice(first_names).title()]
            name = " ".join(hero_name)

        super(Hero, self).__init__(name=name, *args, **kwargs)
        self.isMOB = False
        self.exp = 0
        self.persist = True

# decode example
# >>> def from_json(json_object):
#         if 'fname' in json_object:
#             return FileItem(json_object['fname'])
# >>> f = JSONDecoder(object_hook = from_json).decode('{"fname": "/foo/bar"}')
# >>> f
# <__main__.FileItem object at 0x9337fac>
# >>>
