Create symlinks to the Illumina 100X Shotgun DNA data

```bash 
ln -s ../../02-quality_control/02-fastp_shotgun_DNA/JPQN_PCRfree_1_1_GGCTTAAG_Apple_WA38_I1177_L4_R1.trimmed.fastq.gz
ln -s ../../02-quality_control/02-fastp_shotgun_DNA/JPQN_PCRfree_1_1_GGCTTAAG_Apple_WA38_I1177_L4_R2.trimmed.fastq.gz
```

Next we need a "seed" sequence to get NOVOPlasty started. We will use the Zea mays chloroplast gene for the large subunit of RUBP (ribulose bisphosphate carboxylase). This is the seed recommended by NOVOPlasty for plant chloroplasts. We can retreive the file from the NOVOPlasty website:

```bash
wget https://raw.githubusercontent.com/ndierckx/NOVOPlasty/master/Seed_RUBP_cp.fasta

```

Because apple already has a chloroplast assembly for *Malus sieversii* we can use it as a reference to guide assembly of the cholorplast from our 100X shotgun data. Download the sequence in FASTA format from here:
https://www.ncbi.nlm.nih.gov/nuccore/MH890570.1 

Name the file: `Msieversii.cholorplast.fasta`


Next create the `novoplasty.config` file following the online instructions at: https://github.com/ndierckx/NOVOPlasty

Finally, run NOVOplasty

```bash
slurm novoplasty.srun
```
