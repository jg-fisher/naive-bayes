import numpy as np

"""
Bayes Theorem
P(c|x) = P(x|c) * P(c) / P(x)
"""

weather = ['Sunny', 'Overcast', 'Rainy',
            'Sunny', 'Sunny', 'Overcast',
            'Rainy', 'Rainy', 'Sunny',
            'Rainy', 'Sunny', 'Overcast',
            'Overcast', 'Rainy']

play = ['No', 'Yes', 'Yes',
        'Yes', 'Yes', 'Yes',
        'No', 'No', 'Yes',
        'Yes', 'No', 'Yes',
        'Yes', 'No']

class NaiveBayes:
    def __init__(self, x, y):
        
        self.x = x
        self.y = y

        # probability of an input occuring
        self.p_x = { xi: x.count(xi)/len(x) for xi in list(x) } 

        # probability of an output occuring
        self.p_y = { yi: y.count(yi)/len(play) for yi in sorted(play) }

        # probability of outputs for each input
        self.p_xy = { xi: { yi: len([ i for n, i in enumerate(y) if yi == i and xi == x[n] ]) / x.count(xi) for yi in list(y)} for xi in list(x) } 

    def predict(self, xi):
        y_hat = { y: self.p_xy[xi][y] * self.p_y[y] / self.p_x[xi] for y in list(self.y) } 
        return y_haG


if __name__ == '__main__':
    nb = NaiveBayes(weather, play)
    
    x = ['Sunny', 'Rainy', 'Overcast']
    for xi in x:
        print('Classification of {0}: {1}'.format(xi, nb.predict(xi)))


