# Housing Market Keyword Analysis
## Skills Used: Python - Pandas, Natural Language Processing (NLP)
### Data From: Apartments.com descriptions.  Search limited to top 25 results from the 90007 zip code
Project during my time at Orion Housing.  Task was to find best keywords to use in rental listing descriptions for the 90007 (USC area) zip code.  I used NLTK's word tokenizer to parse through the top 25 listings for the zip code and found the top 8 I felt were what my supervisor wanted.

## Possibilities for Improvement
- Remove company names from coming up in search ("Hive" is one of them)
- Recreate model using ngrams to account for two-word phrases such as city names ("Los Angeles") or types of rooms (e.g. "living room")
- Increase amount of data from only top 25 listings
- Use SEO rankings to weight words and find keywords as opposed to word frequencies
