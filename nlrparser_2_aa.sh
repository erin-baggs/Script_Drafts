#!/bin/bash -e
#SBATCH -p  tgac-medium # partition (queue)
#SBATCH --mem 24G # memory pool for all cores
#SBATCH -J nlrparser
#SBATCH -o slurm.%N.%j.out # STDOUT
#SBATCH -e slurm.%N.%j.err # STDERR
#SBATCH --mail-type=END,FAIL # notifications for job done & fail
#SBATCH --mail-user=baggse@nbi.ac.uk # send-to address

#Path to source java which tool works on 
source jre-6.45
source meme-4.10.1_4

#Command for running tool 
input=$1 
output=$input.aa_nlrparser


mast /tgac/workarea/group-tg/tools/NLRP/meme.xml $1 -o $1.mast_out -ev 1000
java -jar /tgac/workarea/group-tg/tools/NLRP/old_version/NLR-Parser.jar -a $1 -i $1.mast_out/mast.xml -o $output.tsv #-g $output.gff 
rm -rf $1.mast_out



#java -jar /tgac/workarea/group-tg/tools/NLRP/NLR-Parser2.jar -x /tgac/workarea/group-tg/tools/NLRP/meme.xml -y /tgac/software/testing/meme/4.10.1_4/x86_64/bin/mast -i $1 -o $output.tsv -g $output.gff -b $output.bed -c $output.xml 
#/tgac/workarea/group-tg/projects/erinphd/tools/nlrparser_old/NLR-Parser-master/src/coreClasses/NLRParser.java
#-x /tgac/workarea/group-tg/tools/NLRP/meme.xml -y /tgac/software/testing/meme/4.10.1_4/x86_64/bin/mast
