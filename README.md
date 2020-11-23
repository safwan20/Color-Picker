# Color-Picker

### Approach 
To detect the dominant colour I used the approach of finding the intensities of each RGB tuples and creating a dictionary, once the dictionary is prepared I chose the top intensity as the dominant one.
But for border colour I calculated the percentage of dominant colour in the image if it is above 50% then I chose the dominant colour as the border colour I assumed that the dominant colour plays the big role in the border colour, But if it is less then 50% then I need to calculate the average of top 10 intensities as I assume the top 10 contribute most in the border colour.

### Algorithm

1. prepareIntensities of each RGB tuple by counting how many times it appears in the image and put into the dictionary.
2. select topMostIntensity from the intensities dictionary
3. calculate the percentage of topmost colour in the image if it is greater than 50% then it is a dominant as well as border colour but, if it is less then 50% than average of top 10 RGB is calculated.

### Steps to run

1. Create a python3 virtual enviornment.
2. Install the requirements via `pip install -r requirements.txt`.
3. Run the **Flask** app using `python app.py`.
4. Now that the server is running, you can make POST requests to the `/pick_color` endpoint.

### Deployment
deployment can be done in pythonanywhere cloud server or Heroku server
