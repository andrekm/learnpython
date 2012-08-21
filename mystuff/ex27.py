#I found shuffle by running help() and from there entering 'random'.
# It was a shot in the dark that worked out quite well.
from random import shuffle

#Takes a string and splits it around ':'
def split_stat(statement):
    return statement.split(':')

#A list of the 'Truth Tables' from exercise 27.
# Note that each item is in a "Question:Answer" format.
statements = [ "not False:True", "not True:False", "True or False:True",
              "True or True:True", "False or True:True",
              "False or False:False", "True and False:False",
              "True and True:True", "False and True:False",
              "False and False:False", "not (True or False):False",
              "not (True or True):False", "not (False or True):False",
              "not (False or False):True", "not (True and False):True",
              "not (True and True):False", "not (False and True):True",
              "not (False and False):True", "1 != 0:True", "1 != 1:False",
              "0 != 1:True", "0 != 0:False", "1 == 0:False", "1 == 1:True",
              "0 == 1:False", "0 == 0:True" ]
#shuffle() randomizes the items in the list above,
# just like shuffling a set of flash cards.
shuffle(statements)
print "\nDon't type your answer, just press Enter once you have it.\n"
#A for loop. Don't worry, this is covered soon.
for statement in statements:
    stat1, stat2 = split_stat(statement)
    prompt = stat1 + " ... "
    raw_input(prompt)
    print stat2, "\n"
