from emotion_references import EmotionReferences
from sentiment_visualisation import SentimentVisualisation
from embodied_emotions import EmbodiedEmotions


user_input = int(input("""What action do you want to perform on the dataset?
Type '1' for Extracting of emotion references per file and genre
Type '2' for Plotting embodiment of certain emotion(s) per genre 
Type '3' for Plotting sentiment visualisation of certain plays for certain speakers\n"""))

if user_input == 1:
    print("Extracting emotion references for every xml-file in ./data ...")
    extractor = EmotionReferences()
    extractor.run()
    print("Results for every file are stored in ./results/reference_frequencies/per_file")
    print("Results grouped by genre are stored in ./results/reference_frequences/per_genre")


elif user_input == 2:
    print("Plotting per genre the embodiment of the emotions: love, desire, honor, vindictiveness, fear, compassion and sadness...")
    embodiment_analysis = EmbodiedEmotions(['love', 'desire', 'honor', 'vindictiveness', 'fear', 'compassion', 'sadness'])
    embodiment_analysis.run()
    print("Results are stored in ./results/embodied_emotions")


elif user_input == 3:
    data = {'data/vondels_toneel/vond001luci01_01.xml': ['Belzebab', 'Lucifer', 'Gabriël', 'Michaël'], 'data/spaans/lope001bekl02_01.xml': [
        'Rozaura', 'Dionysia', 'Henrijk', 'Octavio'], 'data/senecaans_scaligeriaans/hoof001achi01_01.xml': ['Achilles', 'Polyxena', 
        'Hector', 'Pryamus'], 'data/gruwel_en_spektakeltoneel/vos_002mede03_01.xml': ['Medea', 'Jazon', 'Kreuza'], 'data/vondels_toneel/vond001gysb04_01.xml': 
        ['Gijsbrecht', 'Badeloch'], 'data/spaans/lope001joan01_01.xml': ['Joanna', 'Andreas', 'Lodewijck']}
    print("""Plotting sentiment visualisation for:
    1. 'Lucifer' by Vondel
        - Speakers: Belzebab, Lucifer, Gabriël and Michaël
    2. 'De beklaaghelycke dwangh' by Lope de Vega
        - Speakers: Rozaura, Dionysia, Henrijk and Octavio
    3. 'Achilles en Polyxena' by Hooft
        - Speakers: Achilles, Polyxena, Hector and Pryamus
    4. 'Medea' by Vos
        - Speakers: Medea, Jazon and Kreuza
    5. 'Joanna koninging van Napels' by Lope de Vega
        - Speakers: Joanna, Andreas and Lodewijck
    6. 'Gysbreght van Aemstel' by Vondel
        - Speakers: Gijsbrecht and Badeloch""")
    for path, speakers in data.items():
        sentiment_analysis = SentimentVisualisation(path, speakers)
        sentiment_analysis.run()
    print("Results are stored in ./results/sentiment_plots")
