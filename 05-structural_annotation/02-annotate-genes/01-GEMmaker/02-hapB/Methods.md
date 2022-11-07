Sym link to the HapA assembly

```bash
ln -s ../../../../04-nuclear_assembly/09-renaming/Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa
```
Create a fake GTF file. 

```bash
landmark=`grep ">" Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa | head -n 1 | sed 's/>//'`
echo -e "${landmark}\tDummy\tCDS\t10\t1000\t.\t+\t0\tgene_id \"dummy\"; transcript_id \"dummyM\";" > Malus-domestica-WA_38_hapB-genome-v1.0.a1.gtf
```

