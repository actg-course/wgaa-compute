# Computational Resources for the Whole Genome Annotation and Assembly Course

This repository contains the SLURM scripts, Method files and other resources for all computational steps required of the American Campus Tree Genome (ACTG) Whole Genome Annotation and Assembly curriculum.  This repository was built as part of the WA 38 apple (*Malus domestica*) variety (Cosmic Crisp (TM)) genome assembly project performed at Washington State University. The scripts and methods are meant to help instructors who wish to use their own local compute resources.  The scripts may need to be adapated for local instances of a SLURM-based cluster or adapted for other types of schedulers.

## Supported Data Types
This repository supports the following types of data
- HiFi whole genome PAC Bio reads: for primary genome assembly
- Illumina HiC (OmniC) short-reads: to support scaffolding (as necessary)
- Illumina whole genome short-read:  to support scaffolding (as necessary)
- Illumina multiple tissue RNA-seq reads:  to support structural gene annotations

## Software Dependencies
All software dependencies of this course have been Dockerized and have been tested and used for the WA 38 assembly.  No software installation is required to use this repository.

## Computational Dependecies
This repository was written for use on a SLURM-based scheduler and intended for use on a high-performance compute cluster with multiple nodes, CPUs and machines with large amounts of RAM.  

## Demo Data
A small subset of the WA 38 genome data is available for testing and practice with this repository.  Instructors who wish to use and adapt this resource are encouraged to run through all of the steps using the sample data.  The sample data is available at XXXXX.

## How to use this repository

This respository is organized as a workflow.  The first level directories contains major tasks for whole genome assembly and annotation, subdirectories are divided into sub tasks.  Each directory is numbered and the number indicates the order in which the task should be executed.  For example, at the first-level the following directories are present:

```bash
01-input_data
02-quality_control
03-chloroplast_assembly
04-nuclear_assembly
05-structural_annotation
06-functional_annotation
07-comparative
README.md
```
The `01-input_data` directory is meant to house all of the input data for the project.  All of the sequence data, functional data, etc. should be housed here.  Each of the other directories have subtasks that should be executed in order.  Thus, all of the subtasks in the `02-quality_control` folder should be executed in order before executing the subtasks in the `03-chloroplast_assembly` folder.  

The `README.md` files contain an overview of the task and subtasks that each directory is meant to perform.

Each task directory will have a `Methods.md` file. This file will provide the step-by-step insructions for how to execute the task in that directory.  