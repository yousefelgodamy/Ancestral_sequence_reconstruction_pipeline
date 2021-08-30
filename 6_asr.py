import os
from glob import glob

for ortho_path in glob("/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/node4_analysis/Reconstruction/*"):
    ortho_group = os.path.basename(ortho_path)
    print(ortho_group)
    tree_path = "/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/node4_analysis/Reconstruction/{}/tree_{}.tree".format(ortho_group, ortho_group)
    aln_path = "/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/node4_analysis/Reconstruction/{}/mafft_aligned_{}.fasta".format(ortho_group, ortho_group)
    
    if os.path.exists("{}/asr_{}.fa".format(ortho_path, ortho_group)) == False:
        try:
            os.system("treetime ancestral --aln {} --tree {} --aa --outdir {}/asr_{}.fa".format(aln_path, tree_path, ortho_path, ortho_group))
        except:
            pass
    else:
        print("Done")
