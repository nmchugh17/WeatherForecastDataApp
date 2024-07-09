import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/sky data
    filtered_data = get_data(place, days)

    if option == "Temperature":
        dates = [dict["date"] for dict in filtered_data]
        temperatures = [dict["day"]["avgtemp_c"] for dict in filtered_data]
        # Create a temperature plot/sky data
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Sunny": "images/Sunny.png", "Cloudy": "images/Cloudy.png",
                  "Partly Cloudy ": "images/Partly cloudy.png", "Heavy rain": "images/Heavy rain.png",
                  "Light drizzle": "images/Light drizzle.png", "Mist": "images/ Mist.png",
                  "Moderate rain": "images/Moderate rain.png", "Overcast": "images/ Overcast.png",
                  "Patchy rain nearby": "images/Patchy rain nearby.png", "Snow": "images/ Snow.png"}

        sky_conditions = [dict["day"]["condition"]["text"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        print(image_paths)
        st.image(image_paths, width=150)
