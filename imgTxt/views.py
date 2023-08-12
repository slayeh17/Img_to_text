from django.shortcuts import render
from django.http import JsonResponse
import pytesseract
from PIL import Image
import requests
from urllib.parse import unquote
from io import BytesIO

def extract_text_from_image(request):
    if request.method == 'POST':
        image_url = request.POST.get('image_url')
        response = requests.get(image_url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            extracted_text = pytesseract.image_to_string(image)
            
            text_lines = extracted_text.split('\n')
            text_lines_cpy = []
            for text in text_lines:
                if len(text) > 1:
                    text_lines_cpy.append(text.capitalize())
            text_dict = {f'{i + 1}': line.strip() for i, line in enumerate(text_lines_cpy)}
            
            return JsonResponse(text_dict)
        else:
            return JsonResponse({'error': 'Failed to download image'})
    return render(request, 'imgTxt/layout.html')

def extract_text_api(request):
    image_url = request.GET.get('url')

    if image_url:
        decoded_image_url = unquote(image_url)
        response = requests.get(decoded_image_url)
        
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            extracted_text = pytesseract.image_to_string(image)

            text_lines = extracted_text.split('\n')
            text_dict = {f'line_{i + 1}': line.strip() for i, line in enumerate(text_lines) if line.strip()}

            return JsonResponse(text_dict)
        else:
            return JsonResponse({'error': 'Failed to download image'})
    else:
        return JsonResponse({'error': 'Missing or invalid URL parameter'})
