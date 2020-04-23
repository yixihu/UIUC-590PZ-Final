# UIUC-590PZ-Final
Final project for 590pz 2020 spring.

Rotating Connect4

Our group is thinking about making an AI for the variantion version of Connect4. Originally the game would be played as every player places a "coin" into the vertical board. As the coin falls, the player who connect four of the coin first wins the game. When our group discusses about different games and their potential for extending, we were inspired by the actual game where the coin falls due to the gravity.

By thinking gravity, we're adding one rule to the game, that is: at every term, a player can choose between place a coin into the board or rotate the board at any direction for 90 degree, the coins will fall accordingly.

The following graph shows how the rule affects the game. At the first board, if the red player chooses not to place a red coin at the place where the yellow star stays for the original version of connect4, the player loses. However, at the current version of the game, the red player could choose to rotate the board clockwise for 90 degrees, which makes the red player win immediately.

Our goal of the project is to build an AI which has the ability to choose the relatively perfect action at every step and also has the ability to learn from the game to get closer to always win the game.
