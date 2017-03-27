# DuckHacks 2017

This repository contains the code for our submission to the DuckHacks 2017 Hackathon hosted by JPMorgan and Google, which won the prize for "Most Marketable".

## What is it?

Our submission was an emotion-driven music selection program. It uses Microsoft's emotion API to analyze the emotion of a user and play music to match their mood. The emotion API requires the use of an image taken by the user's webcam every few seconds, which is deleted immediately after its use. After receiving the data, the application will access Pandora and play a genre of music that matches the user's mood.

## How do I use it?

To use it, there are several dependencies that need to be installed. These include `pygame`, `scikit-learn`, `selenium`, `opencv`, and `chromium`. The program itself can be run by downloading the source and running `driver.py` using Python 2. The current version only works on Mac OSX, but can be adapted to work on Linux with some modifications.

## Collaborators
This project was developed by the following:

Taylor He - Web Interface Development

Christopher Hittner - Machine Learning

Jacob Manzelmann - Photograph Retrieval

Elena Oh - Marketing

Jonathan Pavlik - Web Interface Development
