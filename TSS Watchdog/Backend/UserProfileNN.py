import neurolab as nl
import TrainingData as trainer

nn = nl.net.newff([
    [0,1],          # Booleans
    [0,1],          # Booleans
    [0,1],          # Booleans
    [0,1],          # Booleans
    [0,1],          # Booleans
    [0,1],          # Booleans
    [0,1],          # Booleans
    [0,10000],      # Integers
    [0,10000],      # Integers
    [0,10000],      # Integers
    [0,1000],       # Integers (Friends)
    [0,10000],      # Integers
    [0, 16777215],  # Colors
    [0,16777215],   # Colors
    [0,16777215],   # Colors
    [0,16777215],   # Colors
    [0,16777215]    # Colors
    ], [8,1])


def train():
    nn.train(trainer.getNNData(), epochs=100, show=10)


def compute(inputs):
    return nn.sim(inputs)[0]


train()