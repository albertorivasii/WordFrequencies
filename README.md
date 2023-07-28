# Housing Market Keyword Analysis
## Skills Used: Python - Pandas, Natural Language Processing (NLP), Seaborn
### Data From: Apartments.com descriptions.  Search limited to top 25 results from the 90007 zip code
Steps to replicate:
1. Download excel file listed, or choose your own data from Apartments.com.  Apartments.com does not allow web scraping, so you have to do this manually
2. import all necessary modules
3. Create DataFrame object and turn description column into list
4. Create tokens and find frequencies
5. Prints out top 8 words by frequency

## Possibilities for Improvement
- Remove company names from coming up in search ("Hive" is one of them)
- Recreate model using ngrams (or any other technique) to account for two-word phrases such as city names ("Los Angeles") or types of rooms (e.g. "living room")
- Increase amount of data from only top 25 listings
- Use SEO rankings to weight words and find keywords as opposed to word frequencies
