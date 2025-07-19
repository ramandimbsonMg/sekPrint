import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

def generate_qrcode(data):
    qr = qrcode.make(data)
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    return ContentFile(buffer.getvalue(), name='qr_code.png')
