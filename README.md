# Anki Penn Student Flashcard Generator

Generate Anki flashcards from a JSON file containing student data generated by [the Penn Class List Scraper](https://github.com/jlumbroso/penn-classlist-scraper).

## Overview

This project provides a web-based tool and a Python CLI tool to generate Anki decks from a JSON file containing student data. The generated deck contains cards with student names and their corresponding images.

To begin, export a JSON file from the class lists. Start by installing [the Penn Class List Scraper](https://github.com/jlumbroso/penn-classlist-scraper) and then navigate to the class lists on [`courses.at.upenn.edu`](https://courses.at.upenn.edu/). After obtaining the JSON file, this tool can generate an Anki deck with cards for each student.

## Features

* Upload a JSON file containing student data.
* Generate an Anki deck with cards for each student.
* Download the generated `.apkg` file for importing into Anki.


### Prerequisites

* Python 3.x
* pipenv

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/jlumbroso/anki-deck-generator
    cd anki-deck-generator 
    ```

2. Navigate to the Python client directory:

    ```bash
    cd python-client
    ```

3. Install the required dependencies using pipenv:

    ```bash
    pipenv install
    ```

### Usage

1. Activate the virtual environment:

    ```bash
    pipenv shell
    ```

2. Use the CLI tool to generate the Anki deck:

    ```bash
    anki_deck_generator [JSON_FILES] --output [OUTPUT_FILENAME] --separate-decks --include-as-blob --name-format [NAME_FORMAT]
    ```

For more details on the available options, run:

    ```bash
    $ anki_deck_generator --help
    Usage: anki_deck_generator.py [OPTIONS] [JSON_FILES]...

    Options:
    --output FILE       Path to save the generated Anki deck.
    --separate-decks    Generate separate decks for each JSON file.
    --include-as-blob   Embed images directly into the Anki deck. If not set,
                        images will be saved as external files.
    --name-format TEXT  Format for displaying names on the flashcards. Default
                        is "{FormattedName}".
    --help              Show this message and exit.
    ```

## Setup for Local Development of the Website

This is only necessary for local installation. You can access this tool online.

### Prerequisites

* Node.js and npm

### Installation

1. Clone the repository:
    
    ```bash
    git clone https://github.com/jlumbroso/anki-deck-generator
    cd anki-deck-generator 
    ```

2. Install the required dependencies:
    
    ```bash
    npm install 
    ```

3. Start the development server:
    
    ```bash
    npm start 
    ```

4. Open your browser and navigate to `http://localhost:3000`.

## Usage

1. Click on the "Choose File" button and select your JSON file containing student data.
2. Click on the "Generate Deck" button.
3. Once the deck is generated, a download link for the `.apkg` file will appear. Click on it to download the file.
4. Import the downloaded `.apkg` file into Anki.

## JSON File Format

The JSON file should contain an array of student data objects. Each object should have the following format:
    
    ```json
    {
        "First": "Jeyna",
        "Last": "Doe",
        "imageBlob": "data:image/jpeg;base64,...",
        "sectionInformation": {
            "sectionIdWithTerm": "CIS-5000-001-202330"
        }
        /* ... other fields */
    }
    ``` 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)