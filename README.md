# JustEat Restaurant Finder

This is a simple web application that uses the JustEat API to find and display restaurant information based on a UK postcode(EC4M 7RF).

# Features

- Displays the name, cuisines, rating (as a number), and address of the top 10 restaurants in the provided postcode area.
- The postcode used in this app is `EC4M 7RF`.
- The interface is responsive and styled for better user experience.
- The user interface should show all four restaurant data points (name, cuisines, rating, address).

# Getting Started

To run the application locally, follow these steps:

# Prerequisites

Before you start ensure you have following installed:
- Python 3.x
- Flask (Install by runnig `pip install Flask`)
- Requests (Install by running `pip install requests`)

# Setting Up the Virtual Environment

**Create a Virtual Environment**

   To ensure that the project's dependencies are isolated, create a virtual environment:
   ```bash
   python -m venv venv

*Activating the virtual Environment*

- For windows (.\venv\Scripts\activate)
- For macOS/Linux (source venv/bin/activate) 

** Installing Dependecies 

- Once virtual environment is set install dependencies (pip install -r requirements.txt)


# Running the Application

1. Clone this repository to your local machine.
2. Navigate to the project directory (`justeat`).
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

# To run the Flask server
python app.py

# Open browser 
http://127.0.0.1:5000/

# Assumptions

1. **Postcode Format Assumption**  
   The postcode provided (`EC4M7RF`) is used as a fixed value for the API request. This decision was based on the assumption that no user input for different postcodes would be required, as the project prompt specifies displaying results for a specific postcode. Ideally, the application would allow dynamic postcode input, which would involve modifying the UI to accept user input and passing it to the API.

2. **Limited API Documentation**  
   The JustEat API documentation was not fully detailed, particularly regarding error handling and the structure of the response. This required assumptions about how to handle edge cases, such as missing or incomplete restaurant data. The current implementation assumes that the API will always return valid data for restaurants, which might not be the case in a production environment.

3. **Fixed Number of Restaurants**  
   The application currently limits the number of restaurants displayed to 10. This was based on an assumption that displaying a large number of restaurants may clutter the interface and negatively impact user experience. In a real-world scenario, this could be made configurable or paginated based on user preferences.

4. **API Response Consistency**  
   It was assumed that the API’s response structure would remain consistent, particularly the JSON format containing restaurant details (e.g. name, rating, cuisines). This assumption may not hold if the API evolves or if data formats change, so proper error handling would be necessary for future robustness.

5. **No User Authentication**  
   Since the application is a simple demo, there is no user authentication or session management. In a more feature-rich solution, authentication might be necessary to provide personalised recommendations or save user preferences for postcodes or restaurants.

6. **No Internationalisation/Localisation**  
   The application currently assumes that all users will be using the interface in English and within the UK. This doesn’t account for users in other countries or those who might prefer a different language or currency. Internationalisation and localisation considerations could improve the accessibility of the application for a broader audience.

7. **Basic Error Handling**  
   Basic error handling is implemented (e.g. logging API errors). However, it assumes that the user will always have access to the internet and the API will be responsive. In a production environment, the application would need more robust error handling, including retries, fallbacks, and user-friendly messages for network failures or API downtime.

8. **Data Privacy**  
   The application does not currently handle user data (e.g. saved searches or preferences), but if it were to be expanded, it would need to consider privacy policies and how user data is stored, used, and protected, in compliance with regulations.

# Improvements

1. **Error Handling and User Feedback:**
   - **Current Limitation:** The application does not provide sufficient feedback when an error occurs, especially if the API request fails or if the postcode is incorrect.
   - **Suggested Improvement:** Implement better error handling to show user-friendly messages when the API request fails or when an invalid postcode is entered. This would improve the user experience by guiding them through potential issues.

2. **Dynamic Postcode Input:**
   - **Current Limitation:** The postcode is hardcoded in the application as `EC4M 7RF`, making the solution static and not flexible for other users.
   - **Suggested Improvement:** Allow users to input their own postcode dynamically via a form input field. This would make the application more interactive and adaptable to different locations, improving its overall usability.

3. **Asynchronous API Calls:**
   - **Current Limitation:** The API request is synchronous, meaning the user has to wait for the data to load before interacting with the page.
   - **Suggested Improvement:** Implement asynchronous requests to improve performance. By making the request asynchronous, the page can load without waiting for the entire API response, which would enhance the user experience, especially on slower internet connections.

4. **API Rate Limiting and Caching:**
   - **Current Limitation:** The application makes a new API request each time the page is loaded, which could lead to hitting API rate limits or unnecessary requests.
   - **Suggested Improvement:** Introduce caching to store the API response for a short period (e.g. 1 minute) to reduce the number of requests to the API. This would help with both performance and reliability.

5. **Mobile Optimization and Responsiveness:**
   - **Current Limitation:** The current interface might not be fully optimised for all screen sizes.
   - **Suggested Improvement:** Enhance the responsiveness of the web interface by adding additional CSS media queries. This would ensure that the page is usable on a variety of devices, including mobile phones and tablets, without losing functionality or usability.

6. **Unit Testing and Test Coverage:**
   - **Current Limitation:** The project currently does not include any automated tests.
   - **Suggested Improvement:** Add unit tests for critical components of the application, such as the API call logic and the restaurant data formatting. This will ensure that future changes to the code do not introduce bugs or break existing functionality.
