import xml.etree.ElementTree as ET

def identify_speakers(filename):
    """
    This function takes a filename and returns all speaker references in it
    """

    speakers = set()
    tmp_speaker = []

    # parse file
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # iterate over every term
    for terms in root.iter('terms'):
        for term in terms.iter('term'):

            # store lemma in term
            term_att = term.attrib
            lemma = term_att['lemma']

            # get meta information of lemma
            for span in term.iter('span'):
                for target in span.iter('target'):
                    target_att = target.attrib
                    target_id = target_att['id']

                    # append lemma to temporary speaker variable if meta info indicates speaker reference
                    if "stage" in target_id and lemma.isalpha() == True:
                        tmp_speaker.append(lemma.lower())
                    elif "speaker" in target_id and lemma.isalpha() == True:
                        tmp_speaker.append(lemma.lower())
                    
                    # store speaker if speaker reference has passed
                    else:
                        if len(tmp_speaker) > 0:
                            speaker = tuple(tmp_speaker[:])
                            speakers.add(speaker)

                            # clear temporary speaker variable
                            tmp_speaker = []
    
    return speakers
    