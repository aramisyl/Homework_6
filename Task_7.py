def pupils_above_avg_height(massive):
    medium_height = sum(massive)/len(massive)
    counter = 0
    for i in massive:
        if i > medium_height:
            counter +=1
    return counter

print(pupils_above_avg_height([164, 156, 158, 173, 175, 160]))