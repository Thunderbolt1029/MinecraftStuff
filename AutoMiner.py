from mttkinter import mtTkinter as tk
from PIL import ImageGrab
import time, threading, keyboard, mouse, countdown

countdown = countdown.countdown()

root = tk.Tk()
root.title("AutoMiner")
root.minsize(0, 270)
root.resizable(0, 0)

class Window(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        keyboard.add_hotkey("f6", lambda: self.toggleStart())

        self.errorRange = 5

        self.custom1 = tk.LabelFrame(master, relief="sunken")
        self.custom2 = tk.LabelFrame(master, relief="sunken")
        
        mineableItems = ("-", "Mithril", "Titanium", "Diamond", "Emerald", "Gold", "Iron", "Coal", "Custom")

        self.mineColor1 = tk.LabelFrame(self.custom1, relief="flat") 
        self.mineColor1Label = tk.Label(self.mineColor1, text="Mine at Colour")
        self.mineColor1Label_R = tk.Label(self.mineColor1, text="R =")
        self.mineColor1Input_R = tk.Entry(self.mineColor1, width=5)
        self.mineColor1Label_G = tk.Label(self.mineColor1, text="G =")
        self.mineColor1Input_G = tk.Entry(self.mineColor1, width=5)
        self.mineColor1Label_B = tk.Label(self.mineColor1, text="B =")
        self.mineColor1Input_B = tk.Entry(self.mineColor1, width=5)

        self.timePresetFrame1 = tk.LabelFrame(self.custom1, relief="flat")        
        self.time1 = tk.Label(self.timePresetFrame1, text="Time")
        self.time1Input = tk.Entry(self.timePresetFrame1, width=5)
        self.time1Label = tk.Label(self.timePresetFrame1, text="s")
        self.preset1 = tk.Label(self.timePresetFrame1, text="Presets")
        self.preset1Selected = tk.StringVar(self.timePresetFrame1)
        self.preset1Selected.set("-")
        self.preset1ListMenu = tk.OptionMenu(self.timePresetFrame1, self.preset1Selected, *mineableItems, command=self.presetChange1)

        self.mineColor1.grid(column=0, row=0, rowspan=2, padx=10, pady=5)
        self.mineColor1Label.grid(column=0, row=0, columnspan=6, padx=10)
        self.mineColor1Label_R.grid(column=0, row=1, padx=2, pady=5)
        self.mineColor1Input_R.grid(column=1, row=1, padx=2, pady=5)
        self.mineColor1Label_G.grid(column=2, row=1, padx=2, pady=5)
        self.mineColor1Input_G.grid(column=3, row=1, padx=2, pady=5)
        self.mineColor1Label_B.grid(column=4, row=1, padx=2, pady=5)
        self.mineColor1Input_B.grid(column=5, row=1, padx=2, pady=5)

        self.timePresetFrame1.grid(column=1, row=0, rowspan=2, padx=10, pady=5)
        self.time1.grid(column=0, row=0, padx=10, columnspan=2)
        self.time1Input.grid(column=0, row=1, padx=5, pady=5, sticky="E")
        self.time1Label.grid(column=1, row=1, padx=0, pady=5, sticky="W")
        self.preset1.grid(column=2, row=0, padx=10)
        self.preset1ListMenu.grid(column=2, row=1, padx=10)
        

        
        self.mineColor2 = tk.LabelFrame(self.custom2, relief="flat") 
        self.mineColor2Label = tk.Label(self.mineColor2, text="Mine at Colour")
        self.mineColor2Label_R = tk.Label(self.mineColor2, text="R =")
        self.mineColor2Input_R = tk.Entry(self.mineColor2, width=5)
        self.mineColor2Label_G = tk.Label(self.mineColor2, text="G =")
        self.mineColor2Input_G = tk.Entry(self.mineColor2, width=5)
        self.mineColor2Label_B = tk.Label(self.mineColor2, text="B =")
        self.mineColor2Input_B = tk.Entry(self.mineColor2, width=5)

        self.timePresetFrame2 = tk.LabelFrame(self.custom2, relief="flat")        
        self.time2 = tk.Label(self.timePresetFrame2, text="Time")
        self.time2Input = tk.Entry(self.timePresetFrame2, width=5)
        self.time2Label = tk.Label(self.timePresetFrame2, text="s")
        self.preset2 = tk.Label(self.timePresetFrame2, text="Presets")
        self.preset2Selected = tk.StringVar(self.timePresetFrame2)
        self.preset2Selected.set("-")
        self.preset2ListMenu = tk.OptionMenu(self.timePresetFrame2, self.preset2Selected, *mineableItems, command=self.presetChange2)

        self.mineColor2.grid(column=0, row=0, rowspan=2, padx=10, pady=5)
        self.mineColor2Label.grid(column=0, row=0, columnspan=6, padx=10)
        self.mineColor2Label_R.grid(column=0, row=1, padx=2, pady=5)
        self.mineColor2Input_R.grid(column=1, row=1, padx=2, pady=5)
        self.mineColor2Label_G.grid(column=2, row=1, padx=2, pady=5)
        self.mineColor2Input_G.grid(column=3, row=1, padx=2, pady=5)
        self.mineColor2Label_B.grid(column=4, row=1, padx=2, pady=5)
        self.mineColor2Input_B.grid(column=5, row=1, padx=2, pady=5)

        self.timePresetFrame2.grid(column=1, row=0, rowspan=2, padx=10, pady=5)
        self.time2.grid(column=0, row=0, padx=10, columnspan=2)
        self.time2Input.grid(column=0, row=1, padx=5, pady=5, sticky="E")
        self.time2Label.grid(column=1, row=1, padx=0, pady=5, sticky="W")
        self.preset2.grid(column=2, row=0, padx=10)
        self.preset2ListMenu.grid(column=2, row=1, padx=10)



        self.checkPixelFrame = tk.LabelFrame(master, relief="flat")

        self.checkPixel = tk.Label(self.checkPixelFrame, text="Pixel to Check")
        self.pixelX = tk.Entry(self.checkPixelFrame, width=5)
        self.pixelBy = tk.Label(self.checkPixelFrame, text="X")
        self.pixelY = tk.Entry(self.checkPixelFrame, width=5)
        self.pixelCheck = tk.Button(self.checkPixelFrame, text="Check", command=self.checkColor)
        self.pixelX.insert(0, "840")
        self.pixelY.insert(0, "516")
        self.colorAtPixelLabel = tk.Label(self.checkPixelFrame, text="Colour at Pixel")
        self.pixelColor = tk.StringVar()
        self.pixelColor.set("0, 0, 0")
        self.pixelColorLabel = tk.Label(self.checkPixelFrame, textvariable=self.pixelColor)
        

        self.checkPixel.grid(column=0, row=0, columnspan=4)
        self.pixelX.grid(column=0, row=1)
        self.pixelBy.grid(column=1, row=1)
        self.pixelY.grid(column=2, row=1)
        self.pixelCheck.grid(column=3, row=1)
        self.colorAtPixelLabel.grid(column=4, row=0)
        self.pixelColorLabel.grid(column=4, row=1)
        

        
        self.pickobulousFrame = tk.LabelFrame(master, relief="flat")
        
        self.pickobulous = True
        self.pickobulousLabel = tk.Label(self.pickobulousFrame, text="Pickobulous")
        self.pickobulousButton = tk.Button(self.pickobulousFrame, text="On", relief="sunken", command=self.pickobulousToggle)
        
        self.pickobulousLabel.grid(column=0, row=0)
        self.pickobulousButton.grid(column=0, row=1)

        

        self.startStopFrame = tk.LabelFrame(master, relief="flat")

        self.startStop = tk.StringVar(value="off")
        self.stopButton = tk.Radiobutton(self.startStopFrame, text="Stop (F6)", value="off", variable=self.startStop, indicatoron=False, command=self.stop)
        self.startButton = tk.Radiobutton(self.startStopFrame, text="Start (F6)", value="on", variable=self.startStop, indicatoron=False, command=self.start)

        self.stopButton.grid(column=0, row=0)
        self.startButton.grid(column=1, row=0)
        
    def placeFrames(self):
        self.custom1.grid(column=0, row=0, padx=10, pady=5, columnspan=2)
        self.custom2.grid(column=0, row=1, padx=10, pady=5, columnspan=2)

        self.checkPixelFrame.grid(column=0, row=2, columnspan=2)

        self.pickobulousFrame.grid(column=1, row=3, sticky="W")
        self.startStopFrame.grid(column=0, row=3, sticky="SE")

    def dropFrames(self):
        self.custom1.grid_remove()
        self.custom2.grid_remove()

        self.checkPixelFrame.grid_remove()

        self.startStopFrame.grid_remove()

    def checkColor(self):
        countdown.start(5)
        x = self.pixelX.get()
        y = self.pixelY.get()
        color = ImageGrab.grab().getpixel((int(x), int(y)))
        (r, g, b) = color
        self.pixelColor.set(str(r)+", "+str(g)+", "+str(b))

    def presetChange1(self, preset):
        r = self.mineColor1Input_R.get()
        g = self.mineColor1Input_G.get()
        b = self.mineColor1Input_B.get()
        time = self.time1Input.get()
        rLen = len(r)
        gLen = len(g)
        bLen = len(b)
        timeLen = len(time)
        self.mineColor1Input_R.delete(0, rLen)
        self.mineColor1Input_G.delete(0, gLen)
        self.mineColor1Input_B.delete(0, bLen)
        self.time1Input.delete(0, timeLen)
        if preset=="Mithril":
            self.mineColor1Input_R.insert(0, "235")
            self.mineColor1Input_G.insert(0, "193")
            self.mineColor1Input_B.insert(0, "189")
            self.time1Input.insert(0, "4")
        elif preset=="Titanium":
            self.mineColor1Input_R.insert(0, "183")
            self.mineColor1Input_G.insert(0, "194")
            self.mineColor1Input_B.insert(0, "211")
            self.time1Input.insert(0, "5")
        elif preset=="Diamond":
            self.mineColor1Input_R.insert(0, "140")
            self.mineColor1Input_G.insert(0, "82")
            self.mineColor1Input_B.insert(0, "122")
            self.time1Input.insert(0, "0.3")
        elif preset=="Emerald":
            self.mineColor1Input_R.insert(0, "111")
            self.mineColor1Input_G.insert(0, "111")
            self.mineColor1Input_B.insert(0, "110")
            self.time1Input.insert(0, "0.3")
        elif preset=="Gold":
            self.mineColor1Input_R.insert(0, "166")
            self.mineColor1Input_G.insert(0, "166")
            self.mineColor1Input_B.insert(0, "117")
            self.time1Input.insert(0, "0.3")
        elif preset=="Iron":
            self.mineColor1Input_R.insert(0, "96")
            self.mineColor1Input_G.insert(0, "96")
            self.mineColor1Input_B.insert(0, "96")
            self.time1Input.insert(0, "0.3")
        elif preset=="Coal":
            self.mineColor1Input_R.insert(0, "41")
            self.mineColor1Input_G.insert(0, "39")
            self.mineColor1Input_B.insert(0, "35")
            self.time1Input.insert(0, "0.3")
        elif preset=="Custom":
            self.mineColor1Input_R.insert(0, r)
            self.mineColor1Input_G.insert(0, g)
            self.mineColor1Input_B.insert(0, b)
            self.time1Input.insert(0, time)

    def presetChange2(self, preset):
        r = self.mineColor2Input_R.get()
        g = self.mineColor2Input_G.get()
        b = self.mineColor2Input_B.get()
        time = self.time2Input.get()
        rLen = len(r)
        gLen = len(g)
        bLen = len(b)
        timeLen = len(time)
        self.mineColor2Input_R.delete(0, rLen)
        self.mineColor2Input_G.delete(0, gLen)
        self.mineColor2Input_B.delete(0, bLen)
        self.time2Input.delete(0, timeLen)
        if preset=="Mithril":
            self.mineColor2Input_R.insert(0, "235")
            self.mineColor2Input_G.insert(0, "193")
            self.mineColor2Input_B.insert(0, "189")
            self.time2Input.insert(0, "4")
        elif preset=="Titanium":
            self.mineColor2Input_R.insert(0, "183")
            self.mineColor2Input_G.insert(0, "194")
            self.mineColor2Input_B.insert(0, "211")
            self.time2Input.insert(0, "5")
        elif preset=="Diamond":
            self.mineColor2Input_R.insert(0, "122")
            self.mineColor2Input_G.insert(0, "82")
            self.mineColor2Input_B.insert(0, "122")
            self.time2Input.insert(0, "0.3")
        elif preset=="Emerald":
            self.mineColor2Input_R.insert(0, "111")
            self.mineColor2Input_G.insert(0, "111")
            self.mineColor2Input_B.insert(0, "110")
            self.time2Input.insert(0, "0.3")
        elif preset=="Gold":
            self.mineColor2Input_R.insert(0, "166")
            self.mineColor2Input_G.insert(0, "166")
            self.mineColor2Input_B.insert(0, "117")
            self.time2Input.insert(0, "0.3")
        elif preset=="Iron":
            self.mineColor2Input_R.insert(0, "96")
            self.mineColor2Input_G.insert(0, "96")
            self.mineColor2Input_B.insert(0, "96")
            self.time2Input.insert(0, "0.3")
        elif preset=="Coal":
            self.mineColor2Input_R.insert(0, "41")
            self.mineColor2Input_G.insert(0, "39")
            self.mineColor2Input_B.insert(0, "35")
            self.time2Input.insert(0, "0.3")
        elif preset=="Custom":
            self.mineColor2Input_R.insert(0, r)
            self.mineColor2Input_G.insert(0, g)
            self.mineColor2Input_B.insert(0, b)
            self.time2Input.insert(0, time)

    def pickobulousToggle(self):
        if self.pickobulousButton.config('relief')[-1] == 'sunken':
            self.pickobulousButton.config(relief="raised", text="Off")
            self.pickobulous = False
        else:
            self.pickobulousButton.config(relief="sunken", text="On")
            self.pickobulous = True
            
    def toggleStart(self):
        if self.startStop.get()=="on":
            self.stopButton.invoke()
        elif self.startStop.get()=="off":
            self.startButton.invoke()

    def start(self):
        self.mining = True
        threading.Thread(target=self.loop).start()
        if self.pickobulous:
            self.pickobulousThread = threading.Thread(target=self.pickobulousLoop, daemon=True)
            self.pickobulousThread.start()

    def loop(self):
        try:
            (r1, g1, b1, time1) = (float(self.mineColor1Input_R.get()), float(self.mineColor1Input_G.get()), float(self.mineColor1Input_B.get()), float(self.time1Input.get()))
            (r2, g2, b2, time2) = (float(self.mineColor2Input_R.get()), float(self.mineColor2Input_G.get()), float(self.mineColor2Input_B.get()), float(self.time2Input.get()))

            while self.mining:
                one = two = False
                (imageR, imageG, imageB) = ImageGrab.grab().getpixel((int(self.pixelX.get()), int(self.pixelY.get())))
                if r1-self.errorRange<=imageR<=r1+self.errorRange and g1-self.errorRange<=imageG<=g1+self.errorRange and b1-self.errorRange<=imageB<=b1+self.errorRange:
                    one = True
                elif r2-self.errorRange<=imageR<=r2+self.errorRange and g2-self.errorRange<=imageG<=g2+self.errorRange and b2-self.errorRange<=imageB<=b2+self.errorRange:
                    two = True
                if one or two:
                    if one:
                        mouse.drag(0, 0, 0, 0, absolute=False, duration=time1)
                    elif two:
                        mouse.drag(0, 0, 0, 0, absolute=False, duration=time2)
                    time.sleep(1)
        except:
            self.stopButton.invoke()
            print("It no worky")
            
    def stop(self):
        self.mining = False

    def pickobulousLoop(self):
        try:
            time.sleep(5)
            while self.mining:
                mouse.right_click()
                time.sleep(3.5)
                mouse.right_click()
                time.sleep(3.5)
                mouse.right_click()
                for i in range(120):
                    time.sleep(1)
                    if self.mining==False:
                        break
        except:
            pass

window = Window(root)

window.placeFrames()

root.update_idletasks()
