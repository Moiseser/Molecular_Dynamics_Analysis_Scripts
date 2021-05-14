import MDAnalysis
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA
import numpy as np 
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
# This script will read in a trajectory and topology and use MDAAnalysis to calculate 
# Hydrogen bond donors from an enzyme on an NTP ligand. 
# The output will be a file listing the hydrogen bonds found and their occupancy 
# and a list of total H-Bonds per time frame 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Inputs!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
topology    = "topo.tpr" 
trajectory  = "sample.trr"
output_name = "sampleout" 
# Cut off Values to be used by MDAnalysis for Nucleotides 3.5Ang and 140 degrees is standard 
distance_cutoff = 3.5 
angle_cutoff    = 140
donor_heavy    = '(resname ARG and name NE NH1 NH2) or (resname ASN and name ND2) or (resname GLN and name NE2) or (resname GLU and name N) or (resname SER and name OG) or (resname THR and name OG1) or (resname TYR and name OH) or (resname CYS and name SG) or (resname LYS and name NZ)' 
acceptor_heavy = "resname ATP and name N1 N3 N6 N7 O2' O3' O5' O1A O2A O3A O1B O2B O3B O1G O2G O3G'" 

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Analysis!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Read in universe object and get total frames for occupancy percentage 
u = MDAnalysis.Universe(topology, trajectory)
totalframes = len(u.trajectory)

# Create H-Bond Analysis class using input parameters 
hbonds = HBA(universe=u,
              donors_sel= donor_heavy,
              acceptors_sel=acceptor_heavy,
              d_a_cutoff=distance_cutoff,
              d_h_a_angle_cutoff=angle_cutoff,
              update_selections=False)
print ("Begin H Bond Analysis")
start = time.time()
hbonds.run()
print (f'Analysis complete total time = {time.time()-start} seconds')
print ("Printing results .....")
# Get results 
hbond_ids = hbonds.count_by_ids()
hcount = hbonds.count_by_time()

# Print out results 
f1 = open(f'{output_name}_hbondInfo.dat', 'w')
for donor, hydro, acceptor, occupancy in hbond_ids:
    print(f"{u.atoms[donor].resname}{u.atoms[donor].resid+4} {u.atoms[donor].name.rstrip()} {u.atoms[hydro].name} \
            {u.atoms[acceptor].resname} {u.atoms[acceptor].resid+4} {u.atoms[acceptor].name} \
            {(occupancy/totalframes * 100).round()}%", end=" ",file=f1) 
    print(file=f1)
f1.close()

f2 = open(f'{output_name}_count.dat','w')
for count in hcount:
    print(count,file=f2)
f2.close
print ("Done!")
