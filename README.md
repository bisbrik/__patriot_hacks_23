# Weather Clothing Recommendations App

## Overview
This Python program is designed to provide personalized clothing recommendations based on the national weather forecast for a user-provided location. It utilizes API calls to fetch 8 hours of weather forecast data and analyzes it to suggest appropriate clothing options for the user.

## Features
- Takes user input for location (zipcode)
- Retrieves national weather forecast data using API calls
- Analyzes weather data to generate personalized clothing recommendations
- Displays clothing recommendations using images

## Prerequisites
- Python 3.x installed
- Required Python libraries: tkinter, PIL

## Installation
1. Clone or download the repository to your local machine.
2. Ensure you have Python installed.
3. Install the required libraries using pip:
    ```
    pip install pillow
    ```
4. Run the program:
    ```
    python weather_clothing_app.py
    ```

## Usage
1. Launch the program.
2. Enter the zipcode for the desired location.
3. Click the "Tell me the weather!" button.
4. The program will fetch weather data and display personalized clothing recommendations based on the forecast.

## Example
[Weather Clothing Recommendations App](example_screenshot.png)

## Notes
- Ensure an active internet connection for fetching weather data.
- Make sure the provided images for clothing items (shortSleeve.png, longSleeve.png, etc.) are available in the working directory or update the file paths accordingly.
- This program serves as a basic demonstration and may require further enhancements for production use, such as error handling and additional features.

## Credits
- This program was developed by Patrick Kelley, Devin He, and Ha-Dan Huynh.
