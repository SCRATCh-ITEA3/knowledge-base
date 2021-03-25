"""
Author: M.A. Marosvolgyi 2021
(c)Anywi
"""

import json 
import pdb 

FILENAME = "Mapping-of-Code-of-Practice-to-recommendations-and-standards_v4.json"
GUIDEKEY = "DCMS Code of Practice Guidelines Number"
ORGANIZATIONKEY = "Organisation"

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

        return occ

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