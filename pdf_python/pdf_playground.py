import PyPDF2
# Takes a pdf rotates it and puts the rotated version in a different pdf
with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))

    # Get the first page
    page = reader.pages[0]

    # Rotate the first page 90 degrees clockwise
    page.rotate(90)

    # Create a PdfWriter object
    writer = PyPDF2.PdfWriter()

    # Add the rotated page to the writer
    writer.add_page(page)

    # Write the modified content to a new PDF
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
