import argparse
import os
import arg_ranker
import sys
import pandas as pd

################################################### Decalration #######################################################
print ("\
------------------------------------------------------------------------\n\
Sample_ranking.py evaluates and assigns the risk and priority levels to environmental samples\n\
based on their profile of antibiotic resistant genes (ARGs).\n\
Requirement: python packages (pandas, argparse)\n\
Requirement: a mothertable of the ARG abundance in all your samples \n\
annotated by ARGs-OAP v1.0 (see example/All_sample_cellnumber.txt).\n\
Optimal: a table of the metadata of your samples (see example/All_sample_metadata.txt).\n\
Recommend unit of ARG abundance is copy per cell.\n\n\
The mother table can be obtained by ARGs-OAP v1.0.\n\
\'perl dir_to_ARGs_OAP/database/DB/gene_subtype_type_ppm_16s_cellnumber_differentversion.pl dir_to_your_result/extracted.fa.blast6out.txt \
dir_to_your_result/meta_data_online.txt 25 1e-7 80 output_mothertable_name dir_to_ARGs_OAP/database/DB/other/structure_20160422.list \
dir_to_ARGs_OAP/database/DB/other/SARG-20160422.mod.fasta\'\n\
The mother table to input is output_mothertable_name.normalize_cellnumber.gene.tab\n\n\
Copyright:An-Ni Zhang, Prof. Tong Zhang, University of Hong Kong\n\
Citation:\n\
1. This study\n\
2. Yang Y, Jiang X, Chai B, Ma L, Li B, Zhang A, Cole JR, Tiedje JM, Zhang T: ARGs-OAP: online analysis\
pipeline for antibiotic resistance genes detection from metagenomic data using an integrated \
structured ARG-database. Bioinformatics 2016. (optional: antibiotic resistance database)\n\
Contact caozhichongchong@gmail.com\n\
------------------------------------------------------------------------\n\
")

def main():
    usage = ("usage: arg_ranker -i ARG_in_metagenomes -m metadata_metagenomes ")
    version_string = 'arg_ranker {v}, on Python {pyv[0]}.{pyv[1]}.{pyv[2]}'.format(
        v=arg_ranker.__version__,
        pyv=sys.version_info,
    )
    ############################################ Arguments and declarations ##############################################
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-i',
                        default="example/ARGprofile_example_1.txt", action='store', type=str, metavar='ARGprofile.txt',
                        help="input directory or folder of the mother table containing the ARGs abundance of your samples\n"+
                        "recommend unit of ARG abundance is copy per cell")
    parser.add_argument('-m',
                        default="None", action='store', type=str, metavar='metadata.txt',
                        help="input directory or folder of the table containing the metadata of your samples\n"+
                             "\'None\' for no metadata input")
    parser.add_argument('-o',
                        default="ranking", action='store', type=str, metavar='ranking',
                        help="output directory to store the ranking result")
    ################################################## Definition ########################################################
    args = parser.parse_args()
    Metadata=args.m
    Mothertable=args.i
    ARGranks=os.path.join(os.path.abspath(os.path.dirname(__file__)),
    'data', 'ARG_rank.txt')
    try:
        os.mkdir(args.o)
    except OSError:
        pass
    ################################################### Programme #######################################################
    # set output file
    infolder, infile=os.path.split(args.i)
    fout=open(os.path.join(args.o, infile + '_sample_ranking_results.txt'),'w')


    # input metadata
    MD=dict()
    i = 0
    if Metadata != 'None':
        for lines in open(Metadata,'r'):
            lines=str(lines).split('\r')[0].split('\n')[0]
            # output the lable in output file
            if i == 0:
                fout.write(str(lines)+
                           '\tLevel\tRank_code\tRank_I\tRank_II\tRank_III\tRank_IV\tRank_V\tARGs_unranked\tTotal_abu\n')
            else:
                try:
                    # valid metadata input
                    MD.setdefault(str(lines).split('\t')[0],'\t'.join(str(lines).split('\t')[1:]))
                except KeyError:
                    pass
            i += 1
    else:
        fout.write('Sample\tLevel\tRank_code\tRank_I\tRank_II\tRank_III\tRank_IV' +
                   '\tRank_V\tARGs_unranked\tTotal_abu\n')


    # input ARG ranks
    RK=dict()
    RK_profile={'I':0,'II':1,'III':2,'IV':3,'V':4,
    'MGD_A':5,'MGD_N':5,'WGD':5,'ND':5}
    RKN=[0.0,0.0,0.0,0.0,0.0,0.0]
    for lines in open(ARGranks,'r'):
        lines = str(lines).split('\r')[0].split('\n')[0]
        RK.setdefault(lines.split('\t')[0],lines.split('\t')[-1])
        ###RK.setdefault(lines.split('\t')[0].replace('.','_'), lines.split('\t')[-1])
        Rank_num(lines.split('\t')[-1],RKN, RK_profile)


    # input ARG mothertable
    # transpose the mothertable
    df=pd.read_csv(Mothertable, index_col=None, header=None, skipinitialspace=True,sep='\t')
    df.dropna(axis=0, thresh=2, subset=None, inplace=True)
    df=df.T
    df.to_csv(str(Mothertable)+'.t', header=None, index=None, sep='\t', mode='a')
    i = 0
    for row in df.itertuples(index=True, name='Pandas'):
        if i == 0:
            ARGlist = row[2:]
        else:
            Level_ranking(row[1:],ARGlist,RK,RKN,fout, RK_profile,MD, args.i)
        i+=1
    fout.close()
    print('Finished ranking ARGs\nPlease check your results in ' +
          str(os.path.join(args.o, infile + '_sample_ranking_results.txt')))

################################################## Function ########################################################
def Rank_num(rank,RKN,RK_profile):
    # calculate the nuber of genes in each rank
    try:
        RKN[RK_profile[rank]] += 1.0
    except (KeyError, IndexError, TypeError, ValueError):
        pass


def Level_ranking(row,ARGlist,RK,RKN,fout,RK_profile,MD,inputfile):
    Abu=[0.0,0.0,0.0,0.0,0.0,0.0]
    ARGposition = 1
    # calculate the overall rank-based contribution by each rank
    for ARG in ARGlist:
        rank=RK.get(ARG,'None')
        if rank == 'None':
            pass
            print ('ARGs in mothertable do not match with the ARGs in ARG_rank.txt.\nPlease check '\
                  + ARG + ' in ' + inputfile +'!\n')
        else:
            try:
                Abu[RK_profile[rank]] += float(row[ARGposition])
            except (KeyError, IndexError, TypeError, ValueError):
                pass
        ARGposition += 1
    total_abu_all=sum(Abu)
    total_abu_I_V=sum(Abu[0:5])
    if total_abu_all > 0 :
        Abu1 = []
        Abu2 = []
        for abu in range(0, 6):
            Abu1.append(float(Abu[abu])/ total_abu_all)
        Num_all = sum(RKN[0:6]) #considering un-ranked ARGs
        if total_abu_I_V > 0:
            for abu in range(0,6): #considering un-ranked ARGs
                Abu2.append((Abu[abu]/RKN[abu])/(total_abu_all / Num_all)) #considering un-ranked ARGs
            # Level assign
            if Abu2[0] >= 3.0:
                Level = 1
            elif Abu2[0] >= 0.5:
                Level = 2
            elif Abu2[0] > 0.0:
                Level = 3
            elif Abu2[1] >= 1.0:
                Level = 4
            elif Abu2[1] > 0.0:
                Level = 5
            else:
                Level = 6
        else:
            Level = 7
            Abu2=[0.0,0.0,0.0,0.0,0.0,0.0] #considering un-ranked ARGs
        # output results
        samplename = row[0]
        if MD != {}:
            metadata_sample=MD.get(samplename,'None')
            fout.write(str(samplename) + '\t' + str(metadata_sample) + '\tLevel ' + str(Level) + '\t' +
                       str('-'.join(str("%.1f" % abu) for abu in Abu2)) +
                       '\t' + '\t'.join(str('%.1E' % abu) for abu in Abu1) +
                       '\t' + str('%.1E' % total_abu_all) + '\n')
        else:
            fout.write(str(samplename) + '\tLevel ' + str(Level) + '\t' + str('-'.join(str("%.1f" % abu) for abu in Abu2)) +
                       '\t' + '\t'.join(str('%.1E' % abu) for abu in Abu1) +
                       '\t' + str('%.1E' % total_abu_all) + '\n')


if __name__ == '__main__':
    main()
