bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]	



answer = 0 # time
up_list = []


while True:
    answer += 1
    
    if len(up_list) == 0:
        up_list.append(truck_weights.pop(0))
    else:
        if len(up_list) <= bridge_length:
            if len(truck_weights) > 0:
                if sum(up_list) + truck_weights[0] <= weight:
                    up_list.insert(0, truck_weights.pop(0))
                else:
                    up_list.insert(0, 0)
            else:
                up_list.insert(0, 0)
                
        if len(up_list) > bridge_length:
            up_list.pop()
            if sum(up_list) == 0:
                up_list = []
                if len(truck_weights) > 0:
                    up_list.append(truck_weights.pop(0))
                else:
                    break
    
print(answer)
            
            
    
    
    
                
    
        
