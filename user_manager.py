"""
user_manager.py
~~~~~~~~~~~~~
The class UserManager manages the list of users that the bot has interacted with.

In the case in which the bot has not interacted with a given user, this class
adds that new user to the list.
"""

import random
import tweepy
import user
from user import User

class UserManager:
    # Initialize the object
    def __init__(self, api):
        self.user_list = []
        self.api = api

    # Return the contents of the stored user in a readable format
    def __str__(self):
        self_string = "Current saved users: \n"
        for user in self.user_list:
            self_string += user.screen_name + "\n"
        return self_string

    # Create a new user for the given screen_name and add it to the user_list
    def add_user(self, screen_name):
        new_user = User(screen_name)
        new_user.fetch_tweets(self.api)
        self.user_list.append(new_user)

    def get_response(self, screen_name):
        # TODO: Extract the verb in the question aimed to the Bot
        #question_verb = get_question_verb(tweet.text)

        # Get the user object from the user_list
        found_user = False
        target_user = None
        for user in self.user_list:
            if screen_name == user.screen_name:
                found_user = True
                target_user = user
                break
        # If the user was not found, create the user
        if not found_user:
            self.add_user(screen_name)
            target_user = self.user_list[-1]

        if len(target_user.responses_list) == 0:
            return "Deberías " + random.choice(user.VERBS)

        # Choose one of the pre-calculated responses randomly
        choice_idx = random.randint(0, len(target_user.responses_list) - 1)

        base_tweet = target_user.responses_list[choice_idx]
        del target_user.responses_list[choice_idx]

        return "Deberías " + base_tweet



