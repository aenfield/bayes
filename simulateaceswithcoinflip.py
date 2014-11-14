from random import randint, random

numberOfAttempts = 10000


def actuallyHaveTwoAcesWhenTheySayTheyHaveOneAce():    
	if randint(0,1) == 0:
        # pick from the following set, with the specified probabilities
        # TwoAces: 6/28
        # OneAceButNotTwo: 14/28
        # NoAces: 6/28

		# answer truthfully based on what was picked         
		#return random() < likelihoodOneAce
	else:
		# flip another coin and answer based on the result
		return randint(0,1) == 0


def main():
	smokers = [isSmoker() for i in range(numberOfAttempts)]
	print('{:d} said they smoked out of {:d} students ({:.1%}).'.format(sum(smokers), numberOfStudents, sum(smokers)/numberOfStudents))


if __name__ == '__main__':
    main()