# RNA_methylation
RNA methylation is less known until late 1970s and it only has increased its significance as NGS enabled RNA-sequencing revealing the transcriptome which is now being used to study various post-transcriptional modifications. One such modifications is m6A, a methyl transferase based modification on 6th nitrogen of Adenosine on the RNA.

Here, the code outputs spearman correlation of all RBPs listed in my file across 31 tissues. This step was essential to check how are methyl transferase enzymes are correlated with other other proteins

##SPEARMAN CORRELATION##

import csv 
import scipy
from scipy import stats

proteins=[] ##declaring an array

dictionary={} ##declaring a dictionary

with open("<filename>","rU") as csvfile:	##reading the file and adding desired columns into a dictionary
    reader=csv.reader(csvfile, delimiter="\t")
    i=0
    j=0
    for lines in reader:
        dictionary[lines[0]]=[]
        i=i+1
        if i>1314:
        	break



with open("<filename>","rU") as csvfile:	##iterating through the coloumn and appending it to dictionary
    reader=csv.reader(csvfile, delimiter="\t")
    reader.next()
    for lines in reader:
        proteins.append(lines[0]) ##adding proteins into a list
        if lines[0] in dictionary:
            for i in range(1,len(lines)):
                dictionary[lines[0]].append(float(lines[i]))


with open("PXP_ALL_output.txt","w") as f:	##iterating through my list of proteins
    for i in range(len(proteins)):
        for j in range(len(proteins)):
            j=j+1
            if j>1317:
		break
	
 
    print>>f, str(proteins[i])+"\t"+str(proteins[j])+"\t"+str(scipy.stats.spearmanr(dictionary[proteins[i]],dictionary[proteins[j]])[0])	 ##printing the output and calculating spearman correlation for my proteins (key:value) stored in my dictiorary


