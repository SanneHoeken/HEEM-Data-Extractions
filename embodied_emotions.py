import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
import os

class EmbodiedEmotions():

    def __init__(self, list_of_emotions):
        self.emotiontypedata = []
        self.list_of_emotions = list_of_emotions


    def run(self):

        # iterate over every data genre directory
        for genre in os.listdir('data'):
            if not genre.startswith('.'):

                # initialize dic for every genre that maps bodypart counts to emotions
                emotion_bodypart = {}

                # iterate over every file
                for filename in os.listdir(f'data/{genre}'):
                    if filename.endswith('.xml'):
                        
                        # parse xml-file
                        tree = ET.parse(f'data/{genre}/{filename}')
                        root = tree.getroot()

                        # count bodyparts for every emotion in file
                        # store in emotion_bodypart dic
                        self.count_bodyparts(root, emotion_bodypart)

                # transform absolute counts to percentage of all bodypart references of certain emotion
                self.to_percentages(emotion_bodypart)

                # plot for every genre for every emotion a bodypart barplot
                self.plot_bodypartcounts(emotion_bodypart, genre)

                        
    def count_bodyparts(self, root, dic):

        emo = None

        # iterate over every emotion in the file
        for emotions in root.iter('emotions'):
            for emotion in emotions.iter('emotion'):

                # get reference
                for externalref in emotion.iter('externalRef'):
                    reference = externalref.attrib
                    ref = reference['reference']
                    
                    # retrieve and store emotiontype of emotion
                    if ref.startswith('emotionType'):
                        ref = ref[12:len(ref)]
                        if not ref in dic:
                            dic[ref] = {}
                        emo = ref
                    
                    if emo is not None:

                        # check for bodypart references and map to right emotion in dic
                        if reference['resource'] == 'heem:bodyParts':
                            if not ref in dic[emo]:
                                dic[emo][ref] = 1
                            else:
                                dic[emo][ref] += 1   
    

    def to_percentages(self, dic):

        # calculate every bodypart count as percentage of all bodypart references mapped to an emotion
        for emotion in dic:
            total = sum(dic[emotion].values())
            for bodypart in dic[emotion]:
                dic[emotion][bodypart] = dic[emotion][bodypart] / total * 100

    
    def plot_bodypartcounts(self, dic, genre):
        
        # plots for all specified emotions the different bodypart percentages
        for emotion in self.list_of_emotions:
            plt.figure()
            plt.bar(dic[emotion].keys(), dic[emotion].values())
            plt.xlabel('body parts')
            plt.ylabel('percentage of total bodyparts occurences')
            plt.title(f"""Embodiment of {emotion}\nfor 9 plays of genre: {genre}""")
            plt.savefig(f'results/embodied_emotions/{emotion}/{genre}.png')
            plt.close()