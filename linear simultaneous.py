class variable:
    
    def __init__(self, character):
        self.values = []
        self.character = character
        self.final = 0
        
    def collect(self, eq):
        xLeft = True
        
        while xLeft:
            for x in eq:
                if self.character in x:
                    if x.index(self.character) == 0 :
                        self.values.append(1)
                        eq.remove(x)
                    elif x.index(self.character) == 1 and "-" in x:
                        self.values.append(-1)
                        eq.remove(x)
                    else:
                        self.values.append(int(x[:-1]))
                        eq.remove(x)
            
            xLeft = False
            for x in eq:
                if self.character in x:
                    xLeft = True
            
        for x in self.values:
            self.final += x
        
        
        return eq    

def process(equation, terms):
    xTerms = variable(terms[0])
    yTerms = variable(terms[2])

    eq = xTerms.collect(equation)
    eq = yTerms.collect(equation)

    equation = [xTerms.final, yTerms.final, int(equation[0])]
    
    return equation

def solve(eq1, eq2):
    x = ((eq1[2] * eq2[1]) - (eq2[2] * eq1[1]))/((eq1[0] * eq2[1]) - (eq2[0] * eq1[1]))
    y = (eq1[2] - (eq1[0] * x))/eq1[1]
    
    return x, y

def cleanup(string):
    temp = list(string)
    while " " in temp:
        temp.remove(" ")

    string = "".join(temp)

    return string

def userEntry():
    eq1 = input("enter the first equation")
    eq2 = input("enter the second equation")
    terms = input("enter the variables to solve for, separated by a comma")

    eq1 = cleanup(eq1)
    eq2 = cleanup(eq2)
    terms = cleanup(terms)

    return eq1, eq2, terms


def listise(equation):
    minusFirst = False
    
    if "+" in equation:
        equation = equation.split("+")
        for x in equation:
            if "=" in x:
                w = x.split("=")
                equation.remove(x)
                for y in w:
                    equation.append(y)
                
        for x in equation:
            if "-" in x and (x.index("-") != 0):
                w = x.split("-")
                for z in range(len(w)):
                    if z > 0:
                        w[z] = "-" + w[z]
                equation.remove(x)
                for y in w:
                    equation.append(y)
                    
    elif "=" in equation:
        equation = equation.split("=")

        if equation[0].index("-") == 0:
            equation[0] = equation[0][1:]

            minusFirst = True

        for x in equation:
            if "-" in x and (x.index("-") != 0):
                w = x.split("-")
                for z in range(len(w)):
                    if z > 0:
                        w[z] = "-" + w[z]
                equation.remove(x)
                for y in w:
                    equation.append(y)

        if minusFirst:
            equation[1] = "-" + equation[1]

    return equation

loopCondition = True

while loopCondition:
    lists = userEntry()
    try:
        eq1 = lists[0]
        eq2 = lists[1]
        terms = lists[2]
        eq1 = listise(eq1)
        eq2 = listise(eq2)
        terms = listise(terms)
        eq1 = process(eq1, terms)
        eq2 = process(eq2, terms)
        loopCondition = False
    except:
        print("invalid entry")

try:
    (x, y) = solve(eq1, eq2)    
    print(f"{terms[0]}: {x}\n{terms[2]}: {y}")
except:
    print("That system has no solutions :(")


