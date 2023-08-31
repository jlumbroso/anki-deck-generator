import genanki
import os
import base64
import json

# Constants
INCLUDE_AS_BLOB = True  # Set to False if you want to save images as external files
NAME_FORMAT = "{FormattedName}"

# Define a function to format the name
def format_name(student):
    first = student.get('First', '')
    last = student.get('Last', '').upper()
    return f"{first} {last}"

# Load the JSON data
with open('data.json', 'r') as f:
    data = json.load(f)

# Create a directory for images if not using blobs
if not INCLUDE_AS_BLOB:
    image_dir = "images"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

# Define the Anki model with two card types
my_model = genanki.Model(
    1380120064,
    'Student Flashcards',
    fields=[
        {'name': 'Name'},
        {'name': 'Image'},
    ],
    templates=[
        {
            'name': 'Card 1: Name to Image',
            'qfmt': '{{Name}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Image}}',
        },
        {
            'name': 'Card 2: Image to Name',
            'qfmt': '{{Image}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Name}}',
        }
    ],
    css="""
        .card {
            font-family: arial;
            font-size: 20px;
            text-align: center;
            color: black;
            background-color: white;
        }
        img {
            width: 200%;  /* Set the width to 200% of the original size */
        }
    """
)

# Create the Anki deck
deck_id = int("".join(sorted(set([student["sectionInformation"]["sectionIdWithTerm"] for student in data]))).encode("utf-8").hex(), 16) % (10**10)
deck_title = f"Penn {', '.join(sorted(set([student['sectionInformation']['sectionIdWithTerm'] for student in data])))}"
my_deck = genanki.Deck(deck_id, deck_title)

# Process the data to generate notes for the Anki deck
media_files = []
for student in data:
    if 'Name' not in student or 'imageBlob' not in student:
        print(f"Skipping student entry due to missing key: {student}")
        continue

    # Calculate the formatted name and add it to the student dictionary
    student['FormattedName'] = format_name(student)

    # Use the formatted name in your note
    formatted_name = NAME_FORMAT.format(**student)
    
    if INCLUDE_AS_BLOB:
        image = f'<img src="{student["imageBlob"]}" />'  # Format the base64 string as an HTML <img> tag
    else:
        image_filename = os.path.join(image_dir, f"{student['studentId']}.jpg")
        with open(image_filename, 'wb') as img_file:
            img_file.write(base64.b64decode(student['imageBlob'].split(",")[1]))
        media_files.append(image_filename)
        image = f'<img src="{student["studentId"]}.jpg" />'  # Use the filename in the format of an HTML <img> tag

    my_note = genanki.Note(
        model=my_model,
        fields=[formatted_name, image])
    my_deck.add_note(my_note)

# Generate the Anki package
my_package = genanki.Package(my_deck)
if not INCLUDE_AS_BLOB:
    my_package.media_files = media_files
my_package.write_to_file('output.apkg')

print("Anki package generated successfully!")
