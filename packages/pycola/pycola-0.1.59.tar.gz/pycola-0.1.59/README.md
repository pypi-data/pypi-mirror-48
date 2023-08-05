## PyCoLA : Python Module to parse the job bulletins and generate a structure file 

### Kaggle : Data Science for Good Challenge 

https://www.kaggle.com/shivamb/1-bulletin-structuring-engine-cola

## Installation 

```python
    pip install pycola 
```

## Usage 

```python
from pycola.bulletin_parser import Extractor

## define the input path
config = {
	"input_path" : "Job Bulletins/",
	"output_filename" : "structured_file.csv"
}

## create the Extractor Class object
extr = Extractor(config)

## call the extraction function
extr.extraction()
```