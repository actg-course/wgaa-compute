Link to the Augustus final predictionsfrom Braker1 (RNA-seq)

```bash
ln -s ../../02-Braker1_RNAseq/01-hapA/braker/augustus.hints_utr.gtf braker1_augustus.hints_utr.gtf
ln -s ../../02-Braker1_RNAseq/01-hapA/braker/hintsfile.gff breaker1_hintsfile.gff
```

Link to the Augustus final predictions from Braker2 (Proteins)

``bash
ln -s ../../03-Braker2_protein/01-hapA/braker/augustus.hints.gtf braker2_augustus.hints.gtf
ln -s ../../03-Braker2_protein/01-hapA/braker/hintsfile.gff breaker2_hintsfile.gff
```

Now run TSEBRA:
```bash
sbatch 01-TSEBRA.srun
```

