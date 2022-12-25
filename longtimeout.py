# -*- coding: utf-8 -*-

# Sample Python code for youtube.liveChatBans.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import sys

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_authenticated_service():

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = '(ClientSecretsJSONFile HERE).json'

    credentials = None
    if os.path.exists("%s-oauth2.json" % sys.argv[0]):
        credentials = Credentials.from_authorized_user_file("%s-oauth2.json" % sys.argv[0],scopes)

    # If there are no (valid) credentials available, let the user log in.

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            # Get credentials and create an API client
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, scopes)
            credentials=flow.run_console()

    #Save the credentials for next run
    with open("%s-oauth2.json" % sys.argv[0], "w") as token:
        token.write(credentials.to_json())

    return googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

def ban_routine():
    youtube = get_authenticated_service()

    request = youtube.liveChatBans().insert(part="snippet",body={"kind": "youtube#liveChatBan", "snippet": {"banDurationSeconds": 86400,"type": "temporary","bannedUserDetails": {"channelId": "UC...(Channel ID HERE)",},"liveChatId": "Cg...(LiveChatID HERE)" }}
    )
    response = request.execute()
    print(response)

if __name__ == "__main__":
    ban_routine()
