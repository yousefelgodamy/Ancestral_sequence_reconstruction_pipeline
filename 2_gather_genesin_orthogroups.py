import pandas as pd
import numpy as np

df_all_gene = pd.read_csv("/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/OrthoFinder/Results_Jul02/Orthogroups/Orthogroups.tsv", "\t")
df_gene1 = df_all_gene.loc[:, ['Orthogroup', 
'PlasmoDB-52_PadleriG01_AnnotatedProteins', 
'PlasmoDB-52_PgaboniG01_AnnotatedProteins', 
'PlasmoDB-52_PgaboniSY75_AnnotatedProteins']]
df_gene2 = df_all_gene.loc[:, ['Orthogroup', 
'PlasmoDB-52_PblacklockiG01_AnnotatedProteins', 
'PlasmoDB-52_PbillcollinsiG01_AnnotatedProteins', 
'PlasmoDB-52_Pfalciparum3D7_AnnotatedProteins', 
'PlasmoDB-52_PpraefalciparumG01_AnnotatedProteins', 
'PlasmoDB-52_PreichenowiCDC_AnnotatedProteins', 
'PlasmoDB-52_PreichenowiG01_AnnotatedProteins']]

with open("/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/node4_analysis/orthogroups.txt") as orthogroups:
    ortho_list = orthogroups.readlines()

final_ortho_list = []
for row in df_gene1.itertuples():
    if (str(row[1])+'\n') in ortho_list:
        final_ortho_list.append(row[1])
        
newdf = df_all_gene[np.isin(df_all_gene, final_ortho_list).any(axis=1)]
newdf2 = newdf.loc[:, ['Orthogroup', 
'PlasmoDB-52_PadleriG01_AnnotatedProteins', 
'PlasmoDB-52_PgaboniG01_AnnotatedProteins', 
'PlasmoDB-52_PgaboniSY75_AnnotatedProteins',
'PlasmoDB-52_PblacklockiG01_AnnotatedProteins', 
'PlasmoDB-52_PbillcollinsiG01_AnnotatedProteins', 
'PlasmoDB-52_Pfalciparum3D7_AnnotatedProteins', 
'PlasmoDB-52_PpraefalciparumG01_AnnotatedProteins', 
'PlasmoDB-52_PreichenowiCDC_AnnotatedProteins', 
'PlasmoDB-52_PreichenowiG01_AnnotatedProteins']]

newdf2.to_csv("/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/node4_analysis/genes_orthogroups_node4.txt", sep = '\t', index=False)


df_node_genes = pd.read_csv("/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/node4_analysis/genes_orthogroups_node4.txt", '\t')

with open("/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/node4_analysis/node4_genes_list.txt", 'w') as out_file:
    for row in df_node_genes.itertuples():
        # print(row[2])
        out_file.writelines((str(row[1:-1])))
        out_file.write('\n')
        