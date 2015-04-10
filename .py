#aysin Oruz

import random

def number_to_fortune(number):
    if number == 0:
        print "Yes, for sure!"
    elif number == 1:
        print "Probably yes."
    elif number == 2:
        print "Seems like yes..."
    elif number == 3:
        print "Definitely not!"
    elif number == 4:
        print "Probably not!"
    elif number == 5:
        print "I really doubt it..."
    elif number == 6:
        print "Not sure, check back later!"
    elif number == 7:
        print "I really cant tell!"
    else: 
        print "Something is wrong"
        
def mystical_octosphere(question):   
    print question    
    print "You shake the mystical octosphere!!"
    answer_number = random.randrange(0,7)
    print answer_number
    answer_fortune = number_to_fortune(answer_number)
    print "The cloudy liquid swirls...reply is coming to view"
    print "The mystical octosphere says..."

    print " "
    
mystical_octosphere("Will I get rich?")
mystical_octosphere("Are the Cubs going to win the World Series?")






