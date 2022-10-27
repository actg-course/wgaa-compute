# Get all of the conda environment settings
. /opt/conda/etc/profile.d/conda.sh

# Activate the hic_qc environment
conda activate EDTA

# Run the EDTA script
EDTA.pl \
  --genome Malus-domestica-WA_38_hapA-genome-v1.0.a1.fa \
  --cds Gala_diploid_v2.cds.fa \
  --overwrite 1 \
  --sensitive 1 \
  --anno 1 \
  --threads 10

