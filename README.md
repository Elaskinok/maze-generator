# Maze-generator

## About application

Console utility which provides functionality to generate a maze, solve it, and write the raw maze and the solved one into an image.

## Application features

You can generate maze with HEIGTH and WIDTH parametres.

#### WARNING!
##### Do not create the a big maze! You are constrainted with your RAM.

Application creates folder "labyr_gen_results" with 2 .jpg files: pure and solved mazes.

### Example 21x21

- pure maze

![pure labyrinth](example_21x21/labyrinth.jpg)
- solved maze

![pure labyrinth](example_21x21/soluted_labyrinth.jpg)

## Installation and Using application

### Installation

    $ git clone https://github.com/Elaskinok/maze-generator.git
    $ cd maze-generator
    $ pip3 install .
    
### Using

    $ labyr-gen [heigth] [width]

heigth, width - must be odd integer !
