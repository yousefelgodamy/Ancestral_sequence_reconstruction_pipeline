import pandas as pd

df = pd.read_csv("/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/OrthoFinder/Results_Jul02/Orthogroups/Orthogroups.GeneCount.tsv", "\t")

df_n1 = df.loc[:, ['Orthogroup', 
'PlasmoDB-52_PadleriG01_AnnotatedProteins', 
'PlasmoDB-52_PgaboniG01_AnnotatedProteins', 
'PlasmoDB-52_PgaboniSY75_AnnotatedProteins']]

df_n2 = df.loc[:, ['Orthogroup', 
'PlasmoDB-52_PblacklockiG01_AnnotatedProteins', 
'PlasmoDB-52_PbillcollinsiG01_AnnotatedProteins', 
'PlasmoDB-52_Pfalciparum3D7_AnnotatedProteins', 
'PlasmoDB-52_PpraefalciparumG01_AnnotatedProteins', 
'PlasmoDB-52_PreichenowiCDC_AnnotatedProteins', 
'PlasmoDB-52_PreichenowiG01_AnnotatedProteins']]

n1_orthogroups = []
n2_orthogroups = []
final_orthogroups = []
ortho_groups = []

for row in df_n1.itertuples():
    if row[2] > 0:
        n1_orthogroups.append(row.Orthogroup)
for row in df_n2.itertuples():
    if row[2] > 0:
        n2_orthogroups.append(row.Orthogroup)
for n1 in n1_orthogroups:
    if n1 in n2_orthogroups:
        final_orthogroups.append(n1 + '\n')
        ortho_groups.append(n1)

with open("/work/yelgodam/venv/ortho_finder_analysis/N0_genomes/node4_analysis/orthogroups.txt", 'a') as out_file:
    out_file.writelines(final_orthogroups)
