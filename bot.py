# MIT License

# Copyright (c) 2022 ModestJicamaBots

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import subprocess
import yaml
import praw
import os.path

APP_VERSION='v0.0.1'

if(not os.path.exists('secrets.yaml')): subprocess.run(["powershell", f"& 'C:\\Program Files\\1Password CLI\\op.exe' inject -f -i secrets.yaml.tpl -o secrets.yaml"], shell=True)

with open('secrets.yaml', 'r') as file: secrets = yaml.safe_load(file)
with open('config.yaml', 'r') as file: config = yaml.safe_load(file)


reddit = praw.Reddit(password      = secrets['password'],
                     username      = secrets['username'], 
                     client_id     = secrets['client_id'], 
                     user_agent    = f"{secrets['user_agent']}:{APP_VERSION}", 
                     client_secret = secrets['client_secret'])

for sub in config['subreddits']:
    print(f"---------- SUBREDDIT: {sub}----------")
    for post in reddit.subreddit(sub).hot(limit=config['limit']):
        print(f"{post.title}\n  score: {post.score}\n  ratio: {post.upvote_ratio}\n\n")
        post.downvote()
exit
