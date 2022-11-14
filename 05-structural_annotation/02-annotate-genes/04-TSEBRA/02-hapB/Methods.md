Link to the Augustus final predictionsfrom Braker1 (RNA-seq)

```bash
ln -s ../../02-Braker1_RNAseq/02-hapB/braker/augustus.hints_utr.gtf braker1_augustus.hints_utr.gtf
ln -s ../../02-Braker1_RNAseq/02-hapB/braker/hintsfile.gff breaker1_hintsfile.gff
```

Link to the Augustus final predictions from Braker2 (Proteins)

``bash
ln -s ../../03-Braker2_protein/02-hapB/braker/augustus.hints.gtf braker2_augustus.hints.gtf
ln -s ../../03-Braker2_protein/02-hapB/braker/hintsfile.gff breaker2_hintsfile.gff
```

Now run TSEBRA:
```bash
sbatch 01-TSEBRA.srun
```

Renamed Transcript IDs to match the gene names. See the TSEBRA documentation that suggets
this fix: https://github.com/Gaius-Augustus/TSEBRA#renaming-transcripts-from-a-tsebra-output.

Using  an `idev` session:

```bash
module add singularity
singularity exec --no-home -B ${PWD} docker://systemsgenetics/actg-wgaa-braker:2.1.6 \
  rename_gtf.py \
    --gtf braker_combined.gtf \
    --out braker_combined_renamed.gtf
```

Now that we have a GTF file with transcript IDs similar to Gene IDs we still want to create a 
GFF3 file. There are tools out there to convert a GTF file into a GFF file. These include one
provided by Augustus and also the `gffread`. However, we would like to add a few tweaks to the
GFF to make it easier to work with in the future.  A Python script was written for this project to 
specifically to convert the GTF file created in the previous step into one that has the following
features:

- All elements have an ID. IDs are not required if the feature has a parent, but some tools 
  expect them.
- All feature types use proper Sequence Ontology terms.

For this we will just use Python3 that comes with kamiak 

```bash
module add python3
python3 tsebra_gtf2gff.py \
  --gtf braker_combined_renamed.gtf \
  --out braker_combined_renamed.gff
```
