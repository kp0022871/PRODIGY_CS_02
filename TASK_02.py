from PIL import Image
def encrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    image = image.convert("RGB")
    width, height = image.size
    key_bytes = bytes(key, 'utf-8')
    key_length = len(key_bytes)
    encrypted_image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            r ^= key_bytes[(x * y) % key_length]
            g ^= key_bytes[((x * y) + 1) % key_length]
            b ^= key_bytes[((x * y) + 2) % key_length]
            encrypted_image.putpixel((x, y), (r, g, b))
    encrypted_image.save(output_image_path)
def decrypt_image(input_image_path, output_image_path, key):
    encrypted_image = Image.open(input_image_path)
    width, height = encrypted_image.size
    key_bytes = bytes(key, 'utf-8')
    key_length = len(key_bytes)
    decrypted_image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            r, g, b = encrypted_image.getpixel((x, y))
            r ^= key_bytes[(x * y) % key_length]
            g ^= key_bytes[((x * y) + 1) % key_length]
            b ^= key_bytes[((x * y) + 2) % key_length]
            decrypted_image.putpixel((x, y), (r, g, b))
    decrypted_image.save(output_image_path)
input_image = "C:\\wamp64\\www\\html css\\NOT useful\\gaming1.jpeg"
encrypted_image = "encrypted_image.jpg"
decrypted_image = "decrypted_image.jpg"
encryption_key = "secretkey"
encrypt_image(input_image, encrypted_image, encryption_key)
decrypt_image(encrypted_image, decrypted_image, encryption_key)
print("Encryption and decryption successful.")
