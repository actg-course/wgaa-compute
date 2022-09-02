First, creates symlinks to the reports from previous steps that MultiQC will want to look at. The pattern of files that MultiQC will look for are documented in the "Modules" section of hte online documentation:
https://multiqc.info/docs/#multiqc-modules

The PacBio FastQC reports
https://multiqc.info/docs/#fastqc
```
ln -s ../01-FastQC-PacBio/m64233e_211117_203327_fastqc.zip
ln -s ../01-FastQC-PacBio/m64233e_211123_195103_fastqc.zip
```

The fastp results
https://multiqc.info/docs/#fastqc
```
ln -s ../02-fastp_shotgun_DNA/fastp.json
```

The Trimmed Illumina Shotgun FastQC report. We will skip the raw Fastq files
because mixing the raw and trimmed into a single report gets confusing.
https://multiqc.info/docs/#fastqc

```bash
ln -s ../04-FASTQC_trimmed_shotgun_DNA/JPQN_PCRfree_1_1_GGCTTAAG_Apple_WA38_I1177_L4_R1.trimmed_fastqc.zip
ln -s ../04-FASTQC_trimmed_shotgun_DNA/JPQN_PCRfree_1_1_GGCTTAAG_Apple_WA38_I1177_L4_R2.trimmed_fastqc.zip
```

The Jellyfish results
https://multiqc.info/docs/#jellyfish
```bash
ln -s ../05-complexity_analysis/01-jellyfish_trimmed_shotgun/WA38.counts_jf.hist
```
