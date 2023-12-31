# Get all of the conda environment settings
. /opt/conda/etc/profile.d/conda.sh

# ---------------------
# Augustus
# Augustus requires a writeable config folder, but that's
# in the docker image which is not writeable so we need to
# copy it here and set an environment variable to tell
# braker where it is:
mkdir -p config
cp -R /opt/conda/config/* config/

# Now set all of the enrivonment variables
export AUGUSTUS_CONFIG_PATH=`pwd`/config
export AUGUSTUS_BIN_PATH=/opt/conda/bin
export AUGUSTUS_SCRIPTS_PATH=/opt/conda/bin

# ---------------------
# GUSHR
# The  GUSHR tool in the Braker docker image expects
# it's installation directory to be writeable but in
# a singularity image this isn't the case. Let's create a copy
cp -R /usr/local/bin/GUSHR ./
export GUSHR_PATH=`pwd`/GUSHR


# ---------------------
# GeneMark
# Since we already have GeneMark in the local path
# set the environment variable for it
export GENEMARK_PATH=`pwd`/gmes_linux_64_4

bams=`ls ../../01-GEMmaker/01-hapA/results/Samples/*/*.sorted.bam | perl -p -e 's/\n/,/g' | perl -p -e s'/,$//'`

braker.pl \
  --genome=Malus-domestica-WA_38_hapA-genome-v1.0.a1.softmasked.fa \
  --bam ${bams} \
  --cores 20 \
  --softmasking \
  --UTR=on \
  --species=malus_domestica

