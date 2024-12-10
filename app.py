import streamlit as st
import requests

# Streamlit page configuration
st.set_page_config(page_title="🌤 Weather App", layout="centered")

# Function to fetch weather data
def get_weather(city, api_key="YOUR_API_KEY"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# UI of the Weather App
st.title("🌤 Weather App")
st.write("Get real-time weather updates for any city!")

# Input field for city
city = st.text_input("Enter a city name:")

if city:
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    weather_data = get_weather(city, api_key)

    if weather_data:
        st.success("Weather data fetched successfully!")

        # Display weather information
        st.metric("🌡 Temperature (°C)", weather_data["main"]["temp"])
        st.metric("💧 Humidity (%)", weather_data["main"]["humidity"])
        st.metric("🌬 Wind Speed (m/s)", weather_data["wind"]["speed"])
        st.write(f"**🌥 Weather Description:** {weather_data['weather'][0]['description'].capitalize()}")
    else:
        st.error("City not found! Please try again.")
