from functions import simulation, simulation_small, simulation_social, simulation_social_zealots
import matplotlib.pyplot as plt
import numpy as np
from time import time

N = 4039
macrosteps = 3000
ponderas = 3

alltotwords = []
alldifwords = []
allsuccesses = []

p = 0.08
for i in range(ponderas):
    ti = time()
    print("Simulation %i of %i" % ((i+1), (ponderas)))
    total_words, different_words, successes = simulation(N, macrosteps)
    # tiempo, total_words, different_words, successes = simulation_small(
    #     N, macrosteps, p)
    #total_words, different_words, successes = simulation_social(macrosteps)
    # total_words, different_words, successes = simulation_social_zealots(
    #    macrosteps)
    print("tarda %.4f s" % (time()-ti))
    print("different words = %i" % different_words[-1])
    alltotwords.append(total_words)
    alldifwords.append(different_words)
    allsuccesses.append(successes)

Nw, Nd, S = [], [], []
tiempos = 0
t = []
#tlog = []
for a in range(len(allsuccesses[0])):
    medias_Nw, medias_Nd, medias_S = 0, 0, 0
    cuantas = 0
    for i in range(len(allsuccesses)):
        medias_Nw += alltotwords[i][a]
        medias_Nd += alldifwords[i][a]
        medias_S += allsuccesses[i][a]
        cuantas += 1
    Nw.append(medias_Nw/cuantas)
    Nd.append(medias_Nd/cuantas)
    S.append(medias_S/cuantas)
    # tlog.append(tiempo[a])
    t.append(tiempos)
    tiempos += 1

#network = "social_zealots_deg"
network = "smallworld4039Np08"
file_name_s = "t,Nw,Nd,S_"+network+"_" + \
    str(macrosteps)+'steps_'+str(ponderas)+"ponderas"

#network = "social"
# file_name_s = "t,Nw,Nd,S_"+network+"_" + \
#    str(macrosteps)+'steps_'+str(ponderas)+"ponderas"
with open('Naming-Game/Data/{}.dat'.format(file_name_s), 'w') as file:
    for i in range(len(Nw)):
        file.write('{} {} {} {}\n'.format(i, Nw[i], Nd[i], S[i]))

np.save("Nw.npy", Nw)
np.save("Nd.npy", Nd)
np.save("S.npy", S)


fig = plt.figure(figsize=(9, 3))
plt.xscale('log')
plt.yscale('log')
plt.xlabel("t")
plt.ylabel("Nw")
plt.plot(t, Nw, marker='.', linestyle='-')
# plt.plot(tlog, Nw, marker='.', linestyle='-')  # smallworld
plt.show()

fig = plt.figure(figsize=(9, 3))
plt.xlabel("t")
plt.ylabel("Nd")
plt.plot(t, Nd, marker='.', linestyle='-')
plt.show()

fig = plt.figure(figsize=(9, 3))
plt.xlabel("t")
plt.ylabel("S")
plt.plot(t, S, marker='.', linestyle='-')
plt.show()
