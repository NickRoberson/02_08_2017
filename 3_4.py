class dictionary:
    def __init__(self,entries):
        self.list = [0]*(max(entries)+1)
        for index in entries:
            self.list[index] = 1;
        print self.list

    def search(self,index):
        if(self.list[index] == 1):
            print "Found " + str(self.list[index]) + " at Index " + str(index)
            return True
        else:
            print "Couldn't find entry at index " + str(index)
            return False

    def delete(self,index):
        self.list[index] = 0
        print "Deleted entry at index " + str(index)

    def insert(self,index):
        if(self.list[index] != 1):
            self.list[index] = 1
            print "Item inserted at index " + str(index)
            return True # There was nothing there so we are able to insert
        else:
            print "Cannot insert at " + str(index) + ", already a value"
            return False # There was an entry, could not inset


    def toStr(self):
        return self.list


def main():
    entries = [0,1,2,12,3,5,6,8,9]
    d = dictionary(entries)

    d.search(1)
    d.insert(0)
    d.insert(1)
    print d.toStr()
    d.delete(3)
    d.search(3)
    d.insert(3)
    print d.toStr()

main()
