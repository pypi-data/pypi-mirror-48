# texterize
`texterize` is a package that uses pixel aggregation to create ASCII art out of blocks of text.

![texterize Example Images](images/slide.png)

## Installation:
`python3 -m pip install texterize`
*Note: texterize is incompatible with Python 2.X.*

## Usage:
`Texterize` is used to create colorized ASCII art out of a given image and selection of text. Upon feeding in an image and a string of text (either through a text file (via `createFromFile()`) or through raw input via (`create()`), an image will be generated in the desired format (either HTML or MS Word).

```python
import texterize

TEXT_FILE_PATH = "./path/to/text/FILE_NAME.txt"
IMG_FILE_PATH = "./path/to/img/FILE_NAME.txt"
WRITE_PATH = "./my_texterized_image"

texterized_img_path = texterize.createFromFile(TEXT_FILE_PATH, IMG_FILE_PATH, write_path=WRITE_PATH)
```

## Methods:
### *create*
Generates a texterized image given an input string and an image file path.
#### Parameters:
- *text*: A string representing the text to use for texterization.
- *img_path*: The path to the image to be texterized.
- *write_path* (OPTIONAL): The path and filename to which the texterized file should be saved. Defaults to the working directory.
- *output_file_type* (OPTIONAL): String representing the file type the texterized output should be in. Only **"HTML"** and **"Word"** are supported. Defaults to **"HTML"**.
- *overwrite* (OPTIONAL): Boolean determining whether or not a file found with the given *`write_path`* should be overriden if found. Only applies to .docx output. Defaults to True.
#### Returns:
- The relative path to the texterized file.

### *createFromFile*
Generates a texterized image given a path to a .txt file containing the desired text and an image file path.
#### Parameters:
- *text_path*: The path to the .txt file to use in texterization.
- *img_path*: The path to the image to be texterized.
- *write_path* (OPTIONAL): The path and filename to which the texterized file should be saved. Defaults to the working directory.
- *output_file_type* (OPTIONAL): String representing the file type the texterized output should be in. Only **"HTML"** and **"Word"** are supported. Defaults to **"HTML"**.
- *overwrite* (OPTIONAL): Boolean determining whether or not a file found with the given *`write_path`* should be overriden if found. Only applies to .docx output. Defaults to True.
#### Returns:
- The relative path to the texterized file.