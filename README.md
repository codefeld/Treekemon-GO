# Treekemon GO!

An app for the **HATCH 2021** Hackathon

## Inspiration

We were inspired by the videogame **Pokémon GO**, where you go to real-life locations to find and catch Pokémon.

## What it does

This webapp finds **champion trees** around the United States and gives you information about each one. You can view it in **list view**, where it shows every single tree in a big list. You can also view it in **map view**, where it shows an appoximate location of each tree.

## How we built it

Here is a step-by-step process of how we created this app:
1. We made a mockup of our app by drawing it. We did this for most of our pages.
2. We first created a checklist of each thing we wanted our app to do. We would check off each item we completed.
3. We created the Django app from the Heroku Getting Started with Python guide.
4. We used a Bootstrap template to begin with, and we changed some colors and added buttons that took us to the list and map page.
5. We worked on our list page. We added buttons for each tree and added a search bar to make it easier to locate a specific tree.
6. We worked on our map page. We used Google Maps API to get a map on our website, and then we added markers for each tree. We also made it so that if you click a marker, it will take you to the tree.
7. We worked on the tree detail pages. We used a `.json` file to get information for each tree.
8. We added a link to a QR scanner page.

Our mentor mentor helped us write a `python` script to scrape the tree data from the [americanforests.org](https://www.americanforests.org/) and get GPS data from Google’s Geocode API.

## Challenges we ran into

We ran into many challenges, including
 - Placing markers on Google Maps
 - Making the scale image on the detail page with the tree and the person
 - Making a search bar for the list page

## Accomplishments that we're proud of

We are proud of many things, such as:
 - Using a Google Maps API
 - Making a search bar for the list page
 - Making a detail page for each tree
 - Learning `Django` and `Bootstrap`
 - It was hard to get good data. We needed help from our mentor to scrape data from [americanforests.org](https://www.americanforests.org/).

## What we learned

While building this webapp, we learned:
 - How to use `Django` and `Bootstrap`
 - About the champion trees, and which ones are in our state.

## What's next for Treekemon GO!

Next, we would like to do more with **iNaturalist** and add a DNA strand for each tree.
