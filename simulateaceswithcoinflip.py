from __future__ import division     # use Python 3's floating point division - this makes the script run on both Python 2 and Python 3
import random 

number_of_attempts = 100000


def weighted_choice(choices):
    """Like random.choice, but each element can have a different chance of
    being selected.
    
    choices can be any iterable containing iterables with two items each.
    Technically, they can have more than two items, the rest will just be
    ignored. The first item is the thing being chosen, the second item is
    its weight. The weights can be any numeric values, what matters is the
    relative differences between them.
    
    From http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
    """
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w > r:
            return c
        upto += w


def answer():
    """Returns a tuple that contains the answer to the question 'do I have an
    ace?' in the first position and the contents of the hand in the second position.
    Also contains, in the third position, whether a coin was flipped to determine 
    the answer.
        
    The answer to the first question uses the logic where half the time the answer 
    is truthful and half the time the answer is a flip of the coin.
    """
    choices = [ ('TwoAces', 6/28.0), ('OneAce', 16/28.0), ('NoAces', 6/28.0) ]
    hand = weighted_choice(choices)
    
    if random.randint(0,1) == 0:
        # answer truthfully based on what was picked
        did_i_flip_a_coin = 'No coin'
        if (hand ==  'TwoAces' or hand == 'OneAce'):
            at_least_one_ace = True
        else:
            at_least_one_ace = False
    else:
        # flip another coin and answer based on the result
        did_i_flip_a_coin = 'Flipped a coin'
        at_least_one_ace = random.choice([True, False])

    return (at_least_one_ace, hand, did_i_flip_a_coin)


def main():
    """Simulates this problem: if you tell me you have a (at least one) ace, how often 
    do you actually have two aces? The wrinkle is that half the time you answer
    based on the contents of your hand, and the other half of the time you answer
    by flipping a coin. (Also assumes a simplified set of hands that can only have
    aces or kings.) 
    """
    answers = [answer() for i in range(number_of_attempts)]    
    only_yes_answers = [a for a in answers if a[0] == True]
    yes_answers_with_two_aces = [a for a in only_yes_answers if a[1] == 'TwoAces']
    
    print('{:d} "yes" answers in {:d} trials.'.format(len(only_yes_answers), number_of_attempts))
    print('{:d} of them have hands of two aces.'.format(len(yes_answers_with_two_aces)))
    print('{:.1%} of the "yes" answers have two aces.'.format(len(yes_answers_with_two_aces)/len(only_yes_answers)))

    if len(only_yes_answers) <= 20:
        # only print out raw data when there's not too much of it
        print
        print(only_yes_answers)


if __name__ == '__main__':
    main()