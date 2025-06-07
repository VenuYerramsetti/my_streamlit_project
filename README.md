# 📈 Streamlit Stock Forecast App

This Streamlit app forecasts stock prices using **Yahoo Finance** 📊, **Facebook Prophet** 🔮, and **Plotly** 📈.

## ✨ Features

* **Historical Data Retrieval:** Instantly fetch historical stock data from Yahoo Finance. 📅
* **Intelligent Forecasting:** Utilise Facebook Prophet for robust future stock price predictions. 🧙‍♂️
* **Interactive Visualisations:** Explore forecasts with dynamic and interactive plots powered by Plotly. 📊
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


## 📊 What the Output Shows

When you run the Streamlit Stock Forecast App, you'll see several key outputs designed to provide a comprehensive view of the stock's performance and future predictions:

**Interactive Forecast Plot:** This is a Plotly chart displaying both the historical closing prices of the stock and the forecasted future prices. It includes shaded regions representing the confidence intervals (yhat_lower and yhat_upper), showing the probable range of future prices.
**Forecast Components:** Powered by Facebook Prophet, this section breaks down the forecast into its underlying drivers. You'll typically see:
Trend: The overall long-term direction of the stock price (upward, downward, or flat).
**Seasonality (Weekly/Yearly):** Any recurring patterns in the stock price that repeat on a weekly or yearly basis.
**Raw Forecast Data Table:** A detailed table showing the precise forecasted values. For each future date (ds), you'll see the predicted price (yhat) and its lower (yhat_lower) and upper (yhat_upper) confidence bounds.
**Data Used for Forecasting:** A snippet of the historical data (ds, y) that was fed into the Prophet model. This helps confirm the input.
**Error Messages:** If an invalid ticker is entered or data cannot be fetched, clear error or warning messages will be displayed, guiding the user to correct the input.
This output provides a clear and interactive way to understand the past behaviour of a stock and its potential future trajectory based on the forecasting model.
