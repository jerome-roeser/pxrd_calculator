from pymatgen.core import Lattice, Structure
from pymatgen.symmetry.groups import SpaceGroup 
from pymatgen.analysis.diffraction.xrd import XRDCalculator
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

bilayer = r'cifs/BTEB-HHTP.cif'
boe = r'cifs/boe_SqPy-SiCOF.cif'

from pymatgen.io.cif import CifParser

cifs = [bilayer, boe]
structures = []
xrd_calculator = XRDCalculator('CuKa1')

# Replace "path/to/your/file.cif" with the path to your CIF file.
for cif in cifs:
    parsed_cif = CifParser(cif)
    # Parse the CIF file and get the structure object.
    structure = parsed_cif.get_structures()[0]
    structures.append(structure)
    # xrd_calculator.get_plot(structure, annotate_peaks= None)
    
# parser = CifParser(bilayer)
# structure = parser.get_structures()[0]
# p = xrd_calculator.get_plot(structure, two_theta_range= (2, 60), annotate_peaks= None)
# pa = xrd_calculator.get_pattern(structure, two_theta_range=(2,60))
# xrd_calculator.plot_structures()


# # Replace "structure" with your structure object.
# xrd_calculator = XRDCalculator()
# for s in parsed_structures:
#     pattern = xrd_calculator.get_pattern(s)
#     xrd_plot = xrd_calculator.get_plot(s, annotate_peaks= None)

# xrd_calculator.plot_structures([x for x in parsed_structures])

# Print the two-theta angles and intensities of the PXRD peaks.
# for peak in pattern:
#     print(f"{peak.two_theta:.2f}\t{peak.intensity:.2f}")


# from pymatgen.analysis.diffraction.xrd import XRDCalculator
patterns = [xrd_calculator.get_pattern(structure, two_theta_range=(2,60)) for structure in structures]
pa = patterns[0].smear(sigma=0.2)

# Convert the PXRD pattern data to a pandas DataFrame.
data = {"2θ": pa.x, "Intensity": pa.y}
df = pd.DataFrame(data)

# Plot the PXRD pattern with Seaborn.
sns.set_style("whitegrid")
sns.lineplot(data=df, x="2θ", y="Intensity", marker="o")
# plt.xlabel("2θ (degrees)")
# plt.ylabel("Intensity")
plt.show()

# from pymatgen.analysis.diffraction.xrd import XRDCalculator

# # Create a list of 20 structure objects.
# structures = [...] # Replace with your list of structures.

# # Compute the PXRD pattern for each structure.
# xrd_calculator = XRDCalculator()


# Compute the average PXRD pattern.
# num_patterns = len(patterns)
# avg_pattern = patterns[0].copy()  # Create a copy of the first pattern.
# for i in range(1, num_patterns):
#     avg_pattern.intensities += patterns[i].intensities
# avg_pattern.intensities /= num_patterns

# # Print the two-theta angles and intensities of the average PXRD peaks.
# for peak in avg_pattern:
#     print(f"{peak.two_theta:.2f}\t{peak.intensity:.2f}")
