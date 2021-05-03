import os
from os.path import join, dirname

# !pip install evernote3
from evernote.api.client import EvernoteClient
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

# !pip install python-dotenv
import dotenv

# Real applications authenticate with Evernote using OAuth, but for the
# purpose of exploring the API, you can get a developer token that allows
# you to access your own Evernote account. To get a developer token, visit
# https://sandbox.evernote.com/api/DeveloperToken.action

def login():
    dotenv.load_dotenv(verbose=True)
    dotenv_path = join(dirname(__file__), '.env')
    dotenv.load_dotenv(dotenv_path)
    auth_token = os.getenv('EVERNOTE_TOKEN')

    if auth_token == "your developer token":
        print("Please fill in your developer token")
        print("To get a developer token, visit "
            "https://sandbox.evernote.com/api/DeveloperToken.action")
        exit(1)

    # Initial development is performed on our sandbox server. To use the production
    # service, change sandbox=False and replace your
    # developer token above with a token from
    # https://www.evernote.com/api/DeveloperToken.action
    # To access Sandbox service, set sandbox to True
    # To access production (International) service, set both sandbox and china to False
    # To access production (China) service, set sandbox to False and china to True

    sandbox = False
    china = False

    client = EvernoteClient(token=auth_token, sandbox=sandbox, china=china)

    user_store = client.get_user_store()

    version_ok = user_store.checkVersion(
        "Evernote EDAMTest (Python)",
        UserStoreConstants.EDAM_VERSION_MAJOR,
        UserStoreConstants.EDAM_VERSION_MINOR
    )
    print("Is my Evernote API version up to date? ", str(version_ok))
    print("")
    if not version_ok:
        exit(1)
    
    return client
