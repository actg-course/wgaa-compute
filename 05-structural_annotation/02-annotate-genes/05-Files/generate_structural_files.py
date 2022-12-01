#!/usr/bin/env python3

"""
A script written for the WSU Hort 403/503 course for assembly of WA 38

This script takes in a GFF file created during the TSEBRA step and the
GFF file of repeats from RepeatMasker. It returns a variety of new GFF3 and
FASTA files that have features named according to expected nomenclature.

It also outputs mRNA, CDS and protein sequence files for all genes.

"""

import argparse
import csv
import re
import copy
import os.path
import warnings

# Requires package installation: biopython, bcbio-gff
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from BCBio import GFF
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.SeqIO.FastaIO import FastaWriter
from Bio import BiopythonWarning


SeqRecords = {}


def parseGenome(genome):
    """
    Indexes the sequences in the assembly for quick lookup.

    Paramters:
        genome (array): An array of SeqRecords
    """
    for rec in genome:
        SeqRecords[rec.id] = rec


def getSeqRecord(seqid):
    """
    Returns the seqRecord for a sequence in the FASTA file

    Paramters:
        seqid (string): the name of the landmark chromosome or scaffold.

    Returns
        A SeqRecord object for the given chromsome/scaffold sequence.
    """
    if seqid in SeqRecords:
        return SeqRecords[seqid]
    print("Could not find sequence, '{}', in the FASTA file".format(seqid))
    exit(1)


def renameGene(args, seqid, gene, gene_num):
    """
    Renames a gene

    Parameters:
        args: the incoming program arguments provided by the user.
        seqid (string): the name of the landmark chromosome or scaffold.
        gene (SeqFeature): the gene record.
        gene_num (int): the current count of all genes on the landmark.
    """
    fid = args.species + '.' + args.cultivar + ".v" + args.assem_version + "a" + \
        args.annot_version + "." + seqid + \
        "." + "g" + ("%06d" % gene_num)
    gene.id = fid
    #gene.qualifiers['AnnotID'] = gene.qualifiers['ID']
    gene.qualifiers['ID'] = gene.id
    gene.qualifiers['source'] = args.source

    mRNA_num = 1
    for feature in gene.sub_features:
        if feature.type == 'mRNA':
            renameMRNA(args, gene, feature, mRNA_num)
            mRNA_num = mRNA_num + 1
        else:
            print("Unrecognized sub feature type: '{}'".format(sftype))
            exit(1)


def renameMRNA(args, gene, mRNA, mRNA_num):
    """
    Renames the mRNA of a gene

    Parameters:
        args: the incoming program arguments provided by the user.
        gene (SeqFeature): the gene record.
        mRNA (SeqFeature): the mRNA's record.
        mRNA_num (int): the current count of all mRNAs.
    """

    # Set the mRNA name by adding a ".tX" suffix where X is
    # the transcript number.
    gene_id = gene.id
    mRNA.id = gene_id + ".t" + str(mRNA_num)
    mRNA.qualifiers['ID'] = mRNA.id
    mRNA.qualifiers['source'] = args.source

    # Now go through the children of the of the mRNA and
    # rename those features as well.
    ftype_nums = {
        'CDS': 1,
        'exon': 1,
        'intron': 1,
        'three_prime_UTR': 1,
        'five_prime_UTR': 1,
        'start_codon': 1,
        'stop_codon': 1,
        'transcription_end_site': 1,
        'TSS': 1
    }
    for feature in mRNA.sub_features:
        if feature.type not in ftype_nums:
            print(
                "Unrecognized mRNA sub feature type: '{}'".format(ssftype))
            exit(1)
        renameMRNAChild(args, mRNA, feature, ftype_nums)
        ftype_nums[feature.type] = ftype_nums[feature.type] + 1


def renameMRNAChild(args, mRNA, child, ftype_nums):
    """
    Renames the child element of the mRNA

    Parameters:
        args: the incoming program arguments provided by the user.
        mRNA (SeqFeature): the transcript record.
        child (SeqFeature): the mRNA's child record.
        ftype_nums (dict): a dictionary of the current count of all mRNA
            child types.
    """
    # Set the mRNA child's ID by adding the type name and it's number.
    mRNA_id = mRNA.id
    child.id = mRNA_id + "." + child.type + str(ftype_nums[child.type])
    child.qualifiers['ID'] = child.id
    child.qualifiers['source'] = args.source


def processGenes(args, genes):
    """
    Processes and renames the genes in the provided GFF3 file.

    Parameters:
        args: the incoming program arguments provided by the user.
        genes (array): an array of SeqRecords containing gene features.

    Returns
        An array of SeqRecords with the genes features added.
    """
    seq_recs = []
    for rec in genes:

        # Get the landmark sequence record.
        seqid = rec.id
        seq_rec = copy.deepcopy(getSeqRecord(seqid))
        print("Renaming genes for '{}'...".format(seqid))
        gene_num = 10

        # Iterate through the features (i.e. genes).
        for feature in rec.features:
            if feature.type == 'gene':
                renameGene(args, seqid, feature, gene_num)
                seq_rec.features.append(feature)
                gene_num = gene_num + 10
            else:
                print("Unrecognized feature type: '{}'".format(ftype))
                exit(1)

        seq_recs.append(seq_rec)

    return seq_recs


def processRepeats(args, repeats):
    """
    Processes and names the repeats in the provided GFF2 file.

    Parameters:
        args: the incoming program arguments provided by the user.
        repeats (file handle): the repeats GFF file handle

    Returns
        An array of SeqRecords with the repeat features added.
    """

    print("Converting repeats to GFF3 records...")

    # Keep a list of the seq records.
    seq_recs = {}

    # Keep track of the number of repeats per chromosome.
    repeat_nums = {}

    # Iterate through the lines in the RepeatMasker output file.
    line_num = 0
    for line in repeats.readlines():

        # Skip the first 3 hearder lines
        if line_num < 3:
            line_num = line_num + 1
            continue

        # Split the line into values by splitting on spaces.
        cols = line.split()

        # Get the landmark sequence record
        seqid = cols[4]
        if seqid not in seq_recs:
            seq_recs[seqid] = copy.deepcopy(getSeqRecord(seqid))
            repeat_nums[seqid] = 10
        seq_rec = seq_recs[seqid]

        # Create an ID for this repeat
        rid = args.species + '.' + args.cultivar + ".v" + args.assem_version + "a" + \
            args.annot_version + "." + seqid + \
            "." + "r" + ("%08d" % repeat_nums[seqid])

        # Create a new seqFeature for the repeat
        strand = 1 if cols[8] == '+' else -1
        qualifiers = {
            'score': cols[1],
            'perc_div': cols[2],
            'perc_del': cols[3],
            'class': cols[10],
            'source': args.source,
            'ID': rid
        }

        # If this isn't a simple repeat then it's an alignment so we
        # should add a target qualifier.
        if cols[10] == 'Simple_repeat':
            qualifiers['motif'] = cols[9]
        else:
            qualifiers['Target'] = "{} {} {}".format(
                cols[9], cols[11].replace('(', '').replace(')', ''), cols[12].replace('(', '').replace(')', ''))

        # Create the repeat SeqFeature object.
        repeat = SeqFeature(
            FeatureLocation(int(cols[5]), int(cols[6])),
            type="repeat_region",
            strand=strand,
            qualifiers=qualifiers
        )
        repeat.id = rid

        seq_rec.features.append(repeat)
        repeat_nums[seqid] = repeat_nums[seqid] + 10

    return seq_recs.values()


def writeGenesFASTA(genes_fasta_out, seq_recs):
    """
    Write a FASTA file of gene sequences

    Parameters:
        genes_fasta_out (file handle): the file handle for the mRNA FASTA file.
        seq_recs (array): an array of SeqRecord objects one for each chromosome
            or scaffold in the assembly.
    """
    fasta_writer = FastaWriter(genes_fasta_out)

    # Iterate through all of the assembly sequnces.
    for seq_rec in seq_recs:
        # Iterate through all of the features on the sequence.
        for feature in seq_rec.features:
            if feature.type == 'gene':
                # Extract the sequence and write it to the FASTA file.
                gene = feature
                gene_sequence = Seq(gene.location.extract(seq_rec).seq)
                strand = "+" if gene.strand == 1 else "-"
                gene_rec = SeqRecord(gene_sequence, id=gene.id, name=gene.id,
                                     description=gene.type + " from "
                                     + seq_rec.id + ":"
                                     + str(int(gene.location.start))
                                     + "-" + str(int(gene.location.end))
                                     + strand)
                fasta_writer.write_record(gene_rec)


def writeTranscriptChild(fasta_out, seq_rec, mRNA, child_type):
    """
    Writes to a FASTA file the child feature (e.g. exon, CDS) from a transcript

    Parameters:
        fasta_out (file handle): the file handle for the FASTA file.
        seq_rec (SeqRecord): the record for the landmark on which this
            feature resides.
        mRNA (SeqFeature): the transcript record.
        child_type: the type of child feature to generate a FASTA file for.
    """
    warnings.filterwarnings("error", category=BiopythonWarning)

    fasta_writer = FastaWriter(fasta_out)
    type_check = child_type
    if child_type == 'protein':
        type_check = 'CDS'

    # Collect the child sequences.
    child_seqs = []
    for feature in mRNA.sub_features:
        if (feature.type == type_check):
            child_seqs.append(str(feature.location.extract(seq_rec).seq))

    # Combine the child sequences.
    if (mRNA.strand == -1):
        child_seqs.reverse()
    feature_seq = Seq("".join(child_seqs))

    relationship = " within region "
    if (child_type == 'protein'):
        relationship = " dervies from region "
        try:
            feature_seq = feature_seq.translate()
        except BiopythonWarning as w:
            print({
                'warning': w,
                'id': mRNA.id
            })

    # Now build the SeqRecord object and write it to the FASTA file.
    strand = "+" if mRNA.strand == 1 else "-"
    rec = SeqRecord(feature_seq, id=mRNA.id, name=mRNA.id,
                    description=child_type
                    + relationship
                    + seq_rec.id + ":"
                    + str(int(mRNA.location.start))
                    + "-" + str(int(mRNA.location.end))
                    + strand)
    fasta_writer.write_record(rec)
    warnings.resetwarnings()


def writeTranscripts(mRNA_fasta_out, cds_fasta_out, prot_fasta_out, seq_recs):
    """
    Writes all of the FASTA files for the transcripts.

    Parameters:
        mRNA_fasta_out (file handle): the file handle for the mRNA FASTA file.
        cds_fasta_out (file handle): the file handle for the mRNA FASTA file.
        prot_fasta_out (file handle): the file handle for the mRNA FASTA file.
        seq_recs (array): an array of SeqRecord objects one for each chromosome
            or scaffold in the assembly.
    """
    fasta_writer = FastaWriter(mRNA_fasta_out)
    for seq_rec in seq_recs:
        for gene in seq_rec.features:
            for feature in gene.sub_features:
                if feature.type == 'mRNA':
                    writeTranscriptChild(
                        mRNA_fasta_out, seq_rec, feature, 'exon')
                    writeTranscriptChild(
                        cds_fasta_out, seq_rec, feature, 'CDS')
                    writeTranscriptChild(
                        prot_fasta_out, seq_rec, feature, 'protein')


def main():
    """
    The main function
    """
    # Specify the arguments that are allowed by this script
    parser = argparse.ArgumentParser(
                        description='Process some integers.')
    parser.add_argument('--genes', dest='genes', action='store', required=True,
                        help='The path to the GFF file with the gene annotations.')
    parser.add_argument('--repeats', dest='repeats', action='store', required=True,
                        help='The path to the RepeatMasker out file with the repeat annotations.')
    parser.add_argument('--genome', dest='genome', action='store', required=True,
                        help='The path to the whole file FASTA file.')
    parser.add_argument('--species', dest='species', action='store', required=True,
                        help='The name of the GFF outputfile.')
    parser.add_argument('--cultivar', dest='cultivar', action='store', required=True,
                        help='The name of the GFF outputfile.')
    parser.add_argument('--assem_version', dest='assem_version', action='store', required=True,
                        help='The name of the GFF outputfile.')
    parser.add_argument('--annot_version', dest='annot_version', action='store', required=True,
                        help='The name of the GFF outputfile.')
    parser.add_argument('--source', dest='source', action='store', required=True,
                        help='A new value for the source column of the GFF3 file')

    # Parse the arguments provided by the user.
    args = parser.parse_args()

    # Get the basename of the input genome assembly file. We'll use this
    # same basename as a prefix for all of the output files.
    basename = os.path.basename(args.genome)

    # Open the input files
    print("Reading GFF and genome FASTA files...")
    genes_in = open(args.genes, "r")
    repeats_in = open(args.repeats, "r")
    genome_in = open(args.genome, "r")

    # Open the output files
    genes_out_gff = open(basename + '.gff3', "w")
    repeats_out_gff = open(basename + '.repeats.gff3', "w")
    genes_fasta_out = open(basename + '.genes.fna', "w")
    mRNA_fasta_out = open(basename + '.mRNA.fna', "w")
    cds_fasta_out = open(basename + '.CDS.fna', "w")
    prot_fasta_out = open(basename + '.protein.faa', "w")


    # Parse the Genome sequence file
    genome = SeqIO.parse(genome_in, "fasta")
    parseGenome(genome)

    # Parse the GFF file.
    genes = GFF.parse(genes_in)

    # Process the Genes GFF file
    seq_recs = processGenes(args, genes)
    print("Writing GFF file of renamed features...")
    GFF.write(seq_recs, genes_out_gff)
    print("Writing FASTA file of gene sequences...")
    writeGenesFASTA(genes_fasta_out, seq_recs)
    print("Writing FASTA file of transcript sequences (FL-mRNA, CDS, protein)...")
    writeTranscripts(mRNA_fasta_out, cds_fasta_out,
                     prot_fasta_out, seq_recs)

    # Process Repeats
    seq_recs = processRepeats(args, repeats_in)
    GFF.write(seq_recs, repeats_out_gff)

    # Close the file handles
    genes_out_gff.close()
    repeats_out_gff.close()
    genes_fasta_out.close()
    mRNA_fasta_out.close()
    cds_fasta_out.close()
    prot_fasta_out.close()
    genes_in.close()
    repeats_in.close()
    genome_in.close()


if __name__ == "__main__":
    main()
