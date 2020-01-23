# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
import re
import library.space.main as space
import library.vines.main as vines
import library.users.main as users

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        message = turn_context.activity.text
        if (re.search('help', message.lower()) or re.search('enquire', message.lower()) or re.search('menu', message.lower() or re.search('options', message.lower()))):
            await turn_context.send_activity('Ok this what I can assist you with \n\n **1. Co-Working Packages** \n\n **2. Vines and its Units** \n\n **3. Book Meeting Room** \n\n **4. Logging complaints**')
        elif (re.search('no', message.lower()) or re.search('do not know', message.lower())):
            await turn_context.send_activity('Great then you would not mind telling me your username and password in the following format\n\n"**My username and secret password is** **johndlamini** ***jd2020***"')
        elif (re.search('co-working', message.lower()) or re.search('space', message.lower()) or re.search('packages', message.lower())):
            coworking = space.coworking()
            reply = ''
            for package in coworking:
                reply = reply + '* **%s**, \n\nwhich costs ***%s***. \n\nThe Benfits are follows: \n\n *%s* \n\n\n\n' % (str(package['package']), str(package['cost']), str(package['benefit']))
            await turn_context.send_activity(reply)
        elif (re.search('register', message.lower()) and re.search('information', message.lower())):
            userdata = message.split(' ')
            username = userdata[3]
            password = userdata[4]
            if (len(userdata) > 5):
                await turn_context.send_activity('It seems like you had **spaces** in your **password**\n\nTry this format\n\n"**My Register Information** ***johndlamini*** ***jd2020***"')
            else:
                if (users.regusers(username, password) == True):
                    await turn_context.send_activity('Great I have registered you\U0001F60A\n\nPlease enter your username and password in this format:\n\n"**My username and secret password is** **johndlamini** ***jd2020***"')
                else:
                    await turn_context.send_activity('Seems username exists')
                
        elif ( re.search('username', message.lower()) and re.search('secret', message.lower())):
            userdata = message.split(' ')
            username = userdata[6]
            password = userdata[7]
            if (users.login(username, password) == True):
                await turn_context.send_activity('Ok now that we know each other How may I help type **Menu**  ')
            else:
                await turn_context.send_activity('Sorry I do not seem to recognize you try again or register with again`\n\nUse this format\n\n"**My Register Information** ***johndlamini*** ***jd2020***"')
        elif (re.search('first time', message.lower()) or re.search('yes', message.lower())):
            await (turn_context.send_activity('Please give me your username and password.\n\nPlease make sure there is a space between you password and username taking note there are no spaces within your password\n\nUse this format:\n\n"**My Register Information** ***johndlamini*** ***jd2020***"'))
        elif (re.search('units', message.lower()) or re.search('vines', message.lower()) or re.search('vine', message.lower())):
            vns = vines.vines()
            reply = ''
            for vine in vns:
                reply = reply + '* **%s** \n\n*%s*\n\n' % (str(vine['title']), str(vine['brief']))
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
                await turn_context.send_activity("Hi My name is Tamara\U0001F60A.\n Is this your firstime chatting with me? ")
