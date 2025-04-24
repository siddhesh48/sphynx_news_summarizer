📰 AI News Summarizer (Tkinter-Based Desktop App)
👥 Group Members
Siddhesh Tripathi – ku2407u378

Rehan Khan – ku2407u363

Niraj Matai – ku2407u341

Niyati Joshi – ku2407u342

Nidhi Kotian – ku2407u339

🎯 Objective
The objective of the AI News Summarizer desktop application is to:

Enable users to fetch real-time news on a chosen topic.

Use advanced NLP techniques to summarize lengthy articles into concise, readable summaries.

Provide a simple and intuitive Graphical User Interface (GUI) using Tkinter for easy interaction.

🚀 Core Features
Real-Time Article Fetching
Utilizes the NewsAPI to retrieve the top 5 most relevant news articles based on user-defined topics.

AI-Based Summarization
Leverages the Hugging Face Transformers library with the BART (facebook/bart-large-cnn) model to generate concise summaries of news content.

Dynamic Summary Length
Adjusts the summary length dynamically based on the input size, ensuring meaningful and readable output.

User-Friendly GUI
Built using Tkinter, the application includes:

Topic input field

Button to fetch and summarize news

Scrollable output area for displaying summaries

Robust Error Handling
Detects and displays user-friendly messages for issues like empty input, API errors, or missing article content.

🛠️ Libraries & Tools Used
tkinter
Purpose: Desktop GUI development.
Function: Displays interface for input and output.

newsapi-python
Purpose: Real-time news fetching.
Function: Retrieves relevant articles using NewsAPI.

transformers (Hugging Face)
Purpose: Natural Language Summarization.
Function: Generates short summaries using the BART model.

⚙️ Functional Components
get_news_summary()
Main logic function that:

Retrieves articles from NewsAPI

Combines and processes titles and descriptions

Generates summaries

Displays results in the output area

summarizer Pipeline
NLP model from Hugging Face that summarizes long-form news content.

Tkinter GUI
Provides a clean and interactive interface for users to input a topic and read the summarized news.

💡 Future Enhancements (Optional Features)
Export Functionality: Save summaries as .txt or .pdf files.

Category Filtering: Support for multiple news categories (e.g., Politics, Sports).

Summary Length Options: Let users select between short, medium, and detailed summaries.

Visualization Tools: Add word clouds or summary metrics using matplotlib or seaborn.

Improved UX: Loading indicators, progress bars, and threading to prevent freezing.

📌 Conclusion
The AI News Summarizer is a smart, intuitive tool designed to revolutionize how users consume news. With the power of real-time article fetching and AI-driven summarization, it offers concise, digestible content in seconds. The Tkinter-based interface ensures accessibility and ease of use, while the foundation is built to support future scalability and enhancements.

