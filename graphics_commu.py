import numpy as np
import matplotlib.pyplot as plt

##REAL##
t, Nw, Nd, S = [], [], [], []
macrosteps = 10000
ponderas = 10

network = "social"
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(macrosteps)+'steps_'+str(ponderas)+"ponderas"

with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        t.append(float(value[0]))
        Nw.append(float(value[1]))
        Nd.append(float(value[2]))
        S.append(float(value[3]))

Nw = np.asarray(Nw)
Nd = np.asarray(Nd)

##BA##
t_0, Nw_0, Nd_0, S_0 = [], [], [], []
N = 4039
macrosteps = 5000
ponderas = 5

network = "BA"
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(N)+'N_'+str(macrosteps)+'steps_'+str(ponderas)+"ponderas"

with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        t_0.append(float(value[0]))
        Nw_0.append(float(value[1]))
        Nd_0.append(float(value[2]))
        S_0.append(float(value[3]))

Nw_0 = np.asarray(Nw_0)
Nd_0 = np.asarray(Nd_0)

##SW##
t_1, Nw_1, Nd_1, S_1 = [], [], [], []
N = 4039
macrosteps = 3000
ponderas = 3

network = "smallworld4039Np08"
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(macrosteps)+'steps_'+str(ponderas)+"ponderas"

with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        t_1.append(float(value[0]))
        Nw_1.append(float(value[1]))
        Nd_1.append(float(value[2]))
        S_1.append(float(value[3]))

Nw_1 = np.asarray(Nw_1)
Nd_1 = np.asarray(Nd_1)


# PLOTS
fig = plt.figure(figsize=(9, 3))
plt.xlabel("t")
plt.ylabel(r"$N_{w}$")
plt.xscale('log')
plt.yscale('log')
plt.plot(t, Nw, marker=',',
         linestyle='-', linewidth=0.5, label="Real Network")
plt.plot(t_0, Nw_0, marker=',',
         linestyle='-', linewidth=0.5, label="BA Network")
plt.plot(t_1, Nw_1, marker=',',
         linestyle='-', linewidth=0.5, label="SW Network")
plt.legend()
plt.show()

fig = plt.figure(figsize=(9, 3))
plt.xlabel("t")
plt.ylabel(r"$N_{d}$")
plt.xscale('log')
plt.yscale('log')
plt.plot(t, Nd, marker=',',
         linestyle='-', linewidth=0.5, label="Real Network")
plt.plot(t_0, Nd_0, marker=',',
         linestyle='-', linewidth=0.5, label="BA Network")
plt.plot(t_1, Nd_1, marker=',',
         linestyle='-', linewidth=0.5, label="SW Network")
plt.legend()
plt.show()

fig = plt.figure(figsize=(9, 3))
plt.xlabel("t")
plt.ylabel("S")
plt.xscale('log')
plt.yscale('log')
plt.plot(t, S, marker=',',
         linestyle='-', linewidth=0.5, label="Real Network")
plt.plot(t_0, S_0, marker=',',
         linestyle='-', linewidth=0.5, label="BA Network")
plt.plot(t_1, S_1, marker=',',
         linestyle='-', linewidth=0.5, label="SW Network")
plt.legend()
plt.show()
