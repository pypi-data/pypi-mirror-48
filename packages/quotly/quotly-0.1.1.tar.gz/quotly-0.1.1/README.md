# Quotly

A quoting bot for 'Discord Hack Week'.


## Install & Usage

Using pip:

    pip install quotly
    
To start quoty:

    python -m quotly

## Commands

Add new quote:

    !quotly-add "<quote>" <list-of-targets>


Get random quote:

    !quotly-get <list-of-targets>
    
Targets are a list of names which are connected to the given quote. Like the author or someone mentioned in the quote.

Right now the quotes are stored in a text file.

## Planned Features
* Store quotes in database
* Mention discord users in quote
* Command for getting a specific quote