from thinkbayes import Suite

class Aces(Suite):

	def Likelihood(self, data, hypo):
		pass


def main():
	suite = Aces('something')

	suite.Update('something else')

	suite.Print()


if __name__ == '__main__':
	main()