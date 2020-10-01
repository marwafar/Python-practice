with open('file.txt') as input:
    coord=input.read()

#print(coord)
coord=coord.split()
print(coord)

for c in coord:
    if c[0].upper().isalpha():
        print c[0]

x_coord=[]
y_coord=[]
z_coord=[]
for i in range(5,len(coord),4):
    x_coord.append(coord[i])
    y_coord.append(coord[i+1])
    z_coord.append(coord[i+2])

print(x_coord)
print(y_coord)
print(z_coord)
    
