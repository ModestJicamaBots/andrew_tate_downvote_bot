# Andrew Tate Downvote Bot

downvotes based on configured limit in `config.yaml`

1Password CLI for secret injection handled for windows only rn 💀

don't need 1Password CLI if you just create `secrets.yaml` in root dir like:

```
user_agent: <user_agent>
client_id: <client_id>
client_secret: <client_secret>
username: <username>
password: <password>
```

requires pyyaml and praw

then `python ./bot.py`