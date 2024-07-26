# heckorator - the most readable decorators you've ever seen

Python 3.9 relaxed the syntax requirements for decorator expressions, allowing arbitrary expressions to be placed inside decorators. Some worried users raised some concerns about the readability of such code. I think code readability matters a lot, which is why I created this library, `heckorator`! Its purpose is to make decorators a *heck* of a lot more readable!

This initially unreadable piece of code:

```py
x = [Button(position=i) for i in range(10)]

@x[0].on
def handle_click():
    print("First button clicked!")
```

... is transformed into the *massively* readable:

```py
from heckorator import _

x = [Button(position=i) for i in range(10)]

@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_
@_._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._@_
@_._._._._._._._._@_@_@_._._._._._._._._._@_@_@_._._._._._._._._._._._._._._._._._._._._@_
@_._._._._._._._._@_._._._._._@_@_@_._._._._._@_._._._._._._._._._._._._._._._._._._._._@_
@_._._._._._._._._@_._._._._@_._._._@_._._._._@_._._._._._._._._._._._._._._._._._._._._@_
@_._@_._._._@_._._@_._._._._@_._._._@_._._._._@_._._._._._._._._._@_@_@_._._@_@_@_@_._._@_
@_._._@_._@_._._._@_._._._._@_._@_._@_._._._._@_._._._._._._._._@_._._._@_._@_._._._@_._@_
@_._._._@_._._._._@_._._._._@_._@_._@_._._._._@_._._._._._._._._@_._._._@_._@_._._._@_._@_
@_._._._@_._._._._@_._._._._@_._._._@_._._._._@_._._._._._._._._@_._._._@_._@_._._._@_._@_
@_._._@_._@_._._._@_._._._._@_._._._@_._._._._@_._._._@_@_._._._@_._._._@_._@_._._._@_._@_
@_._@_._._._@_._._@_._._._._._@_@_@_._._._._._@_._._._@_@_._._._._@_@_@_._._@_._._._@_._@_
@_._._._._._._._._@_._._._._._._._._._._._._._@_._._._._._._._._._._._._._._._._._._._._@_
@_._._._._._._._._@_@_@_._._._._._._._._._@_@_@_._._._._._._._._._._._._._._._._._._._._@_
@_._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._@_
@_._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._@_
@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_
def handle_click():
    print("First button clicked!")
```

Yippee!

## Why on earth would I want to do this

Self-explanatory, next question

## Okay then but how do I use it

First, go get [that thang](https://pypi.org/project/heckorator/):

```sh
pip install heckorator
```

Stick this before your code:

```py
from heckorator import _
# Optionally customize font
# _.font("path/to/font/file")
```

And then stretch your pixel art muscles! (.....or you can use `python3 -m heckorator generate` to generate the pixel art from normal text.... but that's LAME!)

`heckorator` parses the pixel data of decorators as a string of characters based on a font file which can be specified by the user. By default, it uses the [Cozette](https://github.com/slavfox/Cozette) font.

Oh, and do keep in mind, you have to put a border around your decorators! And separate each row and column of text with a gap of 1 empty pixel! This just makes it cleaner and easier to read 😄 You care about readability, right?

## What caused you to make this wtf

The noble search for clean code. I may also be bedridden with a cold, but that is only tangential.

## Licensing acknowledgements etc etc you know the drill go have fun girlies

See the `LICENSE` file. The `heckorator` library is licensed under MIT. The Cozette font is licensed under MIT. Thanks to the qwdies in the QWD discord server for helping me look for nice fonts.
