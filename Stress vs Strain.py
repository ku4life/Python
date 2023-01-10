import numpy as np
from matplotlib import pyplot as plt
data = np.loadtxt('C:\School\Jcot Lab\Mechanical Lab\Compressive Data\compression_data\jpe1_50_50pct.log', skiprows = 6)

loads = data[:,1]
times = data[:,3]
travel = data [:,2]

fig1, ax1 = plt.subplots()
ax1.plot(times,loads)
ax1.set_title("Load vs Time 1:50 at 50% strain")
ax1.set_xlabel("Time (seconds)")
ax1.set_ylabel("Load (lbF)")

sample=(11/16)
stress = loads/sample
#stress = force/area

#strain = stress/length
strain = (sample-abs(travel))/(sample)

fig2, ax2 = plt.subplots()
ax2.plot(strain,stress)
ax2.set_title("Stress vs Strain 1:50 at 50% strain")
ax2.set_xlabel("Strain")
ax2.set_ylabel("Stress")
