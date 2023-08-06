# Django SSFS (Simple Static File Storage)

## Why?

We build a lot of projects with Django.  Often we're deploying to Heroku which has an ephemeral file system.  We usually just want to get our site up and running.

This project helps by using a one-liner to configure Django's **static media storage** (e.g. user file uploads that aren't part of the codebase).