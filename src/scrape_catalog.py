import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.shl.com/solutions/assessments/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

data = []

for item in soup.find_all("h3"):
    data.append({
        "assessment_name": item.text.strip(),
        "description": item.text.strip() + " assessment for hiring",
        "job_role": "General",
        "skills": "Cognitive, Technical"
    })

df = pd.DataFrame(data)
df.to_csv("data/assessments.csv", index=False)

print("Scraped and saved assessments.csv")
