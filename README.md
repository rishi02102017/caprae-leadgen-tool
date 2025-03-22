# AI-Driven LeadGen Scraper

This project was developed as part of the Caprae Capital **AI-Readiness Pre-Screening Challenge**.

---

## 🚀 Overview
This tool simulates a lead generation scraper inspired by [CohesiveAI’s Lead Scraper](https://getcohesiveai.com/scraper). It uses a public dataset from [BooksToScrape](http://books.toscrape.com) to replicate business-like lead listings with titles, prices, and availability. Users can enter a lead category (e.g., "data tools", "HR solutions"), and the tool filters relevant leads dynamically.

---

## 💡 Features
- 🔍 **Prompt-based search** (simulates keyword scraping)
- 📊 **Lead scoring** based on value (£)
- 🧠 **Simulated lead metadata** (Name, Value, Engagement Status)
- 📥 **Download CSV** of filtered, CRM-ready leads
- 🧼 Clean UI using **Streamlit**

---

## 📂 Tech Stack
- `Streamlit`
- `BeautifulSoup` (bs4)
- `Pandas`
- `Requests`

---

## 🔗 Live Demo
👉 [Click to Run the App](https://caprae-leadgen-tool-ywtu9ekczpkeakcazg8d8u.streamlit.app)

---

## 📁 Repository Structure
```
├── app.py               # Streamlit frontend
├── requirements.txt     # For Streamlit Cloud deployment
├── README.md            # This file
```

---

## 📌 How to Run

### Run Locally
```bash
pip install streamlit beautifulsoup4 pandas requests
streamlit run app.py
```

### Or Use Streamlit Cloud
Push this repo to GitHub → [https://streamlit.io/cloud](https://streamlit.io/cloud) → Deploy directly.

---

## Author's Note
This project was completed in under 5 hours and focused on replicating a **quality-first feature**: prompt-based filtering with dynamic scraping simulation. Ideal for businesses seeking fast, low-code lead qualification solutions.

---

## 📩 Contact
- Email: jyotishmandas85p@gmail.com/m24csa013@iitj.ac.in
- GitHub: rishi02102017
