# Profile sync client
The profile sync client can be used to automatically sync profiles from a local identity store to a Pleio subsite. The client is built in Python and uses a REST/JSON API to connect to Pleio.

## Features
- Automatically creating, updating and blocking users from a subsite
- Ability to sync profile fields and site-specific avatars
- Test the synchronization with the dry-run option

## Usage
Run the CLI using the following command:

```bash
    $ python cli.py --source users.csv --destination https://example.pleio.nl/profile_sync_api/
```
