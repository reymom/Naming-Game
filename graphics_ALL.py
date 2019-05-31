import matplotlib.pyplot as plt

##COMPLETE NETWORK, DATA##
Nw_1, Nd_1, S_1 = [], [], []
N = 1000
macrosteps = 60
ponderas = 15

network = "complete"
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(N)+'N_'+str(macrosteps)+'steps_'+str(ponderas)+"ponderas"

with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        Nw_1.append(float(value[1]))
        Nd_1.append(float(value[2]))
        S_1.append(float(value[3])/float(ponderas))


##REGULAR 2D LATTICE, DATA##
Nw_2, Nd_2, S_2 = [], [], []
N = 1024
macrosteps = 60
ponderas = 100

network = "2Dlattice"
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(N)+'N_'+str(macrosteps)+'steps_'+str(ponderas)+"ponderas"

with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        Nw_2.append(float(value[1]))
        Nd_2.append(float(value[2]))
        S_2.append(float(value[3])/float(ponderas))


##SMALL WORLD, DATA##
Nw_3, Nd_3, S_3 = [], [], []
N = 1024
macrosteps = 60
ponderas = 100

p = 0.08
network = "smallworld" + str(p)
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(N)+'N_'+str(macrosteps)+'steps_'+str(ponderas)+"ponderas"

with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        Nw_3.append(float(value[1]))
        Nd_3.append(float(value[2]))
        S_3.append(float(value[3]))

##BA, DATA##
Nw_4, Nd_4, S_4 = [], [], []
N = 1024
macrosteps = 60
ponderas = 100

network = "BA"
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(N)+'N_'+str(macrosteps)+'steps_'+str(ponderas)+"ponderas"

with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        Nw_4.append(float(value[1]))
        Nd_4.append(float(value[2]))
        S_4.append(float(value[3]))


t = []
for i in range(macrosteps+1):
    t.append(i)

plt.figure(1)
plt.xlabel("t")
plt.ylabel(r"$N_{w}$")
plt.plot(t, Nw_1, marker='.',
         linestyle='-', linewidth=0.5, label='Complete graph')
plt.plot(t, Nw_2, marker='.',
         linestyle='-', linewidth=0.5, label='2D lattice')
plt.plot(t, Nw_3, marker='.',
         linestyle='-', linewidth=0.5, label='Small world')
plt.plot(t, Nw_4, marker='.',
         linestyle='-', linewidth=0.5, label='BA')
plt.legend()
plt.show()

plt.figure(2)
plt.xlabel("t")
plt.ylabel(r"$N_{d}$")
plt.plot(t, Nd_1, marker='.',
         linestyle='-', linewidth=0.5, label='Complete graph')
plt.plot(t, Nd_2, marker='.',
         linestyle='-', linewidth=0.5, label='2D lattice')
plt.plot(t, Nd_3, marker='.',
         linestyle='-', linewidth=0.5, label='Small world')
plt.plot(t, Nd_4, marker='.',
         linestyle='-', linewidth=0.5, label='BA')
plt.legend()
plt.show()

plt.figure(3)
plt.xlabel("t")
plt.ylabel("S")
plt.plot(t, S_1, marker='.',
         linestyle='-', linewidth=0.5, label='Complete graph')
plt.plot(t, S_2, marker='.',
         linestyle='-', linewidth=0.5, label='2D lattice')
plt.plot(t, S_3, marker='.',
         linestyle='-', linewidth=0.5, label='Small world')
plt.plot(t, S_4, marker='.',
         linestyle='-', linewidth=0.5, label='BA')
plt.legend()
plt.show()
