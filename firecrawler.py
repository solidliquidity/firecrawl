from firecrawl import FireCrawl
from os import getenv

api_key = getenv('FIRECRAWL_API_KEY')

# Initialize the FireCrawl object
fc = FireCrawl(api_key=api_key)
# Scrape the website
data = fc.scrape(url="https://www.zacks.com/")
# Convert data to markdown
markdown_data = data.to_markdown()
print(markdown_data)