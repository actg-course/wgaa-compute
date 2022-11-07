# Data Setup
First link to the soft masked genome assembly:

```bash
ln -s ../../../01-annotate_repeats/02-RepeatMasker/01-hapA/Malus-domestica-WA_38_hapA-genome-v1.0.a1.softmasked.fa
```

# GeneMark Setup
Braker uses a variety of software that is already present in the Docker image.
One exception is GeneMark.  GeneMark requires a license file to run and the
software can only be dowloaded with permission. Therefore it is not in the
Docker image. Instead we need to provide it.  Also, GeneMark requires a 
license which cannot be included in the Docker image.  Licenses are free for academic purposes.  
Both software and licenses can be downladed from here:
http://exon.gatech.edu/GeneMark/license_download.cgi 

Note: 
- For the class, the software is already downloaded 
- You can use the GeneMark key found in the `../../../../01-input_data/GeneMark/`
- The key is valid for 200 days from the date it was last obtained.


To setup the key, copy the `gm_key_64.gz` file to your home directory, then run the following 

```bash
cp ../../../../01-input_data/GeneMark/gm_key_64.gz .
gunzip gm_key_64.gz
mkdir -p temp_home
mv gm_key_64 temp_home/.gm_key
```

The `temp_home` directory created in the commands above will be mounted inside of the 
Docker image, when it is run. This will result in the GeneMark key being present 
in the home directory as GeneMark expects.

Next, we need the software. GeneMark software can be downloaded at the same
location where the license is obtained. For the class, the software is pre-downloaded
onto Kamiak and needs to be installed into this directory.

```bash
cp ../../../../01-input_data/GeneMark/gmes_linux_64_4.tar.gz ./
tar -zxvf gmes_linux_64_4.tar.gz
```

# Run Braker
Now we can run Braker. The `braker_RNAseq.sh` script does a bit of setup
that is needed for Braker, such as setting environment variables.

```bash
sbatch 01-braker_RNAseq.srun
```

