import requests
import io
from pdf2image import convert_from_bytes
from PIL import Image


def resolve_name_to_cas(molecule_name):
    
        # Construct the URL for the CIR service
    url = f"https://commonchemistry.cas.org/results?q={molecule_name}"

        # Send a GET request to the CIR service
    response = requests.get(url)

    find = "Result: "
    start=response.text.find(find)+len(find)
    end = response.text.find("," ,start)
    return response.text[start: end]

def merge_images_vertically(image_list):
    # Open all images
    images = image_list

    # Find maximum width and total height
    max_width = max(image.width for image in images)
    total_height = sum(image.height for image in images)

    # Create a new blank image with the maximum width and total height
    merged_image = Image.new("RGB", (max_width, total_height))

    # Paste each image onto the blank image
    y_offset = 0
    for image in images:
        merged_image.paste(image, (0, y_offset))
        y_offset += image.height

    return merged_image

def display_pdf_images(molecule_name):
    images_list = []
    CAS = resolve_name_to_cas(molecule_name)
    # Download the PDF from the URL
    pdf_url = f"https://www.chemblink.com/MSDS/MSDSFiles/{CAS}Sigma-Aldrich.pdf"
    response = requests.get(pdf_url)
    if response.status_code != 200:
        print(f"Failed to download PDF from {pdf_url}. Status code: {response.status_code}")
        return

    # Convert the downloaded PDF bytes to images
    pdf_bytes = response.content
    images = convert_from_bytes(pdf_bytes)

    # Display each image
    for i, image in enumerate(images):
        # Display the image
        images_list.append(image)
    
    return merge_images_vertically(images_list)
    
# Example usage

display_pdf_images("Dichloromethane")
