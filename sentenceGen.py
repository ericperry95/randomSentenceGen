# random sentence generator (non Gui)

import random

articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL", "POTATOE", "NINJA", "CAR", "TURTLE", "CUP")
verbs = ("HIT", "SAW", "LIKED", "THREW", "PASSED", "ATE", "JUMPED")
prepositions = ("WITH", "BY", "ABOVE", "INTO")

def sentence():
  #Builds and returns a sentence.
  return nounPhrase() + " " + verbPhrase()

def nounPhrase(): 
  #Builds and returns a noun phrase
  return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase(): 
  #Builds and returns verb phrase
  return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
  #Builds and returns prepositional phrase
  return random.choice(prepositions) + " " + nounPhrase()

def main():
  #Allows the user to input the number of sentences to generate
  # input phase 
  number = int(input("Please enter the nember of sentences >>")) 

  #processing and output phases 
  for count in range(number):
    print(sentence())

# Global entry point to main() for program execution 
main()