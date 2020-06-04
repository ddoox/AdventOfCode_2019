def prepare(input_data, width, height):

    layers_quanity = int(len(image_data) / (width * height))
    sliced = []
    layers = []

    for current_layer in range(0, layers_quanity * height):
        index1 = current_layer * width
        index2 = ((current_layer + 1) * width) - 1
        sliced.append(image_data[index1:index2 + 1])
    for layer_number in range(0, layers_quanity):
        index1 = layer_number * height
        index2 = (layer_number * height) + height
        layers.append(sliced[index1:index2])
    return layers


width = 25
height = 6
with open("../input", "r") as file:
    image_data = file.read()

zero_sum = 0
zero_min = width * height
zero_min_index = 0

image = prepare(image_data, width, height)
final_image = [["2" for col in range(width)] for row in range(height)]

for layer in image:
    for wid in range(0, height):
        for hei in range(0, width):
            if final_image[wid][hei] == "2":
                final_image[wid][hei] = layer[wid][hei]

for line in final_image:
    for digit in line:
        if digit == "0":
            print(" ", end="")
        else:
            print(".", end="")
    print()
