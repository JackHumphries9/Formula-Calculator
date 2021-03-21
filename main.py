from tkinter import *

geometryX = 340
geometryY = 200

def raise_frame(frame):
    frame.tkraise()


class FormulaCalculator:
    def __init__(self, master):
        master.title("Formula Calculator")
        master.minsize(geometryX, geometryY)
        master.maxsize(geometryX, geometryY)
        
        self.speed = Frame(master)
        self.force = Frame(master)
        self.weight = Frame(master)
        self.momentum = Frame(master)

        for frame in (self.speed, self.force, self.weight, self.momentum):
            frame.grid(row=0, column=0, sticky='news')

        # ==============================================================================================================
        # ======================= Speed Menu Layout ====================================================================
        # ==============================================================================================================

        # Labels
        self.spTitleLabel = Label(self.speed, text="Speed").grid(row=0, column=1)
        self.spDistanceLabel = Label(self.speed, text="Distance (m): ").grid(row=1, column=0)
        self.spTimeLabel = Label(self.speed, text="Time (s): ").grid(row=2, column=0)
        self.spSpeedLabel = Label(self.speed, text="Speed (m/s):  ").grid(row=3, column=0)

        # Entry boxes
        self.spDistance = Entry(self.speed)
        self.spTime = Entry(self.speed)
        self.spSpeed = Entry(self.speed)

        # Packing the entry boxes into the frame
        self.spDistance.grid(row=1, column=1)
        self.spTime.grid(row=2, column=1)
        self.spSpeed.grid(row=3, column=1)

        # Button and packing
        self.spConvertSpeed = Button(self.speed, text="Calculate Speed", command=self.speedCalcSpeed).grid(row=4, column=1)
        self.spConvertDistance = Button(self.speed, text="Calculate Distance", command=self.speedCalcDist).grid(row=5, column=1)
        self.spConvertTime = Button(self.speed, text="Calculate Time", command=self.speedCalcTime).grid(row=6, column=1)

        # ==============================================================================================================
        # ======================= Force Menu Layout ====================================================================
        # ==============================================================================================================

        # Labels
        self.foTitleLabel = Label(self.force, text="Force").grid(row=0, column=1)
        self.foAccelerationLabel = Label(self.force, text="Acceleration (m/s**2): ").grid(row=1, column=0)
        self.foMassLabel = Label(self.force, text="Mass (kg): ").grid(row=2, column=0)
        self.foForceLabel = Label(self.force, text="Force (N): ").grid(row=3, column=0)

        # Entry boxes
        self.foAcceleration = Entry(self.force)
        self.foMass = Entry(self.force)
        self.foForce = Entry(self.force)

        # Entry packing
        self.foAcceleration.grid(row=1, column=1)
        self.foMass.grid(row=2, column=1)
        self.foForce.grid(row=3, column=1)

        # Buttons and packing
        self.foConvertAcceleration = Button(self.force, text="Calculate Acceleration", command=self.foCalcAcceleration)
        self.foConvertMass = Button(self.force, text="Calculate Mass", command=self.foCalcMass)
        self.foConvertForce = Button(self.force, text="Calculate Force", command=self.foCalcForce)

        self.foConvertAcceleration.grid(row=4, column=1)
        self.foConvertMass.grid(row=5, column=1)
        self.foConvertForce.grid(row=6, column=1)

        # ==============================================================================================================
        # ======================= Weight Menu Layout ===================================================================
        # ==============================================================================================================

        # Labels
        self.weTitleLabel = Label(self.weight, text="Weight").grid(row=0, column=1)
        self.weGravityLabel = Label(self.weight, text="Gravity (N/kg): ").grid(row=1, column=0)
        self.weMassLabel = Label(self.weight, text="Mass (kg): ").grid(row=2, column=0)
        self.weWeightLabel = Label(self.weight, text="Weight (N): ").grid(row=3, column=0)

        # Entry Boxes
        self.weGravity = Entry(self.weight)
        self.weMass = Entry(self.weight)
        self.weWeight = Entry(self.weight)

        # Entry packing
        self.weGravity.grid(row=1, column=1)
        self.weMass.grid(row=2, column=1)
        self.weWeight.grid(row=3, column=1)

        self.weConvertGravity = Button(self.weight, text="Calculate Gravity", command=self.weCalcGravity)
        self.weConvertMass = Button(self.weight, text="Calculate Mass", command=self.weCalcMass)
        self.weConvertWeight = Button(self.weight, text="Calculate Weight", command=self.weCalcWeight)

        self.weConvertGravity.grid(row=4, column=1)
        self.weConvertMass.grid(row=5, column=1)
        self.weConvertWeight.grid(row=6, column=1)

        # ==============================================================================================================
        # ======================= Momentum Menu Layout =================================================================
        # ==============================================================================================================

        # Labels
        self.moTitleLabel = Label(self.momentum, text="Momentum").grid(row=0, column=1)
        self.moVelocityLabel = Label(self.momentum, text="Velocity (m/s): ").grid(row=1, column=0)
        self.moMassLabel = Label(self.momentum, text="Mass (kg): ").grid(row=2, column=0)
        self.moMomentumLabel = Label(self.momentum, text="Momentum (kgm/s): ").grid(row=3, column=0)

        # Entry Boxes
        self.moVelocity = Entry(self.momentum)
        self.moMass = Entry(self.momentum)
        self.moMomentum = Entry(self.momentum)

        # Entry packing
        self.moVelocity.grid(row=1, column=1)
        self.moMass.grid(row=2, column=1)
        self.moMomentum.grid(row=3, column=1)

        self.moConvertVelocity = Button(self.momentum, text="Calculate Velocity", command=self.moCalcVelocity)
        self.moConvertMass = Button(self.momentum, text="Calculate Mass", command=self.moCalcMass)
        self.moConvertMomentum = Button(self.momentum, text="Calculate Momentum", command=self.moCalcMomentum)

        self.moConvertVelocity.grid(row=4, column=1)
        self.moConvertMass.grid(row=5, column=1)
        self.moConvertMomentum.grid(row=6, column=1)

        # ==============================================================================================================
        # ========================= Menu bar Layout ====================================================================
        # ==============================================================================================================
        self.menubar = Menu(master)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=master.destroy)

        self.insertmenu = Menu(self.menubar, tearoff=0)
        self.insertmenu.add_command(label="Earth's Gravity Constant", command=self.insertGravity)

        self.formulamenu = Menu(self.menubar, tearoff=0)
        self.formulamenu.add_command(label="FORCES")
        self.formulamenu.add_separator()
        self.formulamenu.add_command(label="Speed", command=lambda: raise_frame(self.speed))
        self.formulamenu.add_command(label="Force", command=lambda: raise_frame(self.force))
        self.formulamenu.add_command(label="Weight", command=lambda: raise_frame(self.weight))
        self.formulamenu.add_command(label="Momentum", command=lambda: raise_frame(self.momentum))

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Insert", menu=self.insertmenu)
        self.menubar.add_cascade(label="Formula Selection", menu=self.formulamenu)

        master.config(menu=self.menubar)

    # ============================ INSERT FUNCTIONS ====================================================================
    
    def insertGravity(self):
        raise_frame(self.weight)
        self.weGravity.delete(0, END)
        self.weGravity.insert(INSERT, "9.81")
    
    # ==================================================================================================================
    # ======================= Logical Processes ========================================================================
    # ==================================================================================================================
    
    """ SPEED CALCULATIONS """
    
    def speedCalcSpeed(self):
        self._distance = float(self.spDistance.get())
        self._time = float(self.spTime.get())
    
        self.spSpeed.delete(0, END)
        self.spSpeed.insert(INSERT, str(self._distance / self._time))
    
    def speedCalcTime(self):
        self._distance = float(self.spDistance.get())
        self._speed = float(self.spSpeed.get())
    
        self.spTime.delete(0, END)
        self.spTime.insert(INSERT, str(self._distance / self._speed))
    
    def speedCalcDist(self):
        self._speed = float(self.spSpeed.get())
        self._time = float(self.spTime.get())
    
        self.spDistance.delete(0, END)
        self.spDistance.insert(INSERT, str(self._time * self._speed))
    
    """ FORCE CALCULATIONS """
    
    def foCalcAcceleration(self):
        self._mass = float(self.foMass.get())
        self._force = float(self.foForce.get())
    
        self.foAcceleration.delete(0, END)
        self.foAcceleration.insert(INSERT, str(self._force / self._mass))
    
    def foCalcMass(self):
        self._acceleration = float(self.foAcceleration.get())
        self._force = float(self.foForce.get())
    
        self.foMass.delete(0, END)
        self.foMass.insert(INSERT, str(self._force / self._acceleration))
    
    def foCalcForce(self):
        self._mass = float(self.foMass.get())
        self._acceleration = float(self.foAcceleration.get())
    
        self.foForce.delete(0, END)
        self.foForce.insert(INSERT, self._mass * self._acceleration)
    
    """ Weight Calculations """
    
    def weCalcGravity(self):
        self._mass = float(self.weMass.get())
        self._weight = float(self.weWeight.get())
    
        self.weGravity.delete(0, END)
        self.weGravity.insert(INSERT, str(self._weight / self._mass))
    
    def weCalcMass(self):
        self._gravity = float(self.weGravity.get())
        self._weight = float(self.weWeight.get())
    
        self.weMass.delete(0, END)
        self.weMass.insert(INSERT, str(self._weight / self._gravity))
    
    def weCalcWeight(self):
        self._gravity = float(self.weGravity.get())
        self._mass = float(self.weMass.get())
    
        self.weWeight.delete(0, END)
        self.weWeight.insert(INSERT, str(self._mass * self._gravity))
    
    """ Momentum Calculations """
    
    def moCalcVelocity(self):
        self._momentum = float(self.moMomentum.get())
        self._mass = float(self.moMass.get())
    
        self.moVelocity.delete(0, END)
        self.moVelocity.insert(INSERT, str(self._momentum / self._mass))
    
    def moCalcMass(self):
        self._momentum = float(self.moMomentum.get())
        self._velocity = float(self.moVelocity.get())
    
        self.moMass.delete(0, END)
        self.moMass.insert(INSERT, str(self._momentum / self._velocity))
    
    def moCalcMomentum(self):
        self._mass = float(self.moMass.get())
        self._velocity = float(self.moVelocity.get())
    
        self.moMomentum.delete(0, END)
        self.moMomentum.insert(INSERT, str(self._mass * self._velocity))

root = Tk()
main = FormulaCalculator(root)
root.mainloop()
