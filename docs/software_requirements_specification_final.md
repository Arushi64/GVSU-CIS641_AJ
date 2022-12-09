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
| FR11 | The overworld window shall open when the main.py file is executed |
| FR12 | The first level shall open when the space bar is pressed from the overworld window |
| FR13 | The second level shall open when the first level is completed and space bar is pressed in overworld |
| FR14 | The third level shall open when the first level is completed and space bar is pressed in overworld |
| FR15 | The fourth level shall open when the first level is completed and space bar is pressed in overworld |
| FR16 | The fifth level shall open when the first level is completed and space bar is pressed in overworld |


### Sprites

| ID  | Requirement |
| :-------------: | :----------: |
| FR4 | <Requirement 1> |
| FR5 | <Requirement 2> |
| FR6 | <Requirement 3> |
| … | … |

### Overworld

| ID  | Requirement |
| :-------------: | :----------: |
| FR4 | <Requirement 1> |
| FR5 | <Requirement 2> |
| FR6 | <Requirement 3> |
| … | … |

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
| NFR11 | The game shall run at 60 FPS |
| NFR12 | The level.py file shall update graphics from game_data.py during gameplay within half a second |
| NFR13 | The level.py file shall draw graphics from game_data.py during gameplay within half a second |
| NFR14 | The level.py file shall update the player direction leftward when the left key is pressed within a second |
| NFR15 | The level.py file shall update the player direction rightward when the right key is pressed within a second |



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
