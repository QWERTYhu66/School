class pokemon:
    def __init__(self, ID, Name, HP, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Base_Stats, normal_weakness, fire_weakness, water_weakness, electric_weakness, grass_weakness, ice_weakness, fighting_weakness, poison_weakness, ground_weakness, flying_weakness, psychic_weakness, bug_weakness, rock_weakness, ghost_weakness, dragon_weakness, dark_weakness, steel_weakness, fairy_weakness, height_inches, height_meters, weight_pounds, weight_kilograms, capturing_rate, gender_male_ratio, egg_steps, egg_cycles, abilities, Type_1, Type_2, Classification_info, Forms, gen, Is_Legendary, Is_Mythical, Is_Ultra_Beast, number_immune, number_not_effective, number_normal, number_super_effective):
        self.ID = ID
        self.Name = Name
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.Sp_Attack = Sp_Attack
        self.Sp_Defense = Sp_Defense
        self.Speed = Speed
        self.Base_Stats = Base_Stats
        self.normal_weakness = normal_weakness
        self.fire_weakness = fire_weakness
        self.water_weakness = water_weakness
        self.electric_weakness = electric_weakness
        self.grass_weakness = grass_weakness
        self.ice_weakness = ice_weakness
        self.fighting_weakness = fighting_weakness
        self.poison_weakness = poison_weakness
        self.ground_weakness = ground_weakness
        self.flying_weakness = flying_weakness
        self.psychic_weakness = psychic_weakness
        self.bug_weakness = bug_weakness
        self.rock_weakness = rock_weakness
        self.ghost_weakness = ghost_weakness
        self.dragon_weakness = dragon_weakness
        self.dark_weakness = dark_weakness
        self.steel_weakness = steel_weakness
        self.fairy_weakness = fairy_weakness
        self.height_inches = height_inches
        self.height_meters = height_meters
        self.weight_pounds = weight_pounds
        self.weight_kilograms = weight_kilograms
        self.capturing_rate = capturing_rate
        self.gender_male_ratio = gender_male_ratio
        self.egg_steps = egg_steps
        self.egg_cycles = egg_cycles
        self.abilities = abilities
        self.Type_1 = Type_1
        self.Type_2 = Type_2
        self.Classification_info = Classification_info
        self.Forms = Forms
        self.gen = gen
        self.Is_Legendary = Is_Legendary
        self.Is_Mythical = Is_Mythical
        self.Is_Ultra_Beast = Is_Ultra_Beast
        self.number_immune = number_immune
        self.number_not_effective = number_not_effective
        self.number_normal = number_normal
        self.number_super_effective = number_super_effective

class move:
    def __init__(self, ID, Name, Power, Accuracy, PP, Priority, Effect, Type_1, Type_2):
        self.ID = ID
        self.Name = Name
        self.Power = Power
        self.Accuracy = Accuracy
        self.PP = PP
        self.Priority = Priority
        self.Effect = Effect
        self.Type_1 = Type_1
        self.Type_2 = Type_2

class trainer:
    def __init__(self, ID, Name, Pokemon, Badges, Money, Items):
        self.ID = ID
        self.Name = Name
        self.Pokemon = Pokemon
        self.Badges = Badges
        self.Money = Money
        self.Items = Items
    def add_pokemon(self, pokemon):
        self.Pokemon.append(pokemon)
    def remove_pokemon(self, pokemon):
        self.Pokemon.remove(pokemon)
    def add_badge(self, badge):
        self.Badges.append(badge)
    def remove_badge(self, badge):
        self.Badges.remove(badge)
    def add_money(self, amount):
        self.Money += amount
    def remove_money(self, amount):
        self.Money -= amount
    def add_item(self, item):
        self.Items.append(item)
    def remove_item(self, item):
        self.Items.remove(item)
    def show_pokemon(self):
        for pokemon in self.Pokemon:
            print(pokemon.Name)
    def show_badges(self):
        for badge in self.Badges:
            print(badge)
    def show_money(self):
        print(self.Money)
    def show_items(self):
        for item in self.Items:
            print(item)
    def show_trainer_info(self):
        print("Trainer ID: ", self.ID)
        print("Trainer Name: ", self.Name)
        print("Trainer Badges: ", self.Badges)
        print("Trainer Money: ", self.Money)
        print("Trainer Items: ", self.Items)
    def show_trainer_pokemon(self):
        print("Trainer Pokemon: ")
        for pokemon in self.Pokemon:
            print(pokemon.Name)
    def show_trainer_pokemon_stats(self):
        print("Trainer Pokemon Stats: ")
        for pokemon in self.Pokemon:
            print("Pokemon Name: ", pokemon.Name)
            print("Pokemon HP: ", pokemon.HP)
            print("Pokemon Attack: ", pokemon.Attack)
            print("Pokemon Defense: ", pokemon.Defense)
            print("Pokemon Sp_Attack: ", pokemon.Sp_Attack)
            print("Pokemon Sp_Defense: ", pokemon.Sp_Defense)
            print("Pokemon Speed: ", pokemon.Speed)
            print("Pokemon Base Stats: ", pokemon.Base_Stats)
            print("Pokemon Normal Weakness: ", pokemon.normal_weakness)
            print("Pokemon Fire Weakness: ", pokemon.fire_weakness)
            print("Pokemon Water Weakness: ", pokemon.water_weakness)
            print("Pokemon Electric Weakness: ", pokemon.electric_weakness)
            print("Pokemon Grass Weakness: ", pokemon.grass_weakness)
            print("Pokemon Ice Weakness: ", pokemon.ice_weakness)
            print("Pokemon Fighting Weakness: ", pokemon.fighting_weakness)
            print("Pokemon Poison Weakness: ", pokemon.poison_weakness)
            print("Pokemon Ground Weakness: ", pokemon.ground_weakness)
            print("Pokemon Flying Weakness: ", pokemon.flying_weakness)
            print("Pokemon Psychic Weakness: ", pokemon.psychic_weakness)
            print("Pokemon Bug Weakness: ", pokemon.bug_weakness)
            print("Pokemon Rock Weakness: ", pokemon.rock_weakness)
            print("Pokemon Ghost Weakness: ", pokemon.ghost_weakness)
            print("Pokemon Dragon Weakness: ", pokemon.dragon_weakness)
            print("Pokemon Dark Weakness: ", pokemon.dark_weakness)
            print("Pokemon Steel Weakness: ", pokemon.steel_weakness)
            print("Pokemon Fairy Weakness: ", pokemon.fairy_weakness)
            print("Pokemon Height Inches: ", pokemon.height_inches)
            print("Pokemon Height Meters: ", pokemon.height_meters)
            print("Pokemon Weight Pounds: ", pokemon.weight_pounds)
            print("Pokemon Weight Kilograms: ", pokemon.weight_kilograms)

class battle:
    def __init__(self, trainer1, trainer2):
        self.trainer1 = trainer1
        self.trainer2 = trainer2
        self.trainer1_pokemon = trainer1.Pokemon[0]
        self.trainer2_pokemon = trainer2.Pokemon[0]
        self.turn = 1
        self.winner = None
        self.loser = None
        self.battle_log = []
    def start_battle(self):
        print("Battle started between ", self.trainer1.Name, " and ", self.trainer2.Name)
        while True:
            if self.turn % 2 == 1:
                print(self.trainer1.Name + "'s turn")
                print("Choose a move for " + self.trainer1_pokemon.Name)
                for move in self.trainer1_pokemon.Moves:
                    print(move.Name)
                move_choice = input("Enter the move name: ")
                move_choice = move_choice.lower()
                for move in self.trainer1_pokemon.Moves:
                    if move.Name.lower() == move_choice:
                        chosen_move = move
                        break
                else:
                    print("Invalid move choice")
                    continue
                damage = chosen_move.Power - (self.trainer2_pokemon.Defense / 2)
                if damage < 0:
                    damage = 0
                print(self.trainer2_pokemon.Name + " took " + str(damage) + " damage")
                self.trainer2_pokemon.HP -= damage
                if self.trainer2_pokemon.HP <= 0:
                    print(self.trainer2_pokemon.Name + " fainted")
                    self.winner = self.trainer1
                    self.loser = self.trainer2
                    break
            else:
                print(self.trainer2.Name + "'s turn")
                print("Choose a move for " + self.trainer2_pokemon.Name)
                for move in self.trainer2_pokemon.Moves:
                    print(move.Name)
                move_choice = input("Enter the move name: ")
                move_choice = move_choice.lower()
                for move in self.trainer2_pokemon.Moves:
                    if move.Name.lower() == move_choice:
                        chosen_move = move
                        break
                else:
                    print("Invalid move choice")
                    continue
                damage = chosen_move.Power - (self.trainer1_pokemon.Defense / 2)
                if damage < 0:
                    damage = 0
                print(self.trainer1_pokemon.Name + " took " + str(damage) + " damage")
                self.trainer1_pokemon.HP -= damage
                if self.trainer1_pokemon.HP <= 0:
                    print(self.trainer1_pokemon.Name + " fainted")
                    self.winner = self.trainer2
                    self.loser = self.trainer1
                    break
            self.turn += 1
        print("Battle ended")
        print("Winner: ", self.winner.Name)
        print("Loser: ", self.loser.Name)
        print("Battle Log: ")
        for log in self.battle_log:
            print(log)
    def add_to_battle_log(self, log):
        self.battle_log.append(log)
    def show_battle_log(self):
        print("Battle Log: ")
        for log in self.battle_log:
            print(log)
class pokemon:
    def __init__(self, ID, Name, HP, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Base_Stats, normal_weakness, fire_weakness, water_weakness, electric_weakness, grass_weakness, ice_weakness, fighting_weakness, poison_weakness, ground_weakness, flying_weakness, psychic_weakness, bug_weakness, rock_weakness, ghost_weakness, dragon_weakness, dark_weakness, steel_weakness, fairy_weakness, height_inches, height_meters, weight_pounds, weight_kilograms, capturing_rate, gender_male_ratio, egg_steps, egg_cycles, abilities, Type_1, Type_2, Classification_info, Forms, gen, Is_Legendary, Is_Mythical, Is_Ultra_Beast, number_immune, number_not_effective, number_normal, number_super_effective, Moves=None):
        self.ID = ID
        self.Name = Name
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.Sp_Attack = Sp_Attack
        self.Sp_Defense = Sp_Defense
        self.Speed = Speed
        self.Base_Stats = Base_Stats
        self.normal_weakness = normal_weakness
        self.fire_weakness = fire_weakness
        self.water_weakness = water_weakness
        self.electric_weakness = electric_weakness
        self.grass_weakness = grass_weakness
        self.ice_weakness = ice_weakness
        self.fighting_weakness = fighting_weakness
        self.poison_weakness = poison_weakness
        self.ground_weakness = ground_weakness
        self.flying_weakness = flying_weakness
        self.psychic_weakness = psychic_weakness
        self.bug_weakness = bug_weakness
        self.rock_weakness = rock_weakness
        self.ghost_weakness = ghost_weakness
        self.dragon_weakness = dragon_weakness
        self.dark_weakness = dark_weakness
        self.steel_weakness = steel_weakness
        self.fairy_weakness = fairy_weakness
        self.height_inches = height_inches
        self.height_meters = height_meters
        self.weight_pounds = weight_pounds
        self.weight_kilograms = weight_kilograms
        self.capturing_rate = capturing_rate
        self.gender_male_ratio = gender_male_ratio
        self.egg_steps = egg_steps
        self.egg_cycles = egg_cycles
        self.abilities = abilities
        self.Type_1 = Type_1
        self.Type_2 = Type_2
        self.Classification_info = Classification_info
        self.Forms = Forms
        self.gen = gen
        self.Is_Legendary = Is_Legendary
        self.Is_Mythical = Is_Mythical
        self.Is_Ultra_Beast = Is_Ultra_Beast
        self.number_immune = number_immune
        self.number_not_effective = number_not_effective
        self.number_normal = number_normal
        self.number_super_effective = number_super_effective
        self.Moves = Moves if Moves is not None else []
