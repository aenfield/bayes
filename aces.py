from thinkbayes import Pmf

class Aces(Pmf):

    def __init__(self):
        Pmf.__init__(self)
    
        priorForTwoAces = 6/28.0

        self.Set('TwoAces', priorForTwoAces)
        self.Set('NotTwoAces', 1 - priorForTwoAces)
        self.Normalize()

    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()
        
    likelihoods = {
        'TwoAces': { 'OneAce':1 },              # if we have two aces, the likelihood of seeing one ace is 1.0
        'NotTwoAces': { 'OneAce':16/22.0 },     # if we don't have two aces, the likelihood of seeing one ace is 16/22 (16 hands have one ace, out of 22 hands that don't have any aces)
    }
    
    def Likelihood(self, data, hypo):
        # if we assume the 'hypo' is true, how likely are we to see 'data'?
        likelihood = self.likelihoods[hypo]
        like = likelihood[data]
        return like

    def Print(self):
        """Prints the hypotheses and their probabilities."""
        for hypo, prob in sorted(self.Items()):
            print hypo, prob


def main():
    p = Aces()

    p.Update('OneAce')
    # in this implementation, we won't get accurate info if we call Update with 'OneAce' more than once 

    p.Print()

if __name__ == '__main__':
    main()