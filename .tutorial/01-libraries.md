# Libraries

Libraries are collections of code that other people have written. Video games often use massive libraries (for example: [game engines](https://en.wikipedia.org/wiki/List_of_game_engines)) to create the epic water reflections, 3-D graphics, etc.

We are going to start a bit smaller by just generating random numbers. (After all, [random numbers are the basis of most games](https://www.gamedeveloper.com/programming/how-classic-games-make-smart-use-of-random-number-generation)).

## Random library

We can use a library by writing `import` and then the library name. 

*This should always be one of the first lines of code.*

👉 Let's import a library that will generate random numbers: (Does this look familiar from Day 14's Rock, Paper, Scissors game?)

```python

import random
```

## How random works
In the code below, I have created a variable, 'myNumber'. I am making it equal to a random number given to me by the `randint` (random integer) library. I add the lowest number (1) and the highest number (100) that can be picked and the computer will generate a number at random.



```python
import random
myNumber = random.randint(1,100)
print(myNumber)
```

### 👉 Give it a try!