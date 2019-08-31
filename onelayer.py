import numpy as np
import random
train_input = [1,2,3,4,5,6,7,8,9]

train_output = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

test_list = [100,23,45,98,56,79,105]

test_val = [10,2.3,4.5,9.8,5.6,7.9,10.5]
#making a random array of one number
w_array = np.random.rand(1,1)

print("How many Epochs?")
#print(w_array)

EPOCH = int(input())

loss_list = []
for i in range(0,EPOCH-1):
	for i in range(0,len(train_output)-1):
		sample_out  = train_input[i]*w_array[0][0]
		loss = abs(sample_out - train_output[i])
		#print(sample_out,loss,train_output[i])
		loss_list.append([loss,w_array[0][0]])
		w_array = np.random.rand(1,1)
		#get the least amount of loss
	w_array = np.array([[min(loss_list)[1]]])
	#print(w_array)	
for i in range(0,len(test_list)-1):
	print(test_val[i],test_list[i]*w_array[0][0])
