# GoCardless sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/gocardless/sample-django-app.git
$ cd sample-django-app
```

## WebScrape
Webscrape.py is resposible for scrapping indeed website for keyword Python Developer. Some urls are giving predefined that are scrapped. The required data is extracted from the scraped data using beautiful soup and then inserted into mongodb.

## Django App
Django app is used to created a very minimal admin panel, only showcasing data from the mongodb cluster with close to no styling. The average salary is found for every keyword searched using numpy and displayed on the screen.
