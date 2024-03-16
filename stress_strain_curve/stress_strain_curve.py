"""
A professor assigned me to analyze experimental data regarding a tensile test of an unknown material
in order to deduce its mechanical properties. Let us then represent the stress-strain curve!
"""
import matplotlib.pyplot as plt
from math import pi

# Definition of experimental data
forces = [0, 12861, 24437, 32154, 38456, 43729, 46301, 47587, 43729, 36012, 27009]
lengths = [50.8, 50.83, 50.85, 50.95, 51.31, 52.07, 52.83, 53.85, 54.86, 55.88, 56.39]
diameter = 12.8
initial_length = 50.8

# Calculating Stress and Strain
stresses = [x / (pi * (diameter / 2) ** 2) for x in forces]
deformations = [(x - initial_length) * 100 / initial_length for x in lengths]

# Creating the plot
plt.figure(figsize=(12, 8))
plt.plot(deformations, stresses, marker='o', linestyle='-')

# Customization of the plot
plt.xlabel('Strain \u03B5 - %')
plt.ylabel('Stress \u03C3 - MPa')
plt.title('STRESS-STRAIN CURVE')

# Adding Annotations
for i in range(len(deformations)):
    plt.text(deformations[i] + 0.3, stresses[i] -5, f"({deformations[i]:.4f}, {stresses[i]:.4f})", fontsize=8, ha='left', va='bottom')

# Adjusting ticks and grid:
plt.yticks(range(0, int(max(stresses)) + 100, 50))
plt.xticks(range(0, int(max(deformations)) + 3, 1))
plt.grid(False)

# Saving and displaying the plot:
plt.savefig('stress_strain_curve.png')
plt.show()

