def translate_speaker(speaker):
    """
    This function translates various references to specific speakers in certain plays into a clear reference.
    Specifically for the following plays and speakers:
    1. 'Lucifer' by Vondel
        - Speakers: Belzebab, Lucifer, Gabriël and Michaël
    2. 'De beklaaghelycke dwangh' by Lope de Vegas
        - Speakers: Rozaura, Dionysia, Henrijk and Octavio
    3. 'Achilles en Polyxena' by Hooft
        - Speakers: Achilles, Polyxena, Hector and Pryamus
    4. 'Medea' by Vos
        - Speakers: Medea, Jazon and Kreuza
    """  
    
    if speaker in ['roz', 'rozaura']:
        return 'Rozaura'
    elif speaker in ['dionysia', 'dion', 'dio']:
        return 'Dionysia'
    elif speaker in ['henr', 'hen', 'henrijk', 'hendrijk', 'henriko']:
        return 'Henrijk'
    elif speaker in ['octav', 'octavio']:
        return 'Octavio'

    elif speaker in ['belz', 'belzebab']:
        return 'Belzebab'
    elif speaker in ['lucifer', 'luc']:
        return 'Lucifer'
    elif speaker in ['gab', 'gabriël']:
        return 'Gabriël'
    elif speaker in ['mich', 'michaël']:
        return 'Michaël'

    elif speaker in ['pryamus', 'priamus']:
        return 'Pryamus'
    
    return speaker.capitalize()