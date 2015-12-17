from character import Mob, MyEncoder, Hero
from flask import Flask, jsonify
app = Flask(__name__)
import json, yaml, pickle, os, shutil, uuid, random

class Librarian(object):
    def __init__(self):
        if os.path.isfile('data/mob_data.yaml'):
            shutil.copyfile('data/mob_data.yaml', 'data/mob_data{0}.yaml'.format(uuid.uuid1()))
            os.remove('data/mob_data.yaml')
        if os.path.isfile('data/player_data.yaml'):
            shutil.copyfile('data/player_data.yaml', 'data/player_data{0}.yaml'.format(uuid.uuid1()))
            os.remove('data/player_data.yaml')

    def create_mobs(self):
        mobs = []
        for x in range(0, random.randint(1, 10)):
            mobs.append(self.create_mob())
        return mobs

    def record(self, data, character):
        with open('data/{0}_data.yaml'.format(character), 'w') as outfile:
            outfile.write(yaml.safe_dump(data, default_flow_style=False))
        return True

    def get_mob(self, id):
        with open('data/mob_data.yaml', 'r') as infile:
            mob = pickle.loads(infile)
        return mob

    def create_hero(self):
        hero = Hero()
        hero_data = pickle.dumps(hero)
        self.record_hero(hero_data, hero)
        return hero

    def create_mob(self):
        mob = Mob()
        mob_data = pickle.dumps(mob)
        #print mob_data
        self.record(mob_data, "mob")
        return mob

    def combat_time(self,hero,villain):
        while hero.is_alive() and villain.is_alive():
            hero.attack(villain)
            villain.attack(hero)
        return hero if hero.is_alive() else villain

    def get_hero(self, id):
        hero = Hero()
        return hero

    def get_mob(self, id):
        mob = Mob()
        return mob

    @app.route('/librarian/get_mob')
    def get_mob():
        my_mob = MyEncoder().encode(Mob())
        return jsonify(json.loads(my_mob))

    # @app.route('/libararian/combat/hero_id/villian_id')
    # def start_combat(self, hero_id, villian_id):
    #     hero = get_hero(hero_id)
    #     villain = get_mob(villian_id)
    #     return combat_time(hero, villian)


if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True, debug=True)
