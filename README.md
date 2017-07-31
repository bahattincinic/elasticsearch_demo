# Elasticsearch Demo

Demo Application for pyistanbul presentation

### Requirements

* Python 3.5+


### Installation

#### OSX

Install Homebrew

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Install Required Packages:

    $ brew install python3

#### Ubuntu/Debian

Install Required Packages:
(python3 is already installed as default on 16.04)

    $ sudo apt-get install python3-dev libpq-dev

### Building the Project

Create Virtual Environment (3.5+)

    $ virtualenv --python=$(which python3) env
    $ sourve env/bin/activate

Clone the repository and:

    $ git clone git@github.com:bahattincinic/elasticsearch_demo.git
    $ cd elasticsearch_demo/

install requirements

    $ pip install -r requirements.txt

To run the project, Follow the following commands:

    $ cd web
    $ python app.py foursquare build
    $ python app.py runserver
