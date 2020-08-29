import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
import os
import csv

class EmbodiedEmotions():

    def __init__(self, list_of_emotions):
        self.emotiontypedata = {}
        self.list_of_emotions = list_of_emotions


    def run(self):

        # iterate over every data genre directory
        for genre in os.listdir('data'):
            if not genre.startswith('.'):

                # initialize dic for every genre that maps bodypart counts to emotions for every file
                self.emotiontypedata[genre] = {}

                # iterate over every file
                for filename in os.listdir(f'data/{genre}'):
                    if filename.endswith('.xml'):
                        
                        # initialize dic for every file that maps bodypart counts to emotions
                        self.emotiontypedata[genre][filename] = {}
                        
                        # parse xml-file
                        tree = ET.parse(f'data/{genre}/{filename}')
                        root = tree.getroot()

                        # count bodyparts for every emotion in file and store in dic
                        self.count_bodyparts(root, genre, filename)

        # transform absolute counts to percentage of all bodypart references of certain emotion
        self.to_relative()
        
        # save plot data in csv-file
        self.save_csv()

                        
    def count_bodyparts(self, root, genre, filename):

        # iterate over every emotion in the file
        for emotions in root.iter('emotions'):
            for emotion in emotions.iter('emotion'):
                
                emo = None

                # get reference
                for externalref in emotion.iter('externalRef'):
                    reference = externalref.attrib
                    ref = reference['reference']
                    
                    # retrieve and store emotiontype of emotion
                    if ref.startswith('emotionType'):
                        emo = ref[12:len(ref)]
                        
                        if emo in self.list_of_emotions and not emo in self.emotiontypedata[genre][filename]:
                            self.emotiontypedata[genre][filename][emo] = {}

                    # check for bodypart references and map to right emotion in dic
                    if reference['resource'] == 'heem:bodyParts':

                        if emo in self.emotiontypedata[genre][filename]:
                            if not ref in self.emotiontypedata[genre][filename][emo]:
                                self.emotiontypedata[genre][filename][emo][ref] = 1
                            else:
                                self.emotiontypedata[genre][filename][emo][ref] += 1   
    

    def to_relative(self):

        # calculate every bodypart count as relative count of all bodypart references mapped to an emotion
        for genre in self.emotiontypedata:
            for filename in self.emotiontypedata[genre]:
                for emotion in self.emotiontypedata[genre][filename]:
                    total = sum(self.emotiontypedata[genre][filename][emotion].values())
                    
                    for bodypart in self.emotiontypedata[genre][filename][emotion]:
                        self.emotiontypedata[genre][filename][emotion][bodypart] = self.emotiontypedata[genre][filename][emotion][bodypart] / total


    def save_csv(self):
        
        # saves for all specified emotions the different bodypart relative counts mapped to the right genre and file
        for emotion in self.list_of_emotions:
            with open(f'results/embodied_emotions/{emotion}.csv', 'w') as csv_file:  
                writer = csv.writer(csv_file)
                writer.writerow(['genre', 'filename', 'body part', 'relative count'])                
                for genre in self.emotiontypedata:
                    for filename in self.emotiontypedata[genre]:
                        if emotion in self.emotiontypedata[genre][filename]:
                            for key, value in self.emotiontypedata[genre][filename][emotion].items():
                                writer.writerow([genre, filename, key, value])