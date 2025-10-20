from app import app

# Vercel requires the app to be named 'app'
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
