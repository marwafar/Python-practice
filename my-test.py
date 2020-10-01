
molecule="""
2
1 2 3
H1 0.0  0.0  0.3
H2 0.0  0.0  -0.3
"""
molecule=molecule.split()
#print(molecule)

for c in molecule:
    if c[0].upper().isalpha():
        print(c[0])

x_coord=[]
y_coord=[]
z_coord=[]

for i in range(5,len(molecule),4):
    x_coord.append(molecule[i])
    y_coord.append(molecule[i+1])
    z_coord.append(molecule[i+2])

print(x_coord)
print(y_coord)
print(z_coord)
    
    





