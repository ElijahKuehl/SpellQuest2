from random import randint
from termcolor import colored
from math import sqrt


class Player(object):
    def __init__(self, name="You", guild="Grey", max_hp=10, spell_list=[]):
        self.name = colored(name.lower().capitalize(), guild.lower())
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.guild = guild
        self.spell_list = spell_list
        self.status = "None"

        self.scrambled = self.name.lower().replace('a', '|').replace('e', 'a').replace('i', 'e').replace('o', 'i').replace('u', 'a').replace('|', 'u').capitalize()

    def attack(self, enemy):
        print "What spell slot will you use?"
        print "Enemy Health: " + str(enemy.hp) + "  Your Health: " + str(self.hp)
        print self.spell_list
        while True:
            slot = raw_input("Spell Slot Number: ")
            try:
                slot = int(slot) - 1
            except ValueError:
                print "You don't have a spell in that slot!"
            else:
                break
        spell = self.spell_list[slot]
        raw_input("You used " + spell + "...")

        status = spellbook[spell][1]
        if status != "None":
            enemy.status = status
            raw_input(enemy.name + " was afflicted with " + status + "!")

        damage = damage_calc(spell, enemy.guild)
        enemy.hp -= damage
        raw_input("You dealt " + str(damage) + " damage!\n")


class NPC(object):
    def __init__(self, name="", guild="Grey", max_hp=9, spell_list=[]):
        if "King" in name:
            self.name = colored(name.split(" ")[0], guild.lower()) + colored(" King", "magenta")
        else:
            self.name = colored(name, guild.lower())
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.guild = guild
        self.spell_list = spell_list
        self.status = "None"

    def attack(self, player):
        print self.name + " attacks!"
        slot = randint(0, len(self.spell_list)-1)
        spell = self.spell_list[slot]
        print self.name + " used " + spell + "..."
        status = spellbook[spell][1]
        if status != "None":
            player.status = status
            raw_input("You are afflicted with " + status + "!")

        damage = damage_calc(spell, player.guild)
        player.hp -= damage
        print "They dealt " + str(damage) + " damage!\n"


you = Player()
elder_wizard = NPC("Elder Wizard", "Magenta", 1000000, ["Smite"])
dummy = NPC("Training Dummy", "Grey", 10, ["Nothing"])
rift_dummy = NPC("Rift Dummy", "Cyan", 10, ["Bend"])
ellis = NPC("Ellis", "Yellow", 15, ["Magic Beam", "Zap"])

spellbook = {
    "Freeze": [0, "Frozen", "Blue"],
    "Snowball": [3, "None", "Blue"],
    "Frost Bite": [6, "None", "Blue"],

    "Fireball": [5, "Burn", "Red"],
    "Firewall": [100000, "Burn", "Red"],

    # "Arc": [0, "None", "Yellow/Cyan"],
    "Zap": [4, "None", "Yellow"],
    "Lightning": [8, "None", "Yellow"],
    "Smite": [100000, "None", "Yellow"],

    "Heal": [0, "Heal", "Green"],
    "Full Regenerate": [0, "Full Heal", "Green"],
    "Raged Claws": [5, "None", "Green"],  # Status of rage? Cuts HP in half?

    "Nothing": [0, "None", "Grey"],
    "Magic Beam": ["2-3", "None", "Grey"],
    "Bite": ["5-6", "None", "Grey"],  # num - num makes the damage random each time
    "Magic Laser": ["4-7", "None", "Grey"],
    "Invisibility": [0, "Invisible", "Grey"],

    "Bend": [3, "None", "Cyan"]
    }


def damage_calc(spell, other_col):  # Calculate the damage from an attack, using all modifiers.
    own_col = spellbook[spell][2]
    damage = spellbook[spell][0]
    if isinstance(damage, str):
        damage = randint(int(damage.split('-')[0]), int(damage.split('-')[1]))

    if own_col == "Blue" and other_col == "Green" \
            or own_col == "Green" and other_col == "Red" \
            or own_col == "Red" and other_col == "Yellow" \
            or own_col == "Yellow" and other_col == "Blue":
        print("Effective, increased Damage!")
        return damage * 2
    if other_col == "Blue" and own_col == "Green" \
            or other_col == "Green" and own_col == "Red" \
            or other_col == "Red" and own_col == "Yellow" \
            or other_col == "Yellow" and own_col == "Blue":
        print("Ineffective, decreased damage!")
        return round(damage / 2, 0)
    return damage


def speak(person, text):
    raw_input(person.name + ": " + text)


def encounter(player, enemy):  # Take turns attacking as long as there is still HP
    print("\nFight between " + player.name + " and " + enemy.name)
    while True:
        if player.hp > 0:
            player.attack(enemy)
        else:
            raw_input("Your hp reached 0!")
            print player.name + ", of the " + player.guild + " Guild, fell to " + enemy.name + "."
            raw_input("You died with the spells " + str(player.spell_list) + " and " + str(player.max_hp) + " hp.")
            quit()
        if enemy.hp > 0:
            enemy.attack(player)
        else:
            bonus_hp = str(round(sqrt(enemy.max_hp), 0)).split('.')[0]
            player.max_hp += int(bonus_hp)
            raw_input(enemy.name + "'s hp reached 0!")
            raw_input("You defeated " + enemy.name + "! You gained " + bonus_hp + " max hp!\n")
            player.hp = player.max_hp
            break


def begin():
    # speak(elder_wizard, "")
    raw_input("Welcome to Spell Quest, a text adventure! Press enter to progress, and make choices as you please.")
    print
    speak(elder_wizard, "Ah! Welcome adventurer! I am the Elder Wizard, and this is the Guild of Wizards!")
    speak(elder_wizard, "Now you may have heard stories about us, both good and bad...")
    speak(elder_wizard, "And I can assure you, they are all true!")
    speak(elder_wizard, "We used to turn perfectly normal objects into entities of massive power!!!")
    speak(elder_wizard, "And unfortunately, we tore a hole in reality doing so!")
    speak(elder_wizard, "We lost the previous elder wizard that way.")
    speak(elder_wizard, "But fret no more! I've created a much safer, and easier method of enchanting. How you ask?")
    speak(elder_wizard, "By doing it on yourself!")
    speak(elder_wizard, "That way, your magic shall be with you always.")
    speak(elder_wizard, "I assume you wish to become a wizard, as you found us here?")
    speak(elder_wizard, "Then lets teach you your first spell!")
    speak(elder_wizard, "Every wizard starts out with the spell magic beam.")
    speak(elder_wizard, "Here is the spell book. Place your hand on it and open your mind!")
    hand = raw_input("The wizard brings out a spellbook. Place your hand on it? Y/N")
    while not ('y' in hand.lower()):
        speak(elder_wizard, "Don't be scared, it's just a bit of magic!")
        hand = raw_input("Place your hand on the spellbook? Y/N")
    speak(elder_wizard, "Now, focus on your hand, and open your mind to it's energy.")

    focus = raw_input("You feel a pulsing energy where your hand rests on the book. Free your mind to the magic? Y/N")
    while not ('y' in focus.lower()):
        speak(elder_wizard, "Now, this only works if you're willing.")
        focus = raw_input("Let the magic into your mind? Y/N")
    raw_input("With your mind opened, you feel the energy on your palm start crawling up your arm, and up, and up.")
    raw_input("When it reaches your head, you feel awakened! You can control the magic!")
    raw_input("The universe has opened up to a whole new realm of possibilities!!!")
    you.spell_list.append("Magic Beam")
    raw_input("\nYou learned the spell Magic Beam!\n")
    speak(elder_wizard, "Now go practice your new spell and cause chaos in the world around you!")
    speak(elder_wizard, "Good luck on your way, young wizard!!!")


def first_encounter():
    raw_input("There appears to be a training dummy in the courtyard. You should practice there.")
    encounter(you, dummy)
    raw_input("Huh? Something is happening!!!")
    raw_input("Along with the dummy, your finishing blow tore the fabric of reality!")
    raw_input("A rift has opened! A mysterious mist emerges, and possesses the dummy!\n")
    speak(rift_dummy, "Goraghghg!!!")
    encounter(you, rift_dummy)
    raw_input("The mysterious mist retreated into the rift.")
    raw_input("The rift sealed itself!")
    encounter(you, ellis)


if __name__ == '__main__':
    # begin()
    you.max_hp = 13
    you.spell_list = ["Magic Beam"]
    first_encounter()
    print("The story will continue soon! Thanks for playing!")

""" 
The cannon story from the first:
    You, the player, find the Guild of Wizards, and join a non-Yellow Guild.
    You meet Noah, defeat and save Samantha, and vow revenge against The Sparks.
    You travel to each of the 3 elemental realms, encountering the Ent King, Snow King, Magma King, and (Shadow King).
    The Natural Kings assist you and inform you that the Yellow Guild is artificial and evil.
    Investigating the Yellow Guild, you find out that they are building the Tech King, to defeat the other Kings.
    Unfortunately, you are caught and defeated, only to be saved by Thomson. 
    To stop The Sparks, you go to the Elder Wizard's Library to learn new spells. 
    The Elder Wizard Catches on. To you. He is on the side of The Sparks.
    Once powered up, you go to fight The Sparks, and get to the nearly powered up Tech King, the robot dragon.
    You call upon the Natural Kings and they start attacking the Tech King, only to be hindered by the Elder Wizard.
    An epic Fight ensues where You fight the Elder Wizard with the King's help, while the Kings attack the Tech King.
    Once at half health, the Elder Wizard resorts to something dire. Spacial Magic. 
    He enchants the Earth and starts draining all magic, including from The Kings, and tries to use it on you.
    But he fails, the magic is too much, and tears a hole in reality, destroying himself first.
    The rift absorbs everything around it, like a black hole.
    Depending on your guild, you resist its pull.
    Blue: Freeze yourself to the ground, Freeze the rift.
    Red: Rocket yourself backwards, melt reality back together.
    Green: Root yourself, Heal and mend the rift.
    Grey: Shadows around you pull you back, control the magic and seal the rift.
    With the rift controlled, you obtain the magic and return it to the world, but you changed some things.
    Yellow magic is gone. Objects can no longer be enchanted, only oneself.
    With the Elder Wizard gone, you become the new owner of the title!
    
The Sparks Path:
    You join the Yellow Guild, and get invited into The Sparks.
    You knock out Noah, who is saved by Thomson
    You learn about the Tech King, and need to power it up. 
    You go around defeating the other Kings, bringing their Essence back to The Sparks
    The Tech King gets powered up by the essence 
    Tech King rivals teh power of the Elder Wizard, who feels threatened
    You gain control of the Tech King and fight the Elder Wizard
    You win and become a being of ultimate energy and magic.
    
Things to change:
    Add a Blue Guild Friend
    Add a story for the Sparks
    
The plan for this story:
    Similar to the first, but new world and characters. The sparks disband and disperse. 
    Happens after SpellQuest 1, previous characters are older, but not oo old, and still at the Guild of Wizards.
    Ethan is still coping with the loss of The Sparks, his entire goal demolished in an instant. Hides from others.
    New character trying to bring back the sparks, naive to their menace. New Noah? Looks up to Ethan. Little Brother?
    Noah has become magma infused, as he is trying to become a new King after the rift destroyed them.
    Samantha is now Grey after Yellow is destroyed. Doesn't cause trouble but won't stop it.
    Thompson is researching what's making the Ents angry and wants to calm them. 
    Elder wizard is back as Spacial Wizard. Large and menacing, uses otherworldly magic. Unaffected by magic reset.
    Spacial Wizard is main threat of the game. Rifts are popping up everywhere with cyan colored creatures.
    First encounter, a training dummy, possessed by a rift monster. Or, training dummy tears a rift after destroyed.   
"""
