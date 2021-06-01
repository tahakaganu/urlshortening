# urlshortening
URL Shortening solution

To execute the solution from the terminal:

curl -i -H "Content-Type: application/json" -X POST -d '{"url": "<URL_TO_BE_ENCODED>"}' http://localhost:80/

To use the API simply do a POST request to the flask container. The POST data must follow the format {"url": "<URL_TO_BE_ENCODED>"} The api will return {"new_url": "<NEW_SHORTEN_URL">}

You can call the NEW_SHORTEN_URL and the application will redirect you to the original URL. If the URL does not exist in the database, the API will return an error message {"message": "URL does not exists."}