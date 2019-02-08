# ZeroDeposit

Please see the following installation guides: 
### I. Window 
### II. Linux

And see the technical report:
### III. Technical report
  
## Prerequisites:
 - Python 3.6 or higher, registered on your path as python3


# I. Windows guide:
## Installation
 1. Clone the ZeroDeposit repository.
 2. Open cmd in ZeroDeposit.
 3. Create and activate a virtual environment: 
        python3 -m venv venv
        venv\Scripts\activate
 4. Install the module: 
        pip install -e .


## Run

 5. Run the project:
        set FLASK_APP=zerodeposit
        flask run
 6. Open url: 127.0.0.1:5000 in web browser.


## Testing

Within the venv, run pytest


# II. Linux Guide:
## Installation

 1. Clone the ZeroDeposit repository.
 2. Open terminal in ZeroDeposit.
 3. Create and activate a virtual environment: 
        python3 -m venv venv
        . venv/bin/activate
 4. Install the module: 
        pip install -e .


## Run

 5. Run the project:
        export FLASK_APP=zerodeposit
        flask run
 6. Open url: 127.0.0.1:5000 in web browser.


## Testing

Within the venv, run pytest

