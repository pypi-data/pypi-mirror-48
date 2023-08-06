# pixit
Label and annotate images using matplotlib widgets.

# Installation
`pip install pixit`

# Usage
## ImageSet
The `ImageSet` data structure is derivative of the `Bunch` from scikit-learn. It is a dictionary-like object whose keys can be accessed as attributes. The `image` entry of the ImageSet should be a numpy array with images to be displayed using matplotlib. 

## label_images
The `label_images` method of `ImageSet` brings up a matplotlib GUI for labeling images as one of the `label_names`.

```python
from pixit import datasets

animals = datasets.load_animals()
print(animals.label_names) # ['elephant', 'giraffe', 'tiger', 'zebra']

animals.label_images()
```

## annotate_images
In development.
