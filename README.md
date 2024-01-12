# 10x-data-exchange

## About this project

### Original project description

We have observed that the public does not have a good understanding of what happens to their data when they share it with the federal government, which results in low public trust, low sign up for optional services intended to benefit the public, and underreporting of civil rights and whistleblower complaints. We believe that by creating a "data passport" or personal file that would allow people to see who accessed the data that they shared with the government and when, or opt into sharing information to match for service eligibility or allow the government to prefill forms like taxes or enrollment forms, that it would result in a more transparent relationship between the public and government and increase public trust. In addition, 10x will explore the concept of a public data trust, which means involving the public not just in information sharing, but in the process of analyzing and making decisions based off that data as well.

### Links to understand the context

* [Data Exchange README](https://docs.google.com/document/d/1IfLms6VMIaOpkgdy0_DiDTQXpntpgtQZgoTyKUExCTw/)
* [Project folder on Google Drive](https://drive.google.com/drive/folders/1Xv6QOYEFwhMv2SfVHi9Rzl4XASAvnbXc)
* [Agile project board](https://github.com/orgs/GSA-TTS/projects/31/)

## Server pair experiment

We are trying to learn if one of our ideas for data exchange is allowable in browsers, and if it runs into rules guarding against XSS attacks. This experiment is the `server-pair` directory.

### To run
* Run `pip install -r requirements.txt`
* And then start two servers:
  * `flask --app a run -p 5001`
  * `flask --app b run -p 5002`

### For code quality
* To lint, run `flake8`
* To format, run `black .`

## Sinatra pair experiment

Experimenting with Login.gov authentication by copying two sandbox apps,[identity-saml-sinatra](https://github.com/18F/identity-saml-sinatra) and [identity-oidc-sinatra](https://github.com/18F/identity-oidc-sinatra), and connecting them to each other. This experiment is the `sinatra-pair` directory.

### To run

You will need to run three servers:

  1. Login's [identity-idp](https://github.com/18F/identity-idp) project at [localhost:3000](http://localhost:3000/). Here's [how to run it](#setup-of-identity-idp).
  2. The app in this repo's `a-saml` directory at [localhost:4567](http://localhost:4567/)
  3. The app in this repo's `b-oidc` directory at [localhost:9292](http://localhost:9292/)

All three are started with:

  * `make setup` the first time you run each, or after changes
  * `make run`

  Visit [Agency A's internal page](http://localhost:4567/internal/) to run the experiment

#### Setup of identity-idp

Use these [local development instructions](https://github.com/18F/identity-idp/blob/main/docs/local-development.md).

Modify the file `config/service_providers.localdev.yml` to contain a URI that Login should expect from the a-saml app. Under the section `urn:gov:gsa:openidconnect:sp:sinatra` add these redirect URIs:
```
- 'http://localhost:9292/auth/result?redirect=http%3A%2F%2Flocalhost%3A4567%2Finternal%2F&linktext=DogJobs.gov'
- 'http://localhost:9292/auth/result?redirect=http://localhost:4567/internal/&linktext=DogJobs.gov'
```
You will have to run (or re-run) `make setup` after modifying this file


