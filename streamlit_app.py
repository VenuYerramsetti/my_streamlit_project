import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

# Prophet import with fallback
try:
    from prophet import Prophet
except ImportError:
    from fbprophet import Prophet

from prophet.plot import plot_plotly

st.set_page_config(page_title="📈 Stock Price Forecast App")
st.title("📈 Stock Price Forecast App")

# Sidebar inputs
st.sidebar.header("Settings")
ticker = st.sidebar.text_input("Enter stock ticker", "AAPL").upper()

forecast_options = {
    "1 Week": 7,
    "1 Month": 30,
    "3 Months": 90,
    "6 Months": 180,
    "1 Year": 365
}
forecast_choice = st.sidebar.selectbox("Forecast period", list(forecast_options.keys()))
period = forecast_options[forecast_choice]

@st.cache(ttl=3600)
def load_data(ticker_symbol):
    try:
        data = yf.download(ticker_symbol, period="5y", auto_adjust=True)
        data.reset_index(inplace=True)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

df = load_data(ticker)

if df is not None and not df.empty:
    df = df.tail(365 * 3)  # Keep last 3 years

    close_col = None
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [' '.join(col).strip() for col in df.columns.values]
    for col in df.columns:
        if 'Close' in col:
            close_col = col
            break

    if close_col is None:
        st.error("Close price column not found in data.")
    else:
        df_train = df[['Date', close_col]].rename(columns={'Date': 'ds', close_col: 'y'})
        df_train['y'] = pd.to_numeric(df_train['y'], errors='coerce')
        df_train = df_train.dropna(subset=['y'])

        st.subheader(f"Data used for forecasting ({len(df_train)} rows):")
        st.write(df_train.tail())

        try:
            m = Prophet(daily_seasonality=False)
            m.fit(df_train)

            future = m.make_future_dataframe(periods=period)
            forecast = m.predict(future)

            st.subheader("Forecast")
            fig1 = plot_plotly(m, forecast)
            st.plotly_chart(fig1, use_container_width=True)

            st.subheader("Forecast Components")
            fig2 = m.plot_components(forecast)
            st.pyplot(fig2)

            st.subheader("Forecast Data")
            st.write(forecast.tail())

        except Exception as e:
            st.error(f"Error during forecasting or plotting: {e}")
else:
    st.warning("No data available. Please check the stock ticker symbol.")
