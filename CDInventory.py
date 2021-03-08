#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
#Muthu , 03-05-2021 , Created CDInventory file with objects
#Muthu , 03-06-2021 , updated program to read / write binary file
#Muthu , 03-07-2021 , updated docstrings
#------------------------------------------#
import pickle

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        strId: (int) with CD ID
        strTitle: (string) with the title of the CD
        strArtist: (string) with the artist of the CD
    methods:

    """

    def __init__(self,localID,localTitle,localArtist):
         self.__strID = localID
         self.__strArtist=localArtist
         self.__strTitle=localTitle
    
    @property    
    def strID(self):
        return self.__strID
    @property
    def strTitle(self):
        return self.__strTitle.title()
    @property
    def strArtist(self):
        return self.__strArtist.title()
    
    @strID.setter
    def strID(self,value):
        if not str(value).isnumeric():
            raise Exception("ID must be an integer")
        else:
            self.__strID = value

    @strArtist.setter
    def strArtist(self,value):
        if str(value).isnumeric():
            raise Exception("Artist must have string")
        else:
            self.__strTopic = value

    @strTitle.setter
    def strTitle(self,value):
        if str(value).isnumeric():
            raise Exception("Title must have string")
        else:
            self.__strTitle = value

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """

    @staticmethod
    def load_inventory(strFileName):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        locallstOfCDObjects=[]
        try:
            with open(strFileName, 'rb') as file_handle:
                locallstOfCDObjects.clear()
                lstoflst = pickle.load(file_handle)
            for data in lstoflst: 
                obj=CD(data[0],data[1],data[2])
                locallstOfCDObjects.append(obj)
        except:
            print("Error opening file, creating new database")
            with open(strFileName, 'wb') as file_handle:
                pass
            
        return(locallstOfCDObjects)

    @staticmethod
    def save_inventory(strFileName,lstOfCDObjects):
        """Function to write data from list of dictionaries to a file

        Reads the data from 2D table row by row 
        Create a list with values from the key value pair of each row
        Join the contents of this list with a "," seperator 
        Write the list to the file
      
        Args:
            file_name (string): name of file used to write the data
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        
        lstTable=[]
        lstValues=[]
        for item in lstOfCDObjects:
            lstValues=[]
            lstValues.append(str(item.strID))
            lstValues.append(item.strTitle)
            lstValues.append(item.strArtist)
            lstTable.append(lstValues)
        with open(strFileName,'wb') as objFile:    
            pickle.dump(lstTable,objFile)
        
    

    pass

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Add/Delete new CD Data entered by user to/from the table
        Print menu . capture users choice , show inventory 
        methods :
                 print_menu () -> None 
                 menu_choice() -> returns choice
                 show_inventory(listofCDObjects) -> None
                 ask_details() -> returns id , title and artist 
                 add_cd(id,title,artist) --> None
                 delete_cd(id,listofCDObjects) --> status
    """         
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')


    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        try:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()             
            if choice not in ['l', 'a', 'i', 'd', 's', 'x']:
                raise Exception('invalid choice') 
            return choice
                
        except Exception as e:
            print('built-in error info')
            print(type(e),e,e.__doc__,sep='\n')
            


    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\t\t\tCD Title\t\t\t(by: Artist)\n')
        #Getter is invoked when dunder variables are read
        for item in table:
            print(item.strID + "\t\t\t" + item.strTitle + "\t\t\t" + item.strArtist)
        print('======================================\n\n')


    @staticmethod
    def ask_details():
        """Ask 3 different data from user ( ID , title , artist)

        Args:
            None.

        Returns:
            CD ID , CD title and Artist name 
        """
        
        idfromuser = input('Enter ID: ').strip()
        titlefromuser = input('What is the CD\'s title? ').strip()
        artistfromuser = input('What is the Artist\'s name? ').strip()
        return(idfromuser,titlefromuser,artistfromuser)
    
    @staticmethod
    def add_cd(localstrID,localstrTitle,localstrArtist):
        """Function to add data entered by user to the 2D table

        Write CD Details as a dictionary entry .
        Add this dictionary to the 2D list .

        Args:
            strID (string ): ID for the CD entered by user
            strTitle (string ) : Title for the CD entered by user
            strArtist ( String ) : Artist name for the CD entered by user 
            
        Returns:
            None.
        """

        try:
            obj=CD(localstrID,localstrTitle,localstrArtist)
            #setter is invoked when we tried to set/write to dunder variables
            obj.strID=localstrID
            obj.strTitle=localstrTitle
            obj.strArtist=localstrArtist 
            lstOfCDObjects.append(obj)
        except Exception as e:
            print('Error from class CD Setter :')
            print(type(e),e,e.__doc__,sep='\n')
            
    @staticmethod    
    def delete_CD(intIDDel,lstOfCDObjects):
        """Function to delete a row identified by user from 2D table

        Checks if there is a match between the ID entered by the user and the ID present in the list .
        If there is a match delete the row that matches the ID .
        Display the latest content in the table .

        Args:
            intIDDel (Integer) : The CD ID entered by user 
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            Status of CD removal.
        """     
        intRowNr = -1
        blnCDRemoved = False
        for item in lstOfCDObjects:
            intRowNr += 1
            if int(item.strID) == intIDDel:
                del lstOfCDObjects[intRowNr]
                blnCDRemoved = True
                break
        return(blnCDRemoved)
       

# -- Main Body of Script -- #

# Load data from file into a list of CD objects on script start
# 1. When program starts, read in the currently saved Inventory

lstOfCDObjects=FileIO.load_inventory(strFileName)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    
        IO.print_menu()                          
        strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    
        
        if strChoice == 'x':
            break
    
    # 3.2 process load inventory
        if strChoice == 'l':
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
            strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled : ')
            if strYesNo.lower() == 'yes':
                print('reloading...')
                lstOfCDObjects=FileIO.load_inventory(strFileName)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu: ')            
            IO.show_inventory(lstOfCDObjects)
            continue
            
        
    # 3.3 process add a CD
        elif strChoice == 'a':
            # 3.3.1 Ask user for new ID, CD Title and Artist
            ID,title,artist=IO.ask_details()
                
            # 3.3.2 Add item to the table
            IO.add_cd(ID,title,artist)
            
            
            
            IO.show_inventory(lstOfCDObjects)        
            continue  # start loop back at top.
            
    # 3.4 process display current inventory
        elif strChoice == 'i':
            IO.show_inventory(lstOfCDObjects)
            continue  # start loop back at top.
            
    # 3.5 process delete a CD
        elif strChoice == 'd':
            # 3.5.1 get Userinput for which CD to delete
            # 3.5.1.1 display Inventory to user
            IO.show_inventory(lstOfCDObjects)
            # 3.5.1.2 ask user which ID to remove

            # Need to error trap this as it can still crash the program
            try:
                intIDDel = int(input('Which ID would you like to delete? ').strip())
                # 3.5.2 search thru table and delete CD
                status=IO.delete_CD(intIDDel,lstOfCDObjects)    
                if status:
                    print('The CD was removed\n\n')
                else:
                    print('Could not find this CD!')
                continue  # start loop back at top.
            except ValueError:
                print("ID to remove must be an integer")
            
    # 3.6 process save inventory to file
        elif strChoice == 's':
            # 3.6.1 Display current inventory and ask user for confirmation to save
            IO.show_inventory(lstOfCDObjects)
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
            # 3.6.2 Process choice
            if strYesNo == 'y':
                # 3.6.2.1 save data
                FileIO.save_inventory(strFileName, lstOfCDObjects)               
            else:
                input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
            continue  # start loop back at top.
    
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
        

