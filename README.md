# Ancestral_sequence_reconstruction_pipeline
A pipeline for reconstruction of ancestral proteins in Plasmodium (malaria) species.

Ancestral sequence reconstruction aims to reconstruct the sequence of a gene common to different gene variants or species. To do so, this requires a number of key steps:

1. Alignment of the present sequences (MAFFT protein alignment)
2. Constructing trees based on the sequence alignment (FastTree)
3. Using an ASR algorithm to infer the ancestral sequence based on the alignment and tree (TreeTime)

In this pipeline, the first 3 files are concerned with determining which genes are conserved at the ancestral species (node) of interest by looking to see if at least one orthologous gene is present in both branches of the species tree. These conserved genes allow us to infer that all genes present in an orthologous group with conserved genes are likely descendant from an ancestral node and are added to the analysis.

The genes within a group of orthologs are subsequently compared to each other in the following steps. Ancestral sequences and relevant files are placed in a directory made for each ortholog group.

The python files are ordered 1 -> 6 to denote the pipeline process.
