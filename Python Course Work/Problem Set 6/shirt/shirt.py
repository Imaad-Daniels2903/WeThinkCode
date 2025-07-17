
from PIL import Image, ImageOps
import sys

def main():
    images = sys.argv
    try:
        put_on_shirt(images)

    except FileNotFoundError:
        sys.exit(f"{images[1]} does not exit")


def put_on_shirt(images):
    if len(images) >= 4:
        sys.exit("Too many command-line arguments")

    elif len(images) <= 2:
        sys.exit("Too few command-line arguments")

    elif not images[1][-4:] == images[2][-4:]:
        sys.exit("Input and output have different extensions")

    elif not "." in images[1] or not "." in images[2]:
        sys.exit("Invalid imput")

    else:
        before_image, after_image = images[1], images[2]
        with Image.open(before_image) as img:
            shirt = Image.open("shirt.png")
            fitted = ImageOps.fit(img, (600, 600))
            fitted.paste(shirt, shirt)
            fitted.save(after_image)


if __name__ == "__main__":
    main()
