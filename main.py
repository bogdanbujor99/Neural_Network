import numpy as np

z = [0,0,0] #valoarea neuronilor
#z[0] va fi pentru primul nod de pe stratul ascuns
#z[1] va fi pentru al doilea neuron de pe stratul ascuns
#z[2] va fi pentru nodul de output
y = [0,0,0] #combinatia liniara / valorea de activare
delta = [0,0,0] #reprezinta erorile
weight = [] #valoarea ponderilor
gradient = [0,0,0,0,0,0] #valoerea gradientelor
learning_rate = float(input("Rata de invatare: ")) # intre 0.01 si 0.5
nr_epochs = int(input("Numarul de epoci: "))
input = []
output = []

def readFromFile():
    file = open('input.txt', 'r')
    lines = file.readlines()
    for line in lines:
        data = line.split(" ")
        data = list(map(lambda string_number: int(string_number),data))
        input.append(data[:2])
        output.append(data[2])

def init_weight():
    # primele 2 valori vor fi pentru cele 2 muchii care pleaca din primul neuron
    # ultimele 2 valori vor fi pentru cele 2 muchii care pleaca din ultimul neuron
    global weight
    weight = np.random.uniform(-1,1,6)

def sigmoid_function(x):
    return(1/(1 + np.exp(-x)))

def calculate_neuron_value_secret_layer(x):
    global z
    z[0] = input[x][0] * weight[0] + input[x][1] * weight[2]
    z[1] = input[x][0] * weight[1] + input[x][1] * weight[3]

def calculate_neuron_linear_combination_secret_layer():
    global y
    y[0] = sigmoid_function(z[0])
    y[1] = sigmoid_function(z[1])

def calculate_neuron_value_output_layer():
    global z
    z[2] = y[0] * weight [4] + y[1] * weight [5]

def calculate_neuron_linear_combination_output_layer():
    global y
    y[2] = sigmoid_function(z[2])

def calculate_delta(x):
    global delta
    delta[2] = y[2] - output[x]
    delta[0] = y[0] * (1 - y[0]) * (delta[2] * weight[4])
    delta[1] = y[1] * (1 - y[1]) * (delta[2] * weight[5])

def calculate_gradient_for_output_layer():
    global gradient
    gradient[4] = delta[2] * y[0]
    gradient[5] = delta[2] * y[1]

def calculate_gradient_for_secret_layer(x):
    global gradient
    for i in range(0,4):
        gradient[i] = delta[i%2] * input[x][i//2]

def weight_corection(x):
    return weight[x] - learning_rate * gradient[x]

def update_weight(x):
    global weight
    for i in range(0,6):
        weight[i] = weight_corection(i)
    
def display_results(x):
    print("Ponderile sunt: " + str(weight))
    print("Pentru inputul : " +  str(input[x]) + " valorea de iesire dupa invatare este:  " + str(y[2]))
    
readFromFile()
for i in range(0,len(input)):
    init_weight()
    for j in range(0,nr_epochs):
        calculate_neuron_value_secret_layer(i)
        calculate_neuron_linear_combination_secret_layer()
        calculate_neuron_value_output_layer()
        calculate_neuron_linear_combination_output_layer()
        calculate_delta(i)
        calculate_gradient_for_output_layer()
        calculate_gradient_for_secret_layer(i)
        update_weight(i)
    display_results(i)