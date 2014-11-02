from thinkbayes import Pmf

class Singing(Pmf):
    
    def __init__(self):
        Pmf.__init__(self)
        self.Set('goodsinger', 0.05)
        self.Set('badsinger', 0.95)
        self.Normalize()
        
    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()
        
    mixes = {
        'goodsinger':dict(yes=0.99, no=0.01),
        'badsinger':dict(yes=0.9, no=0.1),
    }
    
    def Likelihood(self, data, hypo):
        mix = self.mixes[hypo]
        like = mix[data]
        return like