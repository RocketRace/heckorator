# heckorator - the most readable decorators you've ever seen

Python 3.9 relaxed the syntax requirements for decorator expressions, allowing arbitrary expressions to be placed inside decorators. Some worried users raised some concerns about the readability of such code. I think code readability matters a lot, which is why I created this library, `heckorator`! Its purpose is to make decorators a *heck* of a lot more readable!

This initially unreadable piece of code:

```py
xs = [Button(position=i) for i in range(10)]

@xs[0].on
def handle_click():
    print("First button clicked!")
```

... is transformed into the *massively* readable:

```py
from heckorator import _

xs = [Button(position=i) for i in range(10)]

@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_
@_._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._@_
@_._._._._._._._._._._._._@_@_._._._._._._._._@_@_._._._._._._._._._._._._._._._._._@_
@_._._._._._._._._._._._._@_._._._._@_@_._._._._@_._._._._._._._._._._._._._._._._._@_
@_._._._._._._._._._._._._@_._._._@_._._@_._._._@_._._._._._._._._._._._._._._._._._@_
@_._@_._._@_._._@_@_@_._._@_._._._@_._._@_._._._@_._._._._._._._._@_@_._._@_@_@_._._@_
@_._@_._._@_._@_._._._._._@_._._._@_._@_@_._._._@_._._._._._._._@_._._@_._@_._._@_._@_
@_._._@_@_._._._@_@_._._._@_._._._@_@_._@_._._._@_._._._._._._._@_._._@_._@_._._@_._@_
@_._@_._._@_._._._._@_._._@_._._._@_._._@_._._._@_._._._._._._._@_._._@_._@_._._@_._@_
@_._@_._._@_._@_@_@_._._._@_._._._._@_@_._._._._@_._._._._@_._._._@_@_._._@_._._@_._@_
@_._._._._._._._._._._._._@_._._._._._._._._._._@_._._._._._._._._._._._._._._._._._@_
@_._._._._._._._._._._._._@_@_._._._._._._._._@_@_._._._._._._._._._._._._._._._._._@_
@_._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._@_
@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_@_
def handle_click():
    print("First button clicked!")
```

Yippee!

## Why on earth would I want to do this

Next question

## Okay then but how do I use it

Stick this before your code:

```py
from heckorator import _
# Optionally customize font
_.font("path/to/font/file")
```

And then stretch your pixel art muscles!

`heckorator` parses the pixel data of decorators as a string of characters based on a font file which can be specified by the user. By default, it uses the [creep](https://github.com/romeovs/creep) font. The font has to be monospace, and you must include the space used for ascenders & descenders in your decorator even if your text doesn't need it.

Oh, and do keep in mind, `heckorator` requires you put a border around your decorators! And separate each row and column of text with a gap of 1 empty pixel! It just makes it cleaner and easier to read 😄

## Licensing acknowledgements etc etc you know the drill go have fun girlies

See the `LICENSE` file. The `heckorator` library is licensed under MIT. The `creep` font is licensed under MIT. Thanks to the qwdies in the QWD discord server for helping me look for nice fonts.
