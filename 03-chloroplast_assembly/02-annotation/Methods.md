To annotate the Choloroplast we will use GESEq at https://chlorobox.mpimp-golm.mpg.de/geseq.html

Once finished, download all results as a zip file and place here.

Settings:
- FASTA File(s) to annotate:
  - Upload the NOVOPlasty circular chloroplast genome. Select "circular"
  - Sequence source: Plastid (land plants)
  - Annotation options (select):
    - Annotate plastid inverted Repeat (IR)
    - Annotate plasted trans-speliced rps12
  - Annotation Support (select):
    - Support annotation by Chloe
  - Annotation revision (select):
    - Keep best annotation only

Annotation:
- Blat search
  - Protein search identity: 25
  - rRNA, tRNA, DNA search identity: 85
  - Annotate (select): CDS, tRNA, rRNA
  - Options (select):
    - Ignore genes annotated as locus tag
-3rd Party tRNA annotations (select)
  - Aragorn v1.2.38
    - Genetic Code: Bacterial/Plant Choloroplast
    - Max intron length: 3000

Blat REference Sequence:
- MPI-MP Reference Set (Select):
  - Chloroplast land plants (CDS+rRNA)

3rd Party Stand Alone Annotators
- Chloe v0.1.0
  - Annotate (select): CDS, rRNA, rRNA

Output Options
- Generate multi-GenBank
- Generate multi-GFF3
