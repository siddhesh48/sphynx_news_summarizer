import tkinter as tk
from tkinter import scrolledtext
from newsapi import NewsApiClient
from transformers import pipeline

# Initialize News API and summarizer
newsapi = NewsApiClient(api_key='c02cc7383f62490b8f7203206a34f103')  # 🔑 Replace with your real API key
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def get_news_summary():
    topic = topic_entry.get()
    output_box.delete('1.0', tk.END)

    if not topic:
        output_box.insert(tk.END, "Please enter a topic.\n")
        return

    try:
        articles = newsapi.get_everything(q=topic, language="en", sort_by='relevancy', page_size=5)

        all_articles = []
        for a in articles['articles']:
            title = a.get('title', '')
            desc = a.get('description', '')
            if title and desc:
                combined = f"{title}. {desc}"
                all_articles.append(combined)

        print(f"Found {len(all_articles)} articles with descriptions.")

        if not all_articles:
            output_box.insert(tk.END, "No valid articles found for this topic.\n")
            return

        for i, article in enumerate(all_articles):
            print(f"\nSummarizing Article {i+1}: {article[:100]}...")

            # Dynamically adjust max_length
            input_length = len(article.split())
            max_len = max(30, int(input_length * 0.6))

            summary = summarizer(article, max_length=max_len, min_length=20, do_sample=False)
            summary_text = summary[0]['summary_text']
            print("Summary:", summary_text)

            output_box.insert(tk.END, f"News {i+1} Summary:\n{summary_text}\n\n")

    except Exception as e:
        output_box.insert(tk.END, f"Error: {str(e)}\n")

# GUI Setup
app = tk.Tk()
app.title("AI News Summarizer")
app.geometry("700x500")

tk.Label(app, text="Enter Topic:").pack(pady=5)
topic_entry = tk.Entry(app, width=50)
topic_entry.pack(pady=5)

tk.Button(app, text="Fetch & Summarize", command=get_news_summary).pack(pady=10)

output_box = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=80, height=20)
output_box.pack(pady=10)

app.mainloop()

