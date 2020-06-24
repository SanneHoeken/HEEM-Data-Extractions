import xml.etree.ElementTree as ET
import pandas as pd
import os

class ExtractReferences():

    def __init__(self):
        
        # initialize list for every emotion reference type 
        self.emotiontypedata = []
        self.concepttypedata = []
        self.bodypartdata = []
        self.posnegdata = []
        self.clusterdata = []

        # intialize dic with all data
        self.all_data = {'emotiontypedata': self.emotiontypedata, 'concepttypedata': self.concepttypedata,\
            'bodypartdata': self.bodypartdata, 'posnegdata': self.posnegdata, 'clusterdata': self.clusterdata}


    def run(self):

        # iterate over every data genre directory
        for genre in os.listdir('data'):
            if not genre.startswith('.'):

                # iterate over every file
                for filename in os.listdir(f'data/{genre}'):
                    if filename.endswith('.xml'):
                        
                        # parse xml-file
                        tree = ET.parse(f'data/{genre}/{filename}')
                        root = tree.getroot()

                        # retrieve and store file information
                        author, title, termcount = self.get_file_info(root)

                        # initialize dic for every emotion reference type with file information
                        concepttype = {'filename': filename, 'genre': genre, 'author': author, 'title': title}
                        emotiontype = {'filename': filename, 'genre': genre, 'author': author, 'title': title}
                        bodypart = {'filename': filename, 'genre': genre, 'author': author, 'title': title}
                        posneg = {'filename': filename, 'genre': genre, 'author': author, 'title': title}
                        cluster = {'filename': filename, 'genre': genre, 'author': author, 'title': title}
                        
                        # count all emotion references of all reference types
                        self.count_emotion_references(root, concepttype, emotiontype, bodypart, posneg, cluster)
                        
                        # transform absolute counts to relative counts
                        self.to_relative_counts(termcount, concepttype, emotiontype, bodypart, posneg, cluster)

                        # add dictionaries with counts of every emotion reference to right list 
                        self.emotiontypedata.append(emotiontype)
                        self.concepttypedata.append(concepttype)
                        self.bodypartdata.append(bodypart)
                        self.posnegdata.append(posneg)
                        self.clusterdata.append(cluster)

                        # write results to csv files
                        self.csv_results()


    def get_file_info(self, root):
        
        # retrieve author and title information
        for fileDesc in root.iter('fileDesc'):
            author = fileDesc.get('author')
            title = fileDesc.get('title')
        
        # get termcount of file 
        for terms in root.iter('terms'):
            lastterm = terms[-1].attrib
            lastterm_id = lastterm['id'][1:len(lastterm['id'])]
            termcount = int(lastterm_id)
        
        return author, title, termcount


    def count_emotion_references(self, root, concepttype, emotiontype, bodypart, posneg, cluster):
        
        # count for every emotion which emotion references are used
        # adds every reference as key to right reference type dic
        # updates count in reference type dic's values
        for emotions in root.iter('emotions'):
            for emotion in emotions.iter('emotion'):
                for externalref in emotion.iter('externalRef'):
                    reference = externalref.attrib
                    ref = reference['reference']

                    # count concepttype references
                    if ref.startswith('conceptType'):
                        ref = ref[12:len(ref)]
                        if not ref in concepttype:
                            concepttype[ref] = 1
                        else:
                            concepttype[ref] += 1
                    
                    # count emotiontype references
                    if ref.startswith('emotionType'):
                        ref = ref[12:len(ref)]
                        if not ref in emotiontype:
                            emotiontype[ref] = 1
                        else:
                            emotiontype[ref] += 1
                    
                    # count bodypart references
                    if reference['resource'] == 'heem:bodyParts':
                        if not ref in bodypart:
                            bodypart[ref] = 1
                        else:
                            bodypart[ref] += 1   
                    
                    # count pos/neg references
                    if reference['resource'] == 'heem:posNeg':
                        if not ref in posneg:
                            posneg[ref] = 1
                        else:
                            posneg[ref] += 1  
                    
                    # count cluster references
                    if reference['resource'] == 'heem:clusters':
                        if not ref in cluster:
                            cluster[ref] = 1
                        else:
                            cluster[ref] += 1

    
    def to_relative_counts(self, termcount, concepttype, emotiontype, bodypart, posneg, cluster):
        
        # transform every absolute count in count per 1000 terms
        for dic in [concepttype, emotiontype, bodypart, posneg, cluster]:
            for key, value in dic.items():
                if type(value) == int:
                    dic[key] = (value / termcount * 1000)
            dic['termcount'] = termcount


    def csv_results(self):         

        # initialize pandas dataframe for every list of dicts and write to csv
        for name, list_of_dics in self.all_data.items():
            df = pd.DataFrame(list_of_dics)
            df.to_csv(f"results/per_file/{name}.csv", encoding='utf-8')
            mean_df = df.groupby('genre').mean()
            mean_df.to_csv(f"results/per_genre/{name}.csv", encoding='utf-8')