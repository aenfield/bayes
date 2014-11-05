from random import randint, random

likelihoodSmoker = 0.3
numberOfStudents = 10000


def isSmoker():
	if randint(0,1) == 0:
		# answer truthfully
		return random() < likelihoodSmoker
	else:
		# flip another coin and answer based on the result
		return randint(0,1) == 0


def main():
	smokers = [isSmoker() for i in range(numberOfStudents)]
	print('{:d} said they smoked out of {:d} students ({:.1%}).'.format(sum(smokers), numberOfStudents, sum(smokers)/numberOfStudents))


if __name__ == '__main__':
    main()