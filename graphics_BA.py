import numpy as np
import matplotlib.pyplot as plt


##BA##

Nw_0, Nd_0, S_0 = [], [], []
N = 1024
macrosteps = 500
ponderas = 50

network = "BA"
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(N)+'N_'+str(macrosteps)+'steps_'+str(ponderas)+"ponderas"

with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        Nw_0.append(float(value[1]))
        Nd_0.append(float(value[2]))
        S_0.append(float(value[3]))

##BA##

Nw_1, Nd_1, S_1 = [], [], []
N = 1024
macrosteps = 500
ponderas = 15

network = "BAreversed"
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(N)+'N_'+str(macrosteps)+'steps_'+str(ponderas)+"ponderas"

with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        Nw_1.append(float(value[1]))
        Nd_1.append(float(value[2]))
        S_1.append(float(value[3]))

t = []
for i in range(macrosteps+1):
    t.append(i)

Nw_0 = np.asarray(Nw_0)
Nd_0 = np.asarray(Nd_0)
Nw_1 = np.asarray(Nw_1)
Nd_1 = np.asarray(Nd_1)

fig = plt.figure(figsize=(9, 3))
# plt.xlabel("t")
plt.ylabel(r"$N_{w}/N$")
# plt.xscale('log')
# plt.yscale('log')
plt.plot(t, Nw_0/float(N), marker='.',
         linestyle='-', linewidth=0.8, markersize=1, label="direct")
plt.plot(t, Nw_1/float(N), marker='.',
         linestyle='-', linewidth=0.8, markersize=1, label="reversed")
plt.legend()
plt.show()

fig = plt.figure(figsize=(9, 3))
# plt.xlabel("t")
plt.ylabel(r"$N_{d}/N$")
# plt.xscale('log')
# plt.yscale('log')
plt.plot(t, Nd_0/float(N), marker='.',
         linestyle='-', linewidth=0.8, markersize=1, label="direct")
plt.plot(t, Nd_1/float(N), marker='.',
         linestyle='-', linewidth=0.8, markersize=1, label="reversed")
plt.legend()
plt.show()

fig = plt.figure(figsize=(9, 3))
# plt.xlabel("t")
plt.ylabel(r"$S$")
# plt.xscale('log')
# plt.yscale('log')
plt.plot(t, S_0, marker='.',
         linestyle='-', linewidth=0.8, markersize=1, label="direct")
plt.plot(t, S_1, marker='.',
         linestyle='-', linewidth=0.8, markersize=1, label="reversed")
plt.legend()
plt.show()
