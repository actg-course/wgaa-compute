
Note: it is not necessary to do adapter trimming of Illumina Hi-C data for this step see: https://epigeneticsandchromatin.biomedcentral.com/articles/10.1186/s13072-021-00389-5

Create symk links to our assembly haplotypes
```bash
ln -s ../01-hifiasm/WA_38.asm.hic.hap1.p_ctg.fa
ln -s ../01-hifiasm/WA_38.asm.hic.hap2.p_ctg.fa
```

Run mummer
```bash
sbatch mummer.srun
```

Once completed, gzip (compress) the delta file:
```
gzip WA_38.delta
```

Next upload, the compressed delta file to the Assemblytics website for analysis.

The results from the analysis are here:

--Enter the URL for the results page from Assemblytics here--

From the Assemblytics website you can download the results as a Zip file. Once downloaded 
it can be opened:
```bash
WA_38.Assemblytics_results.zip
```
