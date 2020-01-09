# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
import re

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        message = turn_context.activity.text
        if (message.lower() == 'help' or message.lower() == 'enquire'):
            await turn_context.send_activity(f"Ok this what I can assist you with \n 1. Space \n 2. Our Communuity")
        elif (message.lower() == 'space'):
            await turn_context.send_activity(f"For Co-Working Spaces the following is available: \n 1. Basic Membership which is ZW 250 monthly")
        elif (re.search('thanks', message.lower())):
            await turn_context.send_activity(f"You welcome ")
        else:
            await turn_context.send_activity(f'OK, sorry I could not get that try texting "help" or "enquire"')

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome My name is Tamara.\n How may I help you")
