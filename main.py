from fastapi import FastAPI
import pandas as pd

app = FastAPI()
df = pd.read_csv('School_Based_Health_Centers.csv')

@app.post("/ask")
async def ask(question: str):
    q = question.lower()
    
    if "how many" in q or "total" in q:
        return {"response": f"Detroit has {len(df)} school-based health centers."}
    elif "address" in q or "location" in q:
        centers = df[['Site_Name', 'Address', 'City']].to_string()
        return {"response": f"Health centers in Detroit:\n{centers}"}
    elif "sponsor" in q or "organization" in q:
        orgs = df['Sponsoring_Organization'].unique().tolist()
        return {"response": f"Organizations: {', '.join(orgs)}"}
    else:
        return {"response": "Ask about total centers, addresses, or sponsoring organizations in Detroit."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

