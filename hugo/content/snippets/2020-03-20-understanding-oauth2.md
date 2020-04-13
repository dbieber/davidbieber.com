+++
title = "Understanding OAuth2"
date = 2020-03-20T00:00:00
+++

[OAuth2](https://oauth.net/2/) is confusing. I've set it up several times before, and each time I encounter it it's a bit of a mental mess to wrap my mind around it again.

So, this time, as I set up OAuth2 to let [Bieber Bot](/projects/bieber-bot) interact with more Slack workspaces, I will write up my renewed understanding of OAuth2 in the hope that next time I have to set up OAuth2, it's a little easier.

## Overview of the OAuth2 Flow

How does the OAuth2 flow go? Like this:

The user wants to add Bieber Bot to a Slack channel. So, they're on my website ([davidbieber.com](https://davidbieber.com/)) and they click the _Add to Slack_ button. This takes them to Slack, with GET parameters that indicate they want to add Bieber Bot to some Slack workspace. The workspace id can be part of the URL of the Add to Slack button, but even if it's not, Slack will do the right thing and just ask the user to choose one of their workspaces. If the user isn't already logged in to Slack, they'll be prompted to do so at this point.

After the user clicks the _Add to Slack_ button they are taken to Slack, where they are shown the list of OAuth2 scopes that Bieber Bot is requesting. If they approve giving Bieber Bot the permissions listed in the scopes, they are taken to a _redirect url_ that I, the developer of Bieber Bot, have specified. I have both pre-informed Slack of the redirect URLs I might use, and I have included a specific redirect URL in the link on the _Add to Slack_ button. When the user is redirected to this redirect url, two GET parameters are included. The first is a `code`, which my server can use to get an Access Token / Bearer Token. The second is a `state` which is something that I, the developer, can include on the original link from the _Add to Slack_ button in order to make sure the request I'm getting at the redirect URL is genuine.

When the redirect URL is accessed with a `code` GET parameter, it then turns around and uses that `code` to request an Access Token from Slack. Once it has that Access Token, it tucks it away. It can use that access token in order to perform any of the permissions granted by the user during the access flow.

Usually using the Access Token takes the form of issuing post requests to Slack with the Access Token as a parameter.

The user can revoke access to Bieber Bot at any time. Once they do so, the Access Token becomes invalid. If Bieber Bot tries to use the Access Token at that point, it will get an error. The user will have to give Bieber Bot permissions again, and it will get a new access token, in order for it to continue providing its services and companionship.

## Summary of the the Important Bits

1. User navigates from website to service (e.g. via _Add to Slack_ button).
2. Service shows user permissions dialog.
3. Upon accepting permissions, service redirects user back to website's redirect URL with `code`
4. Website uses `code` to get Access Token
5. Website uses Access Token to do the stuff allowed by the permissions granted by the user

## Summary of the Less Important Bits

1. The _Add to Slack_ button should include GET parameters for: a) `state` so the redirect url knows the request is genuine, b) `redirect_url` so Slack knows where to send the user after they accept the permissons, c) `scope` indicating the permissions being requested, d) `client_id` indicating the app (e.g. Bieber Bot) that you're adding to Slack.

2. The permissions that the App can request are set up by the App ahead of time. So I think the `scope` parameter is there if you only need to request a subset of that permissions for a particular user.

3. The full list of possible redirect URLs should be set up ahead of time. Then when you generate the _Add to Slack_ button, you just choose a particular redirect URL that Slack should redirect the user to after they accept the permissions. Why would you want more than one redirect URL? Well, one might be for staging, one for production, and one for local development.

4. The redirect URL receives both the `code` and `state` GET parameters. The website creating the _Add to Slack_ button decides on the state. It can then check that the state is there in the redirect URL. This prevents users from going directly to Slack without going through the website, because if they try to do that, they won't have the state and will fail the check at the redirect URL. This is useful if you want to restrict installs for your App to specific customers, e.g. those who've solved a puzzle, or paid.

## What is this?

This certainly isn't meant to be an OAuth2 guide at all. By writing this out, I think I've helped myself understand the OAuth2 flow better though. That's really what snippets are all about.
