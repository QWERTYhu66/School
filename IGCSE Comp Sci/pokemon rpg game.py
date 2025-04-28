import csv

class Pokemon:
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
        self.Moves = []

class Move:
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

class Trainer:
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

    def show_trainer_info(self):
        print(f"Trainer ID: {self.ID}")
        print(f"Trainer Name: {self.Name}")
        print(f"Badges: {self.Badges}")
        print(f"Money: ${self.Money}")
        print(f"Items: {self.Items}")

    def show_trainer_pokemon(self):
        print(f"{self.Name}'s Pokémon:")
        for p in self.Pokemon:
            print(f"- {p.Name}")

class Battle:
    def __init__(self, trainer1, trainer2):
        self.trainer1 = trainer1
        self.trainer2 = trainer2
        self.trainer1_pokemon = trainer1.Pokemon[0]
        self.trainer2_pokemon = trainer2.Pokemon[0]
        self.turn = 1
        self.winner = None
        self.loser = None
        self.battle_log = []

    def add_to_battle_log(self, log):
        self.battle_log.append(log)

    def show_battle_log(self):
        print("Battle Log:")
        for log in self.battle_log:
            print(log)

    def start_battle(self):
        print(f"Battle started between {self.trainer1.Name} and {self.trainer2.Name}")
        while True:
            if self.turn % 2 == 1:
                attacker = self.trainer1_pokemon
                defender = self.trainer2_pokemon
                trainer = self.trainer1
            else:
                attacker = self.trainer2_pokemon
                defender = self.trainer1_pokemon
                trainer = self.trainer2

            print(f"\n{trainer.Name}'s turn! ({attacker.Name})")
            print("Available moves:")
            for idx, move in enumerate(attacker.Moves):
                print(f"{idx + 1}. {move.Name} (Power: {move.Power})")

            try:
                move_choice = int(input("Enter the move number: ")) - 1
                if move_choice not in range(len(attacker.Moves)):
                    raise ValueError
                chosen_move = attacker.Moves[move_choice]
            except (ValueError, IndexError):
                print("Invalid move choice, try again.")
                continue

            damage = chosen_move.Power - (defender.Defense / 2)
            damage = max(0, int(damage))

            print(f"{attacker.Name} used {chosen_move.Name}!")
            print(f"{defender.Name} took {damage} damage.")
            self.add_to_battle_log(f"{attacker.Name} used {chosen_move.Name} and dealt {damage} damage to {defender.Name}.")

            defender.HP -= damage
            if defender.HP <= 0:
                print(f"\n{defender.Name} fainted!")
                if self.turn % 2 == 1:
                    self.winner = self.trainer1
                    self.loser = self.trainer2
                else:
                    self.winner = self.trainer2
                    self.loser = self.trainer1
                break

            self.turn += 1

        print("\nBattle ended!")
        print(f"Winner: {self.winner.Name}")
        print(f"Loser: {self.loser.Name}")
        self.show_battle_log()

# Pokemon Data
pokemons = []

with open('./pokemon_data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Pokemon(
            ID=int(row['ID']),
            Name=row['Name'],
            HP=int(row['HP']),
            Attack=int(row['Attack']),
            Defense=int(row['Defense']),
            Sp_Attack=int(row['Sp_Attack']),
            Sp_Defense=int(row['Sp_Defense']),
            Speed=int(row['Speed']),
            Base_Stats=int(row['Base_Stats']),
            normal_weakness=float(row['normal_weakness']),
            fire_weakness=float(row['fire_weakness']),
            water_weakness=float(row['water_weakness']),
            electric_weakness=float(row['electric_weakness']),
            grass_weakness=float(row['grass_weakness']),
            ice_weakness=float(row['ice_weakness']),
            fighting_weakness=float(row['fighting_weakness']),
            poison_weakness=float(row['poison_weakness']),
            ground_weakness=float(row['ground_weakness']),
            flying_weakness=float(row['flying_weakness']),
            psychic_weakness=float(row['psychic_weakness']),
            bug_weakness=float(row['bug_weakness']),
            rock_weakness=float(row['rock_weakness']),
            ghost_weakness=float(row['ghost_weakness']),
            dragon_weakness=float(row['dragon_weakness']),
            dark_weakness=float(row['dark_weakness']),
            steel_weakness=float(row['steel_weakness']),
            fairy_weakness=float(row['fairy_weakness']),
            height_inches=float(row['height_inches']),
            height_meters=float(row['height_meters']),
            weight_pounds=float(row['weight_pounds']),
            weight_kilograms=float(row['weight_kilograms']),
            capturing_rate=int(row['capturing_rate']),
            gender_male_ratio=float(row['gender_male_ratio']),
            egg_steps=int(row['egg_steps']),
            egg_cycles=int(row['egg_cycles']),
            abilities=row['abilities'].split(','),
            Type_1=row['Type_1'],
            Type_2=row['Type_2'] if row['Type_2'] else None,
            Classification_info=row['Classification_info'],
            Forms=row['Forms'],
            gen=int(row['gen']),
            Is_Legendary=row['Is_Legendary'] == "True",
            Is_Mythical=row['Is_Mythical'] == "True",
            Is_Ultra_Beast=row['Is_Ultra_Beast'] == "True",
            number_immune=int(row['number_immune']),
            number_not_effective=int(row['number_not_effective']),
            number_normal=int(row['number_normal']),
            number_super_effective=int(row['number_super_effective'])
        )
        pokemons.append(p)
