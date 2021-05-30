from simpleimage import SimpleImage

GREEN = 127
BLUE = 127

CANVAS_WIDTH = 1390
CANVAS_HEIGHT = 200

FRACTION_DATA = 'data-climate.txt'

def main():
    canvas = SimpleImage.blank(CANVAS_WIDTH, CANVAS_HEIGHT)
    data = frac_values()
    number_stripes = int(data[0])
    stripe_width = CANVAS_WIDTH // number_stripes
    stripe_height = CANVAS_HEIGHT
    stripe_img = SimpleImage.blank(stripe_width, stripe_height)
    for index in range(number_stripes):
        start_x = index * stripe_width
        red_fraction = data[index + 1]
        blue_fraction = 1 - data[index + 1]
        green_fraction = 1 - data[index + 1]
        stripe_img = make_colored_stripe(stripe_img, blue_fraction, green_fraction, red_fraction)
        canvas = put_stripe_img(canvas, stripe_img, start_x)
    canvas.show()

def frac_values():
    frac_values = []
    with open(FRACTION_DATA) as f:
        next(f)
        for line in f:
            frac_values.append(float(line.strip()))
    return frac_values

def make_colored_stripe(stripe_img, blue_fraction, green_fraction, red_fraction):
    for pixel in stripe_img:
        pixel.green = green_fraction * GREEN
        pixel.blue = blue_fraction * BLUE
        #pixel.green = GREEN
        #pixel.blue = BLUE
        pixel.red = red_fraction * 255
    return stripe_img

def put_stripe_img(canvas, stripe_img, start_x):
    for y in range(stripe_img.height):
        for x in range(stripe_img.width):
            pixel = stripe_img.get_pixel(x, y)
            canvas.set_pixel(x + start_x, y, pixel)
    return canvas

if __name__ == '__main__':
    main()
