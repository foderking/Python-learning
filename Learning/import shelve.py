import shelve
import os

star = shelve.open('standard')
star['new'] = os.listdir()
print(list(star.values()))
star.close()
