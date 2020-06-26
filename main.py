from extract_references import ExtractReferences
from play_sentiment import PlaySentiment

user_input = int(input("""What action do you want to perform on the dataset?
Type '1' for Extracting of emotion references per file and genre
Type '2' for Plotting sentiment course of a certain play for certain speakers \n"""))

if user_input == 1:
    print("Extracting emotion references for every xml-file in ./data ...")
    extractor = ExtractReferences()
    extractor.run()
    print("Results for every file are stored in ./results/per_file")
    print("Results grouped by genre are stored in ./results/per_genre")

elif user_input == 2:
    # TODO: IMPLEMENT USER INPUT FOR PATHS AND SPEAKERS
    data = {'data/vondels_toneel/vond001gysb04_01.xml': ['Gijsbrecht', 'Badeloch'], 'data/spaans/lope001joan01_01.xml': [
        'Joanna', 'Andreas', 'Lodewijck'], 'data/senecaans_scaligeriaans/hoof001achi01_01.xml': ['Achilles', 'Polyxena', 
        'Hector', 'Pryamus'], 'data/gruwel_en_spektakeltoneel/vos_002mede03_01.xml': ['Medea', 'Jazon', 'Kreuza']}
    print("Plotting sentiment course for every specified play for all specified speakers...")
    for path, speakers in data.items():
        sentiment_analysis = PlaySentiment(path, speakers)
        sentiment_analysis.run()
    print("Results are stored in ./results/sentiment_plots")

    