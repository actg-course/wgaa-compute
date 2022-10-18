# Use MUMmer to align WA 38 to Gala Diploid v2

Link to the curated final scaffolds sequences exported by Juicebox. 

```bash
ln -s ../07-juicebox_curation/WA_38-hap1-JBAT.FINAL.fa
ln -s ../07-juicebox_curation/WA_38-hap2-JBAT.FINAL.fa
```

Download the Gala Dipload v2 chromosomal sequences. 
```bash
wget https://www.rosaceae.org/rosaceae_downloads/Malus_x_domestica/Gala_diploid_v1/assembly/Gala_diploid_v2.chr.fa.gz
gunzip Gala_diploid_v2.chr.fa.gz
```

Get the chromsome A and B haplotype sequences.
```bash
grep ">chr.*A" Gala_diploid_v2.chr.fa  | perl -p -e 's/>//g' > gala_hapA_names.txt
grep ">chr.*B" Gala_diploid_v2.chr.fa  | perl -p -e 's/>//g' > gala_hapB_names.txt
```

Download seqtk and compile it so we can use it to create new FASTA files for each Gala haplotype.
```bash
git clone https://github.com/lh3/seqtk.git;
cd seqtk; make
cd ..
```

Now create the haplotype sequence files
```bash
./seqtk/seqtk subseq Gala_diploid_v2.chr.fa gala_hapA_names.txt > Gala_diploid_v2.chr.hapA.fa
./seqtk/seqtk subseq Gala_diploid_v2.chr.fa gala_hapB_names.txt > Gala_diploid_v2.chr.hapB.fa
```

Use MUMmer to align our WA 38 haplotypes with haplotypes of the Gala v2 assembly.
```bash
sbatch 01-mummer-hap1.srun
sbatch 02-mummer-hap2.srun
```

Compress the delta files and uplaod those Assemblytics like we did when we compared the haplotypes of WA38
```bash
gzip WA_38_hap1-vs-Gala_diploid_v2.delta
gzip WA_38_hap2-vs-Gala_diploid_v2.delta
```

Using the dot plot output from Assemblytics, make a list that maps the scaffolds in the
WA 38 assembly to those in the Gala v2 assembly. Store those in two (one for each haplotype) file named:

- `wa_38_hap1_to_gala2_hapA.txt`
- `wa_38_hap2_to_gala2_hapB.txt`

Each file is tab-delimited and the first column being the WA 38 scaffold/contig names and the
second column being the Gala v2 chromosome name. 

# Rename the Sequences

Create copies of the FASTA files so that we can rewrite the sequence names in the copies. We do not 
want to rewrite the names in the original file in case we mess up. These files will those that we 
will share with the world. So, we need a formal file name for these. We will following the naming 
convention requested by GDR: https://www.rosaceae.org/nomenclature/genome

Copy the FASTA files to their new names

```bash
cp WA_38-hap1-JBAT.FINAL.fa Malus-domestica-WA_38_hapA-genome-v1.0.a1.fa
cp WA_38-hap2-JBAT.FINAL.fa Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa
````

We will use a bit of BASH code to rename the sequences. This code will read the files
created in the previous step named `wa_38_hap1_to_gala2_hapA.txt` and 
`wa_38_hap2_to_gala2_hapB.txt`. These files must have two columns mapping the 
sequences in WA 38 assembly to the Gala Diploid v2 assembly. If the sequences names
are misspelled then this code will not work.

```bash
# Haplotype A
cat wa_38_hap1_to_gala2_hapA.txt | while read line; do
  mapping=($line)
  cmd="perl -pi -e 's/^>${mapping[0]}\$/>${mapping[1]}/g' Malus-domestica-WA_38_hapA-genome-v1.0.a1.fa";
  echo $cmd
  eval $cmd
done;

# Haplotype B
cat wa_38_hap2_to_gala2_haBA.txt | while read line; do
  mapping=($line)
  cmd="perl -pi -e 's/^>${mapping[0]}\$/>${mapping[1]}/g' Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa";
  echo $cmd
  eval $cmd
done;
```

Now that we have renamed the scaffolds that map to chromosomes, we now want to
make sure we keep our scaffolds connected to the appropriate haplotype. We will
simply add an A or B onto the end of the scaffold names. The following does this:
```bash
# Haplotype A
cmd="perl -pi -e 's/^(>scaffold_\d+)/\1A/g' Malus-domestica-WA_38_hapA-genome-v1.0.a1.fa"
echo $cmd
eval $cmd

# Haplotype B
cmd="perl -pi -e 's/^(>scaffold_\d+)/\1B/g' Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa"
echo $cmd
eval $cmd
```

As a sanity check, we will make sure everything got renamed. This code will
pull out only the sequences names from the FASTA file
```
grep ">" Malus-domestica-WA_38_hapA-genome-v1.0.a1.fa
grep ">" Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa
```

Now combine both FASTA files into a single genome file for folks who want the
entire genome in a single file
```bash
cat Malus-domestica-WA_38_hapA-genome-v1.0.a1.fa Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa >  Malus-domestica-WA_38-genome-v1.0.a1.fa
```

Another sanity check: check that we see all of the sequences in the file
```bash
grep ">" Malus-domestica-WA_38-genome-v1.0.a1.fa
```

For a last sanity check, rerun MUMmer with the new haplotype files (with renamed scaffolds) and 
make sure that the same named sequences match the Gala v2 sequences.
