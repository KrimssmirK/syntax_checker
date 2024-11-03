# Hantverk Syntax Checker

 A final project for the subject Programming Language, that checks the syntax of
 the Hantverk Language developed back during midterms

---

## Table of Contents

- [Hantverk Programming Language](#hantverk-programming-language)
- [Syntax Checker](#syntax-checker)
- [Sample Code](#sample-code)
  - [Window](#window)
  - [Player](#player)
  - [Other Sample Code](#other-sample-codes)
- [Sample Code for Presentation](#sample-code-for-presentation)
- [How to Run](#how-to-run)
  - [Using Anaconda or Conda (Environment)](#using-anaconda-or-conda-environment)
  - [Using Python (Standalone)](#using-python-standalone)
- [Resources for Development](#resources-for-development)

---

## Hantverk Programming Language

Hantverk is a (supposedly) new programming language that will help in game
development by simplifying the process of development in a way that it provides
a framework that handles the setup of the main window, title, and layout. This
will allow the developers to focus on adding engaging features to the game and
not worry about the setup of the game window.

## Syntax Checker

The syntax checker is a program that checks the syntax of the Hantverk Language.
As of now, this program only acts as a parser or a syntax checker. It checks the
syntax of the Hantverk Language and outputs the errors found in the code like how
a compiler would do.

## Sample Code

### Window

A sample code that creates a window with a title "Game Title" and maximizes the
window.

```hantverk
use hantverk.hantverkui.Window;
use hantverk.hantverkui.lsiteners.KeyListener;
use hantverk.hantverkui.lsiteners.Event;

template Main ext Window modded KeyListener {
    fn main() {
        my->title = "Game Title";
        my->dimension = Window->Dimension->MAXIMIZED;
        my->state = Window->State->MAXIMIZED;
        
        my->setUI();
        
        my->show();
    }
    
    fn setUI() {
        my->setLayout();
    }
    
    ::Overwrite
    fn keyUp(Event e) {}
    
    ::Overwrite
    fn keyDown(Event e) {}
    
    ::Overwrite
    fn keyPressed(Event e) {}
}
```

### Player

A sample code for a Player template that extends the Entity template.

```hantverk
use hantverk.hantverkui.GameObject;

template Player ext Entity {
    fn Player() {
        parent();
    }
    
    ::Overwrite
    fn clientRun() {
        my->paint(
            my->position,
            my->drawSprite()
        )
    }
}
```

### Other Sample Codes

This sample code provides the other basic functionalities of the Hantverk
Language, along with how declarations, assignments, and function calls are
done in the language. A basic logging function is also provided in the code
in the form of `log()` function.

```hantverk
use util.Math;

template SampleCodes {
    fn main() {
        str txt = "Sample string";
        str literal = `{txt} literal`;
        
        log("Strings:");
        log(txt);
        log(literal);
        log(`Lengths: [txt: {txt.len}, literal: {literal.len}]`);
        
        arr<int> ary = [1, 2, 3, 4, 5];
        
        log("\nArrays:");
        log(ary);
        log(arr->size);
        
        map<str, flt> mp = [
            "pi" => Math->PI,
            "e" => Math->E,
            "tau" => Math->TAU
        ];
        
        log("\nMap:");
        log(mp);
        log(map->size);
        
        log("\nLogs:");
        log("Debugging log", Log->DEBUG);
        log("Information log", Log->INFO);
        log("Warning log", Log->WARNING);
        log("Error log", Log->ERROR);
    }
}
```

## Sample Code for Presentation

```
template CodeChallenge {

    # this is the start point of the program when this template invoked;
    fn main() {
        arr<int> numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1];
        log("before:", numbers);
        bubbleSort(numbers);
        log("after:", numbers);
    }

    fn bubbleSort(arr<int> numbers) {
        # get the length of the array;
        int n = numbers->size();

        # traverse through all array elements;
        from 0 to n as i {
            bol swapped = false;

            # last i elements are already in place;
            from 0 to n-i-1 as j {

                # traverse the array from 0 to n-i-1;
                # swap if the element found is greater;
                # than the next element;
                check (numbers[j] > arr[j+1]) {
                    swap(numbers, j, j+1);
                    swapped = true;
                }
            }
            check (swapped == false) {
                finish;
            }
        }
    }

    fn swap(arr<int> numbers, int i, int j) {
        int temp = numbers[i];
        numbers[i] = numbers[j];
        numbers[j] = temp;
    }
}
```

**Feature Highlighted**
- Variable declaration
- Conditionals (check)
- Loops (from)
- Functions declarations and calls (fn)
- Expressions (boolean)
- Single Line Comments
- Array indexing (numbers[i])
- Object method (numbers->size)

**What to Show to the Presentation**
1. Show one valid syntax
2. Show two invalid syntaxes with error reports of how to fix them

## How to Run

### Dependencies Installation

The project has several dependencies that are needed. To install these dependencies, just follow one of the items below.

#### Using Anaconda or Conda (Environment)

When using Conda, you can open to the directory using a terminal. If Python is able to run
in your terminal, then you could use the following command:

```bat
conda install --f "requirements.txt"
```

#### Using Python (Standalone)

Using a standalone python without environments such as Miniconda or Anaconda, you could simply use the `pip` command in your terminal.

```bat
pip install -r "requirements.txt"
```

### Resources for Development

- [Writing your own programming language and compiler with Python - Marcelo Andrade (Medium)](https://medium.com/@marcelogdeandrade/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df)
- [I wrote a programming language. Here’s how you can, too. - William W Wold (Free Code Camp)](https://www.freecodecamp.org/news/the-programming-language-pipeline-91d3f449c919/)
- [Generating Lexers (rply Documentation)](https://rply.readthedocs.io/en/latest/users-guide/lexers.html)
- [Generating Parsers (rply Documentation)](https://rply.readthedocs.io/en/latest/users-guide/parsers.html)
- [Writing a Tokenizer - ndesmic (Dev.to)](https://dev.to/ndesmic/writing-a-tokenizer-1j85)
# syntax_checker
