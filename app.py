import streamlit as st
import requests

# Function to fetch weather data
def fetch_weather(location, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Main function for the Streamlit app
def main():
    st.title("Weather Forecast App")

    # Input field for the location
    location = st.text_input("Enter the location:", "")

    if st.button("Get Weather"):
        if location:
            api_key = "d0b2a97c0cc97bcebcfda1008e800b26"  # Your API key
            weather_data = fetch_weather(location, api_key)

            if weather_data:
                # Extracting necessary data
                city = weather_data["name"]
                temp = weather_data["main"]["temp"]
                weather_desc = weather_data["weather"][0]["description"]
                humidity = weather_data["main"]["humidity"]
                wind_speed = weather_data["wind"]["speed"]

                # Displaying the weather data
                st.subheader(f"Weather in {city}")
                st.write(f"Temperature: {temp}°C")
                st.write(f"Condition: {weather_desc.capitalize()}")
                st.write(f"Humidity: {humidity}%")
                st.write(f"Wind Speed: {wind_speed} m/s")
            else:
                st.error("Location not found. Please try again.")
        else:
            st.warning("Please enter a location.")

if __name__ == "__main__":
    main()
