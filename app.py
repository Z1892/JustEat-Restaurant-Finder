from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_restaurants(postcode):
    url = f'https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC4M7RF'  # Ensure no space in the URL
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Referer": "https://www.just-eat.co.uk/",
    }
    
    response = requests.get(url, headers=headers)

    print(f"API Response Status Code: {response.status_code}")
    print(f"API Response Text: {response.text}")  # Debugging

    if response.status_code != 200:
        print(f"Error: API request failed with status code {response.status_code}")
        return {"restaurants": []}

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print("Error: Failed to decode JSON response from API")
        return {"restaurants": []}


@app.route('/')
def home():
    postcode = 'EC4M7RF'  # Postcode with space
    raw_restaurants = get_restaurants(postcode)

    # Limit to 10 restaurants
    raw_restaurants = raw_restaurants['restaurants'][:10]  # Limit to first 10 restaurants

    unwanted_terms = ['Low Delivery Fee', 'Deals', 'Collect stamps']  # Terms to exclude from cuisines

    formatted_restaurants = []
    for restaurant in raw_restaurants:
        name = restaurant.get('name')
        
        # Filter out unwanted terms from cuisines
        cuisines = ", ".join([cuisine['name'] for cuisine in restaurant.get('cuisines', []) 
                              if cuisine['name'] not in unwanted_terms])
        
        if not cuisines:
            cuisines = 'No specific cuisines'

        rating = restaurant.get('rating', {}).get('starRating', 'N/A')
        address = f"{restaurant.get('address', {}).get('firstLine', '')}, {restaurant.get('address', {}).get('city', '')}"

        formatted_restaurants.append({
            'name': name,
            'cuisines': cuisines,
            'rating': rating,
            'address': address
        })

    return render_template('index.html', restaurants=formatted_restaurants)

if __name__ == '__main__':
    app.run(debug=True)
