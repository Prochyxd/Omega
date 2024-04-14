#The game will be a simple text based game where the player will be able to move around a map and interact with objects / NPCs
#The player will be able to pick up objects and use them to solve puzzles
#The player will have a limited inventory space
#The player will be able to interact with NPCs and have conversations with them
#The player will be able to fight enemies and level up
#The player will be able to save and load their game into json files
#The player will be able to view their stats
#The player will be able to view the map
#The player will be able to view their inventory
#The player will be able to get quests from NPCs
#The player will be able to view their quest log
#The player will be able to view their achievements

import json
import os
import random
import sys
import time
from typing import List, Dict, Any, Union

# Define the player class
class Player:
    def __init__(self, name: str, level: int, health: int, attack: int, defense: int, experience: int, gold: int, inventory: List[str], location: str, quests: List[str], achievements: List[str]):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense
        self.experience = experience
        self.gold = gold
        self.inventory = inventory
        self.location = location
        self.quests = quests
        self.achievements = achievements

    def __str__(self):
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}\nExperience: {self.experience}\nGold: {self.gold}\nInventory: {self.inventory}\nLocation: {self.location}\nQuests: {self.quests}\nAchievements: {self.achievements}"

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack += 2
        self.defense += 2
        self.experience = 0

    def gain_experience(self, experience: int):
        self.experience += experience
        if self.experience >= 100:
            self.level_up()

    def gain_gold(self, gold: int):
        self.gold += gold

    def add_item_to_inventory(self, item: str):
        self.inventory.append(item)

    def remove_item_from_inventory(self, item: str):
        if item in self.inventory:
            self.inventory.remove(item)

    def add_quest(self, quest: str):
        self.quests.append(quest)

    def remove_quest(self, quest: str):
        if quest in self.quests:
            self.quests.remove(quest)

    def add_achievement(self, achievement: str):
        self.achievements.append(achievement)

# Define the game class
class Game:
    def __init__(self):
        self.player = None
        self.locations = {}
        self.objects = {}
        self.npcs = {}
        self.enemies = {}
        self.quests = {}
        self.achievements = {}

    def load_game(self, file_name: str):
        with open(file_name, "r") as file:
            data = json.load(file)
            self.player = Player(data["player"]["name"], data["player"]["level"], data["player"]["health"], data["player"]["attack"], data["player"]["defense"], data["player"]["experience"], data["player"]["gold"], data["player"]["inventory"], data["player"]["location"], data["player"]["quests"], data["player"]["achievements"])

            for location in data["locations"]:
                self.locations[location["name"]] = location

            for obj in data["objects"]:
                self.objects[obj["name"]] = obj

            for npc in data["npcs"]:
                self.npcs[npc["name"]] = npc

            for enemy in data["enemies"]:
                self.enemies[enemy["name"]] = enemy

            for quest in data["quests"]:
                self.quests[quest["name"]] = quest

            for achievement in data["achievements"]:
                self.achievements[achievement["name"]] = achievement

    def save_game(self, file_name: str):
        data = {
            "player": {
                "name": self.player.name,
                "level": self.player.level,
                "health": self.player.health,
                "attack": self.player.attack,
                "defense": self.player.defense,
                "experience": self.player.experience,
                "gold": self.player.gold,
                "inventory": self.player.inventory,
                "location": self.player.location,
                "quests": self.player.quests,
                "achievements": self.player.achievements
            },
            "locations": [],
            "objects": [],
            "npcs": [],
            "enemies": [],
            "quests": [],
            "achievements": []
        }

        for location in self.locations.values():
            data["locations"].append({
                "name": location["name"],
                "description": location["description"],
                "objects": location["objects"],
                "npcs": location["npcs"],
                "enemies": location["enemies"]
            })

        for obj in self.objects.values():
            data["objects"].append({
                "name": obj["name"],
                "description": obj["description"],
                "use": obj["use"]
            })

        for npc in self.npcs.values():
            data["npcs"].append({
                "name": npc["name"],
                "description": npc["description"],
                "quests": npc["quests"],
                "dialogue": npc["dialogue"]
            })

        for enemy in self.enemies.values():
            data["enemies"].append({
                "name": enemy["name"],
                "description": enemy["description"],
                "health": enemy["health"],
                "attack": enemy["attack"],
                "defense": enemy["defense"],
                "experience": enemy["experience"],
                "gold": enemy["gold"]
            })

        for quest in self.quests.values():
            data["quests"].append({
                "name": quest["name"],
                "description": quest["description"],
                "objectives": quest["objectives"],
                "rewards": quest["rewards"]
            })

        for achievement in self.achievements.values():
            data["achievements"].append({
                "name": achievement["name"],
                "description": achievement["description"]
            })

        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)

    def move(self, direction: str):
        if direction in self.locations[self.player.location]["exits"]:
            self.player.location = self.locations[self.player.location]["exits"][direction]
            print(f"You move {direction} to {self.player.location}")
        else:
            print("You can't go that way.")

    def look(self):
        #if there is nothing in the room print "There is nothing here"
        if not self.locations[self.player.location]["objects"] and not self.locations[self.player.location]["npcs"] and not self.locations[self.player.location]["enemies"]:
            print("There is nothing here.")
            return
        print(self.locations[self.player.location]["description"])
        print("You see:")
        for obj in self.locations[self.player.location]["objects"]:
            print(f"- {obj}")
        for npc in self.locations[self.player.location]["npcs"]:
            print(f"- {npc}")
        for enemy in self.locations[self.player.location]["enemies"]:
            print(f"- {enemy}")

    def examine(self, obj: str):
        if obj in self.objects:
            print(self.objects[obj]["description"])
        else:
            print("You don't see that object here.")

    def use(self, obj: str):
        if obj in self.objects:
            print(self.objects[obj]["use"])
        else:
            print("You can't use that object.")

    def talk(self, npc: str):
        if npc in self.npcs:
            print(self.npcs[npc]["dialogue"])
            for quest in self.npcs[npc]["quests"]:
                if quest not in self.player.quests:
                    print(f"{npc} offers you a quest: {quest}")
        else:
            print("You don't see that NPC here.")

    def fight(self, enemy: str):
        if enemy in self.enemies:
            print(f"You engage in combat with {enemy}!")
            while self.player.health > 0 and self.enemies[enemy]["health"] > 0:
                player_damage = max(0, self.player.attack - self.enemies[enemy]["defense"])
                enemy_damage = max(0, self.enemies[enemy]["attack"] - self.player.defense)
                self.player.health -= enemy_damage
                self.enemies[enemy]["health"] -= player_damage
                print(f"You take {enemy_damage} damage and deal {player_damage} damage to {enemy}.")
                time.sleep(1)
            if self.player.health <= 0:
                print("You have been defeated!")
                sys.exit()
            else:
                print(f"You have defeated {enemy}!")
                self.player.gain_experience(self.enemies[enemy]["experience"])
                self.player.gain_gold(self.enemies[enemy]["gold"])
                self.locations[self.player.location]["enemies"].remove(enemy)
        else:
            print("You don't see that enemy here.")

    def pick_up(self, obj: str):
        if obj in self.locations[self.player.location]["objects"]:
            self.player.add_item_to_inventory(obj)
            self.locations[self.player.location]["objects"].remove(obj)
            print(f"You pick up {obj}.")
        else:
            print("You don't see that object here.")

    def drop(self, obj: str):
        if obj in self.player.inventory:
            self.player.remove_item_from_inventory(obj)
            self.locations[self.player.location]["objects"].append(obj)
            print(f"You drop {obj}.")
        else:
            print("You don't have that object in your inventory.")

    def take_quest(self, npc: str, quest: str):
        if npc in self.npcs and quest in self.npcs[npc]["quests"]:
            self.player.add_quest(quest)
            print(f"You accept the quest: {quest}")
        else:
            print("You can't take that quest.")

    def complete_quest(self, quest: str):
        if quest in self.player.quests:
            objectives = self.quests[quest]["objectives"]
            for obj in objectives:
                if obj not in self.player.inventory:
                    print(f"You need to find {obj} to complete the quest.")
                    return
            for obj in objectives:
                self.player.inventory.remove(obj)
            rewards = self.quests[quest]["rewards"]
            for reward in rewards:
                if reward.startswith("experience"):
                    experience = int(reward.split()[1])
                    self.player.gain_experience(experience)
                elif reward.startswith("gold"):
                    gold = int(reward.split()[1])
                    self.player.gain_gold(gold)
                elif reward.startswith("item"):
                    item = reward.split()[1]
                    self.player.add_item_to_inventory(item)
            self.player.remove_quest(quest)
            print(f"You complete the quest: {quest}")
        else:
            print("You don't have that quest.")

    def view_inventory(self):
        print("Inventory:")
        for item in self.player.inventory:
            print(f"- {item}")

    def view_stats(self):
        print(self.player)

    def view_map(self):
        print("Map:")
        for location in self.locations:
            print(f"- {location}")

    def view_quests(self):
        print("Quests:")
        for quest in self.player.quests:
            print(f"- {quest}")

    def view_achievements(self):
        print("Achievements:")
        for achievement in self.player.achievements:
            print(f"- {achievement}")

# Define the main function
def main():
    game = Game()
    game.load_game("game_data.json")

    while True:
        print("Commands: move, look, examine, use, talk, fight, pick_up, drop, take_quest, complete_quest, view_inventory, view_stats, view_map, view_quests, view_achievements, save, quit")
        command = input("Enter a command: ").split()
        action = command[0]

        if action == "move":
            game.move(command[1])
        elif action == "look":
            game.look()
        elif action == "examine":
            game.examine(command[1])
        elif action == "use":
            game.use(command[1])
        elif action == "talk":
            game.talk(command[1])
        elif action == "fight":
            game.fight(command[1])
        elif action == "pick_up":
            game.pick_up(command[1])
        elif action == "drop":
            game.drop(command[1])
        elif action == "take_quest":
            game.take_quest(command[1], command[2])
        elif action == "complete_quest":
            game.complete_quest(command[1])
        elif action == "view_inventory":
            game.view_inventory()
        elif action == "view_stats":
            game.view_stats()
        elif action == "view_map":
            game.view_map()
        elif action == "view_quests":
            game.view_quests()
        elif action == "view_achievements":
            game.view_achievements()
        elif action == "save":
            game.save_game("game_data.json")
        elif action == "quit":
            sys.exit()
        else:
            print("Invalid command.")

# Call the main function
if __name__ == "__main__":
    main()

# The game is now fully functional and the player can interact with the game world using text commands
# The player can move around the map, pick up objects, talk to NPCs, fight enemies, complete quests, view their inventory, view their stats, view the map, view their quests, view their achievements, save the game, and quit the game
# The game data is loaded from a json file and saved to a json file
# The game loop will continue until the player quits the game
# The player can enter commands to interact with the game world
# The game will respond to the player's commands and update the game state accordingly

