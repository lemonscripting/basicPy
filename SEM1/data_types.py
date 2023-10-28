#sample data types

#checking for type --> type()

x = "Hello World"	                            #str        str()
x = 20	                                        #int        int()
x = 20.5	                                    #float	    float()
x = 1j	                                        #complex	complex()
x = ["apple", "banana", "cherry"]	            #list	    list()
x = ("apple", "banana", "cherry")	            #tuple      tuple()
x = range(6)	                                #range	    range()
x = {"name" : "John", "age" : 36}	            #dict	    dict()
x = {"apple", "banana", "cherry"}	            #set	    set()
x = frozenset({"apple", "banana", "cherry"})	#frozenset	frozenset()
x = True	                                    #bool	    bool()
x = b"Hello"	                                #bytes	    bytes()
x = bytearray(5)	                            #bytearray	bytearray()
x = memoryview(bytes(5))	                    #memoryview	memoryview()
x = None	                                    #NoneType   NA