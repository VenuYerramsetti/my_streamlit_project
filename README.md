# 📈 Streamlit Stock Forecast App

This Streamlit app forecasts stock prices using **Yahoo Finance** 📊, **Facebook Prophet** 🔮, and **Plotly** 📈.

## ✨ Features

* **Historical Data Retrieval:** Instantly fetch historical stock data from Yahoo Finance. 📅
* **Intelligent Forecasting:** Utilize Facebook Prophet for robust future stock price predictions. 🧙‍♂️
* **Interactive Visualizations:** Explore forecasts with dynamic and interactive plots powered by Plotly. 📊
* **Clean User Interface:** Enjoy a simple, intuitive, and responsive UI built with Streamlit. ✨

## 📦 Requirements

All necessary Python packages are listed in [`requirements.txt`](./requirements.txt).

## ▶️ How to Run

You have several ways to run and deploy this application:

Follow these steps to get the app running on your own machine:

### 💻 1. Run Locally

▶️ How to Run


1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/VenuYerramsetti/my_streamlit_project.git](https://github.com/VenuYerramsetti/my_streamlit_project.git)
    cd my_streamlit_project
    ```

2.  **Create a Python Virtual Environment (Highly Recommended):**
    This isolates your project dependencies.
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Required Packages:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Launch the Streamlit App:**
    ```bash
    streamlit run streamlit_app.py
    ```
    Your default web browser should automatically open to `http://localhost:8501/` where you can interact with the app. 🎉

### 🐙 2. Run via Git (After Local Setup):

Once you've cloned the repository and set up your local environment as described in "1. Run Locally", running the app is as simple as:

#### Make sure your virtual environment is activated
streamlit run streamlit_app.py

## 🚀 Deploy to Streamlit Cloud

Streamlit Cloud offers a hassle-free way to deploy your app directly from your GitHub repository to a public URL.

---

#### Ensure Your Project is on GitHub:
This repository is already hosted on GitHub: https://github.com/VenuYerramsetti/my_streamlit_project.

#### Navigate to Streamlit Cloud:
Go to streamlit.io/cloud.

#### Sign In:
Sign in using your GitHub account.

#### Click "New app":
On your Streamlit Cloud dashboard, click the "New app" button.

#### Connect to Repository:

Under "Link to repository", select your GitHub repository: VenuYerramsetti/my_streamlit_project.
For "Main file path", enter streamlit_app.py.
Leave "Branch" as main (or master if applicable).

#### Click "Deploy!":
Streamlit Cloud will automatically handle dependency installation (from requirements.txt) and deploy your application. This usually takes just a few minutes. 🚀

#### Access Your Live App:
Once deployed, you'll receive a unique public URL (e.g., https://myappproject-7c9u8eswocggx2pnvdnvmp.streamlit.app/) where your app will be live and accessible to anyone! ✅

---
