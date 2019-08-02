from tkinter import *
import math
import statistics

class Calculator():
    cText = ""
    var = []
    def __init__(self):
        root = Tk()
        root.title("Calculator")
        root.geometry("330x600")
        self.cText = ""
        self.var = []
        self.converter = 0

        #Clear Window Button
        clearButton = Button(root, text="AC", font=("helvetica", 17, "bold"),
                            command=lambda: self.clearWindow())
        clearButton.place(x=30, y=450)

        #Delete previous inputed character
        deleteButton = Button(root, text="DEL", font=("helvetica", 17, "bold"),
                              command=lambda: self.deleteCharacter())
        deleteButton.place(x=30,y=400)

        # Number Buttons
        zeroButton = Button(root, text="0", font=("helvetica", 17, "bold"),
                            command=lambda: self.addNum("0"))
        zeroButton.place(x=150, y=450)
        oneButton = Button(root, text="1", font=("helvetica", 17, "bold"),
                           command=lambda: self.addNum("1"))
        oneButton.place(x=100, y=400)
        twoButton = Button(root, text="2", font=("helvetica", 17, "bold"),
                           command=lambda: self.addNum("2"))
        twoButton.place(x=150, y=400)
        threeButton = Button(root, text="3", font=("helvetica", 17, "bold"),
                             command=lambda: self.addNum("3"))
        threeButton.place(x=200, y=400)
        fourButton = Button(root, text="4", font=("helvetica", 17, "bold"),
                            command=lambda: self.addNum("4"))
        fourButton.place(x=100, y=350)
        fiveButton = Button(root, text="5", font=("helvetica", 17, "bold"),
                            command=lambda: self.addNum("5"))
        fiveButton.place(x=150, y=350)
        sixButton = Button(root, text="6", font=("helvetica", 17, "bold"),
                           command=lambda: self.addNum("6"))
        sixButton.place(x=200, y=350)
        sevenButton = Button(root, text="7", font=("helvetica", 17, "bold"),
                             command=lambda: self.addNum("7"))
        sevenButton.place(x=100, y=300)
        eightButton = Button(root, text="8", font=("helvetica", 17, "bold"),
                             command=lambda: self.addNum("8"))
        eightButton.place(x=150, y=300)
        nineButton = Button(root, text="9", font=("helvetica", 17, "bold"),
                            command=lambda: self.addNum("9"))
        nineButton.place(x=200, y=300)
        decimalButton = Button(root, text=".", font=("helvetica", 17, "bold"),
                               command=lambda: self.addNum("."))
        decimalButton.place(x=100, y=450)
        negativeButton = Button(root, text="(-)", font=("helvetica", 17, "bold"),
                                command=lambda: self.addNum("-"))
        negativeButton.place(x=200, y=450)
        piButton = Button(root, text="π", font=("helvetica", 17, "bold"),
                          command=lambda: self.addNum("π"))
        piButton.place(x=250, y=150)
        eButton = Button(root, text="e", font=("helvetica", 17, "bold"),
                         command=lambda: self.addNum("e"))
        eButton.place(x=150, y=200)

        # Basic Functions Buttons
        divisionButton = Button(root, text="÷", font=("helvetica", 17, "bold"),
                                command=lambda: self.addFunction("/"))
        divisionButton.place(x=250, y=250)
        multiplicationButton = Button(root, text="*", font=("helvetica", 17, "bold"),
                                      command=lambda: self.addFunction("*"))
        multiplicationButton.place(x=250, y=300)
        subtractionButton = Button(root, text="-", font=("helvetica", 17, "bold"),
                                   command=lambda: self.addFunction("-"))
        subtractionButton.place(x=250, y=350)
        additionButton = Button(root, text="+", font=("helvetica", 17, "bold"),
                                command=lambda: self.addFunction("+"))
        additionButton.place(x=250, y=400)
        equalsButton = Button(root, text="=", font=("helvetica", 17, "bold"),
                              command=lambda: self.equalsSolver()
                              )
        equalsButton.place(x=250, y=450)
        factorialButton = Button(root, text="x!", font=("helvetica", 17, "bold"),
                                 command=lambda: self.factorialSolver())
        factorialButton.place(x=200, y=200)
        moduloButton = Button(root, text="%", font=("helvetica", 17, "bold"),
                              command=lambda: self.addFunction("%"))
        moduloButton.place(x=250, y=200)

        # Exponential and Logarithmic Functions Buttons
        squareButton = Button(root, text="x^2", font=("helvetica", 17, "bold"),
                              command=lambda: self.addFunction("**2"))
        squareButton.place(x=30, y=250)
        cubeButton = Button(root, text="x^3", font=("helvetica", 17, "bold"),
                              command=lambda: self.addFunction("**3"))
        cubeButton.place(x=100, y=250)
        exponentButton = Button(root, text="x^y", font=("helvetica", 17, "bold"),
                                command = lambda: self.addFunction("**"))
        exponentButton.place(x=180, y=250)
        squarerootButton = Button(root, text="√x", font=("helvetica", 17, "bold"),
                                  command = lambda: self.squareRootSolver())
        squarerootButton.place(x=30, y=350)
        cuberootButton = Button(root, text="3√x", font=("helvetica", 17, "bold"),
                                  command = lambda: self.addFunction("**(float(1/3))"))
        cuberootButton.place(x=30, y=300)
        logButton = Button(root, text="log", font=("helvetica", 17, "bold"),
                           command=lambda: self.logSolver())
        logButton.place(x=30, y=200)
        lnButton = Button(root, text="ln", font=("helvetica", 17, "bold"),
                          command=lambda: self.lnSolver())
        lnButton.place(x=100, y=200)

        # Trignonmetric Functions Buttons
        sinButton = Button(root, text="sin", font=("helvetica", 17, "bold"),
                           command=lambda: self.sinSolver())
        sinButton.place(x=30, y=150)
        cosButton = Button(root, text="cos", font=("helvetica", 17, "bold"),
                           command=lambda: self.cosSolver())
        cosButton.place(x=100, y=150)
        tanButton = Button(root, text="tan", font=("helvetica", 17, "bold"),
                           command=lambda: self.tanSolver())
        tanButton.place(x=180, y=150)
        inversesinButton = Button(root, text="sin^-1", font=("helvetica", 17, "bold"),
                                  command=lambda: self.arcsinSolver())
        inversesinButton.place(x=30, y=100)
        inversecosButton = Button(root, text="cos^-1", font=("helvetica", 17, "bold"),
                                  command=lambda: self.arccosSolver())
        inversecosButton.place(x=117, y=100)
        inversetanButton = Button(root, text="tan^-1", font=("helvetica", 17, "bold"),
                                  command=lambda: self.arctanSolver())
        inversetanButton.place(x=210, y=100)

        #Degree/Radian Radiobuttons
        var = IntVar()
        degreeRadiobutton = Radiobutton(root, text="Degrees", font=("helvetica", 17, "bold"),
                                        variable=var, value=1, command=lambda: self.degreeSelection())
        degreeRadiobutton.place(x=30,y=55)

        radianRadiobutton = Radiobutton(root, text="Radians", font=("helvetica", 17, "bold"),
                                        variable=var, value=2, command=lambda: self.radianSelection())
        radianRadiobutton.place(x=180,y=55)
        radianRadiobutton.select()

        #Statistics Buttons
        avgButton = Button(root, text="AVG", font=("helvetica", 17, "bold"),
                           command=lambda: self.meanSolver())
        avgButton.place(x=30, y=500)
        medianButton = Button(root, text="MED", font=("helvetica", 17, "bold"),
                           command=lambda: self.medSolver())
        medianButton.place(x=100, y=500)
        modeButton = Button(root, text="MOD", font=("helvetica", 17, "bold"),
                           command=lambda: self.modeSolver())
        modeButton.place(x=175, y=500)
        rangeButton = Button(root, text="RANGE", font=("helvetica", 17, "bold"),
                           command=lambda: self.rangeSolver())
        rangeButton.place(x=30, y=550)
        varianceButton = Button(root, text="VAR", font=("helvetica", 17, "bold"),
                           command=lambda: self.varSolver())
        varianceButton.place(x=130, y=550)
        stdevButton = Button(root, text="STDEV", font=("helvetica", 17, "bold"),
                           command=lambda: self.stdevSolver())
        stdevButton.place(x=200, y=550)
        commaButton = Button(root, text=",", font=("helvetica", 17, "bold"),
                            command=lambda: self.commaFunction())
        commaButton.place(x=255,y=500)

        # Display Window
        self.window = LabelFrame(root, bg="grey", height=40, width=330,
                                 labelanchor="nw", text="", font=("helvetica", 17, "bold"))
        self.window.grid()

        root.mainloop()

    #Calculator display window and all functions that were preformed on the calcular are cleared
    def clearWindow(self):
        self.var.clear()
        self.cText = ""
        self.window.config(text="")

    #Delete the last imputed character on the calculator
    def deleteCharacter(self):
        self.cText = self.cText[:-1]
        self.window.config(text=self.cText)

    #Numbers are displayed when the corresponding buttons are clicked
    def addNum(self, i):
        self.cText = self.cText + i
        self.window.config(text=self.cText)

    #Basic functions (÷,*,+,-) are added to self.var list
    def addFunction(self,i):
        self.var.append(self.cText)
        self.var.append(i)
        self.cText = ""
        self.window.config(text=self.cText)

    #Basic functions (÷,*,+,-) are solved and displayed in the calculator window
    def equalsSolver(self):
        for n, i in enumerate(self.var):
            if i== "π":
                self.var[n]= math.pi
            elif i== "e":
                self.var[n]= math.e
        self.var.append(self.cText)
        problem = ("".join([str(x) for x in self.var]))
        try:
            self.cText = str(eval(problem))
        except ZeroDivisionError:
            self.window.config(text="Divide by Zero Error")
        self.window.config(text=self.cText)
        self.var.clear()
        self.cText = ""

    #Factorials are solved and displayed in the calculator window
    def factorialSolver(self):
        self.var.append(self.cText)
        self.var.append("!")
        solution = math.factorial(int(self.var[-2]))
        self.updateFunction(solution)

    #Square roots are solved and displayed in the calculator window
    def squareRootSolver(self):
        self.var.append(self.cText)
        self.var.append("√")
        solution = math.sqrt(int(self.var[-2]))
        self.updateFunction(solution)

    # Square roots are solved and displayed in the calculator window
    def logSolver(self):
        self.var.append(self.cText)
        self.var.append("log")
        try:
            solution = math.log10(int(self.var[-2]))
        except ValueError:
            self.window.config(text="Math Domain Error")
        self.updateFunction(solution)

    # Square roots are solved and displayed in the calculator window
    def lnSolver(self):
        self.var.append(self.cText)
        self.var.append("ln")
        try:
            solution = math.log1p(int(self.var[-2]))
        except ValueError:
            self.window.config(text="Math Domain Error")
        self.updateFunction(solution)

    # Upon selecting the degrees radiobutton all trigonometric functions will be calculated in degrees
    def degreeSelection(self):
        self.converter = float(math.pi/180)
        self.arcconverter = float(180/math.pi)

    # Upon selecting the radian radiobutton all trigonometric functions will be calculated in degrees
    def radianSelection(self):
        self.converter = 1
        self.arcconverter = 1

    # Sine functions are solved in radians and displayed in the calculator window
    def sinSolver(self):
        self.var.append(self.cText)
        self.var.append("sin")
        try:
            solution = math.sin(float(self.var[-2])*float(self.converter))
        except ValueError:
            self.window.config(text="Math Domain Error")
        self.updateFunction(solution)

    # Cosine functions are solved in radians and displayed in the calculator window
    def cosSolver(self):
        self.var.append(self.cText)
        self.var.append("cos")
        try:
            solution = math.cos(float(self.var[-2])*float(self.converter))
        except ValueError:
            self.window.config(text="Math Domain Error")
        self.updateFunction(solution)

    # Tangent functions are solved in radians and displayed in the calculator window
    def tanSolver(self):
        self.var.append(self.cText)
        self.var.append("tan")
        try:
            solution = math.tan(float(self.var[-2])*float(self.converter))
        except ValueError:
            self.window.config(text="Math Domain Error")
        self.updateFunction(solution)

    # Inverse sine functions are solved in radians and displayed in the calculator window
    def arcsinSolver(self):
        self.var.append(self.cText)
        self.var.append("sin^-1")
        try:
            solution = math.asin(float(self.var[-2]))*float(self.arcconverter)
        except ValueError:
            self.window.config(text="Math Domain Error")
        self.updateFunction(solution)

    # Inverse cosine functions are solved in radians and displayed in the calculator window
    def arccosSolver(self):
        self.var.append(self.cText)
        self.var.append("cos^-1")
        try:
            solution = math.acos(float(self.var[-2]))*float(self.arcconverter)
        except ValueError:
            self.window.config(text="Math Domain Error")
        self.updateFunction(solution)

    # Inverse tangent functions are solved in radians and displayed in the calculator window
    def arctanSolver(self):
        self.var.append(self.cText)
        self.var.append("tan^-1")
        try:
            solution = math.acos(float(self.var[-2]))*float(self.arcconverter)
        except ValueError:
            self.window.config(text="Math Domain Error")
        self.updateFunction(solution)

    # Numbers are appended to a list to be stored for further manipulation
    def commaFunction(self):
        self.var.append(self.cText)
        print(self.var)
        ("".join([str(x) for x in self.var]))
        self.cText=""
        self.window.config(text=self.cText)

    # Average is calculated and displayed in the calculator window given a series of number inputs stored in fVar
    def avgSolver(self):
        self.var.append(self.cText)
        fVar = []
        for i in self.var:
            fVar.append(float(i))
        avg = statistics.mean(fVar)
        self.updateFunction(avg)

    # Median is calculated and displayed in the calculator window given a series of number inputs stored in fVar
    def medSolver(self):
        self.var.append(self.cText)
        fVar = []
        for i in self.var:
            fVar.append(float(i))
        median=statistics.median(fVar)
        self.updateFunction(median)

    # Mode is calculated and displayed in the calculator window given a series of number inputs stored in fVar
    def modeSolver(self):
        self.var.append(self.cText)
        fVar = []
        for i in self.var:
            fVar.append(float(i))
        mode=statistics.median(fVar)
        self.updateFunction(mode)

    # Variance is calculated and displayed in the calculator window given a series of number inputs stored in fVar
    def varSolver(self):
        self.var.append(self.cText)
        fVar = []
        for i in self.var:
            fVar.append(float(i))
        var = statistics.variance(fVar)
        self.updateFunction(var)

    # Standard deviation is calculated and displayed in the calculator window given a series of number inputs stored in fVar
    def stdevSolver(self):
        self.var.append(self.cText)
        fVar = []
        for i in self.var:
            fVar.append(float(i))
        stdev = statistics.variance(fVar)
        self.updateFunction(stdev)

    # Range is calculated and displayed in the calculator window given a series of number inputs stored in fVar
    def rangeSolver(self):
        self.var.append(self.cText)
        fVar = []
        for i in self.var:
            fVar.append(float(i))
        range = int(max(fVar))-int(min(fVar))
        self.window.config(text=range)
        self.cText=""

    def updateFunction(self,answer):
        self.window.config(text=answer)
        self.cText=""