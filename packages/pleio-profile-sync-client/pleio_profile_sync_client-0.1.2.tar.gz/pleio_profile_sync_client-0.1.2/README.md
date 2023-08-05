# Profile sync client
The profile sync client can be used to automatically sync profiles from a local identity store to a Pleio subsite. The client is built in Python and uses a REST/JSON API to connect to Pleio.

## Features
- Automatically creating, updating and blocking users from a subsite
- Ability to sync profile fields and site-specific avatars
- Test the synchronization with the dry-run option

## Requirements
The package requires a Python version >= 3.3.

## Installation
Installation (and updates) are done with a single command:

    pip3 install pleio-profile-sync-client

## Usage
Use the CLI tool as follows:

```bash
    $ pleio-profile-sync-client --source example.csv --destination http://www.pleio.test:7000/profile_sync_api/
```

The CSV accepts the following fields:

- **name**, the fullname of the user
- **email**, the e-mailaddress of the user
- **avatar**, a relative link to the avatar in jpeg of the user
- **profile.\***, a field containing profile information, for example: `profile.occupation`.

Check [example/users.csv](./example/users.csv) for an example.
