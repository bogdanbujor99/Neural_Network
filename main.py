import numpy as np

z = [0,0,0,0,0,0] #valoarea neuronilor
#z[0] va fi pentru primul nod de pe stratul ascuns
#z[1] va fi pentru al doilea neuron de pe stratul ascuns
#z[2] va fi pentru nodul de output
y = [0,0,0,0,0,0] #combinatia liniara
delta = []
wait = []
gradient = []
import numpy as np
rata_invatare = int(input("Rata de invatare: ")) # intre 0.1 si 0.5
nr_epoci = int(input("Numarul de epoci: "))
output = int(input("Output dorit: "))

def init_wait():
    # primele 2 valori vor fi pentru cele 2 muchii care pleaca din primul neuron
    # ultimele 2 valori vor fi pentru cele 2 muchii care pleaca din ultimul neuron
    global wait
    wait = np.random.uniform(-1,1,6)

def sigmoid_function(x):
    return(1/(1 + np.exp(-x)))

def calculate_neuron_value_secret_layer():
    global z
    z[0] = 0 * wait[0] + 1 * wait[2]
    z[1] = 0 * wait[1] + 1 * wait[3]

def calculate_neuron_linear_combination_secret_layer():
    global y
    y[0] = sigmoid_function(z[0])
    y[1] = sigmoid_function(z[1])

def calculate_neuron_value_output_layer():
    global z
    z[2] = y[0] * wait [4] + y[1] * wait [5]

def calculate_neuron_linear_combination_output_layer():
    global y
    y[2] = sigmoid_function(z[2])
    

init_wait()
calculate_neuron_value_secret_layer()
calculate_neuron_linear_combination_secret_layer()
calculate_neuron_value_output_layer()
calculate_neuron_linear_combination_output_layer()
print(y[2])