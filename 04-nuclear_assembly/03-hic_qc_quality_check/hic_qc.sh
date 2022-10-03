# Get all of the conda environment settings
. /opt/conda/etc/profile.d/conda.sh

# Activate the hic_qc environment
conda activate hic_qc

# Run the hic_qc python script which is installed in the
# Docker image in the /hic_qc directory.
/usr/local/bin/hic_qc/hic_qc.py -b WA_38.asm.hic.hap1.p_ctg_vs_HiC.sorted.bam -o WA_38.hap1_vs_HiC
