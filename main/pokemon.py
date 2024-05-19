import random

#class for creating your trainer
class Trainer:

    #tainers information
    def __init__(self, rival) -> None:
        self.rival = rival
        self.trainer = input("What is your name?")
        self.pick_gender = input("\nWhat is your gender?")
        self.gender = ("boy", "girl")


#player can choose gender and name for trainer
    def char(self):

        self.trainer
        for genders in self.gender:
            self.pick_gender
            if self.pick_gender == genders:
                print(f"\nOk, you are a {self.pick_gender}\n")
                
                break
            else:
                print("Not a gender")
        print(f"My grandson name is {self.rival}\n")
        print("Welcome to the world of Pokemon")

#class for pokemon
class Pokemon(Trainer):

    def __init__(self, rival) -> None:
        super().__init__(rival)
        

        #trainer's pokemon information
        self.party = ["Charmander"]
        self.level = 16
        self.hp = random.randint(50, 75)
        self.stats = {"attack": random.randint(10, 25), "defense": random.randint(10, 25), "special attack": random.randint(10, 25), 
                      "special defense": random.randint(10, 25), "speed ": random.randint(10, 25), }
        self.pokemon_health = self.hp
        self.random_choice = self.party[-1]
        
        #damage calculator 
        self.damage = self.hp // self.stats["attack"] + 1 * 3
        self.special_damage = self.hp //  self.stats["special attack"] + 1 * 3

        #attack moves 
        self.attacks = ["tackle", "scratch", "pound"]
        self.special_attacks = ["vine whip", "ember", "bubble"]

        # enemy battle conditions 
        self.enemy = "Blue"
        self.enemy_party = ["Squirtle"]
        self.enemy_choice = random.choice(self.attacks)
        self.enemy_choice2 = random.choice(self.special_attacks)
        self.enemy_pokemon = self.enemy_party[-1]
        self.enemy_health = self.hp
        self.enemy_damage = self.hp // self.stats["attack"] + 1 * 2
        self.enemy_special_damage = self.hp //  self.stats["special attack"] + 1 * 2

        #pokemon pc

        self.pc = ["pidgey", "nidoran" "spearow", "caterpie"]

        #items in bag 
        self.bag = {"potions": random.randint(1, 10), "super potions": random.randint(1, 10), 
                    "hyper potions": random.randint(1, 10), "revives": random.randint(1, 10), 
                    "rare candies": random.randint(1, 10), "escape ropes": random.randint(1, 10)}
        
    

    #the battle system 
    def battle(self):


        #Message to start the battle
        print(f"You sent out {self.random_choice}: ")

        while True:

            user_choice = str(input("What will you do?: "))

            #battle conditions 
            if user_choice in self.attacks:
                print(f"\n{self.random_choice} did {self.damage} damage!!!")
                self.enemy_health -= self.damage
                if self.enemy_choice:
                    self.pokemon_health -= self.enemy_damage
                    print(f"\n{self.enemy_pokemon} did {self.enemy_damage} damage!!!")
                elif self.enemy_choice2:
                    self.pokemon_health -= self.enemy_special_damage
                    print(f"\n{self.enemy_pokemon} did {self.enemy_special_damage} damage!!!")
            elif user_choice in self.special_attacks:
                self.enemy_health -= self.special_damage
                print(f"\n{self.random_choice} did {self.special_damage} damage!!!")
                if self.enemy_choice:
                    self.pokemon_health -= self.enemy_damage
                    print(f"\n{self.enemy_pokemon} did {self.enemy_damage} damage!!!")
                elif self.enemy_choice2:
                    self.pokemon_health -= self.enemy_special_damage
                    print(f"\n{self.enemy_pokemon} did {self.enemy_special_damage} damage!!!")
            else:
                print(f"{self.random_choice} can't do that!!!")
            print(f"\n{self.enemy_pokemon} has {self.enemy_health} hp left!!!\n")
            print(f"{self.random_choice} has {self.pokemon_health} hp left!!!\n")
    
            #if pokemon fainted, pokemon is popped from the party
            if self.enemy_health <= 0:
                self.enemy_party.pop()
                print(f"{self.enemy}'s pokemon has fainted {self.enemy_party}")
                print(f"{self.enemy} sent out {self.enemy_pokemon}")
            elif self.pokemon_health <= 0:
                self.party.pop()
                print(f"{self.rival}'s pokemon has fainted\n")
                print(f"{self.party[-1]} was sent out")
            elif self.enemy and self.pokemon_health <= 0:
                self.enemy_party.pop()
                self.party.pop()
                print("HUH??? IT'S A DRAW!!!")

            #if all pokemon in party is fainted, the game ends
            if len(self.party) == 0:
                return f"{self.enemy} is the winner"
            elif len(self.enemy_party) == 0:
                return f"{self.rival} is the winner"
            
 
    #lets trainer catch pokemon, if party is full, pokemon is sent to pc
    def catch_pokemon(self, pokemon):
        try:
            #commands for catching pokemon
            commands = ('catch', 'c', 'e') 
            catching = str(input(f"Will you catch {pokemon}?: "))

            #if trainer's party is 6, pokemon will be sent to pc, else it will go into trainer's party
            if catching in commands:
                if len(self.party) == 6:
                    self.pc.append(pokemon)
                    print(f"Your party is full, {pokemon} was sent to the pc: {self.pc}")
                else:
                    self.party.append(pokemon)
                    print(f"YAY, you caught {pokemon}, {self.party}")
            else:
                print("Not a commmand")               
        except IndexError as e:
            return("Index has exceded ", e)
        except ValueError as e:
            return("Value is invalid ", e)
        except NameError as e:
            return("Name doesn't exist ", e)
        
    #escape battle 
    def run(self):
        while True:
            #escape commands for user 
            commands = ("run", "r", "q")
            flee = str(input("Do you want to flee?: "))
            if flee in commands:
                print("You escaped battle")
                exit()
            #function will loop untill correct command is inputted 
            else:
                print("You couldn't run")
    
    #poke mart for shopping 
    def poke_mart(self):
        try:
            print("Welcome to the pokemart. What would you like to buy?\n")
            while True:
                #trainer's money and poke mart selection
                money = 2000
                commands = ("poke ball", "great ball", "potion", "super potion", "hyper potion", "revive", "escape rope", "repel", 'super repel')

                print("Poke ball: $200,", "Great ball: $600,", "Potion: $300,", "\nSuper potion: $200,", 
                      "hyper potion: $1,200,", "revive: $1,500,", 
                      "\nescape rope: $550,", "repel: $350,", 'super repel: $500')
                
                buy = input()

                #trainer can buy different options only if the money amount is enough
                if buy in commands:
                    if buy == "poke ball":
                        if money >= 200:
                            money -= 200
                            self.bag['poke balls'] = 1
                            print(f"You bought a poke ball: You have ${money} left")
                        else:
                            print("You don't have enough")
                    elif buy == "great ball":
                        if money >= 600:
                            money -= 600
                            self.bag['great balls'] = 1
                            print(f"You bought a great ball: You have ${money} left")
                        else:
                            print("You don't have enough")
                    elif buy == "escape rope":
                        if money >= 550:
                            money -= 550
                            self.bag['escape ropes'] += 1
                            print(f"You bought a escape rope: You have ${money} left")
                        else:
                            print("You don't have enough")
                    elif buy == "hyper potion":
                        if money >= 1200:
                            money -= 1200
                            self.bag['hyper potions'] += 1
                            print(f"You bought a hyper potion: You have ${money} left")
                        else:
                            print("You don't have enough")
                    elif buy == "potion":
                        if money >= 300:
                            money -= 300
                            self.bag['potions'] += 1
                            print(f"You bought a potion: You have ${money} left")
                        else:
                            print("You don't have enough")
                    elif buy == "repel":
                        if money >= 350:
                            money -= 350
                            self.bag['repels'] = 1
                            print(f"You bought a repel: You have ${money} left")
                        else:
                            print("You don't have enough")
                    elif buy == "revive":
                        if money >= 1500:
                            money -= 1500
                            self.bag['revives'] += 1
                            print(f"You bought a revive: You have ${money} left")
                        else:
                            print("You don't have enough")
                    elif buy == "super potion":
                        if money >= 700:
                            money -= 700
                            self.bag['super potions'] += 1
                            print(f"You bought a super potion: You have ${money} left")
                        else:
                            print("You don't have enough")
                    elif buy == "super repel":
                        if money >= 500:
                            money -= 500
                            self.bag['super repels'] = 1
                            print(f"You bought a super repel: You have ${money} left")
                        else:
                            print("You don't have enough")

                    return self.bag
                else:
                    return("Ummm not a option")

        except ValueError as e:
            return("Not a value " + e) 
        
    #level up function for pokemon in party
    def level_up(self, result):
        exp = 0

        win = True
        lose = False
        
        #if pokemon win's battle, pokemon will gain 500 experience 
        while win and exp < (500):
            for pokemon in self.party:
                if result == "win":
                    exp += 100
                    print(f"{pokemon} gained {exp} experience points")
                    # if 500 exp is reached, pokemon will level up
                    if exp == 500:
                        print(f"{pokemon} has reached level {self.level + 1}")
                    else:
                        pass
                #pokemon will only gain experience if win condition is true
                else:
                    print(f"You fainted, you gained {exp} experience")
                    return lose
            
    #evolve pokemon (only for charmander)
    def evolve(self):
        for index, pokemon in enumerate(self.party):
            if (index == 0) and (self.level == 16):
                return(f"WOW!!!, {pokemon} has evolved to Charmeleon!")
            else:
                pass


#prints the function of choice
if __name__ == "__main__":

    start = Pokemon("Blue")
    start.char()
    start.level_up("win")