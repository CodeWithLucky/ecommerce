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


    max_width = 800  # set your desired max width
    max_height = 600  # set your desired max height

    img = Image.open(image)
    width, height = img.size

    if width != max_width or height != max_height:
        raise ValidationError(f'Image dimensions should be {max_width}x{max_height}px.')

