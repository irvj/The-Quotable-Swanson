## The Quotable Swanson

The Quotable Swanson ([u/the-quotable-swanson](https://www.reddit.com/user/the-quotable-swanson)) is a quote-bot built for Reddit with Python and the [PRAW](https://pypi.org/project/praw/) package. This bot monitors the 'Parks and Recreation' ([r/PandR](https://www.reddit.com/r/PandR/)) subreddit, looks for comments that call it with `!Ron`, and replies with a random quote from the character [Ron Swanson](https://en.wikipedia.org/wiki/Ron_Swanson).

If you'd like to help me add quotes to this bot, please submit your list of quotes as an [Issue](https://github.com/pyji/The-Quotable-Swanson/issues). Make sure your quotes are word-for-word from the show, correctly spelled and punctuated, and not already present in the [quotes.py](https://github.com/pyji/The-Quotable-Swanson/blob/master/quotes.py) list file.

## Using This Code For Your Own Bot

If you want to use this code to create your own quote-bot, or even just some kind of reply-bot, it should be very easy to fork, edit, and deploy. Here's what you need to know.

### config.ini

The `_config.ini` file contains the variables for your user-specific Reddit credentials. The variables `reddit_user`, `reddit_pass`, and `reddit_target_subreddit` should be self-explanatory.

`reddit_client_id` and `reddit_client_secret` can be obtained by creating an app in your [Reddit profile preferences](https://www.reddit.com/prefs/apps/). Click the 'create an app' button at the bottom, give it a name and choose 'script.' You'll also have to enter a redirect url; you can just enter `http://127.0.0.1` in that field. Once you create the app, your `reddit_client_id` is the value underneath 'personal use script' and your `reddit_client_secret` is the value in the 'secret' field.

As for `reddit_user_agent`, it is very important that you create a unique user agent to identify your bot to Reddit with. Make it something descriptive about your bot and consider including your username as well. Creating a unique and identifiable user agent is part of Reddit's API terms of service. An example would be something like `purple-monkey-dishwasher-bot-v1.0-by-u/username-here`.

Once you've edited `_config.ini`, save the file and rename it to `config.ini`.

### the-quotable-swanson.py

You shouldn't have to edit much in this file. Let's take a look at what you will need to change.

    Line 28:    if re.search('!ron', comment.body, re.IGNORECASE) and not comment.author == reddit.redditor(reddit_user):

Here, you should edit `'!ron'` to be whatever phrase you want your bot to look for. The regex `re.IGNORECASE` here means your phrase won't be case-sensitive. The second condition in this if-statement indicates that your bot will not reply to itself, so your trigger phrase can also be included in your bot response without fear of an infinite loop of replies.

    Line 29:    comment_reply = random.choice(
    Line 30:        quotes) + "\n\n__________________________________________________\n^^Greetings ... "

If you simply want your bot to reply with one of your random quotes, you can safely remove everything after and including the `+`. However, if you'd like to also include a sentence about your bot, you can edit everything between the quotation marks to your liking. The `^^` here before each word indicates superscript in Reddit's comment code. You will want to have these before each word if you want them to be smaller text.

You may rename this file to anything you want, but if you do so, you will also need to edit the Dockerfile if you plan to deploy this in Docker. More on that in a moment.

### quotes.py

This file should contain all your quotes. `quotations` is just a list variable, so you'll want it to look like:

    quotations = \
        [
            'quote one goes here.',
            'quote two goes here.',
            'and finally quote three.'
        ]

### Deploying with Docker

You can optionally deploy this bot with Docker quite easily using the included `Dockerfile`, `docker-compose.yml`, and `.dockerignore` files. The only one you'll need to edit is `Dockerfile`.

    Line 11:    CMD ["python", "./the-quotable-swanson.py"]

This line should be changed to the name of your script.

Create a folder with a name specific to your bot (as Docker uses the folder name to help name the container image) and copy all of the files listed out below into the folder. It should look something like this:

    purple-monkey-dishwasher-bot/
                    .dockerignore
                    Dockerfile
                    config.ini
                    docker-compose.yml
                    quotes.py
                    requirements.txt
                    purple-monkey-dishwasher.py

Next build your image and start the container with `docker-compose.yml` with the following command:

    docker-compose up --build -d

This will build the image, and start the container in a detached state. Your bot should now be live.

### Testing

It's important to test your bot first before actually deploying it to your target subreddit. I recommend spending some time in a test subreddit, playing with your live bot yourself, so that you can work out any kinks. To do this, edit your `config.ini` file and change `reddit_target_subreddit` to your testing subreddit. You should test your bot in the command line first before deploying with Docker so that you're not continuously building and rebuilding images.
