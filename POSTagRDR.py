#!/usr/bin/python
# -*- coding: utf-8 -*-
import tamil
import nltk
from tamil import utf8
import nltk.data
import re
import os
import Utility
from Utility import Utils
import pSCRDRtagger
from pSCRDRtagger import RDRPOSTagger as rd
rdr = rd.RDRPOSTagger()
nltk.download('punkt')
from nltk.tokenize import sent_tokenize 

# Load the POS tagging model for Tamil
trainedmodel = os.path.join(os.path.dirname(__file__), 'Resources/TrainedModel.RDR')
rdr.constructSCRDRtreeFromRDRfile(trainedmodel)

# Load the lexicon for Tamil
generatedlexicon = os.path.join(os.path.dirname(__file__), 'Resources/GeneratedLexicon.DICT')
#DICT =rdr.readDictionary(generatedlexicon)
DICT =Utils.readDictionary(generatedlexicon)
# Load the file that contains the text to be tagged

f = open('D:/suba/Tamil Computing  Research/data/input.txt', "r", encoding="utf-8")
targetfile = open('D:/suba/Tamil Computing  Research/data/output.txt', 'wt')
tobetagged=f.read()
f.close()

seg=sent_tokenize(tobetagged)
#print(seg)

# Read sentences one-by-one
for sent in seg:
    # Strip all double quotes - POS tagger is unable to handle these
    sent = re.sub(r'"', '', sent)
    # Strip all single quotes - POS tagger is unable to handle these
    sent = re.sub(r'\'', '', sent)
    # Change all ! to dot - POS tagger is unable to handle !
    sent = re.sub(r'!', '.', sent)
    # Change all ; to , - POS tagger is unable to handle ;
    sent = re.sub(r';', ',', sent)
    # Change all : to , - POS tagger is unable to handle :
    sent = re.sub(r':', ',', sent)
    # Add a space in front of the sentence ending dot - tagging is done based on whitespace
    sent = re.sub(r'\.\Z', ' .', sent)
    # Add a space in front of the sentence ending ? - tagging is done based on whitespace
    sent = re.sub(r'\?', ' ?', sent)
    # Add a space in front of the paragraph ending dot - tagging is done based on whitespace
    sent = re.sub(r'\.\n', ' .', sent)
    # Add a space in front of every comma - tagging is done based on whitespace
    sent = re.sub(r',', ' ,', sent)
    print(sent)
    # Tag the sentence and write it to the file
   # tagged = rdr.tagRawSentence(DICT, sent.encode('utf8'))
    tagged = rdr.tagRawSentence(DICT,sent)
    print("tagged data ready")
    print (tagged)
   

