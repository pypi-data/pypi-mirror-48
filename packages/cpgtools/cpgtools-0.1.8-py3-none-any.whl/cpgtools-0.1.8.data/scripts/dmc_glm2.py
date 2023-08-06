#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
"""
#=========================================================================================
This program performs differential CpG analysis using linear regression model based on
beta values. 

allow for covariables. 
...

#=========================================================================================
"""


import sys,os
import collections
import subprocess
import numpy as np
from scipy import stats
from optparse import OptionParser
from cpgmodule import ireader
from cpgmodule.utils import *
from cpgmodule import BED
from cpgmodule import padjust

__author__ = "Liguo Wang"
__copyright__ = "Copyleft"
__credits__ = []
__license__ = "GPL"
__version__="0.1.5"
__maintainer__ = "Liguo Wang"
__email__ = "wang.liguo@mayo.edu"
__status__ = "Development"

	
def main():
	usage="%prog [options]" + "\n"
	parser = OptionParser(usage,version="%prog " + __version__)
	parser.add_option("-i","--input-file",action="store",type="string",dest="input_file",help="Data file containing beta values with the 1st row containing sample IDs (must be unique) and the 1st column containing CpG positions or probe IDs (must be unique). This file can be regular text file or compressed file (*.gz, *.bz2) or accessible url.")
	parser.add_option("-g","--group",action="store",type="string",dest="group_file",help="Group file defining the biological groups of each sample as well as other covariables such as gender, age. The first varialbe is usually categorical and used to make the contrast (calculate pvalues), all the other variables are considered as covariates.   Sample IDs shoud match to the \"Data file\".")
	parser.add_option("-o","--output",action="store",type='string', dest="out_file",help="Prefix of the output file.")
	(options,args)=parser.parse_args()
	
	print ()
	if not (options.input_file):
		print (__doc__)
		parser.print_help()
		sys.exit(101)

	if not (options.group_file):
		print (__doc__)
		parser.print_help()
		sys.exit(102)
				
	if not (options.out_file):
		print (__doc__)
		parser.print_help()
		sys.exit(103)	
	
	if not os.path.isfile(options.input_file):
		print ("Input data file \"%s\" does not exist\n" % options.input_file) 
		sys.exit(104)
	if not os.path.isfile(options.group_file):
		print ("Input group file \"%s\" does not exist\n" % options.input_file) 
		sys.exit(105)
	if os.path.exists(options.out_file + '.results.txt'):
		os.remove(options.out_file + '.results.txt')
	
	
	ROUT = open(options.out_file + '.r','w')
	
	printlog("Read group file \"%s\" ..." % (options.group_file))
	(samples,cv_names, cvs, v_types) = read_grp_file2(options.group_file)
	for cv_name in cv_names:
		print ("%s: %s" % (cv_name, v_types[cv_name]))
		for sample in samples:
			print ('\t' + sample + '\t' + cvs[cv_name][sample])	
	
	print ('lrf <- function (cgid, y, %s){' % ','.join(cv_names), file=ROUT)
	print ('\ttry(fit1 <- glm(y ~ %s, family=gaussian))' % ('+'.join(cv_names)), file=ROUT)
	if len(cv_names) == 1:
		print ('\ttry(fit0 <- glm(y ~ 1, family=gaussian))', file=ROUT)
	elif len(cv_names) >1:
		print ('\ttry(fit0 <- glm(y ~ %s, family=gaussian))' % ('+'.join(cv_names[1:])), file=ROUT)
	
	print ('\ttest <- anova(fit1, fit0,test="Chisq")', file=ROUT)
	print ('\tpval <- test[[5]][[2]]', file=ROUT)
	print ('\tresults <- list(cgID = cgid, pvalue = pval)', file=ROUT)
	print ('\twrite.table(file=\"%s\",x=results, quote=FALSE, row.names=FALSE, sep="\\t",append = TRUE, col.names=FALSE)' % (options.out_file + '.results.txt'),  file = ROUT)
	print ('}', file=ROUT)	
	print ('\n', file=ROUT)

	

	printlog("Processing file \"%s\" ..." % (options.input_file))

	line_num = 0
	for l in ireader.reader(options.input_file):
		line_num += 1
		f = l.split()
		if line_num == 1:
			sample_IDs = f[1:]
			# check if sample ID matches
			for s in samples:
				if s not in sample_IDs:
					printlog("Cannot find sample ID \"%s\" from file \"%s\"" % (s, options.input_file))
					sys.exit(3)
			for cv_name in cv_names:
				if v_types[cv_name] == 'continuous':
					print (cv_name + ' <- c(%s)' % (','.join([str(cvs[cv_name][s]) for s in  sample_IDs  ])), file = ROUT)
				elif  v_types[cv_name] == 'categorical':
					print (cv_name + ' <- as.factor(c(%s))' % (','.join([str(cvs[cv_name][s]) for s in  sample_IDs  ])), file = ROUT)
				else:
					printlog("unknown vaiable type!")
					sys.exit(1)
			print ('\n', file=ROUT)
			continue
		else:
			beta_values = []
			cg_id = f[0]
			for i in f[1:]:
				try:
					beta_values.append(float(i))
				except:
					beta_values.append("NaN")
			#print ('%s = c(%s),' % (cg_id, ','.join([str(i) for i in beta_values])), file=ROUT)
			print ('lrf(\"%s\", c(%s), %s)' % (cg_id,  ','.join([str(i) for i in beta_values]), ','.join(cv_names)), file=ROUT)	

	
	ROUT.close()

	try:
		printlog("Runing Rscript file \"%s\" ..." % (options.out_file + '.r'))
		subprocess.call("Rscript %s 2>%s" % (options.out_file + '.r', options.out_file + '.r.warnings.txt' ), shell=True)
	except:
		print ("Error: cannot run Rscript: \"%s\"" % (options.out_file + '.r'), file=sys.stderr)
		sys.exit(1)
	
	printlog("Perfrom Benjamini-Hochberg (aka FDR) correction ...")
	probe_list = []
	p_list = []
	if os.path.exists(options.out_file + '.results.txt') and os.path.getsize(options.out_file + '.results.txt') > 0:
		for l in ireader.reader(options.out_file + '.results.txt'):
			f = l.split()
			probe_list.append(f[0])
			p_list.append(float(f[1]))
	q_list =  padjust.multiple_testing_correction(p_list)
	
	OUT = open(options.out_file + '.results.txt','w')
	print ("probe\t\tP-value\tadj.Pvalue", file = OUT)
	
	for id,p,q in zip(probe_list, p_list, q_list):
		print (id + '\t' + str(p) + '\t' + str(q), file=OUT)
	OUT.close()
		
if __name__=='__main__':
	main()
