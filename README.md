# SoundWord
See Venv.txt and Requirements.txt for getting dependencies

Create a key.txt file in your repo that has one string for the Rev API key

Text Analyzers:\
    - Classify to Liberal or Conservative\
    - Classify Sentiment\
    - Get Word Frequencies


Website Routing:\
        - [ ] / -> home: (allows user to choose 3 classification options from above)\
        - [ ] /uploadMP3: triggered by button (leads to speech to text and then, backend classification and to /results)\
        - [ ] /results: results of classifying uploaded input (pretty output page using results from backend)\
