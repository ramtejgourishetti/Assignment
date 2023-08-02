import requests

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
API_KEY = "b6907d289e10d714a6e88b30761fae22"

def get_weather_data(city):
    url = f"{API_BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def get_temp_by_date(data, date):
    for forecast in data["list"]:
        if date in forecast["dt_txt"]:
            return forecast["main"]["temp"]
    return None

def get_wind_speed_by_date(data, date):
    for forecast in data["list"]:
        if date in forecast["dt_txt"]:
            return forecast["wind"]["speed"]
    return None

def get_pressure_by_date(data, date):
    for forecast in data["list"]:
        if date in forecast["dt_txt"]:
            return forecast["main"]["pressure"]
    return None

def main():
    city = input("Enter the city name (e.g., London,us): ")
    data = get_weather_data(city)
    
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            temp = get_temp_by_date(data, date)
            if temp is not None:
                print(f"Temperature on {date}: {temp}°C")
            else:
                print("No data available for the provided date.")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed_by_date(data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("No data available for the provided date.")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure_by_date(data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("No data available for the provided date.")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
