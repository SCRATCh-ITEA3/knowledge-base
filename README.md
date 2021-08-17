# UK's Code of Practice for Consumer IoT Security mapping to global recommendations and standards as published by UK Department for Digital, Culture, Media & Sport#

### Source of the data set is https://iotsecuritymapping.uk/open-data-files-latest-v4/

### This tool has two components
1. A backend that downloads /reads the sourcefiles from the Url above and transcripts the information into a new data structure.
2. A front end allows for making structures/filters and export of the information.

The Code of Practice for Consumer IoT Security contains 13 highlevel requirements that can be compared with the OWASP top ten for IoT security.
The interessting part of this dataset is the mapping of these 13 highlevel requirements to a wide variaty of international standards and guidelines. 
There are over a 1000 records in this mapping. Organized by organisation that published a certain standard or guideline. About 47 organisations are investigated.
The dataset was published in 2018 and had 4 revisions, there is no information on how regular the data set is updated.
 

##Structure of the tool##
XX.py looks for update of Mapping-of-Code-of-Practice-to-recommendations-and-standards_v4.json on the DCMS website, if update available it will be donloaded as latest version.
prototype.py converts the latest Mapping-of-Code-of-Practice-to-recommendations-and-standards_vx.json file to a internal datastructure in memory.
by executing ui.py in powershell or unixscript a flask webserver will initiated on port 5000.
opening http://localhost:5000 will open the interface page to the data stored in memory.


## Implementation
see knowledge-base/build/latex/practice2standards.pdf


### docker
automation by use of docker

```bash
docker build -t scratchkb . && docker run -i -p 5000:5000 scratchkb
```

## Demo of tool

https://scratch-kb.cloud.consider-ip.com/


### Disclaimer: 
The information in this database is for general guidance and is not to be relied upon as professional advice. DCMS has tried to ensure that the information on this database is accurate and up to date. DCMS will not accept liability for any loss and/or damage or inconvenience arising as a consequence of any use of or the inability to use any information on this website. DCMS endeavours to provide a reliable service; DCMS does not guarantee that its service will be uninterrupted or error-free. DCMS shall not be responsible for claims brought by third parties arising from your use of this database. DCMS assumes no responsibility for the contents of linked websites. The inclusion of any link should not be taken as endorsement of any kind by DCMS of the linked website or any association with its operators. DCMS has no control over the availability of the linked pages. 
Copyright: The copyright of the original material remains that of the original authors and any usage of excerpts in the mapping is made under fair use. References to organisations do not imply endorsement by DCMS.
