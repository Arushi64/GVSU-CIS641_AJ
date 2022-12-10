# Overview

The purpose of the game Nostalgia Development created is to provide users with a sense of nostalgia. The game is designed to highlight similar features
that many users found enjoyable in various Mario 2D platformers from the late 1990s and early 2000s. Nostalgia Development developed a game that
roped in familiar elements of 2D platformers but also included familiar characters that would bring forth nostalgia for users. This platformer
has 50 requirements, precisely 25 functions and 25 non-functional. These requirements can be found in the requirements file and also seen below. Nostalgia Developments platformer will be available on oue website, where users can interact with the five currently developed levels.

# Software Requirements

The software requirements describe what our game will do and how it is expected to perform. There is a total of 50 requirements that have been laid out. Out of the 50 requirements, there are 25 functional and 25 non-functional requirements with 5 differing categories.

## Functional Requirements

### Audio 

| ID  | Requirement |
| :-------------: | :----------: |
| FR1 | Audio shall begin playing once overworld is opened |
| FR2 | Audio shall begin playing once a level is entered |
| FR3 | Audio shall play when a player jumps |
| FR4 | Audio shall play when a player interacts with an enemy |
| FR5 | Audio shall play when a player interacts with a coin |

### Level Data

| ID  | Requirement |
| :-------------: | :----------: |
| FR6 | The level.py file shall pull graphics data from game_data.py |
| FR7 | The level.py file shall update graphics from game_data.py during gameplay |
| FR8 | The level.py file shall draw graphics from game_data.py during gameplay |
| FR9 | The level.py file shall update the player direction when left and right arrow keys are pressed |
| FR10 | The level.py file shall check the y-position of the player during gameplay |

### Game Window

| ID  | Requirement |
| :-------------: | :----------: |
| FR11 | The first level shall open when the space bar is pressed from the overworld window |
| FR12 | The second level shall open when the first level is completed and space bar is pressed in overworld |
| FR13 | The third level shall open when the first level is completed and space bar is pressed in overworld |
| FR14 | The fourth level shall open when the first level is completed and space bar is pressed in overworld |
| FR15 | The fifth level shall open when the first level is completed and space bar is pressed in overworld |
| FR16 | The game shall exit the level and return to overworld when a player death occurs |
| FR17 | The game shall exit the level and return to overworld when a player win occurs |
| FR18 | The game shall reset player health and return to the overworld when a player death occurs |
| FR19 | The game window shall have a fixed screen height |
| FR20 | The game window shall have a fixed screen width |


### Tiles

| ID  | Requirement |
| :-------------: | :----------: |
| FR21 | All tiles used in game window shall be the same size |


### Overworld

| ID  | Requirement |
| :-------------: | :----------: |
| FR22 | The overworld shall allow the player to navigate unlocked levels |
| FR23 | The overworld levels shall have a fixed position |
| FR24 | The overworld shall have a unqiue graphic for each level |
| FR25 | The overworld window shall open when the main.py file is executed |
| FR26 | The overworld shall close once a player selects the exit button on the window |

### User Interface

| ID  | Requirement |
| :-------------: | :----------: |
| FR27 | The health bar shall update during gameplay |
| FR28 | The health bar shall have a fixed position |
| FR29 | The health bar shall have a fixed height |
| FR30 | The health bar shall have a fixed width |
| FR31 | The coin count shall update |
| FR32 | The coin count shall have a fixed position |

### Decorations

| ID  | Requirement |
| :-------------: | :----------: |
| FR33 | All levels shall have water decorations |
| FR34 | All levels shall have sky decorations |

### Animations

| ID  | Requirement |
| :-------------: | :----------: |
| FR35 | All enemy sprites shall animate when main character jumps on the enemy  |





## Non-Functional Requirements

### Audio

| ID  | Requirement |
| :-------------: | :----------: |
| NFR1 | Audio for overworld shall play fifty percent less than the original volume |
| NFR2 | Audio for the level shall play fifty percent less than the original volume |
| NFR3 | Audio for character jumping shall play fifty-percent louder than the background level audio |
| NFR4 | Audio for character interaction with enemy shall play fifty-percent louder than the background level audio |
| NFR5 | Audio for character interaction with coins shall play fifty-percent louder than the background level audio |

### Level Data

| ID  | Requirement |
| :-------------: | :----------: |
| NFR6 | The level.py file shall pull graphics data from csv files in game_data.py |
| NFR7 | The level.py file shall update graphics from game_data.py during gameplay within half a second |
| NFR8 | The level.py file shall draw graphics from game_data.py during gameplay within half a second |
| NFR9 | The level.py file shall update the player direction leftward when the left key is pressed within a second |
| NFR10 | The level.py file shall update the player direction rightward when the right key is pressed within a second |

### Game Window

| ID  | Requirement |
| :-------------: | :----------: |
| NFR11 | The first level shall load within five seconds when the space bar is pressed from the overworld window |
| NFR12 | The second level shall load within five seconds when the first level is completed and space bar is pressed in overworld |
| NFR13 | The third level shall load within five seconds when the first level is completed and space bar is pressed in overworld |
| NFR14 | The fourth level shall load within five seconds when the first level is completed and space bar is pressed in overworld |
| NFR15 | The fifth level shall load within five seconds when the first level is completed and space bar is pressed in overworld |
| NFR16 | The game shall exit the level and return to overworld when a player death occurs within five seconds |
| NFR17 | The game shall exit the level and return to overworld when a player win occurs within five seconds |
| NFR18 | The game shall reset player health and return to the overworld when a player death occurs within five seconds |
| NFR19 | The game window shall have a fixed screen height of of 768 pixels |
| NFR20 | The game window shall have a fixed screen width of 1280 pixels |

### Tiles

| ID  | Requirement |
| :-------------: | :----------: |
| NFR21 | All tiles used in game window shall have a tile size of 64x64 pixels |

### Overworld

| ID  | Requirement |
| :-------------: | :----------: |
| NFR22 | The overworld level one shall have a fixed node position of (110, 400) |
| NFR23 | The overworld level two shall have a fixed node position of (300, 220) |
| NFR24 | The overworld level three shall have a fixed node position of (480, 610) |
| NFR25 | The overworld level four shall have a fixed node position of (610, 350) |
| NFR26 | The overworld level five shall have a fixed node position of (880, 210) |

### User Interface

| ID  | Requirement |
| :-------------: | :----------: |
| NFR27 | The health bar shall adjust by a ratio of current health divided by original health |
| NFR28 | The health bar shall have a fixed x and y position of (54, 30) |
| NFR29 | The health bar shall have a fixed height of 4 pixels |
| NFR30 | The health bar shall have a fixed width of 152 pixels |
| NFR31 | The coin count shall increase by 1 when player interacts with coins |
| NFR32 | The coin count shall have a fixed position x and y position of (50, 51) |

### Decorations

| ID  | Requirement |
| :-------------: | :----------: |
| NFR33 | All level screens shall have water decorations with a water tile width of 192pixels |
| NFR34 | All level screens shall have sky decorations at various (x, y) positions |


# Change management plan

Nowadays, consumers are a click away from downloading a game from an app store. So why play our game? Nostalgia development incorporates a user-friendly experience with a touch of nostalgia. Have you ever missed old 2D platformer games such as Super Mario Bros!, Dangerous Dave, and Sonic? Nostalgia Developments swing on old 2D platformer games and bring back a sense of joy with familiar characters such as Princess Peach and Mario while incorporating new graphics, audio, and enemies.

The gameplay is so simple that you could even teach your Grandmother to use the program! Users are only required to use three keys: the left, the right, and the spacebar keys. The left and right keys will allow the player to move left and rightward during gameplay and allow for level selection once a level is unlocked in the overworld. The spacebar will enable users to select their desired level in the overworld and let players jump during level gameplay.  

Users of our game can download a .zip file containing all the necessary files to run it on their computers. All users are expected to download this file and access the main.py file through the following path: src/code/levels/main.py. Once users run the main.py file, they will be greeted with an overworld experience containing five unique gameplay levels. All users are required to do is the following:

1. Access our GitHub Repository here: https://github.com/Arushi64/GVSU-CIS641_NostalgiaDevelopment
2. Click on the code button and download .zip
3. Extract the files from .zip folder
4. Download Python onto users computer here: https://www.python.org/downloads/
5. Download Visual Studio Code (VSC) onto users computer here: https://code.visualstudio.com/download
6. Navigate to the main.py file using VSC following this path: src/code/levels/main.py
7. Select the 'play/run' button on the top right of VSC
8. Enjoy!

Following these steps will ensure that users can enjoy this game on any operating system or ecosystem. Suppose users have any suggestions or experience any issues during gameplay/installation. In that case, they will be able to contact us directly through our GitHub Repository for advice and troubleshooting by accessing the file called 'Contact Us.'


# Traceability links

<Description of this section>

## Use Case Diagram #1 Traceability

| Artifact ID  | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| MainCharacter | CollectCoins | FR31, NFR31, FR35 |
| MainCharacter | Move(Actions) | FR9-10, NFR9-10 |
| MainCharacter | TravereseGame | FR22-26, NFR22-26, FR11-17, NFR11-17 |


## Class Diagram Traceability

| Artifact Name | Requirement ID |
| :-------------: |:----------: |
| Water | FR33, NFR33 |
| Sky | FR34, NFR34 |
| Level | FR6-17, NFR6-17, FR23-25, NFR23-25 |
| AnimatedTile | FR35 |

In our class diagrams we originally had a level editor and camera groupbut these classes did not make the final cut of our game. 


## Activity Diagram #1 Traceability


| Artifact ID  | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| ![Activity Diagram](https://github.com/Arushi64/GVSU-CIS641_NostalgiaDevelopment/blob/master/artifacts/activity_diagram.png) | BeginGame | FR1, NFR1, FR25 |
| ![Activity Diagram](https://github.com/Arushi64/GVSU-CIS641_NostalgiaDevelopment/blob/master/artifacts/activity_diagram.png) | LevelOne | FR2-11, NFR2-11, FR16-18, NFR16-18, FR25, FR27-32 |
| ![Activity Diagram](https://github.com/Arushi64/GVSU-CIS641_NostalgiaDevelopment/blob/master/artifacts/activity_diagram.png) | LevelTwo | FR2-10, NFR2-10, FR12, NFR12, FR16-18, NFR16-18, FR25, FR27-32 |
| ![Activity Diagram](https://github.com/Arushi64/GVSU-CIS641_NostalgiaDevelopment/blob/master/artifacts/activity_diagram.png) | LevelThree | FR2-10, NFR2-10, FR13, NFR13, FR16-18, NFR16-18, FR25, FR27-32 |
| ![Activity Diagram](https://github.com/Arushi64/GVSU-CIS641_NostalgiaDevelopment/blob/master/artifacts/activity_diagram.png) | Quit | FR26 |



# Software Artifacts

Software Artifacts folder holds the artifacts which were created throughout the development of this game to help us visualize the requiremnents. These artifacts contain UML charts, class diagrams, use case diagrams, as well as a Gantt chart which we used to plan our project timeline out with.

* [Software Artifacts](https://github.com/Arushi64/GVSU-CIS641_NostalgiaDevelopment/tree/master/artifacts)
