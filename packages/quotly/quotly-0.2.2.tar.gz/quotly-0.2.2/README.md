# Quotly

A quoting bot for 'Discord Hack Week'.


## Install & Usage

Using pip:

    pip install quotly
    
To tell quotly to use your discord-bot token type:

    python -m quotly --token='<TOKEN>'
    
To start quotly type:

    python -m quotly --run
    
Your discord-bot token is stored inside an __.env__ file inside your working directory.
The quotes are stored inside a SQLite database which is also placed in the current working directory.

## Commands

Add new quote:

    !quotly-add "<quote>" <author>
    
After adding the quote to database, the command-call is deleted from channel and the user 
receives a dm with a confirmation that the quote was added.


Get random quote:

    !quotly-get
    
Get random quote from specific author:

    !quotly-get <author>
        

## Planned Features
* Mention discord users in quote
* Command for getting a specific quote
* Web-interface

## License
MIT