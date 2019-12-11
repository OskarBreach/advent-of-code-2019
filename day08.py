def signal_checksum(signal, width, height):
    size = width * height
    layers = [signal[i:i + size] for i in range(0, len(signal), size)]

    min_zeros = size
    checksum = 0
    for layer in layers:
        if layer.count('0') < min_zeros:
            min_zeros = layer.count('0')
            checksum = layer.count('1') * layer.count('2')

    return checksum

def translate_signal(signal, width, height):
    size = width * height

    pixels = ''
    for pixel in range(0, size):
        pixel_candiates = [signal[i] for i in range(pixel, len(signal), size)]
        while pixel_candiates[0] == '2':
            pixel_candiates.pop(0)

        pixels += pixel_candiates[0]

    image_lines = [pixels[i:i + width] for i in range(0, len(pixels), width)]

    return '\n'.join(image_lines)  

def test1():
    print("Test 1: ")

    with open("inputs/input08.txt", "r") as f:
        print(signal_checksum(f.readline().rstrip(), 25, 6))


def test2():
    print("Test 2: ")

    with open("inputs/input08.txt", "r") as f:
        print(translate_signal(f.readline().rstrip(), 25, 6))


if __name__ == "__main__":
    test1()
    test2()