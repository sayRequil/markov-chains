## Welcome to Twig!
Twig is the best framework for Markov chains in Python.  The Twig library is a simple script, but powerful.

Here is an example:
```python
from twig import *
chain = Chain()
chain.AddWordToChain("Zack")                      # This will add one word to the chain.
chain.AddWordsToChain(["Made","This","Script"])   # This will add an array of words to the chain.
print(chain.GetChain("-"))
```

The output of this code could be from a wide way of:
```
Zack-Made
This-Zack
This-Made
```

If you change the ```chain.GetChain("")```, the string in the parentheses will seperate the text.  The output could be: ```Made*This``` if the ```chain.GetChain("")``` was ```chain.GetChain("*")```.
