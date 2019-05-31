import matplotlib.pyplot as plt
import numpy as np

##SMALL WORLD, DATA##

N = 500
macrosteps = 5000
ponderas = 20

# p=0
Nw_0, Nd_0, S_0 = [], [], []

p = 0
network = "smallworld" + str(p)
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(N)+'N_'+str(macrosteps)+'steps_'+str(ponderas)+"ponderas"

with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        Nw_0.append(float(value[1]))
        Nd_0.append(float(value[2]))
        S_0.append(float(value[3]))


# p=0.01
Nw_1, Nd_1, S_1 = [], [], []

p = 0.01
network = "smallworld" + str(p)
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(N)+'N_'+str(macrosteps)+'steps_'+str(ponderas)+"ponderas"

with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        Nw_1.append(float(value[1]))
        Nd_1.append(float(value[2]))
        S_1.append(float(value[3]))

# p=0.02
Nw_2, Nd_2, S_2 = [], [], []

p = 0.02
network = "smallworld" + str(p)
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(N)+'N_'+str(macrosteps)+'steps_'+str(ponderas)+"ponderas"

with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        Nw_2.append(float(value[1]))
        Nd_2.append(float(value[2]))
        S_2.append(float(value[3]))

# p=0.04
Nw_3, Nd_3, S_3 = [], [], []

p = 0.04
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

# p=0.08
Nw_4, Nd_4, S_4 = [], [], []

p = 0.08
network = "smallworld" + str(p)
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(N)+'N_'+str(macrosteps)+'steps_'+str(ponderas)+"ponderas"

t = []
with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        t.append(float(value[0]))
        Nw_4.append(float(value[1]))
        Nd_4.append(float(value[2]))
        S_4.append(float(value[3]))

#t = []
# for i in range(macrosteps+1):
#    t.append(i)

Nw_0 = np.asarray(Nw_0)
Nw_1 = np.asarray(Nw_1)
Nw_2 = np.asarray(Nw_2)
Nw_3 = np.asarray(Nw_3)
Nw_4 = np.asarray(Nw_4)
Nd_0 = np.asarray(Nd_0)
Nd_1 = np.asarray(Nd_1)
Nd_2 = np.asarray(Nd_2)
Nd_3 = np.asarray(Nd_3)
Nd_4 = np.asarray(Nd_4)
t = np.asarray(t)

"""
m, b = np.polyfit(np.log10(t), np.log10(Nd_0), 1)
print(m, b)
line = []
for i in range(len(t)):
    line.append(t[i]**(-0.50786))
"""

plt.figure(1)
plt.xlabel("t")
plt.ylabel(r"$N_{w}/N$")
# plt.xscale('log')
# plt.yscale('log')
plt.plot(t, Nw_0/N, marker='.',
         linestyle='-', linewidth=0.5, label='p = 0')
plt.plot(t, Nw_1/N, marker='.',
         linestyle='-', linewidth=0.5, label='p = 0.01')
plt.plot(t, Nw_2/N, marker='.',
         linestyle='-', linewidth=0.5, label='p = 0.02')
plt.plot(t, Nw_3/N, marker='.',
         linestyle='-', linewidth=0.5, label='p = 0.04')
plt.plot(t, Nw_4/N, marker='.',
         linestyle='-', linewidth=0.5, label='p = 0.08')
plt.legend()
plt.show()


plt.figure(2)
plt.xlabel("t")
plt.ylabel(r"$N_{d}/N$")
plt.xscale('log')
plt.yscale('log')
plt.plot(t, Nd_0/N, marker='.',
         linestyle='-', linewidth=0.5, label='p = 0')
plt.plot(t, Nd_1/N, marker='.',
         linestyle='-', linewidth=0.5, label='p = 0.01')
plt.plot(t, Nd_2/N, marker='.',
         linestyle='-', linewidth=0.5, label='p = 0.02')
plt.plot(t, Nd_3/N, marker='.',
         linestyle='-', linewidth=0.5, label='p = 0.04')
plt.plot(t, Nd_4/N, marker='.',
         linestyle='-', linewidth=0.5, label='p = 0.08')
# plt.plot(t, line, linestyle='-',
#         linewidth=0.5, label=r"$\alpha = -1/2 $")
plt.legend()
plt.show()

plt.figure(3)
plt.xlabel("t")
plt.ylabel("S")
# plt.xscale('log')
# plt.yscale('log')
plt.xlim(1, 1000)
plt.plot(t, S_0, marker='.',
         linestyle='-', linewidth=0.5, label='p = 0')
plt.plot(t, S_1, marker='.',
         linestyle='-', linewidth=0.5, label='p = 0.01')
plt.plot(t, S_2, marker='.',
         linestyle='-', linewidth=0.5, label='p = 0.02')
plt.plot(t, S_3, marker='.',
         linestyle='-', linewidth=0.5, label='p = 0.04')
plt.plot(t, S_4, marker='.',
         linestyle='-', linewidth=0.5, label='p = 0.08')

plt.legend()
plt.show()
