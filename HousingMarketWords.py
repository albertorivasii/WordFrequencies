#import relevant packages
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk import FreqDist

# call RegexpTokenizer to remove punctuation
tokenizer = RegexpTokenizer(r'[a-z]\w+')

# initiate DF object with description column
apartments_data = pd.read_excel('Housing Descriptions\Apartments_Descriptions.xlsx', usecols='B:C')

# create list of words out of company names column
company_list = apartments_data['Company Name'].values.tolist()

# turn description column into list of descriptions and tokenize
desc_list = apartments_data.description.values.tolist()
tokens_list = [tokenizer.tokenize(d.lower()) for d in desc_list]

# remove stopwords from description
for desc in tokens_list:
    for token in desc:
        if token in stopwords.words('english'):
            desc.remove(token)

# initiate word_freq dict - will be used to hold words and their frequencies
word_freq = {}

# for loop to iterate over each desc
for desc in tokens_list:
    frequency = FreqDist(desc)
    for word in desc:
        if len(word) < 4:
            continue
        elif word not in word_freq.keys():
            word_freq[word] = frequency[word]
        else:
            word_freq[word] += frequency[word]

total_words = sum(word_freq.values())
for w in word_freq:
    word_freq[w] = "{:.2%}".format((word_freq[w] / total_words))

word_freq_sorted = sorted(word_freq.items(), key=lambda x:x[1], reverse=True)
print("List of words and their frequency:")
for i in range(8):
    print(word_freq_sorted[i][0] + " - " + str(word_freq_sorted[i][1]).format())
