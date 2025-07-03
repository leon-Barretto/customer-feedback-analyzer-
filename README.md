
## Project Overview

### SITUATION  
A small business receives customer feedback via surveys, online reviews, and service forms.  
Manually analyzing this data is time-consuming and risks missing key patterns in complaints or praise.

### TASK  
Develop a Python-based solution to automatically classify each comment as **positive**, **negative**, or **neutral**, giving businesses a clearer picture of their customer sentiment.

### ACTION  
This tool scrapes real-world positive and negative keywords from a public website using `requests` and `BeautifulSoup`.  
It processes a list of comments, classifies them, and visualizes the results using a pie chart via `matplotlib`.

### RESULT  
The result is a time-saving tool that identifies feedback trends, helping businesses take faster, smarter actions.

---

## Key Concepts Used

- **Lists & Dictionaries**: Store and categorize feedback
- **Functions**: For scraping and classification logic
- **Web Scraping**: Using `requests` + `BeautifulSoup`
- **Data Visualization**: Pie chart using `matplotlib`

---
## Output
- **Categorized feedback will print in the terminal
- **A pie chart will be saved as feedback_chart.png in your folder

---

## How to Run

### 1. Install Required Packages
```bash
pip3 install beautifulsoup4 lxml matplotlib
