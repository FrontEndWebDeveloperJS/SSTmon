import random
computerHealth = 0

for i in range(1,6):
    print(".")
print("Made By FOA Inc.")
print("UX Design by Santhiyaa Senthilkumar and Jonathan Tan Jiayi")
print("Developed by Koh Kai Sern")
for i in range(1,6):
    print(".")
print("Welcome to the world of SSTmon! I'm professor Oak.")
playerName = input("First, tell me your name. Please put your name in double quotes. If you don't, the game will crash and you will have to restart.")
if isinstance(playerName, str):
    playerAge = input("Perfect! Now, what is your age? No double quotes.")
    if isinstance(playerAge, int):
        playerGender = input("Perfect! Are you a boy or a girl? Type Male or Female. Once again, put your gender in double quotes.")
        if (isinstance(playerGender, str) and playerGender == "Male") or playerGender == "Female":
            playerPokemon = input("Finally, what pokemon will you choose? Type Bulbasaur, Charmander or Squirtle. Remember: Double quotes!")
            if isinstance(playerPokemon, str) and  playerPokemon == "Bulbasaur":
                for i in range(1,6):
                    print(".")
                print("All right! Let's start your SSTmon adventure!")
                for i in range(1,6):
                     print(".")
                print("Walking...")
                for i in range(1,4):
                     print(".")
                playerHealth = 100
                computerHealth = 100
                print("A trainer spotted you! He wants to fight!")
                print("John sent out Caterpie!")
                print("You sent out " + str(playerPokemon) + "!")
                for i in range(1,4):
                    print(".")
                computerMoveset = ["crimson charge","tackle","unnerving growl","dart bullet"]
                print("Your moves:")
                print("1. Leaf Whirlwind; Minus 5 health from opponent with a 25 percent chance of poisoning the enemy")
                print("2. Quasi-Protect; Minus 4 health from opponent with a 20 percent chance of immunity for the next turn")
                print("3. Nature's Fury; Minus 6 health from opponent with 12 percent chance of critical")
                print("4. Rebound Smash; Minus 5 health from opponent with a 30 percent chance of enemy flinching")
                for i in range(1,4):
                    print(".")
                while playerHealth > 0 or computerHealth > 0:
                    playerChoice = input("Enter your move number. No double quotes!")
                    for i in range(1,3):
                        print(".")
                    if isinstance(playerChoice, int) and (playerChoice == 1 or playerChoice == 2 or  playerChoice == 3 or  playerChoice == 4):
                        moveSet = ["leaf whirlwind","quasi-protect","rebound smash","nature's fury"]
                        playerChoice -= 1
                        print(str(playerPokemon) + " used " + moveSet[playerChoice] + "!")
                        computerChoice = random.randint(0,3)
                        if playerChoice == 0 and computerChoice == 0:
                            p_mChance1 = random.randint(1,100)
                            c_mChance1 = random.randint(1,100)
                            p_poisonChance = random.randint(1,4)
                            if p_mChance1 == 1:
                                print("You missed!")
                            elif p_poisonChance == 1:
                                print("You used " + moveSet[playerChoice] + ". Caterpie lost 5 health!")
                                print("Caterpie was poisoned!")
                                computerHealth -= 5
                                if c_mChance1 == 1:
                                    print("Caterpie used crimson charge but missed!")
                                else:
                                    print("Caterpie used crimson charge! Bulbasaur lost 8 health!")
                                    playerHealth -= 8
                                    print("Your health is " + str(playerHealth))
                            else:
                                print("You used " + moveSet[playerChoice] + ". Caterpie lost 5 health!"
                                computerHealth -= 5
                                print("Caterpie's health is " + str(computerHealth))
                                if c_mChance1 == 1:
                                    print("Caterpie used crimson charge but missed!")
                                else:
                                    print("Caterpie used crimson charge! Bulbasaur lost 8 health!")
                                    playerHealth -= 8
                                    print("Your health is " + str(playerHealth))
        else:
            print("Please restart the game and enter in either Male or Female.")
