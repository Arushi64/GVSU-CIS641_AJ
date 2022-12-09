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
| NFR22 | The overworld level one shall have a fixed node posiiton of (110, 400) |
| NFR23 | The overworld level two shall have a fixed node posiiton of (300, 220) |
| NFR24 | The overworld level three shall have a fixed node posiiton of (480, 610) |
| NFR25 | The overworld level four shall have a fixed node posiiton of (610, 350) |
| NFR26 | The overworld level five shall have a fixed node posiiton of (880, 210) |

### User Interface

| ID  | Requirement |
| :-------------: | :----------: |
| NFR27 | The health bar shall adjust by a ratio of current health divided by original health |
| NFR28 | The health bar shall have a fixed x and y position of (54, 30) |
| NFR29 | The health bar shall have a fixed height of 4 pixels |
| NFR30 | The health bar shall have a fixed width of 152 pixels |
| NFR31 | The coin count shall increase by 1 when player interacts with coins |
| NFR32 | The coin count shall have a fixed position x and y position of (50, 51) |




# Change management plan

<Description of what this section is>

# Traceability links

<Description of this section>

## Use Case Diagram Traceability

| Artifact ID  | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| UseCase1 | Move Player | FR5 |
| … | … | … |


## Class Diagram Traceability

| Artifact Name | Requirement ID |
| :-------------: |:----------: |
| classPlayer | NFR3, FR5 |
| … | … | … |


## Activity Diagram Traceability

<In this case, it makes more sense (I think, feel free to disagree) to link to the file and to those requirements impacted>

| Artifact ID  | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| <filename> | Handle Player Input | FR1-5, NFR2 |
| … | … | … |


# Software Artifacts

Software Artifacts folder holds the artifacts which were created throughout the development of this game to help us visualize the requiremnents. These artifacts contain UML charts, class diagrams, use case diagrams, as well as a Gantt chart which we used to plan our project timeline out with.

* [Software Artifacts](https://github.com/Arushi64/GVSU-CIS641_NostalgiaDevelopment/tree/master/artifacts)
