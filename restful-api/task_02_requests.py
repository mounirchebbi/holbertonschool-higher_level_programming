#!/usr/bin/python3
# task_02_requests.py
""""""
import requests
import json
import csv


def fetch_and_print_posts():
    """print get response"""
    url = "https://jsonplaceholder.typicode.com/posts"
    responce = requests.get(url)

    print(f"Status Code: {responce.status_code}")

    if responce.status_code == 200:
        data = responce.json()
        for post in data:
            print(post["title"])
    else:
        print(f"Error: {responce.status_code}")


def fetch_and_save_posts():
    """save get reponse to csv file"""
    url = "https://jsonplaceholder.typicode.com/posts"
    responce = requests.get(url)

    print(f"Status Code: {responce.status_code}")

    if responce.status_code == 200:
        data = responce.json()
        # restructure the data to remove userid key
        new_data = [{"id": post["id"],
                     "title": post["title"],
                     "body": post["body"]} for post in data]
        with open("posts.csv", 'w', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(new_data)
