from Bio import SeqIO
import os

rows_lists =[]
with open("/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/node4_analysis/node4_genes_list.txt") as in_file:
    inlines = in_file.readlines()
    for row in inlines:
        row_list = row.split(', ')
        rows_lists.append(row_list)
    # print(rows_lists[0])
orthogroup_list = []
gene_list = []
for row in rows_lists:
    #below gets the orthogroup
    orthogroup1 = row[0][2:-1]
    orthogroup_list.append(orthogroup1)

    #below gathers all genes for each orthogroup
    genes = row[1:-1]
    genes.append(row[-1])

    #below removes unneeded symbols that will confuse later analyses
    i = 0
    for x in genes:
        if "'" in x:
            genes[i] = str(genes[i]).replace("'", "")
        if ")\n" in x:
            genes[i] = str(genes[i]).replace(")\n", "")
        i+=1

    genes.append(orthogroup1)
    gene_list.append(genes)
    print(genes)

for iter_ortho in gene_list:
    lav_gene_list = []
    for lav_seq in iter_ortho[0:-1]:
        for all_seq in SeqIO.parse('/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/OrthoFinder/Results_Jul02/Orthogroup_Sequences/{}.fa'.format(iter_ortho[-1]), 'fasta'):
            if lav_seq in all_seq.id:
                lav_gene_list.append(all_seq)
                break
    os.mkdir("/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/node4_analysis/Reconstruction/{}".format(iter_ortho[-1]))
    SeqIO.write(lav_gene_list, "/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/node4_analysis/Reconstruction/{}/{}.fasta".format(iter_ortho[-1], iter_ortho[-1]), 'fasta')