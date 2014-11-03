from thinkbayes import Suite

class Monty(Suite):
            
    def Likelihood(self, data, hypo):
        if hypo == data:
            return 0    # Monty will never choose the door with the car, I think
        elif hypo == 'A':
            return 0.5
        else:
            return 1
            
        
        