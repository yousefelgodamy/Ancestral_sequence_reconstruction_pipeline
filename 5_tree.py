import os
from glob import glob

for ortho_path in glob("/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/node4_analysis/Reconstruction/OG*"):
    ortho_group = os.path.basename(ortho_path)
    aln_path = "/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/node4_analysis/Reconstruction/{}/mafft_aligned_{}.fasta".format(ortho_group, ortho_group)
    tree_path = "/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/node4_analysis/Reconstruction/{}/tree_{}.tree".format(ortho_group, ortho_group)

    os.system("fasttree {} > {}".format(aln_path, tree_path))