import xml.etree.ElementTree as ET
import re

def split_coster():
    """
    This function takes the original 'cost001rako01_01.xml' file from the HEEM dataset. This file contains data of multiple plays of Coster.
    This function creates 4 new files, each with a selected control range from the original file that contains the 
    data for one of Coster's multiple plays. Specifically the plays: Ithys, Iphigenia, Isabella and Polyxena; 
    respectively stored as 'cost001rako01_ithys.xml', 'cost001rako01_iphigenia.xml', 'cost001rako01_isabella.xml' 
    and 'cost001rako01_polyxena.xml'.
    """

    coster = {'ithys':{'filename':'cost001rako01_ithys.xml', 'termids': (23557, 43135), 'phrasenumbers': (3883, 6888)},\
        'iphigenia':{'filename': 'cost001rako01_iphigenia.xml', 'termids': (61820, 81068), 'phrasenumbers': (10271, 13570)},\
            'isabella':{'filename': 'cost001rako01_isabella.xml', 'termids': (81069, 103626), 'phrasenumbers': (13704, 16720)},\
                'polyxena':{'filename': 'cost001rako01_polyxena.xml', 'termids': (103627, 127514), 'phrasenumbers': (16818, 19810)}}


    for play in coster:
        tree = ET.parse('cost001rako01_01.xml')
        root = tree.getroot()

        n = 2
        while(True):
            if n < 1:
                break
            else:
                n = 0
            for text in root.iter('text'):  
                for wf in text.iter('wf'):
                    wf_att = wf.attrib
                    wf_id = wf_att['id']
                    phrasenumber = re.search(r"[.]\d+[.]s[.]", wf_id)
                    phrasenumber = phrasenumber.group(0)
                    phrasenumber = int(phrasenumber[1:-3])
                    if phrasenumber < coster[play]['phrasenumbers'][0] or phrasenumber > coster[play]['phrasenumbers'][1]:
                        text.remove(wf)
                        n += 1

        n = 2
        while(True):
            if n < 1:
                break
            else:
                n = 0
            for terms in root.iter('terms'):
                for term in terms.iter('term'):
                    term_att = term.attrib
                    term_id = int(term_att['id'][1:len(term_att['id'])])
                    if term_id < coster[play]['termids'][0] or term_id > coster[play]['termids'][1]:
                        terms.remove(term)
                        n += 1

        n = 2
        while(True):
            if n < 1:
                break
            else:
                n = 0
            for emotions in root.iter('emotions'):
                for emotion in emotions.iter('emotion'):
                    targetids = []
                    for span in emotion.iter('span'):
                        for target in span.iter('target'):
                            target_att = target.attrib
                            target_id = int(target_att['id'][1:len(target_att['id'])])
                            targetids.append(target_id)
                    if all(item < coster[play]['termids'][0] for item in targetids) == True or all(item > coster[play]['termids'][1] for item in targetids) == True:
                        emotions.remove(emotion)
                        n += 1

        tree.write(coster[play]['filename'])