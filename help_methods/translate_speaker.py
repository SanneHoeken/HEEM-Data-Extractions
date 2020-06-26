def translate_speaker(speaker):
    """
    This function translates various references to specific speakers in certain plays into a clear reference.
    Specifically for the following plays and speakers:
    1. 'Gysbreght van Aemstel' by Vondel
        - Speakers: Gijsbrecht and Badeloch
    2. 'Joanna koninging van Napels' by Lope de Vega
        - Speakers: Joanna, Andreas and Lodewijck
    3. 'Achilles en Polyxena' by Hooft
        - Speakers: Achilles, Polyxena, Hector and Pryamus
    4. 'Medea' by Vos
        - Speakers: Medea, Jazon and Kreuza
    """  
    
    if speaker in ['hecvba', 'hecuba']:
        return 'Hecuba'
    elif speaker in ['polydorvs', 'polidorvs', 'polydoor']:
        return 'Polydorus'

    elif speaker in ['and', 'andreas', 'ans']:
        return 'Andreas'
    elif speaker in ['lodewijck', 'lod', 'lo', 'lode']:
        return 'Lodewijck'
    elif speaker in ['koningin', 'ko']:
        return 'Joanna'

    elif speaker in ['gijsbrecht', 'gysbreght', 'gysbrecht', 'gys']:
        return 'Gijsbrecht'
    elif speaker in ['ba', 'badeloch']:
        return 'Badeloch'

    elif speaker in ['pryamus', 'priamus']:
        return 'Pryamus'
    
    return speaker.capitalize()