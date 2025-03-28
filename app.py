# import streamlit as st
# import pandas as pd
# from bs4 import BeautifulSoup
# import requests

# # App Title
# st.title("AI-Driven LeadGen Scraper")
# st.write("""
# This tool simulates lead scraping by extracting book data from an openly scrapable site — [Books to Scrape](http://books.toscrape.com). 
# Think of books as business listings: each has a title (Lead Name), price (Lead Value), and availability (Engagement Status).
# """)

# # User input for category (simulated search)
# query = st.text_input("Enter your lead category (e.g., 'data tools', 'marketing agencies'):", "tech books")

# # Scrape button
# if st.button("Scrape Leads"):
#     st.write(f"🔍 Simulating scraping for category: **{query}**")

#     # Scraping logic
#     def scrape_books(pages=2):
#         base_url = "http://books.toscrape.com/catalogue/page-{}.html"
#         all_books = []

#         for page in range(1, pages + 1):
#             response = requests.get(base_url.format(page))
#             soup = BeautifulSoup(response.content, "html.parser")
#             books = soup.find_all("article", class_="product_pod")

#             for book in books:
#                 title = book.h3.a["title"]
#                 price = book.find("p", class_="price_color").text.strip()[2:]
#                 stock = book.find("p", class_="instock availability").text.strip()
#                 all_books.append({
#                     "Lead Name": title,
#                     "Lead Value (£)": float(price),
#                     "Engagement Status": stock
#                 })

#         return pd.DataFrame(all_books)

#     df = scrape_books(pages=2)

#     # Filter: leads > £10
#     filtered_df = df[df["Lead Value (£)"] > 10].copy()

#     st.success(" Scraping complete! Preview below:")
#     st.dataframe(filtered_df)

#     # Download button
#     csv = filtered_df.to_csv(index=False).encode('utf-8')
#     st.download_button(
#         label="Download CSV of Leads",
#         data=csv,
#         file_name="filtered_crm_leads.csv",
#         mime="text/csv"
#     )

#     # Extra Thoughtfulness: Add lead scoring (simulated)
#     filtered_df["Lead Score"] = filtered_df["Lead Value (£)"].apply(lambda x: " High" if x > 40 else " Medium")
#     st.write("### Lead Scoring Summary")
#     st.dataframe(filtered_df[["Lead Name", "Lead Value (£)", "Lead Score"]])



# import streamlit as st
# import pandas as pd
# from bs4 import BeautifulSoup
# import requests

# # App Title
# st.title("AI-Driven LeadGen Scraper")
# st.write("""
# This tool simulates lead scraping by extracting book data from an openly scrapable site — [Books to Scrape](http://books.toscrape.com). 
# Think of books as business listings: each has a title (Lead Name), price (Lead Value), and availability (Engagement Status).
# """)

# # User input for category (simulated search)
# query = st.text_input("Enter your lead category (e.g., 'data tools', 'marketing agencies'):", "tech books")

# # Scrape button
# if st.button("Scrape Leads"):
#     st.write(f"🔍 Simulating scraping for category: **{query}**")

#     # Scraping logic
#     def scrape_books(pages=2):
#         base_url = "http://books.toscrape.com/catalogue/page-{}.html"
#         all_books = []

#         for page in range(1, pages + 1):
#             response = requests.get(base_url.format(page))
#             soup = BeautifulSoup(response.content, "html.parser")
#             books = soup.find_all("article", class_="product_pod")

#             for book in books:
#                 title = book.h3.a["title"]
#                 price = book.find("p", class_="price_color").text.strip()[2:]
#                 stock = book.find("p", class_="instock availability").text.strip()
#                 all_books.append({
#                     "Lead Name": title,
#                     "Lead Value (£)": float(price),
#                     "Engagement Status": stock
#                 })

#         return pd.DataFrame(all_books)

#     df = scrape_books(pages=2)

#     # Simulated smart filtering based on input query
#     query = query.lower()
#     # filtered_df = df[df["Lead Name"].str.lower().str.contains(query)]
#     filtered_df = df  # Skip filtering

#     st.success("✅ Scraping complete! Preview below:")
#     st.dataframe(filtered_df)

#     # Download button
#     csv = filtered_df.to_csv(index=False).encode('utf-8')
#     st.download_button(
#         label="Download CSV of Leads",
#         data=csv,
#         file_name="filtered_crm_leads.csv",
#         mime="text/csv"
#     )

#     # Extra Thoughtfulness: Add lead scoring (simulated)
#     filtered_df["Lead Score"] = filtered_df["Lead Value (£)"].apply(lambda x: "🔥 High" if x > 40 else "👍 Medium")
#     st.write("### Lead Scoring Summary")
#     st.dataframe(filtered_df[["Lead Name", "Lead Value (£)", "Lead Score"]])

import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import requests

# App Title
st.title("AI-Driven LeadGen Scraper")
st.write("""
This tool simulates lead scraping by extracting book data from an openly scrapable site — [Books to Scrape](http://books.toscrape.com). 
Think of books as business listings: each has a title (Lead Name), price (Lead Value), and availability (Engagement Status).
""")

# User input
query = st.text_input("Enter your lead category (e.g., 'data tools', 'marketing'):", "tech")

# Option to bypass filtering
show_all = st.checkbox("Show all leads without filtering", value=False)

# Scrape button
if st.button("Scrape Leads"):
    st.write(f"🔍 Scraping in progress...")

    def scrape_books(pages=2):
        base_url = "http://books.toscrape.com/catalogue/page-{}.html"
        all_books = []

        for page in range(1, pages + 1):
            response = requests.get(base_url.format(page))
            soup = BeautifulSoup(response.content, "html.parser")
            books = soup.find_all("article", class_="product_pod")

            for book in books:
                title = book.h3.a["title"]
                price = book.find("p", class_="price_color").text.strip()[2:]
                stock = book.find("p", class_="instock availability").text.strip()
                all_books.append({
                    "Lead Name": title,
                    "Lead Value (£)": float(price),
                    "Engagement Status": stock
                })

        return pd.DataFrame(all_books)

    df = scrape_books(pages=2)

    # Filter logic
    if show_all:
        filtered_df = df
    else:
        keywords = query.lower().split()
        filtered_df = df[df["Lead Name"].str.lower().apply(lambda x: any(k in x for k in keywords))]

    # Lead scoring
    filtered_df["Lead Score"] = filtered_df["Lead Value (£)"].apply(
        lambda x: "🔥 High" if x > 40 else "👍 Medium"
    )

    # Display
    st.success("✅ Scraping complete! Preview below:")
    st.write("### Lead Scoring Summary")
    st.dataframe(filtered_df)

    # Download CSV
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV of Leads",
        data=csv,
        file_name="filtered_crm_leads.csv",
        mime="text/csv"
    )

