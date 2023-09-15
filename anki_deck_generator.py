import genanki
import os
import base64
import json
import click
from collections import defaultdict

# Constants
NAME_FORMAT = "{FormattedName}"

# Define a function to format the name
def format_name(student):
    first = student.get('First', '')
    last = student.get('Last', '').upper()
    return f"{first} {last}"

def generate_single_deck(students, section_name, output_filename, include_as_blob=False, name_format=NAME_FORMAT):
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
                font-family: Arial;
                font-size: 20px;
                text-align: center;
                color: black;
                background-color: white;
            }
            img {
                height:  300px;
                width: 236px;
            }
        """
    )

    # Create the Anki deck
    deck_id = int(section_name.encode("utf-8").hex(), 16) % (10**10)
    deck_title = f"Penn {section_name}"
    my_deck = genanki.Deck(deck_id, deck_title)

    # Process the students to generate notes for the Anki deck
    media_files = []
    for student in students:
        if 'Name' not in student or 'imageBlob' not in student:
            print(f"Skipping student entry due to missing key: {student}")
            continue

        # Calculate the formatted name and add it to the student dictionary
        student['FormattedName'] = format_name(student)

        # Use the formatted name in the note
        formatted_name = name_format.format(**student)
        
        if include_as_blob:
            image = f'<img src="{student["imageBlob"]}" />'  # Format the base64 string as an HTML <img> tag
        else:
            image_filename = f"{student['studentId']}.jpg"
            with open(image_filename, 'wb') as img_file:
                img_file.write(base64.b64decode(student['imageBlob'].split(",")[1]))
            media_files.append(image_filename)
            image = f'<img src="{student["studentId"]}.jpg" />'  # Use the filename in the format of an HTML <img> tag

        my_note = genanki.Note(
            model=my_model,
            # build a GUID based on "anki deck generator student flashcards", Penn (the school) and the student ID
            guid="adgsf.penn.{studentId}".format(**student),
            fields=[formatted_name, image])
        my_deck.add_note(my_note)

    # Generate the Anki package
    my_package = genanki.Package(my_deck)
    if not include_as_blob:
        my_package.media_files = media_files
    my_package.write_to_file(output_filename)

    click.secho(f"Anki package generated successfully at {output_filename}!", fg="green")

@click.command()
@click.argument('json_files', nargs=-1, type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True))
@click.option('--output', default=None, type=click.Path(file_okay=True, dir_okay=False, writable=True), help='Path to save the generated Anki deck.')
@click.option('--separate-decks', is_flag=True, help='Generate separate decks for each JSON file.')
@click.option('--include-as-blob', is_flag=True, default=False, help='Embed images directly into the Anki deck. If not set, images will be saved as external files.')
@click.option('--name-format', default="{FormattedName}", help='Format for displaying names on the flashcards. Default is "{FormattedName}".')
def generate_anki_deck(json_files, output, separate_decks, include_as_blob, name_format):
    # Check if input files are provided
    if not json_files:
        click.secho("Error: No input files provided.", fg="red")
        click.secho("Use '--help' for information on how to use this tool.", fg="yellow")
        return

    all_students = []
    for json_file in json_files:
        with open(json_file, 'r') as f:
            data = json.load(f)
            all_students.extend(data)

    sections = defaultdict(list)
    for student in all_students:
        section = student["sectionInformation"]["sectionIdWithTerm"]
        sections[section].append(student)

    if separate_decks:
        for section, students in sections.items():
            if output:
                base_output = os.path.splitext(output)[0]  # Remove .apkg if present
                output_filename = f"{base_output}_{section}.apkg"
            else:
                output_filename = f"{section}.apkg"
            generate_single_deck(students, section, output_filename, include_as_blob, name_format)
    else:
        unique_section_ids = "_".join(sorted(sections.keys()))
        if output:
            base_output = os.path.splitext(output)[0]  # Remove .apkg if present
            output_filename = f"{base_output}.apkg"
        else:
            output_filename = f"{unique_section_ids}.apkg"
        generate_single_deck(all_students, unique_section_ids, output_filename, include_as_blob, name_format)

if __name__ == "__main__":
    try:
        generate_anki_deck()
    except Exception as e:
        click.secho(f"An unexpected error occurred: {e}", fg="red")
