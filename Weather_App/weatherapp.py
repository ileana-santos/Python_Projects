import tkinter as tk
from tkinter import Frame, Label, Entry, Button, messagebox
from PIL import Image, ImageTk
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

API_KEY = os.environ.get("OPENWEATHER_API_KEY")
BASE_URL = os.environ.get("OPENWEATHER_BASE_URL")

if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY not found in .env file.")
if not BASE_URL:
    raise ValueError("OPENWEATHER_BASE_URL not found in .env file.")

class WeatherApp:
    """A simple weather application using Tkinter and OpenWeatherMap API."""

    def __init__(self, root: tk.Tk) -> None:
        """
        Initializes the weather application.

        :param root: The main Tkinter window.
        """
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("500x500+300+200")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f4f4")

        self.create_search_box()
        self.create_logo()
        self.create_info_box()

    def create_search_box(self) -> None:
        """Creates a search box with an entry field and a search button."""
        search_frame = Frame(self.root, bg="white", bd=2, relief="groove")
        search_frame.place(x=50, y=20, width=400, height=50)

        self.textfield = Entry(search_frame, justify="left", width=20, font=("poppins", 18), border=0)
        self.textfield.pack(pady=10, padx=10, side="left", expand=True)

        search_btn = Button(
            search_frame, text="Search", font=("poppins", 12, "bold"),
            bg="#2196F3", fg="white", activebackground="#1976D2",
            activeforeground="white", border=0, cursor="hand2",
            command=self.get_weather
        )
        search_btn.pack(padx=10, pady=5, side="right")

    def create_logo(self) -> None:
        """Loads, resizes, and displays the application logo centered above the info box."""
        original_image = Image.open("weather-forecast.png")
        resized_image = original_image.resize((80, 80))  # Adjusted size
        self.logo_image = ImageTk.PhotoImage(resized_image)

        # Center the logo above the info box
        self.logo = Label(self.root, image=self.logo_image, bg="#f4f4f4")
        self.logo.place(x=210, y=90)

    def create_info_box(self) -> None:
        """Creates a frame to display weather details like temperature, wind speed, etc."""
        info_frame = Frame(self.root, bg="white", bd=2, relief="groove")
        info_frame.place(x=50, y=180, width=400, height=250)

        self.labels = {}
        weather_details = ["Temperature", "Condition", "Wind", "Humidity", "Pressure"]

        for detail in weather_details:
            label = Label(info_frame, text=f"{detail}: --", font=("poppins", 14), bg="white", anchor="w")
            label.pack(pady=5, padx=10, fill="x")
            self.labels[detail] = label  # Store labels for dynamic updates

    def get_weather(self) -> None:
        """Fetches weather data from OpenWeatherMap and updates the UI."""
        city: str = self.textfield.get().strip()
        if not city:
            messagebox.showerror("Error", "Please enter a city name!")
            return

        params: dict = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        data: dict = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", "City not found!")
            return

        # Extract weather information
        temperature: float = data["main"]["temp"]
        condition: str = data["weather"][0]["description"].title()
        wind: float = data["wind"]["speed"]
        humidity: int = data["main"]["humidity"]
        pressure: int = data["main"]["pressure"]

        # Update labels with fetched data
        self.labels["Temperature"].config(text=f"Temperature: {temperature}°C")
        self.labels["Condition"].config(text=f"Condition: {condition}")
        self.labels["Wind"].config(text=f"Wind: {wind} km/h")
        self.labels["Humidity"].config(text=f"Humidity: {humidity}%")
        self.labels["Pressure"].config(text=f"Pressure: {pressure} hPa")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()