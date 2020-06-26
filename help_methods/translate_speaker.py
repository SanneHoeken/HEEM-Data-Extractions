def translate_speaker(speaker):
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