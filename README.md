# 10x-data-exchange

Experiments in consumer-mediated exchange of data between agency partners

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

Use these [local development instructions](https://github.com/18F/identity-idp/blob/main/docs/local-development.md) to setup Login.gov's identity-idp app.

Modify the file `config/service_providers.localdev.yml` to contain a URI that Login should expect from the a-saml app, which makes the "Return to" link in the b-oidc app work. Add these two lines:
```
- 'http://localhost:9292/auth/result?redirect=http%3A%2F%2Flocalhost%3A4567%2Finternal%2F&linktext=DogJobs.gov'
- 'http://localhost:9292/auth/result?redirect=http://localhost:4567/internal/&linktext=DogJobs.gov'
```
In the part of the file configuring `urn:gov:gsa:openidconnect:sp:sinatra`

You will have to run (or re-run) `make setup` after modifying this file.

The purpose of this is to allow-list params the Sinatra pair experiment needs. This error indicates either the allow-listing or the params are incorrect:
```
Redirect uri redirect_uri does not match registered redirect_uri
```
