


with open ("irisdataset.txt" , "r") as f:
# Open text file called 'Irisdataset.txt file in read mode
   print("")
   frequency = (f.read () .lower (). count ('e'))
   # Read all characters in the file, convert to lower case and count 
   # the number of times 'e' appears
   print ("The number of times 'e' occurs in the book 'Moby Dick' is:" , frequency)
   # Print the result