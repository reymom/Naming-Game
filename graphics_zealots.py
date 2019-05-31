import numpy as np
import matplotlib.pyplot as plt

macrosteps = 300
ponderas = 10

##BY DEGREE##
t, Nw0, Nd0, S0 = [], [], [], []
network = "social_zealots"
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(macrosteps)+'steps_'+str(ponderas)+"ponderas"
with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        t.append(float(value[0]))
        Nw0.append(float(value[1]))
        Nd0.append(float(value[2]))
        S0.append(float(value[3]))
Nw0 = np.asarray(Nw0)
Nd0 = np.asarray(Nd0)

##BY DEGREE more zealots##
Nw10, Nd10, S10 = [], [], []
network = "social_zealots_deg"
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(macrosteps)+'steps_'+str(ponderas)+"ponderas"
with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        Nw10.append(float(value[1]))
        Nd10.append(float(value[2]))
        S10.append(float(value[3]))
Nw10 = np.asarray(Nw10)
Nd10 = np.asarray(Nd10)

##BY BETWEENNESS##
Nw1, Nd1, S1 = [], [], []
network = "social_zealots_bet"
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(macrosteps)+'steps_'+str(ponderas)+"ponderas"
with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        Nw1.append(float(value[1]))
        Nd1.append(float(value[2]))
        S1.append(float(value[3]))
Nw1 = np.asarray(Nw1)
Nd1 = np.asarray(Nd1)

##RANDOMLY##
Nw2, Nd2, S2 = [], [], []
network = "social_zealots_rand"
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(macrosteps)+'steps_'+str(ponderas)+"ponderas"
with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        Nw2.append(float(value[1]))
        Nd2.append(float(value[2]))
        S2.append(float(value[3]))
Nw2 = np.asarray(Nw2)
Nd2 = np.asarray(Nd2)

##REAL##
t0, Nw, Nd, S = [], [], [], []
macrosteps = 10000
ponderas = 10

network = "social"
file_name = "t,Nw,Nd,S_"+network+"_" + \
    str(macrosteps)+'steps_'+str(ponderas)+"ponderas"

with open('Naming-Game/Data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[3].split("/n")
        t0.append(float(value[0]))
        Nw.append(float(value[1]))
        Nd.append(float(value[2]))
        S.append(float(value[3]))
Nw = np.asarray(Nw)
Nd = np.asarray(Nd)

"""
# PLOTS
fig = plt.figure(figsize=(9, 3))
plt.xlabel("t")
plt.ylabel(r"$N_{w}$")
plt.xlim(0, 100)
# plt.xscale('log')
# plt.yscale('log')
plt.plot(t, Nw0, marker=',',
         linestyle='-', linewidth=0.5, label="By degree")
plt.plot(t, Nw1, marker=',',
         linestyle='-', linewidth=0.5, label="By betweenness")
plt.plot(t, Nw2, marker=',',
         linestyle='-', linewidth=0.5, label="Randomly")
plt.legend()
plt.show()

fig = plt.figure(figsize=(9, 3))
plt.xlabel("t")
plt.ylabel(r"$N_{d}$")
plt.xlim(0, 100)
# plt.xscale('log')
# plt.yscale('log')
plt.plot(t, Nd0, marker=',',
         linestyle='-', linewidth=0.5, label="By degree")
plt.plot(t, Nd1, marker=',',
         linestyle='-', linewidth=0.5, label="By betweenness")
plt.plot(t, Nd2, marker=',',
         linestyle='-', linewidth=0.5, label="Randomly")
plt.legend()
plt.show()
"""

fig = plt.figure(figsize=(3, 4))
plt.xlabel("t")
plt.ylabel("S")
plt.xlim(0, 100)
# plt.xscale('log')
# plt.yscale('log')
plt.plot(t0, S, marker=',',
         linestyle='-', linewidth=0.5, label="No zealots")
plt.plot(t, S0, marker=',',
         linestyle='-', linewidth=0.5, label="By degree 1%")
plt.plot(t, S1, marker=',',
         linestyle='-', linewidth=0.5, label="By betweenness 1%")
plt.plot(t, S2, marker=',',
         linestyle='-', linewidth=0.5, label="Randomly 1%")
plt.plot(t, S10, marker=',',
         linestyle='-', linewidth=0.5, label="By degree 5%")

plt.legend()
plt.show()
