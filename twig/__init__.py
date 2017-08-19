from random import *

data = []

class Chain:
  def __init__():
    return "Chain With Twig."
    
  def AddWordToChain(w):
    data.append(w)
    
  def AddWordsToChain(w):
    data.extend(w)
    
  def GetChain(join):
    chain = random.sample(data, 2)
    return join.join(chain)
    
class Waiter:
  def __init__(period):
    nexttime = time.time() + period
    for i in count():
        now = time.time()
        tosleep = nexttime - now
        if tosleep > 0:
            time.sleep(tosleep)
            nexttime += period
        else:
            nexttime = now + period
        yield i, nexttime
