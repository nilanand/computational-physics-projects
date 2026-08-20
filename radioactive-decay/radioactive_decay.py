import numpy as np
import matplotlib.pyplot as plt

# -- Variables --
N0, decay_constant, t, dt = map(float, input(" Enter N0, decay constant, t, dt separated by a space: ").split())
total_time = np.arange(0, t, dt)
N = np.zeros(len(total_time)) # Number of undecayed particles
N[0] = N0                     # Set initial number of undecayed particles

# Iteration

for i in range(len(total_time)-1):
    dNdt = -decay_constant*N[i]
    N[i+1]= N[i]+dNdt*dt

#Plotting
plt.plot(total_time, N)

plt.xlabel("Time")
plt.ylabel("Number of Undecayed Particles")
plt.title("Radioactive Decay")

plt.show()
    


