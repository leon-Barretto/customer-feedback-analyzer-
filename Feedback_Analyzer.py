"""
Customer Feeback anaylzer
Name: Leon Barretto
Course: MGT-3850-D1/D2-Summer 2025 - Assignment 1



SITUATION:  
A small business receives a steady flow of customer feedback through surveys, online reviews, and service forms.  
Manually organizing and interpreting this feedback is time-consuming, and without a consistent method,  
important patterns—such as recurring complaints or praise—can be overlooked.

TASK:  
Develop a Python-based solution that automatically analyzes and categorizes each customer comment  
by feedback type (positive, negative, neutral). The goal is to provide the business with a clearer picture  
of how customers feel and what areas may need improvement.

ACTION:  
I created a Python program that automatically classifies feedback using keyword-based analysis.  
The program uses `requests` and `BeautifulSoup` to scrape real-world positive and negative word lists  
from a public website. It processes a list of customer comments and checks each one against these keywords  
to determine its tone. The feedback is grouped using a dictionary structure, and a pie chart is generated  
with `matplotlib` to visually summarize the distribution of feedback types.

RESULT:  
The final solution provides a quick and accurate way for the business to assess customer feedback trends.  
By automating the analysis and visualizing the results, the business can make informed decisions faster,  
identify areas for improvement, and better respond to customer concerns.


Key Concepts Applied:
- Lists: Used to store keywords and customer feedback
- Dictionaries: Used to group classified results by feedback category
- Functions: `get_keywords()` for scraping, `analyze_comment()` for classification
- Flow Control: Loops and conditional logic to match words and tally feedback
- API Integration: Scrapes real-time keyword lists using `requests` and `BeautifulSoup`
- Data Visualization: Generates a pie chart using `matplotlib`


How to Run the Program:
1. Install required packages if not already installed:
   pip/pip3 install beautifulsoup4, lxml, matplotlib

2. Save the file as `feedback_analyzer.py`

3. Run the program in your terminal or IDE:
   python feedback_analyzer.py

4. The categorized results will print in the terminal, and a pie chart  
   summarizing the feedback will be saved as 'feedback_chart.png' in your directory.

"""

import matplotlib.pyplot as plt 
import requests
from bs4 import BeautifulSoup

# Scraper function

"""
Retrieve a list of words from the specified URL.

Parameters
    url : str
    A web page that lists vocabulary items inside
    <div class="wordlist-item"> … </div> elements.

Returns
    list[str]
    All extracted words, converted to lowercase and stripped of
    surrounding whitespace. If the page is unreachable or contains
    no matching elements, an empty list is returned.
"""
def get_keywords(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    word_divs = soup.find_all("div", class_="wordlist-item")
    words = [div.get_text(strip=True).lower() for div in word_divs if div.get_text(strip=True)]
    return words

# URLs for wordlists
positive_url = "https://www.enchantedlearning.com/wordlist/positivewords.shtml"
negative_url = "https://www.enchantedlearning.com/wordlist/negativewords.shtml"

# Get keywords
positive_keywords = get_keywords(positive_url)
negative_keywords = get_keywords(negative_url)
neutral_keywords = ["okay", "fine", "average", "meh", "decent"]

# Sample feedback list
feedback_list = [
            # "The staff were incredibly friendly and helpful.",
            # "Delivery was late and the packaging was damaged.",
]

# Initialize results
results = {
    "positive": [],
    "negative": [],
    "neutral": ["okay", "fine", "average", "meh", "decent"],
    "uncategorized": []
}
if not feedback_list:
    print("No feedback to analyze.")


"""
Classify a customer-feedback string as positive, negative, neutral, or uncategorized.

Parameters

    comment : str
    The raw feedback text to be analyzed.

    Returns
    str
    One of the four category names:
    * "positive"       - the text contains at least one positive keyword
    * "negative"       - the text contains at least one negative keyword
    * "neutral"        - the text contains at least one neutral keyword
    * "uncategorized"  - none of the above keywords were detected
"""
def analyze_comment(comment):
    comment = comment.lower()
    for word in positive_keywords:
        if word in comment:
            return "positive"
    for word in negative_keywords:
        if word in comment:
            return "negative"
    for word in neutral_keywords:
        if word in comment:
            return "neutral"
    return "uncategorized"

# Process the feedback list
if not feedback_list:
    print("No feedback to analyze.")
else:
    for comment in feedback_list:
        category = analyze_comment(comment)
        results[category].append(comment)

    # Print summary to console
    for category, comments in results.items():
        print(f"\n{category.upper()} ({len(comments)} comments):")
        for c in comments:
            print(f"- {c}")

    # Generate pie chart
    labels = list(results.keys())
    sizes = [len(results[label]) for label in labels]

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Customer Feedback Summary")
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig("feedback_chart.png")
    print("\nChart saved as 'feedback_chart.png'")
    plt.show()