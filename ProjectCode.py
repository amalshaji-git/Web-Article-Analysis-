# %% [markdown]
# Load and Display Excel Data

# %%
import pandas as pd
data1= pd.read_excel(r"C:\Users\amals\Desktop\project\Input.xlsx")
pd.set_option('display.max_columns', None)
data1

# %% [markdown]
# This script loads data from an Excel file named Input.xlsx using the pandas library. It sets the display option to show all columns, ensuring that no columns are hidden when viewing the DataFrame. The loaded data is then displayed in its entirety for easy inspection and analysis.

# %% [markdown]
# Load and Display Output Data Structure

# %%
import pandas as pd
data2= pd.read_excel(r"C:\Users\amals\Desktop\project\Output Data Structure.xlsx")
pd.set_option('display.max_columns', None)
data2

# %% [markdown]
# This script loads data from an Excel file named Output Data Structure.xlsx using the pandas library. It sets the display option to show all columns, ensuring that no columns are hidden when viewing the DataFrame. The loaded data is then displayed in its entirety for review, allowing for easy verification of the expected output structure for the project.

# %% [markdown]
# Web Article Extractor

# %%
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

input_path = r"C:\Users\amals\Desktop\project\Input.xlsx"
data = pd.read_excel(input_path)

# Function to extract article title and body using BeautifulSoup
def extract_article(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract the title
            title = soup.find('title').get_text()
            
            # Extract the article body (assuming it's under <p> tags)
            article_text = ' '.join([p.get_text() for p in soup.find_all('p')])
            
            return title, article_text
        else:
            return None, None
    except Exception as e:
        print(f"Error extracting {url}: {e}")
        return None, None

# Create a folder to save the extracted articles
output_folder = r"C:\Users\amals\Desktop\project\extracted_articles"  # Adjust this path
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each row in the pandas DataFrame and extract the article
for index, row in data.iterrows():
    url_id = row['URL_ID']  # Get URL_ID from the Excel file
    url = row['URL']        # Get URL from the Excel file
    
    # Extract article using BeautifulSoup
    title, article_text = extract_article(url)
    
    # If extraction is successful, save the data
    if title and article_text:
        content = f"Title: {title}\n\n{article_text}"  # Combine title and article text
        
        # Save the content to a text file named with the URL_ID
        file_path = os.path.join(output_folder, f"{url_id}.txt")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"Article {url_id} saved to {file_path}")
    else:
        print(f"Failed to extract article {url_id} from {url}")


# %% [markdown]
# This script extracts article titles and bodies from a list of URLs provided in an Excel file (Input.xlsx). It uses the requests library to fetch webpage content and BeautifulSoup to parse the HTML. The extracted titles and article texts are saved as text files in a designated output folder named after the article's URL_ID. This process ensures that each article is stored in a structured format, ready for further analysis or processing.

# %% [markdown]
# Article Text Analysis and Output Generation

# %%
import os
import pandas as pd
from textblob import TextBlob
import re
import nltk
from nltk.corpus import cmudict

# Path to extracted articles folder
extracted_articles_path = r"C:\Users\amals\Desktop\project\extracted_articles"

# Load the output structure Excel file (for structure/order reference)
output_structure_path = r"C:\Users\amals\Desktop\project\Output Data Structure.xlsx"
output_data_structure = pd.read_excel(output_structure_path)

# Dictionary to store syllables for complex word calculation
d = cmudict.dict()

# Helper function to count syllables in a word
def syllable_count(word):
    word = word.lower()
    if word in d:
        return max([len([y for y in x if y[-1].isdigit()]) for x in d[word]])
    else:
        return 1  # Default to 1 syllable if not found

# Check if a word is complex (3 or more syllables)
def is_complex(word):
    return syllable_count(word) >= 3

# Function to perform analysis for each article
def analyze_article(text):
    # TextBlob for sentiment analysis
    blob = TextBlob(text)
    
    # 1. Positive Score: Use your own logic or predefined sentiment lexicons
    positive_score = sum(1 for word in blob.words if TextBlob(word).sentiment.polarity > 0)
    
    # 2. Negative Score: Similar logic as positive score
    negative_score = sum(1 for word in blob.words if TextBlob(word).sentiment.polarity < 0)
    
    # 3. Polarity Score
    polarity_score = blob.sentiment.polarity
    
    # 4. Subjectivity Score
    subjectivity_score = blob.sentiment.subjectivity
    
    # 5. Average Sentence Length
    sentences = blob.sentences
    avg_sentence_length = sum(len(sentence.words) for sentence in sentences) / len(sentences)
    
    # 6. Percentage of Complex Words
    words = blob.words
    complex_words_count = sum(1 for word in words if is_complex(word))
    percentage_of_complex_words = (complex_words_count / len(words)) * 100
    
    # 7. Average Number of Words per Sentence
    avg_words_per_sentence = len(words) / len(sentences)
    
    # 8. Complex Word Count
    complex_word_count = complex_words_count
    
    # 9. Word Count
    word_count = len(words)
    
    # 10. Syllables per Word
    total_syllables = sum(syllable_count(word) for word in words)
    syllables_per_word = total_syllables / len(words)
    
    # 11. Personal Pronouns (using regex to find occurrences of personal pronouns)
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.I))
    
    # 12. Average Word Length
    avg_word_length = sum(len(word) for word in words) / len(words)
    
    # Return results in the specified order
    return [positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length, 
            percentage_of_complex_words, avg_words_per_sentence, complex_word_count, word_count, 
            syllables_per_word, personal_pronouns, avg_word_length]

# Create a list to store the results for all articles
results = []

# Loop through each article file
for file_name in os.listdir(extracted_articles_path):
    if file_name.endswith(".txt"):
        url_id = file_name.split('.')[0]  # Get URL_ID from the file name
        with open(os.path.join(extracted_articles_path, file_name), 'r', encoding='utf-8') as file:
            text = file.read()
            # Perform analysis on the article text
            analysis_result = analyze_article(text)
            # Append the URL_ID and analysis results to the list
            results.append([url_id] + analysis_result)

# Convert the results to a pandas DataFrame
columns = ['URL_ID', 'Positive Score', 'Negative Score', 'Polarity Score', 'Subjectivity Score', 
           'Avg Sentence Length', 'Percentage of Complex Words', 'Avg Number of Words per Sentence', 
           'Complex Word Count', 'Word Count', 'Syllables per Word', 'Personal Pronouns', 'Avg Word Length']

output_df = pd.DataFrame(results, columns=columns)

# Save the DataFrame to a new Excel file in the same order as "Output Data Structure.xlsx"
output_df.to_excel(r"C:\Users\amals\Desktop\project\final_output.xlsx", index=False)

print("Text analysis completed and saved in final_output.xlsx")


# %% [markdown]
# This script analyzes text from extracted articles stored in a specified folder. It performs various analyses, including sentiment scoring, average sentence length, complex word percentage, and more. The results are compiled into a structured DataFrame and saved as an Excel file named final_output.xlsx. The output follows the specified order defined in the "Output Data Structure.xlsx" file, ensuring compatibility for further analysis or reporting.

# %% [markdown]
# Project Documentation for Text Analysis

# %%
import pandas as pd

# Load the CSV file
data = pd.read_excel(r"C:\Users\amals\Desktop\project\Output Data Structure.xlsx")

data['AVG_POSITIVE_SCORE'] = data['POSITIVE SCORE'].mean()
data['AVG_NEGATIVE_SCORE'] = data['NEGATIVE SCORE'].mean()
# Save the updated DataFrame to a new CSV file
data.to_csv(' analysis_results.csv', index=False)


# %% [markdown]
# Code to Extract and Combine Articles from URLs

# %%
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

# Load the data
input_file_path = r"C:\Users\amals\Desktop\project\Input.xlsx"
df = pd.read_excel(input_file_path)

# Specify the directory and file path
combined_folder_path = r'C:\Users\amals\Desktop\project\combined_file'
combined_file_path = os.path.join(combined_folder_path, 'combined_articles.txt')

# Create the combined folder if it doesn't exist
os.makedirs(combined_folder_path, exist_ok=True)

# Function to extract text from a URL
def extract_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Open the combined file for writing
with open(combined_file_path, 'w', encoding='utf-8') as combined_file:
    # Iterate through the DataFrame and extract text from each URL
    for index, row in df.iterrows():
        url = row['URL']
        article_text = extract_text(url)
        
        if article_text:
            # Write the URL_ID and the article text into the combined file
            combined_file.write(f"URL_ID: {row['URL_ID']}\n")
            combined_file.write(article_text)
            combined_file.write("\n\n")  # Separate articles with a blank line
            
            print(f"Article from {url} saved to combined file.")
        else:
            print(f"Failed to extract article from {url}")

print(f"All articles combined into: {combined_file_path}")


# %% [markdown]
# This script extracts text from articles provided in a specified Excel file. It retrieves content from each URL listed in the input file, processes the text, and combines it into a single text file named combined_articles.txt. The output file is stored in a designated folder named "combined_file." Error handling is included to manage issues during the web scraping process


