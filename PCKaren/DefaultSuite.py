# suite.file
"""
Program Name: defaultsuite.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: A collection of basic functions
"""

import dialogflow

CLIENT_ACCESS_TOKEN = 'b3def782c82448d09039f553d5222dc4'


class DefaultSuite:
    def __init__(self):
        """Initializes DialogFlow agent"""
        self.agent = dialogflow.Agent(CLIENT_ACCESS_TOKEN)

    def checkcommand(self, assistant, usermsg):
        """
        Sends the DialogFlow agent a message and speaks the response.
        :param assistant: The assistant that is interacting with the user
        :param usermsg: The message that the user inputted
        :returns True: True if response is found
        :returns False: False if response is not found
        """
        self.agent.sendcommand(usermsg)
        whattosay = self.agent.getresponse()
        if len(whattosay) <= 0:
            return False
        elif whattosay.lower() == "none":
            return False  # Add additional features here if desired
        else:
            assistant.speak(whattosay)
            return True
