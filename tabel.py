# crawler v1.0
# In this version, constructor will create a crawler object,
# give it some default constructor (based on the default
# values spec'd at api.tabelog.com).
# crawl() will make contiguous calls to makeURL() to build
# api param URL then call writeToFile() to create .xml file
# with each page of return appended to each other


# Required libraries:
#  - urllib2
#  - os


# Later versions will give the user options about how to handle
# return data (write to sql-type database, put in hash table
# (dictionary), etc.)

 

from urllib2 import Request, urlopen, URLError, HTTPError
import os

class crawler:

    def __init__( self , apiKey ):
        """
        apiKey: 40-digit string, user's API Key

        Will construct a crawler object using key

        """
        
        self.__key = apiKey
        self.__pagenumber = 0
        self.__PAGEMAX = 60
        self.__MAXPARAMS = 11
        self.__nbParams = 0

        # set default values
        self.setLatitude("")
        self.setLongitude("")
        self.setStation("")
        self.setResultSet("")
        self.setSortOrder("")
        self.setResultDatum("")
        self.setSearchRange("")
        self.setPrefecture("")
        # Default file will be in pwd named temp.xml
        self.setOutputFile(os.getcwd()+'/temp.xml')

        
########
# SETS #
########

        # API REQUEST PARAMETERS #
    def setLatitude(self,Latitude):
        """
        Latitude (Japan only)

        Default: null
        """
        self.__latitude = Latitude

    def setLongitude(self,Longitude):
        """
        Longitude (Japan only)

        Default: null
        """
        self.__longitude =Longitude

    def setStation(self,Station):
        """
        Nearest station name
        
        Default: null
        """
        self.__station = Station

    def setResultSet(self,ResultSet):
        """
        Default: small
        """
        self.__resultset = ResultSet

    def setSortOrder(self,SortOrder):
        """
        Sort ordering

        Default: reviewcount
        """
        self.__sortorder = SortOrder

    def setResultDatum(self,ResultDatum):
        """
        (Valid only when the latitude and longitude are specified)

        Default: world
        """
        self.__resultdatum = ResultDatum

    def setSearchRange(self,SearchRange):
        """
        (Valid only when the latitude and longitude are specified)

        Default: medium
        """
        self.__searchrange = SearchRange

    def setPrefecture(self,Prefecture):
        """
        State
        
        Default: japan
        """
        self.__prefecture = Prefecture

        # RETURN PARAMETERS #
    def setOutputFile( self , FileName ):
        """
        
        """
        self.__OutputFile = FileName
        

    
########
# GETS #
########

    def getKey(self):
        
        return self.__key

    def getLatitude(self):
        
        return self.__latitude

    def getLongitude(self):

        return self.__longitude

    def getStation(self):
        
        return self.__station

    def getResultSet(self):
        
        return self.__resultset

    def getSortOrder(self):
        
        return self.__sortorder

    def getResultDatum(self):
        
        return self.__resultdatum

    def getSearchRange(self):
        
        return self.__searchrange

    def getPageNumber(self):
        
        return self.__pagenumber
    


###########
# WORKERS #
###########

    def countParams(self):
        s = 1

        if self.__latitude == "":
            s+=1

        if self.__longitude == "":
            s+=1
 
        if self.__station == "":
            s+=1
    
        if self.__resultset == "":
            s+=1

        if self.__sortorder == "":
            s+=1
       
        if self.__resultdatum == "":
            s+=1
       
        if self.__searchrange == "":
            s+=1

        if self.__prefecture == "":
            s+=1
        
        if self.__pagenumber == "":
            s+=1
        
        return self.__MAXPARAMS - s

    def crawl(self):
        """

        CRAWL: calls __makeURL() to build the URL, writes the 
        output to __OutputFile under mode 'a'


        returns: 
        
        nbCalls - number of calls used in this crawl

        """

        print "Ok, I'm crawling now!"

        # open file
        fp = open(self.__OutputFile,'a')

        
        for page in range(1,61):
            
            # build url
            self.__pagenumber += 1
            URL = self.__makeURL()
            
            # request and write
            try:
                urlf = urlopen(URL)
                fp.write(urlf.read())
                
            # handle error
            except HTTPError, e:
                print "HTTP Error:",e.code,URL
            except URLError, e:
		print "URL Error:",e.reason , URL
                
             
   
        # close file
        fp.close()
        return self.__pagenumber        
                



    def __makeURL(self):
        
        URL = 'http://api.tabelog.com/Ver2.1/RestaurantSearch/?'      
        
        paramLat = "Latitude=%s" % (self.__latitude)
        
        paramLon = "Longitude=%s" % (self.__longitude)

        paramPgNum = "PageNum=%s" % (self.__pagenumber)

        paramKey = "Key=%s" % (self.__key)

        params = "&".join((paramLat,paramLon,paramPgNum,paramKey))
        # just try this for now
        return "".join((prefix,params))


        
