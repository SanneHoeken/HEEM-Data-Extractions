import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
import csv
from help_methods.translate_speaker import translate_speaker

class SentimentVisualisation():

    def __init__(self, path, speakers):
        self.filename = path
        self.speakers = speakers
        self.play = {}
        self.speaker_list = []
        self.text = {}
        self.title = None
    
    def run(self):
        
        # parse xml file
        tree = ET.parse(self.filename)
        root = tree.getroot()

        # retrieve and store title of file
        for fileDesc in root.iter('fileDesc'):
            self.title = fileDesc.get('title')

        # load dictionary of dictionaries
        # for every speaker, for every turn, for every term id, a sentiment value
        self.load_play(root)

        # change sentiment value to right value for every term id
        self.load_sentiment(root)

        # calculate for every turn the mean sentiment
        # replace seperate term ids with sentiment values to a single mean sentiment value
        self.set_averages()

        # plot sentiment against turns for every speaker
        self.plot_sentiment()

        # plot trendline 
        self.plot_trend()

        # clean text dic and store in csv
        for turn in self.text:
            self.text[turn] = ' '.join(self.text[turn])
        
        self.to_csv()


    def load_play(self, root):

        speaker = None
        turn = 0

        # iterate over every term in the file
        for terms in root.iter('terms'):
            for term in terms.iter('term'):

                # get term id
                term_att = term.attrib
                term_id = int(term_att['id'][1:len(term_att['id'])])
                
                # get lemma connected to term
                lemma = term_att['lemma']

                # get meta information about term
                for span in term.iter('span'):
                    for target in span.iter('target'):
                        target_att = target.attrib
                        target_id = target_att['id']

                        # append lemma to speaker_list if meta data indicates start of turn
                        # start of turns can consist of multiple lemma's that together form the name of the speaker
                        if "stage" in target_id:
                            if lemma.isalpha() == True:
                                self.speaker_list.append(lemma.lower())
                        elif "speaker" in target_id:
                            if lemma.isalpha() == True:
                                self.speaker_list.append(lemma.lower())
                         
                        # else add target id to right turn
                        else:
                            # store name of speaker in variable 
                            if len(self.speaker_list) > 0:
                                if self.speaker_list[0] == 'prins':
                                    speaker = translate_speaker(self.speaker_list[1])
                                else:
                                    speaker = translate_speaker(self.speaker_list[0])
                                
                                # empty speaker_list
                                self.speaker_list = []
                            
                            # append speaker to play dic 
                            if not speaker in self.play:
                                self.play[speaker] = {}
                            
                            # append turn to speaker dic
                            if not turn in self.play[speaker]:
                                turn += 1
                                self.play[speaker][turn] = {}

                                # append turn to text dic
                                self.text[turn] = []
                                
                                # set begin and end of turn seperate in dic and set values to 0
                                self.play[speaker][turn+0.9] = 0
                                self.play[speaker][turn-0.1] = 0
                            
                            # add term id to turn dic and set sentiment value to zero
                            self.play[speaker][turn][term_id] = 0
                            
                            # add lemma to list of lemmas mapped to the current turn
                            self.text[turn].append(lemma)
    

    def load_sentiment(self, root):

        # iterate over every emotion in the file
        for emotions in root.iter('emotions'):
            for emotion in emotions.iter('emotion'):
                ref = None
                
                # get reference
                for externalref in emotion.iter('externalRef'):
                    reference = externalref.attrib

                    # store reference if reference type is pos/neg
                    if reference['resource'] == 'heem:posNeg':
                        ref = reference['reference']    
                
                # get target id's connected to emotion
                for span in emotion.iter('span'):
                    for target in span.iter('target'):
                        target_att = target.attrib
                        target_id = int(target_att['id'][1:len(target_att['id'])])

                        # changes sentiment value of target id's in play dictionary
                        for speaker in self.play.keys():
                            for target_ids in self.play[speaker].values():
                                if type(target_ids) is dict:
                                    if target_id in target_ids:

                                        # change sentiment score to 1 if reference is positive
                                        if ref == 'positive':
                                            target_ids[target_id] = 1
                                        
                                        # change sentiment score to -1 if reference is negative
                                        elif ref == 'negative':
                                            target_ids[target_id] = -1
    

    def set_averages(self):
        
        # iterate over every turn
        for speaker in self.play.keys():
            for turn in self.play[speaker].keys():

                # divide sum of sentiment values by amount of terms in term
                if type(self.play[speaker][turn]) is dict:
                    terms = len(self.play[speaker][turn])
                    sentiment_sum = sum([term_id for term_id in self.play[speaker][turn].values()])
                    average = sentiment_sum / float(terms)
                
                    # set average as value to right turn as key
                    self.play[speaker][turn] = average


    def plot_sentiment(self):

        plt.figure()

        # plot for every speaker the sentiment values against the turns
        for speaker in self.speakers:
            tuplelist = sorted([(turn, value) for turn, value in self.play[speaker].items()])
            xdata = [turn for turn, value in tuplelist]
            ydata = [value for turn, value in tuplelist]
            plt.plot(xdata, ydata, label=speaker)

            # set axis labels and plot title
            plt.xlabel('speaker turns')
            plt.ylabel('positivity/negativity')
            plt.title(self.title)

        plt.legend()
        plt.savefig(f'results/sentiment_plots/{self.title}.png')
        plt.close()


    def plot_trend(self):

        plt.figure()

        # plot for every speaker the sentiment values against the turns
        for speaker in self.speakers:
            tuplelist = sorted([(turn, value) for turn, value in self.play[speaker].items()])
            xdata = [turn for turn, value in tuplelist]
            ydata = [value for turn, value in tuplelist]

            # plot trendline 
            zdata = np.polyfit(xdata, ydata, 1)
            trend = np.poly1d(zdata)
            plt.plot(xdata,trend(xdata), label=f'{speaker}')

            # set axis labels and plot title
            plt.xlabel('speaker turns')
            plt.ylabel('positivity/negativity')
            plt.title(self.title)

        plt.legend()
        plt.savefig(f'results/sentiment_plots/{self.title}_trend.png')
        plt.close()

    
    def to_csv(self):

        # save text mapped to right turn number in csv-file
        with open(f'results/sentiment_plots/{self.title}_text.csv', 'w') as csv_file:  
            writer = csv.writer(csv_file)
            writer.writerow(['turn', 'text'])                
            for turn, text in self.text.items():
                writer.writerow([turn, text])


