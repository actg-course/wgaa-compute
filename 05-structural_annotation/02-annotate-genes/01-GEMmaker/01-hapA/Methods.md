First, create a sym link to the HapA assembly

```bash
ln -s ../../../../04-nuclear_assembly/09-renaming/Malus-domestica-WA_38_hapA-genome-v1.0.a1.fa
```

GEMmaker can process both local and remote (NCBI SRA) RNA-seq files.  It will generate
the BAM files we need to provide to Braker for gene predictions.  However, GEMmaker was
written primarily to provide expression levels and not just to create BAM files. It will
refuse to run if we do not give a GTF file of gene positions. It needs those gene 
positions to do the counting.  We do not have gene positions yet, but also we do not
need the read counts either. So, we can create a fake GTF file with a fake gene
to get around this requirement.

```bash
landmark=`grep ">" Malus-domestica-WA_38_hapA-genome-v1.0.a1.fa | head -n 1 | sed 's/>//'`
echo -e "${landmark}\tDummy\tCDS\t10\t1000\t.\t+\t0\tgene_id \"dummy\"; transcript_id \"dummyM\";" > Malus-domestica-WA_38_hapA-genome-v1.0.a1.gtf
```

The first step is to index the genome for the STAR aligner. We will follow 
the instrcutions in the GEMmaker manual and use the GEMmaker recommended
Docker image to do it: https://gemmaker.readthedocs.io/en/latest/prepare_reference.html#star

```bash
sbatch 01-STAR_index.srun
```

Now, we can run GEMmaker. Since STAR runs better with more memory and CPUs we
will give it some additional resources by setting those in the `nextflow.config` file.
We will let Nextflow use the defaults for everything else.

```bash
sbatch 02-GEMmaker.srun
```


