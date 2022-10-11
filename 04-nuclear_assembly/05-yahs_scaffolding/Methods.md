First create symlinks to the haplotype assemblies

```bash
ln -s ../01-hifiasm/WA_38.asm.hic.hap1.p_ctg.fa
ln -s ../01-hifiasm/WA_38.asm.hic.hap2.p_ctg.fa
```

Next create symlinks to the BAM alignment files
```bash
ln -s ../02-bwa_hic_alignment/WA_38.asm.hic.hap1.p_ctg_vs_HiC.sorted.bam
ln -s ../02-bwa_hic_alignment/WA_38.asm.hic.hap2.p_ctg_vs_HiC.sorted.bam
```

The first step prior to scaffolding is to use samtools to index the contigs 
from the hifiasm step. We need to index each haplotype assembly separatly so they can be 
run at the same time in parallel:
```bash
01-samtools-index-hap1.srun
02-samtools-index-hap2.srun
```

After the indexing has completed we can then run YaHS for scaffolding.
```bash
03-yahs-hap1.srun
04-yahs-hap2.srun
```
