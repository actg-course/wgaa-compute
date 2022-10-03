As part of the nuclear genome assembly workflow we will want to perfrom 
quality checks on the Hi-C alignments and perform scaffolding. The hifiasm 
tool does not perform scaffolding. It only generates the contigs for the
haplotype assemblies.  Prior to both the quality checks and the scaffodling
we need to align the Hi-C data to the asesmbled contigs. 

Note: we will be using the BWA aligner to align reads in the Hi-C dataset to the 
contigs of the assembly. We do not, however, need to trim for adapters.
See https://epigeneticsandchromatin.biomedcentral.com/articles/10.1186/s13072-021-00389-5

Create sym links to our HiC data. The link below is for the reduced 40X coverage
dataset.  Groups working on the full WA 38 assembly should instead link to the full
data sets.

```bash
ln -s ../../01-input_data/Illumina/Hi-C/JNQM_OmniC_NA_NA_CTTGTCGA_Apple_Cosmic_Crisp-Apple_WA_38_Cosmic_OmniC_I1161L1_L1_40x_R1.fastq
ln -s ../../01-input_data/Illumina/Hi-C/JNQM_OmniC_NA_NA_CTTGTCGA_Apple_Cosmic_Crisp-Apple_WA_38_Cosmic_OmniC_I1161L1_L1_40x_R2.fastq
```

Create symk links to our assembly haplotypes

```bash
ln -s ../01-hifiasm/WA_38.asm.hic.hap1.p_ctg.fa
ln -s ../01-hifiasm/WA_38.asm.hic.hap2.p_ctg.fa
```

Step 1: The BWA aligner requires that the input sequences are indexed.
```bash
sbatch 01-bwa-index-hap1
sbatch 02-bwa-index-hap2
```

Step 2: Perform the BWA alignment
```bash
sbatch 03-bwa-align-hap1
sbatch 04-bwa-align-hap2
```

Step 3: The BWA aligner creates an alignment file in [SAM format](https://en.wikipedia.org/wiki/SAM_(file_format)). 
This is a plain text file format for alignments. However, the binary format is smaller and easier to work 
with (although it cannot be viewed as plain text).  Next, convert the SAM alignment to a BAM file
```bash
sbatch 05-samtools-view-hap1
sbatch 06-samtools-view-hap2
```

Step 4: Lastly, the BAM file can be sorted which makes lookups easier for other applications. 
```bash
sbatch 07-samtools-sort-hap1.srun
sbatch 08-samtools-sort-hap2.srun
```
