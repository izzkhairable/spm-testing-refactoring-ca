class ContactInformation:
    def __init__(self, custNm, custContact):
        self.__customerContact = custContact
        self.__customerName = custNm

    def setToAddContact(self, toAdd, toCon):
        self.__toAddress = toAdd
        self.__toContact = toCon
