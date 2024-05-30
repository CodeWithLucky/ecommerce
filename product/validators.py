import os
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from PIL import Image

def validate_image_format(image):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.img']
    ext = os.path.splitext(image.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError(f'Unsupported file extension. Allowed extensions are: {", ".join(valid_extensions)}')

    try:
        img = Image.open(image)
        img.verify()  # Verify that it is an image
    except (IOError, SyntaxError) as e:
        raise ValidationError('Invalid image file')

