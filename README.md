# Labyrinth-generator

## About application

Console utility, which allows to generate labyrinth and solve it.

## Application features

You can generate labyrinth with HEIGTH and WIDTH parametres.

#### WARNING!
##### Do not create the big labyrinth! You are bordered your RAM.

Application creates folder "labyr_gen_results" with 2 .jpg files: pure labyrinth and soluted labyrinth.

### Example 21x21

- pure labyrinth

![pure labyrinth](example_21x21/labyrinth.jpg)
- soluted labyrinth

![pure labyrinth](example_21x21/soluted_labyrinth.jpg)

## Installation and Using application

### Installation

    $ git clone https://github.com/Elaskinok/Labyrinth-generator.git
    $ cd Labyrinth-generator
    $ pip3 install .
    
### Using

    $ labyr-gen [heigth] [width]
    
heigth, width - must be odd integer !
