#!/usr/bin/env python
# coding: utf-8

# In[8]:


class PostcardList():
    
    def __init__(self, _file, _postcards, _date, _from, _to):
        """
        class initializer: 
        _file is the file name (or path);
        _postcards is the list of postcards read from _file;
        _date is a dict: "date" string is key, each index refers to the corresponding record;
        _from is a dict: the sender name is key, each index refers to the corresponding record;
        _to is a dict: the receiver is key, each index refers to the corresponding record.
        """
        self._file = _file
        self._postcards = []
        self._date = {}
        self._from = {}
        self._to = {}
        
        
    def __iter__(self):
        """
        a function used for unpacking class members
        """
        return (i for i in (self._postcard, self._date, self._from, self._to))
    
    
    def __eq__(self, other):
        """
        a function used to assert equivalence between class instances
        """
        return tuple(self)==tuple(other)
    
    
    def writeFile(self, nomefile): 
        """
        this function writes postcards to an outfile "nomefile"
        """
        self._file = nomefile
        out_file = open(self._file,"w")
        
        for i in self._postcards:
            out_file.write(i)
            out_file.write("\n")
            
        out_file.close()
        
        
    def readFile(self, nomefile):
        """
        this function reads postcards from an outfile "nomefile"
        """
        self._file= nomefile
        with open(self._file) as f:
            content = f.readlines()
        self._postcards = [x.strip() for x in content]            #until here i stored every line in content
            
            
    def parsePostcards(self):
        """
        this function updates the dictionaries with already stored postcards
        """
        for i in range(len(self._postcards)):
            date,sender,receiver = self._postcards[i].split("; ") #now I split date, sender and receiver.
            if date not in self._date:
                self._date[date] = []
            self._date[date].append(i)
            if sender not in self._from:
                self._from[sender] = []
            self._from[sender].append(i)
            if receiver not in self._to:
                self._to[receiver] = []
            self._to[receiver].append(i)
            
    
    def updateFile(self, nomefile):
        """
        this function appends postcards to an outfile "nomefile"
        """
        self._file = nomefile
        out_file = open(self._file,"a") #the option "a" appends to an existing file
        
        for i in self._postcards:
            out_file.write(i)
            out_file.write("\n")
            
        out_file.close()
        

    def updateLists(self, nomefile):
        """
        this function reads postcards from an outfile and appends them to
        self._postcards
        """
        self._file= nomefile
        with open(self._file) as f:
            content = f.readlines()
        content = [x.strip() for x in content] #until here i stored every line in content
        
        for i in range(len(content)):
            self._postcards.append(content[i])
            
        nomefile.close()
           
            
    def getNumberOfPostcards(self):
        """
        this function returns the number of postcards read
        """
        return len(self._postcards)
    
    
    def getPostcardsByDateRange(self,date_range):
        """
        this function returns all the postcards within a given date_range
        """
        returned_postcards = [];
        for key in self._date:
            if (key < date_range):
                for value in self._date[key]:
                    returned_postcards.append(self._postcards[value])
        
        return returned_postcards
    
    
    def getPostcardsBySender(self, sender):
        """
        this function returns all the postcards from a given sender
        """
        returned_postcards = [];
        for key in self._from:
            if (key == sender):
                    for value in self._from[key]:
                        returned_postcards.append(self._postcards[value])
        
        return returned_postcards
    
        #i = 0
        #while i < len(self._postcards):
        #    d,f,t = self._postcards[i].split(" ")
        #    
        #    if f != sender:
        #        del self._postcards[i]
        #    else:
        #        i += 1        
                
                
    def getPostcardsByReceiver(self, receiver):
        """
        this function returns all the postcards to a given receiver
        """
        returned_postcards = [];
        for key in self._to:
            if (key == receiver):
                    for value in self._to[key]:
                        returned_postcards.append(self._postcards[value])
        
        return returned_postcards
               
        #i = 0
        #while i < len(self._postcards):
        #    d,f,t = self._postcards[i].split(" ")
        #    
        #    if t != receiver:
        #        del self._postcards[i]
        #    else:
        #        i += 1 


# In[9]:


#p = postcardclass("txt", [], {}, {}, {})
#p._postcards = ["date:2013-09-16; from:Dewey; to:Happy;", "date:2017-03-31; from:Mickey; to:Pluto;", "date:2011-08-24; from:Dewey; to:Dopey;"]
#p.writeFile("txt") #scrivo su file


#p2 = postcardclass("txt", [], {}, {}, {})
#p2.readFile("txt") #leggo su file

#guardo se ha letto correttamente
#print(p2._postcards)
#print(p2._date) #in realtà non ha molto senso far leggere anche i singoli elementi perché con l'update nei dictionary
#si sovrascrivono gli elementi uguali (vedi i "from")
#print(p2._from)
#print(p2._to)


# In[10]:


#p3 = postcardclass("txt", [], {}, {}, {})
#p3._postcards = ["date:2010-06-23; from:Sneezy; to:Alice;", "date:2011-08-04; from:Louie; to:Grumpy;"]
#p3.updateFile("txt") #qui aggiorno il file


# In[11]:


#p2._postcards #qui ho le postcard iniziali


# In[12]:


#p._postcards == p2._postcards #serve per capire il bug di dopo


# In[13]:


#p2.updateLists("txt")#qui le aggiorno
#p2._postcards


# In[14]:


###########ATTENZIONE###############
#p._postcards #qui ho le postcard iniziali uguali a quelle di p2!! Ma siccome nella classe le comparo con quelle
#del self e p.self != p2.self, allora se aggiorno quelle di p, queste si duplicano


# In[15]:


#p.updateLists("txt")#qui le aggiorno
#p._postcards


# In[16]:


#Inoltre se si continua a eseguire
#p2.updateLists("txt")#qui le aggiorno
#p2._postcards
#allora p2._postcards continua ad allungarsi


# In[17]:


#p2.getNumberOfPostcards()


# In[18]:


#p2.getPostcardsBySender("from:Dewey;")
#p2._postcards


# In[19]:


#p2.getPostcardsByReceiver("to:Happy;")
#p2._postcards


# In[ ]:



