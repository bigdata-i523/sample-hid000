
# Requirements

You must have cmd5 installed from source

# Install

clone
cd
python setup.py install; pip install -e

# Proceedings

## Checkout

    $ cms proceedings clean
    $ cms proceedings clone

## Compile All

    $ cd paper1
    $ make
    
## LaTeX only 

    $ cd paper1
    $ make proc
    
    
## Commit and push changes

Find good commit message

    $ cms proceedings commit \"fix readme\"
    
## List owners

    $ cms proceedings list owner
