#!/usr/bin/env python3

import argparse
import csv
import re

# Specify the arguments that are allowed by this script
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--gtf', dest='gtf', action='store', required=True, 
                   help='The name of the GTF file to be converted.')
parser.add_argument('--out', dest='out', action='store', required=True,
                   help='The name of the GFF outputfile.')

# Read in the input arguments
args = parser.parse_args()

with open(args.gtf, "r") as gtf_file:
   gtf_reader = csv.reader(gtf_file, delimiter="\t")
   with open(args.out, "w") as gff_file:
      gff_writer = csv.writer(gff_file, delimiter="\t")
      counts = {}
      for row in gtf_reader:

        attrs = {}
        (seqid, source, ftype, start, end, score, strand, phase, attrstr) = row 

        if (ftype == "gene"):
          attrs['ID'] = attrstr
        elif (ftype == "transcript"):
          attrs['ID'] = attrstr
          attrs['Parent'] = re.sub(r"(g\d+)\.t\d+", r'\1', attrstr)
          counts = {}
        else:
          
          if (ftype == 'tss'):
            ftype = 'TSS' 
          elif (ftype == 'tts'):
            ftype = 'transcription_end_site' 
          elif (re.search(r'3\'+\-UTR', ftype)):
            ftype = 'three_prime_UTR'
          elif (re.search(r'5\'+\-UTR', ftype)):
            ftype = 'five_prime_UTR'

          if (ftype not in counts.keys()):
            counts[ftype] = 0
          else:
            counts[ftype] = counts[ftype] + 1
          parent = re.sub(r"transcript_id \"(.+?)\";.*", r'\1', attrstr)
          attrs['ID'] = parent + "." + ftype.lower() + str(counts[ftype])
          attrs['Parent'] = parent

        attrstr = ";".join("=".join([key, str(value)]) for key, value in attrs.items())
        gff_writer.writerow([seqid, source, ftype, start, end, score, strand, phase, attrstr])

