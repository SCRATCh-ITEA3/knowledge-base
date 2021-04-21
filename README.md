# mapping of code of practice to recommendations and standards

Aim is to help navigate the mapping database.

https://iotsecuritymapping.uk/open-data-files-latest-v4/



There are two components in this project. The backend which reads the database from local file or
web-resource and stores the data in a structure.

The front end allows for making structures/filters and export.

## Use
Execute either the native python code or use the docker version.
Then open a browser and go to `localhost:5000`


### native
Start by

```bash
python3 ui.py
```
### docker

```bash
docker build -t scratchkb . && docker run -i -p 5000:5000 scratchkb
```
