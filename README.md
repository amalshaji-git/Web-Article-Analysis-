# Web Article Analysis Project

## Project Overview
This Web Article Analysis project focuses on extracting, analyzing, and generating insights from a collection of web articles. The project involves scraping article text from URLs, performing textual analysis to compute metrics such as sentiment scores, polarity, subjectivity, word count, and complexity. The resulting insights can help understand article tone, readability, and sentiment patterns.

## Project Objectives
- Extract article content from a list of URLs.
- Analyze text to compute variables such as positive/negative score, polarity, subjectivity, and other readability metrics.
- Output the analysis in a structured format for further exploration and interpretation.

## Project Structure
The project is organized as follows:
- **data/**: Contains input data, such as URLs and identifiers.
- **notebooks/**: Jupyter notebooks for extraction, analysis, and visualization of results.
- **scripts/**: Python scripts for data extraction, analysis, and processing.
- **output/**: Final analysis results, including structured data with computed metrics.

## Key Features and Steps
1. **Data Extraction**:
   - Read URLs from a CSV file and extract article content.
   - Parse and clean article text to remove unwanted characters, HTML tags, and irrelevant data.
   - Save the extracted content in text format for analysis.

2. **Text Analysis**:
   - **Sentiment Analysis**: Compute positive and negative scores, polarity score, and subjectivity score.
   - **Readability Metrics**: Calculate metrics such as average sentence length, percentage of complex words, and syllables per word.
   - **Word-Level Analysis**: Calculate word count, complex word count, and average word length.
   - **Personal Pronouns**: Identify and count the use of personal pronouns to gauge article personalization.
   - **Other Metrics**: Generate the percentage of complex words and average number of words per sentence to assess readability.

3. **Output Generation**:
   - Compile results into a structured format (CSV or Excel) for easy access and interpretation.
   - Ensure that output data matches the expected format as outlined in the project’s output structure.

## Technology Stack
- **Programming Language**: Python
- **Libraries**:
  - Data Manipulation: `Pandas`
  - Text Extraction: `BeautifulSoup`, `requests`
  - Text Analysis: `TextBlob`, `NLTK`
  - Excel/CSV Handling: `openpyxl`

## Results
- Computed sentiment and readability metrics for each article, providing a quantitative measure of tone, complexity, and engagement.
- Structured the output data in a CSV/Excel format for ease of interpretation and future analysis.
- The analysis can inform content creators and analysts about trends in article sentiment, language complexity, and readability.

## Challenges
- Handling diverse HTML structures across articles and inconsistent formatting.
- Optimizing the accuracy of sentiment and complexity metrics across different article topics.
- Managing large data volumes and automating the extraction and processing pipeline for efficiency.

## Conclusion
The Web Article Analysis Project provides a comprehensive approach to extracting and analyzing online article content. By systematically computing various sentiment and readability metrics, this project offers valuable insights that can help with content strategy, customer engagement, and linguistic analysis.

## How to Run the Project
1. Clone the repository.
2. Install the required packages from `requirements.txt`.
3. Run the extraction script to retrieve article content from URLs.
4. Execute the analysis scripts to compute metrics and generate the output file.

## Contact
For any questions or further information, please reach out to me at [your email address].

