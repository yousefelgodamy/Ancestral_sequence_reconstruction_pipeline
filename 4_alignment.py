from glob import glob
import os

for x in glob("/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/node4_analysis/Reconstruction/*"):
    ortho_group = os.path.basename(x)
    if os.path.isfile("{}/mafft_aligned_{}.fasta".format(x, ortho_group)) == False:
        os.system("mafft --auto {}/{}.fasta > {}/mafft_aligned_{}.fasta".format(x, ortho_group, x, ortho_group))
    else:
        print('Done')
