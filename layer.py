inputs = [1, 2, 3, 2.5]
weights = [[0.2,0.8,-0.5,1.0],[0.5,-0.91,0.26,-0.5],[-0.26,-0.27,0.17,0.87]]
biases = [2,3,0.5]
final_output = []

count = 0
c = 0
outputs = []
for j in weights:
    for k in j:
        op = (k*inputs[c])
        c+=1
        count += op
        if c == len(inputs):
            outputs.append(count)
            c = 0
            count = 0
for j in range(len(biases)):
    final_output.append(outputs[j]+biases[j])
print(final_output)





            


        
