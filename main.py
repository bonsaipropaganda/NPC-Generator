import tkinter as tk
import random
from names import name_list
from traits import trait_list
from appearence import appearence_list
from inventory import inventory_list

# tkinter shit
root = tk.Tk()
root.configure(bg = 'grey')

# functions
def save():
    with open("Saved NPCs.txt", "a") as file:
        file.write("\n\n" + name_label.cget("text") + "\n")
        file.write(gender_label.cget("text"))
        file.write(race_label.cget("text"))
        file.write(traits_label.cget("text"))
        file.write(appearence_label.cget("text"))
        file.write(motivation_label.cget("text"))
        file.write(inventory_label.cget("text"))
        file.write(gold_label.cget("text"))

def generate():
    choose_name()
    choose_gender()
    choose_race()
    choose_traits()
    choose_appearence()
    choose_motivation()
    choose_inventory()
    choose_gold()

def choose_name():
    choice = random.choice(name_list)
    name_label.configure(text = "Name: " + choice)

def choose_gender():
    choice = random.choice((["male","female"]))
    gender_label.configure(text = "\nGender: " + choice)

def choose_race():
    choice = random.choice((["Elf", "Dwarf", "Tabaxi", "Half-Orc", "Goblin", "Human", "Owlin", "Frog person", "Dragonborne", "Half-Elf", "Gnome", "Halfing", "Tiefling", "Bugbear", "Genesai", "Fairy", "Kenku", "Lizardfolk", "Tortle", "Firbolg"]))
    race_label.configure(text="\nRace: " + choice)

def choose_appearence():
    choice1 = random.choice(appearence_list)
    choice2 = random.choice(appearence_list)
    appearence_label.configure(text = "\nAppearence: " + choice1 + " and " + choice2)

def choose_traits():
    choice1 = random.choice(trait_list)
    choice2 = random.choice(trait_list)
    traits_label.configure(text="\nTraits: " + choice1 + " and " + choice2)

def choose_motivation():
    choice = random.choice((["A drive for exploration, discovery, and adventure", "seeking treasure and riches", "Heroism", "Solitude", "Revenge", "Peace", "Being good/being right", "being wanted/ being loved", "being valuable/being admired", "Being Authentic/To find meaning", "Being Competent / Being Capable", "Being Secure / Being Supported ", "Being Satisfied / Being Content", "Being Independent/ To Protect Themselves", "Being at Peace/ Being Harmonious"]))
    motivation_label.configure(text="\nMotivation: " + choice)

def choose_inventory():
    choice1 = random.choice((inventory_list))
    choice2 = random.choice((inventory_list))
    choice3 = random.choice((inventory_list))
    choice4 = random.choice((inventory_list))
    inventory_label.configure(text = "\nInventory: " + choice1 + ", " + choice2 + ", " + choice3 + ", and " + choice4)

def choose_gold():
    choice = random.randint(0,100)
    gold_label.configure(text = "\nGold: " + str(choice))

# main label
name_label = tk.Label(root, text = "Name: ", font = 14,)
name_label.grid(row = 1, sticky = 'W')

gender_label = tk.Label(root, text = "\nGender: ", font = 14)
gender_label.grid(row = 2, sticky = 'W')

race_label = tk.Label(root, text = "\nRace: ", font = 14)
race_label.grid(row = 3, sticky = 'W')

appearence_label = tk.Label(root, text = "\nAppearence: ", font = 14)
appearence_label.grid(row = 4, sticky = 'W')

traits_label = tk.Label(root, text = "\nTraits: ", font = 14)
traits_label.grid(row = 5, sticky = 'W')

motivation_label = tk.Label(root, text = "\nMotivation: ", font = 14)
motivation_label.grid(row = 6, sticky = 'W')

inventory_label = tk.Label(root, text = "\nInventory: ", font = 14)
inventory_label.grid(row = 7, sticky = 'W')

gold_label = tk.Label(root, text = "\nGold: ", font = 14)
gold_label.grid(row = 8, sticky = 'W')

# buttons
generate_button = tk.Button(root, text = "\nGenerate", font = 14, command = generate)
generate_button.grid(row = 9, sticky = 'W')

save_button = tk.Button(root, text = "\nSave", font = 14, command = save)
save_button.grid(row = 10, sticky = 'W')


# main loop
root.mainloop()
