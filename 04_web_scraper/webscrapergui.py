import tkinter as tk
from tkinter import messagebox
from webscraper import scrape_website

root = tk.Tk()
root.title("Simple Web Scraper")
root.geometry("600x400")

tk.Label(root, text="Enter website URL:").pack()
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

def scrape_site():
    url = entry.get()
    result_box.delete(1.0, tk.END)  # Clear previous results
    result_box.insert(tk.END, "Scraping website...\n")
    data = scrape_website(url)
    if data:
        for item in data:
            result_box.insert(tk.END, f"\"{item['text']}\" - {item['author']} (Tags: {', '.join(item['tags'])})\n\n")
    else:
        result_box.insert(tk.END, "Failed to scrape the website.\n")

tk.Button(root, text="Scrape", command=scrape_site).pack(pady=5)

result_box = tk.Text(root, height=15, width=60)
result_box.pack(pady=10)

root.mainloop()
