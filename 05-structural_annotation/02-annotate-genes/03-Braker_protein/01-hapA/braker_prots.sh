# Get all of the conda environment settings
. /opt/conda/etc/profile.d/conda.sh

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
export GENEMARK_PATH=`pwd`/gmes_linux_64_4

braker.pl \
  --genome=Malus-domestica-WA_38_hapA-genome-v1.0.a1.Nmasked.fa \
  --prot_seq=proteins.fa \
  --cores 20 \

