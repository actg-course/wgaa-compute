Here we will examine the quality of the Hi-C data. We did not do this in the `02-quality_control` 
workflow because we need the assembly to do this QC check. Now we have an assembly.  

[Phase Genomics](https://phasegenomics.com/) provides a 
[helpful QC pipeline ](https://phasegenomics.github.io/2019/09/19/hic-alignment-and-qc.html)
that can quickly tell us the quality of our data. We will use this pipeline here. The BWA 
alignment portions of this workflow was already perormed in the 
`02-bwa_hic_alignment` folder.

Remember: that our Hi-C data used the DoveTail Omni-C method, which means there were
no restriction enzymes used to fragment the crosslinked DNA.

First, create symlink to the BAM file created in the previous step

```bash
ln -s ../02-bwa_hic_alignment/WA_38.asm.hic.hap1.p_ctg_vs_HiC.sorted.bam
```

To run the hic_qc python script, we need to perform several command-line instructions
in a row. The `hic_qc.py` script provided by Phase Genomics (and which is pre-installed
inside of the Docker image we will be using), requires a Conda envirotnment activated
before we can run the script.  Here are the instructions we want to execute:

```bash
# Get all of the conda environment settings
. /opt/conda/etc/profile.d/conda.sh

# Activate the hic_qc environment
conda activate hic_qc

# Run the hic_qc python script which is installed in the
# Docker image in the /hic_qc directory.
/hic_qc/hic_qc.py -b WA_38.asm.hic.hap1.p_ctg_vs_HiC.sorted.bam -o WA_38.asm.hic.hap1.p_ctg_vs_HiC
```

Singularity will only let us run one command at a time. So, we need to convert 
all of these into a single command-line instruction. We can do this by creating 
a bash script that contains these commands. Then we run the script via Singularity.

To to do this, the commands above were cut-and-pasted into a file named `hic_qc.sh`. 
Notice it is just a simple file of the command-line instructions we want to run. 
Creating this type of bash script is easy!

We need to make our script executable so it can run.
```bash
chmod 755 hic_qc.sh
```

Now, run the script using a SLURM job:
```bash
sbatch 04-hic_qc.srun
```

The `hic_qc.py` program generates an HTML report. But, the HTML report has hardcoded paths 
for images which means it will not show the images if we move the file, but we cannot easily
view this file from Kamiak. We have to move it. The following perl command will fix the HTML 
so that as long as the images are in the same directory, the HTML report will show the images

```bash
perl -pi -e 's/src="(.+)\/(.*.png)"/src="\2"/g' WA_38.hap1_vs_HiC_qc_report.html
```

Note: the command above uses a [regular expression](https://en.wikipedia.org/wiki/Regular_expression)
to find matches in the HTML file and make changes.  It is a powerful tool that used in all
modern programming languages and is an essential tool for data wrangling.  We do not have time
to learn regular expressions in this course, but if you would like to learn more consider 
taking that AFS505 Unit 3 in the Spring semester.
