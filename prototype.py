"""
Author: M.A. Marosvolgyi 2021
(c)Anywi
"""

import json 
import pdb 

FILENAME = "Mapping-of-Code-of-Practice-to-recommendations-and-standards_v4.json"
GUIDEKEY = "DCMS Code of Practice Guidelines Number"
ORGANIZATIONKEY = "Organisation"

guideNames = {
    'CoP 1':'No default passwords',
    'CoP 2':'Implement a vulnerability disclosure policy',
    'CoP 3':'Keep software updated',
    'CoP 4':'Securely store credentials and security-sensitive data',
    'CoP 5':'Communicate securely',
    'CoP 6':'Minimise exposed attack surfaces',
    'CoP 7':'Ensure software integrity',
    'CoP 8':'Ensure that personal data is protected',
    'CoP 9':'Make systems resilient to outages',
    'CoP 10':'Monitor system telemetry data',
    'CoP 11':'Make it easy for consumers to delete personal data',
    'CoP 12':'Make installation and maintenance of devices easy',
    'CoP 13':'Validate input data',
}

class Processor(object):

    def __init__(self, guides):

        self.guides = guides
        self.setOfOrganisations = self.generateSetOfOrganisations()

    def generateSetOfOrganisations(self):

        organisations = set()
        for i, element in enumerate(self.guides):
            organisations.add(element.Organisation)

        return organisations

    def getOccurencesOfOrganisation(self, organisations):
        occ = []
        for organisation in organisations:    
            if organisation in self.setOfOrganisations:
                for i, e in enumerate(self.guides):
                    if (e.Organisation == organisation):
                        occ.append(e)
        #https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects                        
        return sorted(occ, key=lambda x: int(x.DCMSCodeOfPracticeGuideLinesNumber), reverse=False)

class CodeOfPracticeGuideline( object ):
    """ 
        Fields:
            DCMS Code of Practice Guidelines Number
            Organisation
            Standard / Recommendation Name
            Recommendation Number / Section
            Recommendation Extracted from Linked Source
            Web Link
            Notes
            Added at Version
         
    """
    def __init__(self):

        self.DCMSCodeOfPracticeGuideLinesNumber = ""
        self.GuideName = ""
        self.Organisation = ""
        self.StandardOrRecommendationName = ""
        self.RecommendationNumberOrSection = ""
        self.RecommendationExtractedFromLinkedSource = ""
        self.WebLink = ""
        self.Notes = ""
        self.AddedAtVersion = ""

class CodeOfPracticeReader( object ):

    def __init__(self):
        self.f = open(FILENAME, 'r')
        self.data = json.load(self.f)
        self.organizations = set()
        
    def setup(self):
        self.generateOrganizationsSet()

    def getGuides(self):

        guides = []

        for item in self.data:
            if GUIDEKEY in item:
                guideItem = CodeOfPracticeGuideline()
                guideItem.DCMSCodeOfPracticeGuideLinesNumber = item["DCMS Code of Practice Guidelines Number"]
                guideItem.GuideName = translateGuideId2GuideName(int(guideItem.DCMSCodeOfPracticeGuideLinesNumber))
                guideItem.Organisation = item["Organisation"]
                guideItem.StandardOrRecommendationName = item["Standard / Recommendation Name"]
                guideItem.RecommendationNumberOrSection = item["Recommendation Number / Section"]
                guideItem.RecommendationExtractedFromLinkedSource = item["Recommendation Extracted from Linked Source"]
                guideItem.WebLink = item["Web Link"]
                guideItem.Notes = item["Notes"]
                guideItem.AddedAtVersion = item["Added at Version"]
                guides.append(guideItem)

        return guides

    def generateOrganizationsSet(self):

        for item in self.data:
            if ORGANIZATIONKEY in item:
                self.organizations.add(item[ORGANIZATIONKEY])

    def listOrganizations(self):
        return list(self.organizations)

    def listGuideLineOfOrganization(self, organization):
        if organization in self.organizations:
            for element in self.data:
                #print (element)
                if organization in element:
                    print (element)

def propsOf(l):

    print("GuideLine No: {0}".format(l.DCMSCodeOfPracticeGuideLinesNumber))
    print(l.Organisation)
    print(l.StandardOrRecommendationName)
    print(l.RecommendationNumberOrSection)
    print(l.RecommendationExtractedFromLinkedSource)
    print(l.WebLink)
    print(l.Notes)
    print(l.AddedAtVersion)
    print ()

def translateGuideId2GuideName(id):
    return guideNames['CoP {0}'.format(id)]

if __name__ == '__main__':
    gl = CodeOfPracticeReader()
    gl.setup()

    guides = gl.getGuides()

    processor = Processor(guides)

    list = processor.getOccurencesOfOrganisation(["IEEE"])

    for l in list:
        print (propsOf(l))





    #pdb.set_trace()

    """
    org0 = gl.listOrganizations()[0]
    print (org0)
    gl.listGuideLineOfOrganization(org0)
    """