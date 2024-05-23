import requests
from pdf2image import convert_from_bytes
from PIL import Image

def resolve_name_to_cas(molecule_name):
    url = f"https://commonchemistry.cas.org/results?q={molecule_name}"
    response = requests.get(url)

    find = "Result: "
    start = response.text.find(find) + len(find)
    end = response.text.find(",", start)
    return response.text[start:end].strip()

def merge_images_vertically(image_list):
    images = image_list
    max_width = max(image.width for image in images)
    total_height = sum(image.height for image in images)
    merged_image = Image.new("RGB", (max_width, total_height))

    y_offset = 0
    for image in images:
        merged_image.paste(image, (0, y_offset))
        y_offset += image.height

    return merged_image

def list_companies(molecule_name, company):
    images_list = []
    CAS = resolve_name_to_cas(molecule_name)
    pdf_url = f"https://www.chemblink.com/MSDS/MSDSFiles/{CAS}{company}.pdf"
    
    response = requests.get(pdf_url)
    if response.status_code != 200:
        return False

    pdf_bytes = response.content
    images = convert_from_bytes(pdf_bytes)

    for i, image in enumerate(images):
        images_list.append(image)
    merged_image = merge_images_vertically(images_list)
    if merged_image:
         return True
    return False

def test_display_pdf_images(molecule_name):
    successful_companies = []
    companies = [
    "Alfa-Aesar", "Sigma-Aldrich", "TCI", "Acros-Organics", "Matrix",
    "Strem", "Apollo", "Combi-Blocks", "Oakwood", "Ambeed", "Syn-Quest",
    "Cayman", "Biosnyth", "SRL",
]
    for company in companies:
        success = list_companies(molecule_name, company)
        if success:
            successful_companies.append(company)
    return successful_companies
    
def display_pdf_images(molecule_name, company):
    images_list = []
    CAS = resolve_name_to_cas(molecule_name)
    pdf_url = f"https://www.chemblink.com/MSDS/MSDSFiles/{CAS}{company}.pdf"
    
    response = requests.get(pdf_url)
    if response.status_code != 200:
        return 

    pdf_bytes = response.content
    images = convert_from_bytes(pdf_bytes)

    for i, image in enumerate(images):
        images_list.append(image)
    merged_image = merge_images_vertically(images_list)
    if merged_image:
        return merged_image
