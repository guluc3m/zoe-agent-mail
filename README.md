zoe-agent-mail
==============

Zoe agent to sent emails.

In order to be able to sent emails before running this agent you have to set a valid `config.json` with your email and password.

After that, expected intents are in this format:

```
{ 'intent': 'mail.zoeMail',
  'dest': ['destinationMail', ...],
  'subject': 'text',
  'content': 'text',
  'adjunt': [doc1, [doc2...]] (WIP)
}
```
