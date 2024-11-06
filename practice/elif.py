def get_weather_report(weather: str = input("What is the weather? ")) -> str:
    if weather == "rainy" or weather == "cold":
        print("bring a jacket")
    elif weather == "hot":
        print("keep cool out there")
    else:
        print("I don't recognize this weather")
    return weather
