# 10x-data-exchange

10x is looking for pilot partners to help test a new idea for transferring data between systems that, we think, might avoid the need for a data sharing agreement between the system owners. We’re hoping to find a situation where:
- Two systems need the same data but for compliance reasons are not connected.
- Data is transferred between the two systems via a manual process—potentially even by a user downloading a file from one system and then manually uploading it to another.
- The risk of failure is fairly low; this isn’t PII or mission-critical data transfer. Perhaps the users are federal employees rather than members of the public.

Can you think of a situation like this? Are you the system owner for a system that’s involved in a situation like this? If so, please contact the 10x team working on this idea: mike.gintz@gsa.gov and jim.moffet@gsa.gov

Below is a demo of what this might look like in practice. In general, the experience we're trying to deliver feels to a user like "Do you want to get a doc from another agency? Just keep clicking "yes", after 6-10 clicks it'll be done and you'll be back where you started and ready to move on." 

For agency partners, we aim to help them deliver this experience to users, *without needing a data-sharing agreement*, and with minimal integration (adding links and url params to existing web pages).

https://github.com/GSA-TTS/10x-data-exchange/assets/5996125/08475d0c-0180-4e4f-93f9-a33ea8a526ed


Experiments in consumer-mediated exchange of data between agency partners

* [Data Exchange README](https://docs.google.com/document/d/1IfLms6VMIaOpkgdy0_DiDTQXpntpgtQZgoTyKUExCTw/)
* [Project folder on Google Drive](https://drive.google.com/drive/folders/1Xv6QOYEFwhMv2SfVHi9Rzl4XASAvnbXc)
* [Agile project board](https://github.com/orgs/GSA-TTS/projects/31/)

## Sinatra pair experiment

This experiment is demo'd in [the "Dog Jobs" video](https://gsa.enterprise.slack.com/files/U02H3PT5Y5S/F06DRN13FV5/dataexchangedemo1.mp4). The experiment uses Login.gov authentication by copying two sandbox apps,[identity-saml-sinatra](https://github.com/18F/identity-saml-sinatra) and [identity-oidc-sinatra](https://github.com/18F/identity-oidc-sinatra), connected to each other. This experiment is the `sinatra-pair` directory.

### To run

You will need to run three servers:

  1. Login's [identity-idp](https://github.com/18F/identity-idp) project at [localhost:3000](http://localhost:3000/). Here's [how to run it](#setup-of-identity-idp).
  2. The app in this repo's `sinatra-pair/a-saml` directory at [localhost:4567](http://localhost:4567/)
  3. The app in this repo's `sinatra-pair/b-oidc` directory at [localhost:9292](http://localhost:9292/)

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

**Optional:** to make Login's handoff screens look right, replace placeholder names in the above file.
* Replace `Test SAML SP` with `DogJobs.gov`
* Replace `Example Sinatra App` with `IRS Dog Services`

#### Mobile device testing

To test the Sinatra pair experiment with a mobile device, you will need [these instructions](https://github.com/18F/identity-idp/blob/main/docs/mobile.md) for broadcasting Login.gov over your home or office WiFi. Adapt the technique to broadcast the other two servers, `a-saml` and `b-oidc`.

## Old server pair experiment

We are trying to learn if one of our ideas for data exchange is allowable in browsers, and if it runs into rules guarding against XSS attacks. This experiment is the `server-pair` directory.

### To run
* Run `pip install -r requirements.txt`
* And then start two servers:
  * `flask --app a run -p 5001`
  * `flask --app b run -p 5002`

### For code quality
* To lint, run `flake8`
* To format, run `black .`
