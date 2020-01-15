# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
import re
import library.space.main as space

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        message = turn_context.activity.text
        if (re.search('help', message.lower()) or re.search('enquire', message.lower())):
            await turn_context.send_activity('Ok this what I can assist you with \n\n **1. Co-Working Packages** \n\n **2. Our Communuity** \n\n **3. Book Meeting Room** \n\n **4. Logging complaints**')
        elif (re.search('co-working', message.lower()) or re.search('space', message.lower()) or re.search('packages', message.lower())):
            coworking = space.coworking()
            reply = ''
            for package in coworking:
                reply = reply + '* **%s**, \n\nwhich costs ***%s***. \n\nThe Benfits are follows: \n\n *%s* \n\n\n\n' % (str(package['package']), str(package['cost']), str(package['benefit']))
            await turn_context.send_activity(reply)
        elif (re.search('thanks', message.lower()) or (re.search('thank', message.lower()))):
            await turn_context.send_activity('You welcome \U0001F60A')
        else:
            await turn_context.send_activity('OK, sorry I could not get that try texting "help" or "enquire"')

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome My name is Tamara.\n How may I help you")
