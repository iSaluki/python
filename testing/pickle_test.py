import pickle

data = input("What would you like to stick in the file?: ")

filename = 'test_data'
outfile = open(filename, 'wb')
pickle.dump(data, outfile)
outfile.close()
print ("File closed and saved.")
print ("Opening file.")
infile = open(filename, 'rb')
new_str = pickle.load(infile)
infile.close()
print ("Printing file contents")
print (new_str)
