from PIL import Image

def encode_message(image_path, message):
    img = Image.open(image_path)
    img = img.convert("RGB")
    encoded = img.copy()

    width, height = img.size
    message += chr(0)  # Add a null character to signify the end of the message

    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            if index < len(message):
                char = message[index]
                encoded.putpixel((col, row), (r, ord(char), b))
                index += 1
            else:
                break
    encoded_path = f"{image_path.split('.')[0]}_encoded.png"
    encoded.save(encoded_path)
    return encoded_path.split('/')[-1]

def decode_message(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")

    width, height = img.size
    message = ""
    for row in range(height):
        for col in range(width):
            _, g, _ = img.getpixel((col, row))
            if g == 0:  # Null character signifies the end
                return message
            message += chr(g)
    return message
