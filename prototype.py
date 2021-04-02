"""
Author: M.A. Marosvolgyi 2021
(c)Anywi
"""

import json 
import pdb 
import doctest

FILENAME = "Mapping-of-Code-of-Practice-to-recommendations-and-standards_v4.json"
GUIDEKEY = "DCMS Code of Practice Guidelines Number"
ORGANIZATIONKEY = "Organisation"

"""
guide names
"""

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
    """
        Processor returns an object which can do manipulations
        on the set of guides. 

        :param guides: list of guides 
        :type guides: CodeOfPracticeGuide

        example:
        
        >>> import prototype as pt
        >>> list = processor.getOccurencesOfOrganisation(["IEEE"])
        >>> print (pt.propsOf(list[0]))
        GuideLine No: 1
        IEEE
        IoT Security Principles and Best Practices
        5
        IoT devices should not use easy-to-guess username/password credentials, such as admin/admin. Devices should not use default credentials that are invariant across multiple devices and should not include back doors and debug-mode settings (secret credentials established by the device's programmer) because, once guessed, they can be used to hack many devices. 
        Each device should have a unique default username/password, perhaps printed on its casing, and preferably resettable by the user. Passwords should be sophisticated enough to resist educated guessing and so-called brute force methods.
        https://internetinitiative.ieee.org/images/files/resources/white_papers/internet_of_things_feb2017.pdf
        Use strong authentication
        1

    """

    def __init__(self, guides):

        self.guides = guides
        self.setOfOrganisations = self.generateSetOfOrganisations()

    def generateSetOfOrganisations(self):
        """
            Generates a set of all organisations occuring in 
            all guides.
        """
        organisations = set()
        for i, element in enumerate(self.guides):
            organisations.add(element.Organisation)

        return organisations

    def getOccurencesOfOrganisation(self, organisations):
        """
            Returns an ordered list (by Guide ID) of guides
            which belong to organisations listed in the 
            argument variable (list) organisations.

            :params organisations: list of organisations
            :type: list of CodeOfPractiveGuideline
            :return: sorted list of guides
        """
        occ = []
        for organisation in organisations:    
            if organisation in self.setOfOrganisations:
                for i, e in enumerate(self.guides):
                    if (e.Organisation == organisation):
                        occ.append(e)
        #https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects                        
        return sorted(occ, key=lambda x: int(x.DCMSCodeOfPracticeGuideLinesNumber), reverse=False)

    def getMatrix(self):
        """
            Return matrix of guides against organisations involved
        """

        numberOfOrganisations = len(self.setOfOrganisations)
        numberOfCoPs = len(guideNames)

        # Initialize nested list, we call it 'matrix' 
        matrix = [['']*numberOfOrganisations] * numberOfCoPs

        # In order to gen the table we need an ordered set set of 
        # organisations. 

        coordinateOfOrganisations = list(self.setOfOrganisations)

        for g in self.guides:
            pass

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
    if (id in [1,2,3,4,5,6,7,8,9,10,11,12,13]):
        return guideNames['CoP {0}'.format(id)]
    else:
        return "ID Nr NOT FOUND"

if __name__ == '__main__':
    gl = CodeOfPracticeReader()
    gl.setup()

    guides = gl.getGuides()

    processor = Processor(guides)

    list = processor.getOccurencesOfOrganisation(["IEEE"])

    print (propsOf(list[0]))




    #pdb.set_trace()

    """
    org0 = gl.listOrganizations()[0]
    print (org0)
    gl.listGuideLineOfOrganization(org0)
    """