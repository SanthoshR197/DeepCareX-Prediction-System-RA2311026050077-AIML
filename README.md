# 🏥 DeepCareX: AI-Powered Healthcare Diagnostic System

[![Docker Hub](https://img.shields.io/badge/Docker-Hub-blue?logo=docker&logoColor=white)](https://hub.docker.com/r/ra2311026050077/deepcarex)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/SanthoshR197/DeepCareX-Prediction-System-RA2311026050077-AIML)

DeepCareX is a professional healthcare diagnostic application that leverages state-of-the-art Machine Learning and Deep Learning models to predict various diseases based on symptoms and medical imaging (X-Rays, CT Scans, MRI).

---

## 👨‍💻 Credits & Acknowledgments

This project is a modernized and containerized version of the original **DeepCareX** project.
- **Original Author**: [Sumon Singh](https://github.com/sumony2j)
- **Original Repository**: [sumony2j/DeepCareX](https://github.com/sumony2j/DeepCareX)

---

## 🚀 What We Accomplished

In this version of the project, we focused on **Modernization** and **Deployment Readiness**:

1.  **Containerization**: Wrapped the entire Flask application, its dependencies, and the ML models into a Docker container for consistent cross-platform execution.
2.  **Infrastructure-as-Code**: Created specialized scripts (`containerize.ps1`, `Dockerfile`) to automate the build and deployment process.
3.  **Cloud Readiness**: Published the containerized image to **Docker Hub** and updated the codebase for seamless integration with GitHub.
4.  **Optimized Workflow**: Streamlined the database initialization and server startup within the container environment.

---

## 🐳 Docker Usage Guide

You can run this entire healthcare system with a single command without installing any Python dependencies locally.

### 1. Pull the Image from Docker Hub
```bash
docker pull ra2311026050077/deepcarex:latest
```

### 2. Run the Application
```bash
docker run -it -p 5000:5000 --name deepcarex_app ra2311026050077/deepcarex:latest
```

### 3. Access the System
Once the container is running, open your browser and navigate to:
👉 **[http://localhost:5000](http://localhost:5000)**

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python 3.10)
- **AI/ML**: TensorFlow, Keras, XGBoost, Scikit-Learn
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **DevOps**: Docker, GitHub Actions

---

## 📂 Project Highlights

- **8 Disease Modules**: Alzheimer's, Brain Tumor, Breast Cancer, COVID-19, Diabetes, Hepatitis C, Kidney Disease, and Pneumonia.
- **Hybrid Modeling**: Uses CNNs for image-based diagnosis and XGBoost/Random Forest for symptom-based analysis.
- **Secure Data Handling**: Integrated database to allow users to save their diagnostic history.

---
*Developed for research and educational purposes.*
