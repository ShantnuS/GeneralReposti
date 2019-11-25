import praw
import config 
import random

#Logs into reddit with the details in config.py
def login():
    print("Trying to log in...")
    reddit = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = config.user_agent)
    print("Logged in!")
    return reddit

def print_options():
    print("Select one of the following options:")
    print("1. Repost from specific subreddit")
    print("2. Repost from random subreddit")
    
def repost_specific():
    print("Enter a subreddit name: ")
    subreddit = input(": ")
    return subreddit

def repost_random():
    subreddit = "test"
    return subreddit

def main():
    reddit = login()
    options = [repost_specific, repost_random]

    print_options()
    selected_option = int(input(": "))-1
    sub = options[selected_option]()
    submissions = reddit.subreddit(sub).top('month', limit=5)
    rando = random.randrange(1,5,1)
    repost = list(submissions)[rando]
    
    while repost.is_self:
        rando = random.randrange(1,5,1)
        repost = submissions[rando]
    
    reddit.subreddit(sub).submit(title=repost.title, url=repost.url)

if __name__ == "__main__":main()