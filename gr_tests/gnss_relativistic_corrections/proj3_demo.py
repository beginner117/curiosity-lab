
import numpy as np, math
import matplotlib.pyplot as plt

c = 299792458.0
daily_offset = 38.0e-6
days = np.linspace(0, 7, 8)
cum_time_error = days * daily_offset
cum_range_error = c * cum_time_error

plt.figure()
plt.plot(days, cum_range_error/1000.0, marker='o')
plt.xlabel("Days"); plt.ylabel("Range error [km]")
plt.title("If GNSS relativity were ignored"); plt.grid(True)
#plt.savefig("proj3_nav_error_growth.png", dpi=160, bbox_inches="tight")
plt.show()

GMe = 398600441800000.0
F = -2 * math.sqrt(GMe) / c**2
a = 26560e3
e = 0.01
E = np.linspace(0, 2*math.pi, 500)
dt_rel = F * e * math.sqrt(a) * np.sin(E)
plt.figure()
plt.plot(np.degrees(E), dt_rel*1e9)
plt.xlabel("E [deg]"); plt.ylabel("Relativistic correction [ns]")
plt.title("Broadcast eccentricity relativistic term"); plt.grid(True)
plt.savefig("proj3_broadcast_rel_correction.png", dpi=160, bbox_inches="tight")
plt.show()
