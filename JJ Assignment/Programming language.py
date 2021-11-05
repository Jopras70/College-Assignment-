dict = { 
    "L1": 'Go, Go is an open source programming language developed at Google.',
    "L2": 'Java, Java is a general-purpose, concurrent, strongly typed, class-based object-oriented language.',
    "L3": 'Python, Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes.',
    "L4": 'C++, C++ is supports object-oriented programming features like classes.',
    "L5": 'PHP, PHP is known as a general-purpose scripting language that can be used to develop dynamic and interactive websites.'
}

seq = [2,1,3,0,4]

for i in seq: 
    print ([key for key in dict.keys()][i])
    print ([val for val in dict.values()][i])
    print ('')

