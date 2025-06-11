#!/usr/bin/python3
""" It contains the function:
    fetch_and_print_posts
    fetch_and_save_posts """

import requests
import csv


def fetch_and_print_posts():
    """ Print the titles of the retrieved posts. """
    # Makes an HTTP GET request to the API URL to get the list of posts.
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """ Fetches posts and saves them to a CSV file. """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        data = response.json()
        structured_data = []
        for post in data:
            entry = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            structured_data.append(entry)

        with open("posts.csv", "w") as file:
            """ Create a DictWriter object to write dictionaries to the CSV file,
            specifying the columns to write."""
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()  # Writes the first line of the CSV file
            # Writes all lines of data to the file, from the structured_data list.
            writer.writerows(structured_data)
