ourNames = """Jennifer
Aprajta
Stephanie
Joke
John
Jared
Heekyoung
Lalita
Léna
Kimberly
Yana
Mathews
Jeremy
Yihuang""".split('\n')

from random import shuffle

shuffle(ourNames)

for aName in ourNames:
    print(aName)