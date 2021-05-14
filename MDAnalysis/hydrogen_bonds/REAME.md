# Hydrogen Bond Analysis Script 
This script takes in a topology file and trajectory file given a disrance cutoff, angle cutoff,
donor selection, and acceptor selection and spits out an occupancy for each pair found for each hydrogen. 
The particular version here takes all the possible Amino Acid H-Bond donor and takes a Nucleotide Triphosphate (NTP) 
and finds all h-bonds donors to this ligand. 

This script could easily be changed for other ligands and other NTPs (ATP is used here). 
It could with an even greater ease be changed to find h-bonding within the protein itself. 

Please take a look in the example directory to see a trajectory and topolgy used and a sample output. 

## Changes I would like to make 

### Multiple Traj Version 
I should be making a version that loops over multiple trajectories since the prupose of me 
writing this is to anaylze some umbrella sampling trajectories I generated to see how hydrogen-bonds
affects the barrier. 

I will also likely modify this soon to also include the template in the active site.   

### Aeshtetics 
The current output is legible however I would like it spaced evenly. However science and deadlines does not appreciate this kind 
of time investment :/  
