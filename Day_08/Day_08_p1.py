def slice(input_data, width, height):

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

image = slice(image_data, width, height)

for idx, layer in enumerate(image):
    for row in layer:
        zero_sum += str(row).count("0")

    if zero_sum < zero_min:
        zero_min = zero_sum
        zero_min_index = idx
    zero_sum = 0

ones = 0
twos = 0
for row in image[zero_min_index]:
    ones += str(row).count("1")
    twos += str(row).count("2")

print(ones * twos)
