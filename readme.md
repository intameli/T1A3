# T1A3: Bookworm Adventures Terminal Clone

Jacob Smith

## Github link

[Link](https://github.com/intameli/T1A3)

## Style conventions

[PEP 8](https://peps.python.org/pep-0008/)

[Google style docstrings](https://google.github.io/styleguide/pyguide.html)

## Help

### Installation

Run `bash script.sh` in your terminal at the programs directory to start

### Requirements

- python 3.6 or higher
- bash

Should run on any computer that meets those two. 3.6 required due to using fstrings. The program has no dependencies.

### How to play

When the game starts you can choose between long and short modes. In long you face all 13 enemies. In short you only face the three bosses and you level up much faster. Short mode is a fast way to see all the mechanics in the game.

/quit to exit game.

/scramble to skip your attack and get all new tiles.

Fight the enemies by making words out of the 16 random letter tiles. You can only use each letter as many times as it appears. Your damage is determined by word length and letter rarity. Each tile you use is replaced by a new random tile at the end of your turn. Minimum word length is 3 tiles.

Enemies have various attacks they can use against you so watch out. Some even last multiple turns. As you beat each enemy you gain XP and will eventually level up. Each location has a boss and a treasure at the end. Treasures help you out in some way.

Treasures:

The Bow of Zyx: Increases damage done by X, Y and Z letter tiles

Golden Fleece: Increases player health

## Features

### Core gameplay loop

The core gameplay loop consists of displaying the UI, getting input and then displaying the resulting changes. This is the order the program executes these step in the code. However, due to the program pausing for player input, the player sees the output from the previous turn first.

Under the previous input, a line of stars is printed so that each turn can be differentiated. Below that, outputs from what happened in the previous turn are printed by various functions. I will go into more detail about this in each features specific section. The outputs you might see here include your attack, the enemies attack, ailments that have begun or ended, whether you have defeated an enemy and a new one has appeared, treasures you have obtained and the next chapter/location you will be entering.

Variables from all the other features are displayed in the UI. Player health, enemy health, location, enemy name, player level and player XP are all displayed everytime. If any ailments are affecting the player they are optionally shown. Also optionally, if at least one treasure has been found they are displayed in a column.

Above the input, the tiles the player can use to make words are displayed. The 26 possible tiles correspond to the 26 letters of the alphabet except for Q which is joined with a u to make a Qu tile representing both letters used together. There is still an individual U tile. The "random" tiles are chosen randomly from a list of the possible tiles where the vowels appear twice in the list making them more likely to be chosen.

A promt asking for the player to make a word is displayed next to the user input. Possible valid inputs include a word made of the tiles that is also in the dictionary, /quit to quit the program and /scramble to get random new tiles at the cost of not attacking for a turn. If the input is not one of those options, a message is displayed providing the reason for its rejection.

The finished version of what this all looks like can be seen below.
![UI](docs/UI.png)

### Player Attack

Luckily the wiki for Bookworm Adventures

### Health

The player and every enemy have an instance attribute in their class representing their health. The player also has a max health attribute so that their health can be reset to full after each enemy. If the player health is equal or less than zero at the end of a turn then the player is taken back to the first enemy of the chapter. If the enemies health is equal or less than zero at the end of a turn, the player progresses to the next enemy. If it is the last enemy in the chapter that is defeated, the player progresses to the next chapter and recieves the treasure from the chapter they just completed.

## Implementation plan

### Core gameplay loop

- test

# References

[Bookworm Adventures Wiki](https://bookwormadvs.fandom.com/wiki/Bookworm_Adventures_Wikia)

[The Other Bookworm Adventures Wiki](https://bookwormadventures.fandom.com/wiki/Bookworm_Adventures)
