# 10x-data-exchange

## About this project

### Original project description

We have observed that the public does not have a good understanding of what happens to their data when they share it with the federal government, which results in low public trust, low sign up for optional services intended to benefit the public, and underreporting of civil rights and whistleblower complaints. We believe that by creating a "data passport" or personal file that would allow people to see who accessed the data that they shared with the government and when, or opt into sharing information to match for service eligibility or allow the government to prefill forms like taxes or enrollment forms, that it would result in a more transparent relationship between the public and government and increase public trust. In addition, 10x will explore the concept of a public data trust, which means involving the public not just in information sharing, but in the process of analyzing and making decisions based off that data as well.

### Links to understand the context

* [Data Exchange README](https://docs.google.com/document/d/1IfLms6VMIaOpkgdy0_DiDTQXpntpgtQZgoTyKUExCTw/)
* [Project folder on Google Drive](https://drive.google.com/drive/folders/1Xv6QOYEFwhMv2SfVHi9Rzl4XASAvnbXc)
* [Agile project board](https://github.com/orgs/GSA-TTS/projects/31/)

## Server pair experiment

We are trying to learn if one of our ideas for data exchange is allowable in browsers, and if it runs into rules guarding against XSS attacks.
* In the directory `server-pair`
* Run `pip install -r requirements.txt`
* And then start two servers:
  * `flask --app a run -p 5001`
  * `flask --app b run -p 5002`

