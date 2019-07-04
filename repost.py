
def print_options():
    print("Select one of the following options:")
    print("1. Repost from specific subreddit")
    print("2. Repost from random subreddit")
    
def repost_specific():
    print("Enter a subreddit name: ")
    subreddit = input(": ")
    print(subreddit)

def repost_random():
    subreddit = "aww"
    print(subreddit)

def main():
    options = [repost_specific, repost_random]

    print_options()
    selected_option = int(input(": "))-1
    options[selected_option]()


if __name__ == "__main__":main()