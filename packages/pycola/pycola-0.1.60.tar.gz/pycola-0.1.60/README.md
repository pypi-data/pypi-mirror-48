## PyCoLA : Python Module to parse the job bulletins and generate a structure file 

### Kaggle : Data Science for Good Challenge 

https://www.kaggle.com/shivamb/1-bulletin-structuring-engine-cola

## Installation 

```python
    pip install pycola 
```

## Usage 

Extractor class is used to generate the structured csv file. It accepts one user input config:

"input_path" : path of the bulletin text files    
"output_filename" : name of the output file   

```python
from pycola.bulletin_parser import Extractor

## define the input path
config = {
	"input_path" : "Bulletins/",
	"output_filename" : "structured_file.csv"
}

## create the Extractor Class object
extr = Extractor(config)

## call the extraction function
extr.extraction()
```

## Documentation 

http://www.shivambansal.com/blog/network/cola/BulletinStructuringEngine.html    

By Shivam Bansal