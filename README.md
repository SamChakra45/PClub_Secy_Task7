# PClub_Secy_Task7
Clickbait Generation using LSTM Tensorflow
For this given problem, I have used a tensorflow LSTM model to generate text that closely resembles clickbaits from the training data provided

I have a total number of 8 layers comprising of an input layer, embedding layer, dropout layer, LSTM, bidirectional Lstm, a pooling layer and two dense layers. Total of 520 Lstm units, embedding size is 124, bidirectional Lstm units 340 and 1024 dense units. The model takes in the padded and tokenized sequence of the clickbait sentences. The last word of the sentence is kept as target value and the rest of the sentence forms the input. The maximum length upon investigation was 26 words for a sentence so the input layer has 25 nodes.

Upon training using kaggle, the model achieved an accuracy of 71.26 percent after 100 epochs which is par for NLP models. Furthermore, the mmodel was trained on only the first 4471 clickbaits as memory was constrained and doing several batches was very long for the resources at my disposal. The entire dataset had 16001 clickbaits and 15999 non clickbaits. The model file is included as a google drive link is approximately 213MB in size.(https://drive.google.com/file/d/1yF7q7xcXPrkJ0bkxmjp-mrmXxcFGZzrG/view?usp=sharing)

The generation of a clickbait using the model requires the provision of a seed text and the number of words, which if not provided results in a random number between 5 and 15 being selected as the word count. I have provided the API to call the model and also to test the model. The API could not be perfected as a website (mostly due to my own inexperience of web development) and hence, the model remains open to modifications and betterment. A sample API request is also included to help understand the procedure and parameters required for the call.

I plan on including the resources that I used for development at a later time which were a great help to me

Some sample outputs and their respective prompts are:

world's most simple clothing line ideas to get you through the cold
"world's most" ; 10

animal rights abrams broke his back trying to invent fake advice after long beers
"animal rights" ; 12
