# BinaryPipe

binarypipe provides easy pipeline to use different binary format files in different Machine Larning models.

#### Installation

```bash
pip install binarypipe
```

### ImagePipe

imagepipe provides utilities to use image datasets in ML models

* import imagepipe

```python
from binarypipe import imagepipe as ip
```

* Load single image file

```python
# Load image
img= ip.load("path/image.jpg")

# Load in certain size
img= ip.load("path/image.jpg", size= (400, 600))
```

* Load all images of folder as dataset

```python
X, y= ip.load_dataset("folder_path/", 0)
# X= (?, width, height, channel)
# y is label 
```

* Load multiple class images 

```python
X, y= ip.load_datasets("folder_path/", )
```


