# Define the duration of each segment in minutes
national_news_duration = 12
international_news_duration = 5
sports_duration = 5
weather_forecasts_duration = 2

# Define the total duration of the newscast in minutes
total_newscast_duration = 30

# Calculate the total duration of news and other segments
total_news_duration = (national_news_duration +
                       international_news_duration +
                       sports_duration +
                       weather_forecasts_duration)

# Calculate the duration of advertisements by subtracting the total news duration from the total newscast duration
advertisements_duration = total_newscast_duration - total_news_duration

# Print the final answer
print(f"The number of minutes of advertising in the newscast is: {advertisements_duration}")