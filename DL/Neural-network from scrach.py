import numpy as np
class Network(object):
    def __init__(self,sizes):
        self.sizes = sizes
        self.num_layers = len(sizes)
        self.bias = [np.random.randn(y,1) for y in sizes[1:]]
        self.weights = [np.random.randn(y,x) for x,y in zip(sizes[1:],sizes[1:])]

    def sigmoid(z):
        return 1.0/(1.0+np.exp(-z))
    
    def feedforward(silf, a):
        """Return the output of a  network if input a"""
        for b,w in zip(self.bias, self.weights):
            a = sigmoid(np.dot(w,a)+b)
        return a


net = Network([2,3,1]) 

print(f"weight: {net.weights[0]}")