import io
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_path = "path/to/your/image.jpg"

# Loads the image into memory
with io.open(file_path, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)

# Performs object detection on the image file
response = client.object_localization(image=image)
localized_object_annotations = response.localized_object_annotations

print('Number of objects found: {}'.format(len(localized_object_annotations)))

for object_annotation in localized_object_annotations:
    print('\nObject name: {}'.format(object_annotation.name))
    print('Confidence: {}'.format(object_annotation.score))
    print('Normalized Vertices:')
    for vertex in object_annotation.bounding_poly.normalized_vertices:
        print('({},{})'.format(vertex.x, vertex.y))