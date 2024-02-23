
'''b="Rishi singh is a good boy"
print(b)
#print(len(b)) # print length of string 


print(b[0:5])   # 0 - 5 but 6 element so 1 mines 6-1 = 5
print(b[0:50])  # print all element int string under 50 parsent all element  
print(b[0:5:2]) # print element skip 2-1 = 1  element out put will be Rsi
print(b[:5])
print(b[::])
print(b[::2])
print(b[::3])

#0 1 2 3 4 5 6 7 8 9 10 11
#\R\i\s\h\i\ \s\i\n\g\h 
#-12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 
print(b[17:21])
print(b[-8:-4])
print(b[::-1])
print(b[17:-2])
print(b[::-2])
# check bollen True or False
e= "Rishi singh"      # alpha numeric nahi hai beech mai space hai
e= "Rishisingh"       # This is alpha numeric

print(e.isalnum())    #check numeric
print(e.isalpha())    #check alpha
print(e.endswith("singh"))    #check 
print(e.endswith("fingh"))    #check 
print(e.count("s"))
print(e.count("d"))
'''

# some most important functions
x="rishi singh is good boy"
y="Rishisingh is good boy"
print(x.capitalize()) 

print(x.find("is"))

print(y.lower()) 
print(y.upper()) 
print(y.replace( "is","are"))
