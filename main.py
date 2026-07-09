inputs = [1,2,3]
weights = [0.2,0.8,-0.5]
bias = 2
opc = 0
output = []
for i in range(len(inputs)):
    op = ((inputs[i]*weights[i]))
    opc+=op
output.append(opc+bias)
print(output)