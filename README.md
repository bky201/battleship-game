# Battleship Game

Battleship game is a website that allows users to play game against computer. Both players will try to guess the location of ships.  The location of the ships is unknown and it is generated randomly on player board and computer board. If the player missed the location the player gets an alert message "You miised" and the location gets assigned "x". If the player hits the battleship the player gets an alert message "you hit one" and the location gets assigned "#". If the computer missed the location the player gets an alert message "computer miised" and the location gets assigned "O". If the computer hits the battleship the player gets an alert message "computer hits ship" and the location gets assigned "#". 
[View the live site here](https://battleships-app-3b11e752263f.herokuapp.com/).

  ![alt text](images/responsive.png)

## Game Features

### Game Indroductory page

* Heading
  * A heading is the name of the game and is displayed at the top of the page. It gives the user an overview about the game.

  ![alt text](images/GameHeading.png)

* Play / Quit Option
  * On the home page the user is provided with two option that is to play or to quit. Once the user selects "1" and press enter then the user will be prompted to the game.

  ![alt text](images/home.png)  



### Game main page

* The Game Area
  * The player will get to read the key information about the board and the symbols used in the game board with their meaning and representation.

  * Here the player will be able to select the board size and start playing. The player has to enter his board size in order to play.

  ![alt text](images/boardInfo.png)

* Game Board
  * The game board is where the player guesses the battle ship locations. The game board will include different type of information about the game. 
    * A  4x4 game board

      ![alt text](images/gameboard4x4.png)
    * A 5x5 game board

        ![alt text](images/gameboard5x5.png) 

* A hit / A miss
  * Every time the player makes a guess the player will get back the result of the location entered. 
  * If the player guessed the correct location, will get a hit notification. If the player guess is wrong, will get a miss notification. 

    ![alt text](images/playerHitInfo.png)
    ![alt text](images/playerMissInfo.png)

  * The player will also get information about the computer result.

    ![alt text](images/computerHitInfo.png)
    ![alt text](images/computerMissInfo.png)

* Game Score
  * The game ends when one of the players reachs the maximum score. When a player hits a battleship score will get 1 point incremented.

   ![alt text](images/gameScore.png)

* Game Over Messages
  * At the end of the game a pop up message will be generated if all the battleship hit by the player or the computer.
  * This message will identify the winner.
  * Player wins

    ![alt text](images/winPlayerMessage.png)

  * Computer wins

    ![alt text](images/winComputer%20Message.png)

  * Game Draw

    ![alt text](images/winDrawMessage.png)




