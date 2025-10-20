#!/usr/bin/env python3
"""
HealthShip AI - Cloud Deployment Script
Deploys HealthShip AI to various cloud platforms for global access
"""

import os
import subprocess
import json
import requests
from pathlib import Path

class CloudDeployer:
    def __init__(self):
        self.project_path = Path(__file__).parent
        self.app_name = "healthship-ai"
        
    def create_requirements_txt(self):
        """Create requirements.txt for cloud deployment"""
        requirements = [
            "fastapi==0.104.1",
            "uvicorn[standard]==0.24.0",
            "pydantic==2.5.0",
            "requests==2.31.0",
            "python-multipart==0.0.6"
        ]
        
        with open(self.project_path / "requirements.txt", "w") as f:
            f.write("\n".join(requirements))
        
        print("Created requirements.txt")
    
    def create_dockerfile(self):
        """Create Dockerfile for containerized deployment"""
        dockerfile_content = """FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
"""
        
        with open(self.project_path / "Dockerfile", "w") as f:
            f.write(dockerfile_content)
        
        print("Created Dockerfile")
    
    def create_railway_config(self):
        """Create Railway deployment configuration"""
        railway_config = {
            "build": {
                "builder": "DOCKERFILE"
            },
            "deploy": {
                "startCommand": "uvicorn app:app --host 0.0.0.0 --port $PORT",
                "healthcheckPath": "/test-ai"
            }
        }
        
        with open(self.project_path / "railway.json", "w") as f:
            json.dump(railway_config, f, indent=2)
        
        print("Created Railway configuration")
    
    def create_vercel_config(self):
        """Create Vercel deployment configuration"""
        vercel_config = {
            "version": 2,
            "builds": [
                {
                    "src": "app.py",
                    "use": "@vercel/python"
                }
            ],
            "routes": [
                {
                    "src": "/(.*)",
                    "dest": "app.py"
                }
            ]
        }
        
        with open(self.project_path / "vercel.json", "w") as f:
            json.dump(vercel_config, f, indent=2)
        
        # Create Vercel-compatible app
        vercel_app = """from app import app

# Vercel requires the app to be named 'app'
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
"""
        
        with open(self.project_path / "api" / "index.py", "w") as f:
            f.write(vercel_app)
        
        print("Created Vercel configuration")
    
    def create_render_config(self):
        """Create Render deployment configuration"""
        render_config = {
            "services": [
                {
                    "type": "web",
                    "name": "healthship-ai",
                    "env": "python",
                    "buildCommand": "pip install -r requirements.txt",
                    "startCommand": "uvicorn app:app --host 0.0.0.0 --port $PORT",
                    "healthCheckPath": "/test-ai"
                }
            ]
        }
        
        with open(self.project_path / "render.yaml", "w") as f:
            json.dump(render_config, f, indent=2)
        
        print("Created Render configuration")
    
    def create_deployment_guide(self):
        """Create comprehensive deployment guide"""
        guide = """# 🌍 HealthShip AI - Global Cloud Deployment Guide

## 🚀 **Quick Deploy Options**

### **Option 1: Railway (Recommended - Free)**
1. **Visit:** https://railway.app
2. **Sign up** with GitHub
3. **New Project** → **Deploy from GitHub repo**
4. **Connect** your HealthShip AI repository
5. **Deploy** - Gets automatic HTTPS URL
6. **Access:** https://your-app.railway.app

### **Option 2: Render (Free Tier)**
1. **Visit:** https://render.com
2. **Sign up** with GitHub
3. **New Web Service** → **Connect Repository**
4. **Build Command:** `pip install -r requirements.txt`
5. **Start Command:** `uvicorn app:app --host 0.0.0.0 --port $PORT`
6. **Deploy** - Gets HTTPS URL

### **Option 3: Heroku (Paid)**
1. **Install Heroku CLI**
2. **Login:** `heroku login`
3. **Create app:** `heroku create healthship-ai-[your-name]`
4. **Deploy:** `git push heroku main`
5. **Access:** https://healthship-ai-[your-name].herokuapp.com

### **Option 4: Vercel (Serverless)**
1. **Visit:** https://vercel.com
2. **Import** GitHub repository
3. **Framework:** Other
4. **Deploy** - Gets global CDN

## 🔧 **Local Testing Before Deploy**

```bash
# Test locally first
uvicorn app:app --host 0.0.0.0 --port 8000

# Test API endpoint
curl http://localhost:8000/test-ai
```

## 🌐 **After Deployment**

### **Your HealthShip AI will be available at:**
- **Railway:** https://your-app.railway.app
- **Render:** https://healthship-ai.onrender.com
- **Heroku:** https://your-app.herokuapp.com
- **Vercel:** https://healthship-ai.vercel.app

### **Access from anywhere:**
- **Mobile browsers** - works on any device
- **Desktop computers** - full functionality
- **Tablets** - optimized interface
- **Any internet connection** - global access

## 📱 **Mobile Access Features**

✅ **Works on any mobile browser**
✅ **No app installation required**
✅ **Responsive design** for all screen sizes
✅ **Touch-optimized** interface
✅ **Fast loading** on mobile data
✅ **Offline fallback** capabilities

## 🔒 **Security & Privacy**

- **HTTPS encryption** on all cloud platforms
- **No personal data storage** (stateless)
- **Professional medical responses**
- **Safe for family use**

## 💡 **Pro Tips**

### **For Best Performance:**
- Use **Railway** or **Render** for fastest deployment
- **Custom domain** available on most platforms
- **Environment variables** for configuration
- **Auto-scaling** handles traffic spikes

### **For Mobile Users:**
- **Bookmark** the URL for quick access
- **Add to home screen** for app-like experience
- **Works offline** with cached responses
- **Voice input** supported in modern browsers

## 🆓 **Cost Breakdown**

- **Railway:** Free tier (500 hours/month)
- **Render:** Free tier (750 hours/month)
- **Vercel:** Free tier (100GB bandwidth)
- **Heroku:** $7/month (no free tier)

## 🎯 **Recommended Setup**

1. **Deploy to Railway** (easiest, most reliable)
2. **Test thoroughly** on mobile and desktop
3. **Share URL** with family/friends
4. **Set up custom domain** (optional)
5. **Monitor usage** and upgrade if needed

---

## 🏥 **HealthShip AI - Professional Healthcare Anywhere**

**Your personal medical consultation platform, accessible globally from any device with internet connection!**
"""
        
        with open(self.project_path / "CLOUD_DEPLOYMENT.md", "w", encoding="utf-8") as f:
            f.write(guide)
        
        print("Created deployment guide")
    
    def setup_all_configs(self):
        """Set up all deployment configurations"""
        print("Setting up HealthShip AI for global cloud deployment...")
        print()
        
        # Create necessary directories
        os.makedirs(self.project_path / "api", exist_ok=True)
        
        # Create all configuration files
        self.create_requirements_txt()
        self.create_dockerfile()
        self.create_railway_config()
        self.create_vercel_config()
        self.create_render_config()
        self.create_deployment_guide()
        
        print()
        print("All deployment configurations created!")
        print()
        print("Next Steps:")
        print("1. Choose a cloud platform (Railway recommended)")
        print("2. Follow the guide in CLOUD_DEPLOYMENT.md")
        print("3. Deploy your HealthShip AI globally")
        print("4. Share the URL for worldwide access")
        print()
        print("Your HealthShip AI will be accessible from anywhere!")

if __name__ == "__main__":
    deployer = CloudDeployer()
    deployer.setup_all_configs()
