#%%
import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient insantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient("xoxb-1007220339588-2701735116594-jFdfQG41BOBp78InzInTXLWN")
# logger = logging.getLogger(__name__)
# %%
channel_name = "test-channel"
conversation_id = None
try:
    # Call the conversations.list method using the WebClient
    for response in client.conversations_list():
        if conversation_id is not None:
            break
        for channel in response["channels"]:
            if channel["name"] == channel_name:
                conversation_id = channel["id"]
                #Print result
                print(f"Found conversation ID: {conversation_id}")
                break

except SlackApiError as e:
    print(f"Error: {e}")
    
# %%
channel_id = "C02MBCYLF08"

try:
    # Call the conversations.list method using the WebClient
    result = client.chat_postMessage(
        channel=channel_id,
        text="Hello world!"
        # You could also use a blocks[] array to send richer content
    )
    # Print result, which includes information about the message (like TS)
    print(result)

except SlackApiError as e:
    print(f"Error: {e}")
# %%


from github import Github

g = Github("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")
for issue in g.get_user().get_repo('AiBetCore').get_issues():
    print(issue.created_at)
    print(issue.title)
    print(issue.url)
# %%
