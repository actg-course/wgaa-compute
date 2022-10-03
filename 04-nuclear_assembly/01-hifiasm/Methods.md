Create symbolic links to the PacBio long reads. 

Note: For practice, the number of reads in the PacBio dataset has
been limited to only those that are needed to construct the first two scaffolds
of the genome.  The reduced file has the `sf12_reads.fq` suffix.  This will allow
for quick processing of all steps of the assembly workflow without requiring large
amounts of computation.  The groups assigned to perform the WA 38 full assembly will
need to change the link below to use the full data set (which constis of two files,
not just one).

```bash
ln -s ../../01-input_data/PacBio/WA_38.PacBio_HiFi.sf12_reads.fq .
```

Create symbolic linkes to the Hi-C data. 

Note: The Hi-C data has also been reduced. The number
of reads are expected to provide a 40X coverage on average. There are two files (one
for each set of pairs). The reduced files have a `40X_R[12].fastq` extension where 
the `[12]` means to substitute either a 1 or a 2. This reduced read set will allow
for quick processing of all steps of the assembly workflow without requiring large
amounts of computation.  The groups assigned to perform the WA 38 full assembly will
need to change the link below to use the full data set.

```bash
ln -s ../../01-input_data/Illumina/Hi-C/JNQM_OmniC_NA_NA_CTTGTCGA_Apple_Cosmic_Crisp-Apple_WA_38_Cosmic_OmniC_I1161L1_L1_40x_R1.fastq
ln -s ../../01-input_data/Illumina/Hi-C/JNQM_OmniC_NA_NA_CTTGTCGA_Apple_Cosmic_Crisp-Apple_WA_38_Cosmic_OmniC_I1161L1_L1_40x_R2.fastq

```

Run the hifasm program
```bash
sbatch hifiasm.srun
```

Hifiasm does not create FATA files of our assemblies. Instead it genrates GFA files. We
can use `awk` to do this. Awk is an essential tool for data wrangling on the command-line.
You can often do the same with awk on a single command-line that would take multiple  lines
of a Python code. We do not have time to learn about Awk in class. If you want that, take 
The 3rd unit of the Spring AFS 505 course. We will use awk to parse the GFA files output
by hifiasm to extract the contigs and generate a FASTA file. We will do this for the primary
assembly and the the two haplotype assemblies. The instructions to do this were found here: 
https://hifiasm.readthedocs.io/en/latest/faq.html#how-do-i-get-contigs-in-fasta

```bash
awk '/^S/{print ">"$2;print $3}' WA_38.asm.hicdd.p_ctg.gfa > WA_38.asm.hic.p_ctg.fa
awk '/^S/{print ">"$2;print $3}' WA_38.asm.hic.hap1.p_ctg.gfa > WA_38.asm.hic.hap1.p_ctg.fa
awk '/^S/{print ">"$2;print $3}' WA_38.asm.hic.hap2.p_ctg.gfa > WA_38.asm.hic.hap2.p_ctg.fa
```

Next we want to find some statistics about our assembly.  Years ago, a group of folks
got together in an event call Assemblathon. At this event some code was written, including
a Perl script that reads in FASTA files from an assembly and calculates those important
stats. But first, we need to download the script and make it executable.

```bash
wget https://raw.githubusercontent.com/KorfLab/Assemblathon/master/assemblathon_stats.pl
wget http://korflab.ucdavis.edu/Unix_and_Perl/FAlite.pm
chmod 755 assemblathon_stats.pl
```

Now run the assemblathon stats script.
```bash
./assemblathon_stats.pl WA_38.asm.hic.p_ctg.fa > WA_38.asm.hic.p_ctg.stats.txt
./assemblathon_stats.pl WA_38.asm.hic.hap1.p_ctg.fa > WA_38.asm.hic.hap1.p_ctg.stats.txt
./assemblathon_stats.pl WA_38.asm.hic.hap2.p_ctg.fa > WA_38.asm.hic.hap2.p_ctg.stats.txt
```
