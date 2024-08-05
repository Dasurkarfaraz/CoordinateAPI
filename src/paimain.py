import requests

def post_image_and_text(image_path, text, api_url):
    """
    Sends a POST request to the specified API URL with an image and text.

    Args:
    - image_path (str): Path to the image file to upload.
    - text (str): The text to include in the form data.
    - api_url (str): The URL of the API endpoint.

    Returns:
    - dict: The JSON response from the API.
    """
    # Open the image file in binary mode
    with open(image_path, 'rb') as image_file:
        # Prepare the files and data for the POST request
        files = {'image': image_file}
        data = {'text': text}

        # Send the POST request
        response = requests.post(api_url, files=files, data=data)

        # Check if the request was successful
        if response.status_code == 200:
            # Return the JSON response
            return response.json()
        else:
            # Print the error and raise an exception
            print(f"Request failed with status code {response.status_code}")
            print(response.text)
            response.raise_for_status()

# Usage example
if __name__ == "__main__":
    image_path = 'screenshots\tem.png'  # Replace with your image path
    text = 'hello'             # Replace with the text you want to send
    api_url = 'http://localhost:5000/extract-coordinates'  # Replace with your API URL

    try:
        result = post_image_and_text(image_path, text, api_url)
        print("Response:", result)
    except Exception as e:
        print("An error occurred:", e)
