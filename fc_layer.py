from layer import Layer
import numpy as np
#clase que define una layer del tipo fully connected, los outputs de esta layer están conectados a todos los imputs de la siguiente
#hereda de la clase layer.py
class FCLayer(Layer):
    # input_size = numero de neuronas en el input
    # output_size = numero de neuronas en el output
    def __init__(self, input_size, output_size):
        self.weights = np.random.rand(input_size, output_size) - 0.5 #crea array de un tamaño y ejemplos random del [0, 1)
        self.bias = np.random.rand(1, output_size) - 0.5

    # returns output for a given input
    def forward_propagation(self, input_data):
        self.input = input_data
        self.output = np.dot(self.input, self.weights) + self.bias
        return self.output
    
    # Calcula dE/dW, dE/dB para un error deoutput (output_error=dE/dY). Devuelve el error de input input_error=dE/dX.
    def backward_propagation(self, output_error, learning_rate):
        #producto punto
        input_error = np.dot(output_error, self.weights.T)
        weights_error = np.dot(self.input.T, output_error)
        # dBias = output_error
        # update parameters
        self.weights -= learning_rate * weights_error
        self.bias -= learning_rate * output_error
        return input_error