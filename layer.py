#clase que define una de las layer de la red neuronal

class Layer:
    def __init__(self):
        self.input=None
        self.output=None

    #propagación hacia delante, calcula el output Y dado un input X
    def forward_prop(self,input):
        raise NotImplementedError

    #propagación hacia atrás, calcula el error y actualiza los parámetros en caso de ser necesario (dado dE/dX para dE/dY)
    # El parámetro learning rate es una regla de actualización (optimizador), se va a actualizar usando el descenso por gradiente
    def backward_prop(self, output_error,learning_rate):
        raise NotImplementedError