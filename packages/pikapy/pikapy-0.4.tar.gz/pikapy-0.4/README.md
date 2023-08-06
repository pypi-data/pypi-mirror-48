# Pikachu Interpreter

This is an interpreter for Pikachu for Python 2.7.x

The definition of the esoteric programming language named 'pikachu' can be found [here](http://trove42.com/introducing-pikachu-programming-language/). This is built as a cleaner version of https://github.com/joelsmithjohnson/pikachu-interpreter.

### Installation:

1. Run `$ pip install pikapy`
2. Go to your Sublime Packages folder, which defaults to `~/Library/Application Support/Sublime Text 3/Packages` on Mac OSX and ` ` on Windows, create a new folder called Pikachu, and copy pikachu.sublime-syntax to there.

3. In the same Packages folder, find `Color Scheme - Default`, and copy `pikachu.sublime-color-scheme` there.

4. In Sublime Text, go to Preferences → Color Scheme, and select Pikachu.


### Usage

In the command line, go to the installation directory, and run:

```bash
$ pikachu <pikachu filename> [arguments*]
```


### Pikachu Language

In Pikachu, you have two Pikachus (i.e. stacks): `pi pikachu` and `pika pikachu`. Upon starting a Pikachu script, the arguments are pushed into `pi pikachu` in the order they're given.

#### Pikachu Syntax

##### Arithmetic Operations

 - `pi pika <PIKACHU>` - add the top two values in the given Pikachu, and push the sum to the same Pikachu
 - `pika pi <PIKACHU>` - subtract the top value in the Pikachu from the second top, then push the difference
 - `pi pikachu <PIKACHU>` - multiply the top two values in the Pikachu, and push the product
 - `pikachu <PIKACHU>` - divide the second-from-the-top value in the Pikachu by the top value, then push the product

##### Stack Operations

 - `pika pikachu <PIKACHU>` - pop the top value from the Pikachu, and print as a number
 - `pikachu pikachu <PIKACHU>` - pop the top value from the Pikachu, and print as ASCII
 - `<PIKACHU>` - pop the top value from the Pikachu
 - `<n terms> <PIKACHU>` - push `n` into the PIkachu
 - `<pi pika>` - push the top value of `pika pikachu` into `pi pikachu`
 - `<pika pi>` - push the top value of `pi pikachu` into `pika pikachu`

##### Control Operations

 - `pikachu pikachu` - if the top values of both Pikachus are equal, goto line `n`, where `n` is the number of terms in the following line
 - `pika pika` - if the top values of both Pikachus are not equal, goto line `n`, where `n` is the number of terms in the following line

*Note: Pikachus start counting lines from 1, not 0*

##### Other Options

 - `pi pi` - push to `pika pikachu` a random number between `1` and `n`, where `n` is the top value in `pika pikachu`
 - `chu` - anything that comes after a `chu`, is treated as a comment, and will be ignored by the interpreter. This includes any line beginning with the word `chu`.

*Note: Things in this section are not part of the original definition of the language, rather features added for the convenience of the programming Pikachus*