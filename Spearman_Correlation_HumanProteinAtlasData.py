import csv
import scipy
from scipy import stats
proteins=[]
dictionary={}
with open("HPM_gene_level_epxression_matrix_Kim_et_al_052914.csv","rU") as csvfile:
	reader=csv.reader(csvfile, delimiter=",")
	for lines in reader:
		i=0
		dictionary[lines[0]]=[]
		i=i+1
with open("HPM_gene_level_epxression_matrix_Kim_et_al_052914.csv","rU") as csvfile:
	reader=csv.reader(csvfile, delimiter=",")
	reader.next()
	for lines in reader:
		proteins.append(lines[0])
		if lines[0] in dictionary:
			for i in range(1,len(lines)):
				dictionary[lines[0]].append(float(lines[i]))
with open("HPM_corr_final.txt","w") as f:
	for i in range(len(proteins)):
		for j in range(len(proteins)):
			try:
				print>>f, str(proteins[i])+"\t"+str(proteins[j])+"\t"+str(scipy.stats.spearmanr(dictionary[proteins[i]],dictionary[proteins[j]])[0])+ "\t" + str(scipy.stats.spearmanr(dictionary[proteins[i]],dictionary[proteins[j]])[1])
			except:
				pass
