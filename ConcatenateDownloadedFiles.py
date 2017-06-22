import os
import glob
import pandas

def concatenate(indir = '/IA_MN_NE',outfile = '\IA_MN_NE\IA_MN_NE_Concatenate.csv'):
    os.chdir(indir)
    fileList = glob.glob("*.csv")
    dfList = []
    for filename in fileList:
        print(filename)
        df = pandas.read_csv(filename)
        dfList.append(df)
    concatDf = pandas.concat(dfList,axis=0)
    concatDf.to_csv(outfile)    

concatenate(indir = '/Volumes/R2D2/Dropbox/PhD_research/Twitter_Mining/Twitter_Streaming_API/IA_MN_NE',
outfile = '/Volumes/R2D2/Dropbox/PhD_research/Twitter_Mining/Twitter_Streaming_API/IA_MN_NE/IA_MN_NE_Concatenate.csv')        