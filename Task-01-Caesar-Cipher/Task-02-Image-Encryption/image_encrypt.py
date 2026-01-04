from PIL import Image

img = Image.open("input.jpg")  # use your image name
pixels = img.load()

for x in range(img.width):
    for y in range(img.height):
        r, g, b = pixels[x, y]
        pixels[x, y] = (255 - r, 255 - g, 255 - b)

img.save("encrypted.png")
print("Image encrypted successfully")
