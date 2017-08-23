
class word :
    
    def __init__ (self, number, text) :

        self.number = number
        self.text = text

    def check (self, counter) :

        if counter % self.number == 0 :
            return self.text
        else : 
            return ""

fizz = word(3, "fizz")
buzz = word(5, "buzz")
patata = word(7, "patata")



for i in range (1,201) :

    output = ""

    output += fizz.check(i)
    output += buzz.check(i)
    output += patata.check(i)


    if output == "" :
        output = i

    print (output)