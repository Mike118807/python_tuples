# Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about 
# a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. 
# For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")].

# List each flight itinerary.

def format_itineraries(itinerary_list):
    result = ""
    for index, (traveler_name, origin, destination) in enumerate(itinerary_list, start=1):
        result += f"Itinerary {index}: {traveler_name} - Fron {origin} to {destination}\n "
    return result.strip()

# Use function format_itineraries

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_itineraries = format_itineraries(itineraries)
print(formatted_itineraries)