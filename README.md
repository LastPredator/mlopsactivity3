# 🚀 MLOps Class Activity: CI/CD Pipeline using GitHub Actions

This repository is part of the **MLOps course activity** on **Continuous Integration and Deployment (CI/CD)** for Machine Learning.  
The goal is to automate an ML workflow using **GitHub Actions** — from preprocessing to training, evaluation, and containerization.

---

## 🎯 Learning Objectives

By the end of this activity, you will be able to:

- Understand CI/CD concepts applied to ML projects  
- Automate data preprocessing, model training, and evaluation using GitHub Actions  
- Upload trained model artifacts automatically  
- (Optionally) Build and push Docker containers after successful training  

---

## 🧩 Repository Structure

mlops-ci-activity/
│
├── data/ # Optional: sample dataset (if used)
│
├── preprocess.py # Preprocessing script
├── train.py # Model training script
├── evaluate.py # Model evaluation script
├── requirements.txt # Dependencies
├── Dockerfile.train # Docker image for training
├── Dockerfile.serve # Docker image for serving
│
└── .github/
└── workflows/
└── ci-pipeline.yml # GitHub Actions workflow definition
