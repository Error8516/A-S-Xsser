import time
import sys
import os
#############################
def __banner__():
      os.system("clear")
      print("")
      time.sleep(0.1)
#############################      
      print("""
    ___        _____    _  __                    
   /   |      / ___/   | |/ /_____________  _____
  / /| |______\__ \    |   // ___/ ___/ _ \/ ___/
 / ___ /_____/__/ /   /   |(__  |__  )  __/ /    
/_/  |_|    /____/   /_/|_/____/____/\___/_/ V1                                      
##########################################################
##            Developer: Seyyed Ali Taansan             ##
##            My Age: 15 Yers Old                       ##
##            Country: Iran-Qasre Shirin                ## 
##            Instagram: seyyedalitanasan               ##
##            Github: github.com/Error8516              ##
##########################################################
      """)

#############################           
def __main__():
      __banner__()
      time.sleep(0.5)
      
      print("(1) Go To...")
      time.sleep(0.1)
      print("(2) Update")
      time.sleep(0.1)
      print("(3) Exit") 
      print("")
      
      try:
            MainInput= input("[+] Select Number 卐 ")
      except:
            sys.exit() 
            
      if (MainInput == ""):
            time.sleep(1)
            __main__()

      if (MainInput == "1"):
            __MohitMasaht__() 
      elif (MainInput == "2"):
            Update()
      elif (MainInput == "3"):
            sys.exit()
#############################
def Update():
      time.sleep(0.5)
      __banner__()
      
      print("*"*58)
      print("[1] God willing, in the next updates, we will improve this \n    tool and cover the weaknesses")
      print("*"*58)
#############################
def __MohitMasaht__():
      __banner__()
      time.sleep(0.5)
      
      print("(01) Square") # مربع
      time.sleep(0.1)
      print("(02) Rectangle") # مستطیل
      time.sleep(0.1)
      print("(03) Triangle") # مثلث
      time.sleep(0.1)
      print("(04) Equivalent Legs") # متساوی الساقین
      time.sleep(0.1)
      print("(05) Equivalent Sides") # متساوی اضلاع
      time.sleep(0.1)
      print("(06) Qaem Al-Zawiya") # قائم لزاویه
      time.sleep(0.1)
      print("(07) Trapezius") # ذوزنقه
      time.sleep(0.1)
      print("(08) Diamond") # لوزی
      time.sleep(0.1)
      print("(09) Circle") # دایره
      time.sleep(0.1)
      print("(10) Butter") # کره
      time.sleep(0.1)
      print("(11) Oval") # بیضی
      time.sleep(0.1)
      print("(12) Regular Polygons") # چند ضلعی منتظم
      time.sleep(0.1)
      print("(13) Volume Rectangular Cube") # حجم مکعبمستطیل
      print("")
      
      try:
            MohitInput= input("[+] Select Number 卐 ")
      except:
            sys.exit()
            
      if (MohitInput == ""):
            time.sleep(0.5)
            __main__()
            
      elif (MohitInput == "1"):
            Square()
      elif (MohitInput == "01"):
            Square()
            
      elif (MohitInput == "2"):
            Rectangle()
      elif (MohitInput == "02"):
            Rectangle()
            
      elif (MohitInput == "3"):
            Triangle()
      elif (MohitInput == "03"):
            Triangle()
            
      elif (MohitInput == "4"):
            EquivalentLegs()
      elif (MohitInput == "04"):
            EquivalentLegs() 
            
      elif (MohitInput == "5"):
            EquivalentSides()
      elif (MohitInput == "05"):
            EquivalentSides()

      elif (MohitInput == "6"):
            QaemAlZawiya()
      elif (MohitInput == "06"):
            QaemAlZawiya() 

      elif (MohitInput == "7"):
            Trapezius()
      elif (MohitInput == "07"):
            Trapezius() 

      elif (MohitInput == "8"):
            Diamond()
      elif (MohitInput == "08"): 
            Diamond()

      elif (MohitInput == "9"):
            Circle()
      elif (MohitInput == "09"): 
            Circle()
            
      elif (MohitInput == "10"):
            Butter()
 
      elif (MohitInput == "11"): 
            Oval()

      elif (MohitInput == "12"):   
            RegularPolygons()

      elif (MohitInput == "13"):   
            VolumeRectangularCube()

#############################
def Square():   # مربع
      time.sleep(0.5)
      __banner__()      
      print("")
      
      try:
            SquareInput= float(input("Enter a side 卐 "))
            print("")
      except:
            sys.exit()
            
      if (SquareInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()

      time.sleep(2)
      print("-"*40)
      print("[+] Environment: ",SquareInput ** 2)
      print("[+] Area: ", SquareInput * SquareInput)
      print("-"*40)
      
      try:
            print("")
            Square_Input= input("[!] Go To Home (press Enter...) ")
            __main__()
      except:
            sys.exit()      
#############################
def Rectangle():  # مستطیل
      time.sleep(0.5)
      __banner__()      
      print("")
      
      try:
            HeightInput= float(input("Enter the Lenght 卐 "))
            WidthInput= float(input("Enter the Width 卐 "))
            print("")
      except:
            sys.exit()
            
      if (HeightInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (WidthInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()

      time.sleep(2)
      print("-"*40)
      print("[+] Environment: ",(HeightInput + WidthInput) * 2)
      print("[+] Area: ", HeightInput * WidthInput)
      print("-"*40)
      
      try:
            print("")
            Rectangle_Input= input("[!] Go To Home (press Enter...) ")
            __main__()
      except:
            sys.exit()
#############################
def Triangle():  # مثلث
      time.sleep(0.5)
      __banner__()
      
      try:
            Zel1= float(input("Enter the first side 卐 "))
            Zel2= float(input("Enter the second side 卐 "))
            Zel3= float(input("Enter the third side 卐 "))
            QedInput= float(input("Enter the rule 卐 "))
            heightInput= float(input("Enter the Lenght 卐 "))
            print("")
      except:
            sys.exit()
            
      if (QedInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (heightInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (Zel1 == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (Zel2 == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (Zel3 == ""):
            time.sleep(0.5)
            __MohitMasaht__()
   
      time.sleep(2)
      print("-"*40)
      print("[+] Environment: ",(Zel1 + Zel2 + Zel3))
      print("[+] Area: ", (QedInput * heightInput) / 2)
      print("-"*40)
      
      try:
            print("")
            Triangle_Input= input("[!] Go To Home (press Enter...) ")
            __main__()
      except:
            sys.exit()      

#############################
def EquivalentLegs():  # متساوی الساقین
      time.sleep(0.5)
      __banner__()
      
      try:
            QedELInput= float(input("Enter the rule 卐 "))
            heightELInput= float(input("Enter the Lenght 卐 "))
            ZleELInput= float(input("Enter a side 卐 "))
            print("")
      except:
            sys.exit()

      if (QedELInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (heightELInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (ZleELInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
                        
      time.sleep(2)
      print("-"*40)
      print("[+] Environment: ",(ZleELInput * 3))
      print("[+] Area: ", (QedELInput * heightELInput) / 2)   
      print("-"*40)

      try:
            print("")
            EquivalentLegsInput= input("[!] Go To Home (press Enter...) ")
            __main__()
      except:
            sys.exit()
#############################
def EquivalentSides(): # متوازی اضلاع
      time.sleep(0.5)
      __banner__()
      
      try:
            ZelES1= float(input("Enter the first side 卐 "))
            ZelES2= float(input("Enter the second side 卐 "))
            ZelES3= float(input("Enter the third side 卐 "))
            QedESInput= float(input("Enter the rule 卐 "))
            heightESInput= float(input("Enter the Lenght 卐 "))
            print("")
      except:
            sys.exit()      

      if (QedESInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (heightESInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (ZelES1 == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (ZelES2 == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (ZelES3 == ""):
            time.sleep(0.5)
            __MohitMasaht__()

      time.sleep(2)
      print("-"*40)
      print("[+] Environment: ",(ZelES1 * 3))
      print("[+] Area: ", (QedESInput * heightESInput) / 2)   
      print("-"*40)
      
      try:
            print("")
            EquivalentSidesInput= input("[!] Go To Home (press Enter...) ")
            __main__()
      except:
            sys.exit()      
#############################
def QaemAlZawiya(): # قائم لزاویه
      time.sleep(0.5)
      __banner__()
      
      try:
            ZelQAZ1= float(input("Enter the first side 卐 "))
            ZelQAZ2= float(input("Enter the second side 卐 "))
            ZelQAZ3= float(input("Enter the third side 卐 "))
            QedQAZInput= float(input("Enter the rule 卐 "))
            heightQAZInput= float(input("Enter the Lenght 卐 "))
      except:
            sys.exit()

      if (QedQAZInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (heightQAZInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (ZelQAZ1 == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (ZelQAZ2 == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (ZelQAZ3 == ""):
            time.sleep(0.5)
            __MohitMasaht__()

      time.sleep(2)
      print("")
      print("-"*40)
      print("[+] Environment: ",(ZelQAZ1 + ZelQAZ2 + ZelQAZ3))
      print("[+] Area: ", (QedQAZInput * heightQAZInput) / 2)   
      print("-"*40)
      
      try:
            print("")
            QaemAlZawiyaInput= input("[!] Go To Home (press Enter...) ")
            __main__()
      except:
            sys.exit()      

#############################
def Trapezius(): # ذوزنقه
      time.sleep(0.5)
      __banner__()
      
      try:
            ZelT1= float(input("Enter the first side 卐 "))
            ZelT2= float(input("Enter the second side 卐 "))
            ZelT3= float(input("Enter the third side 卐 "))
            ZelT4= float(input("Enter the four side 卐 ")) 
            QedTBZInput= float(input("rule Big 卐 "))
            QedKoInput= float(input("rule small 卐 "))
            HeightTInput= float(input("Enter the Lenght 卐 "))
      except:
            sys.exit()      

      if (ZelT1 == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (ZelT2 == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (ZelT3 == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (ZelT4 == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (QedTBZInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (QedKoInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (HeightTInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()

      time.sleep(2)
      print("")
      print("-"*40)
      print("[+] Environment: ",(ZelT1 + ZelT2 + ZelT3 + ZelT4))
      print("[+] Area: ", (QedTBZInput + QedKoInput) * (HeightTInput) / 2)
      print("-"*40)

      try:
            print("")
            TrapeziusInput= input("[!] Go To Home (press Enter...) ")
            __main__()
      except:
            sys.exit()      
#############################
def Diamond():   # لوزی
      time.sleep(0.5)
      __banner__()
      
      try:
            ZelD1= float(input("Enter a side 卐 "))
            LargeDiameterInput= float(input("large a diameter 卐 "))
            smallDiameterInput= float(input("small a diameter 卐 "))
      except:
            sys.exit()          

      if (ZelD1 == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (LargeDiameterInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (smallDiameterInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()

      time.sleep(2)
      print("")
      print("-"*40)
      print("[+] Environment: ",(ZelD1 ** 4))
      print("[+] Area: ", (LargeDiameterInput * smallDiameterInput) / 2)
      print("-"*40)

      try:
            print("")
            DiamondInput= input("[!] Go To Home (press Enter...) ")
            __main__()
      except:
            sys.exit()      

#############################
def Circle(): # دایره
      time.sleep(0.5)
      __banner__()
      
      try:
            RadiusCInput= float(input("Enter a Radius 卐 "))
      except:
            sys.exit()      

      if (RadiusCInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()

      time.sleep(2)
      print("")
      print("-"*40)
      print("[+] Environment: ",((RadiusCInput * RadiusCInput) * 3.14))
      print("[+] Area: ", (RadiusCInput * RadiusCInput) * 3.14)
      print("-"*40)

      try:
            print("")
            CircleInput= input("[!] Go To Home (press Enter...) ")
            __main__()
      except:
            sys.exit()      
#############################
def Butter():  # کره
      time.sleep(0.5)
      __banner__()
      
      try:
            RadiusBInput= input("Enter a Radius 卐 ")
      except:
            sys.exit()
            
      if (RadiusBInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()

      time.sleep(2)
      print("")
      print("-"*40)
      print("[+] Area: ",((RadiusCInput ** 2) * (3.14) * 4))
      print("-"*40)

      try:
            print("")
            ButterInput= input("[!] Go To Home (press Enter...) ")
            __main__()
      except:
            sys.exit() 
#############################
def Oval(): # بیضی
      time.sleep(0.5)
      __banner__()
      
      try:
            bigInput= float(input("Enter big a diameter 卐 "))
            smallInput= float(input("Enter small a diameter 卐 "))
      except:
            sys.exit()
            
      if (smallInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (bigInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()

      time.sleep(2)
      print("")
      print("-"*40)
      print("[+] Area: ",(bigInput / 2) * (smallInput / 2) / 3.14)
      print("-"*40)

      try:
            print("")
            OvalInput= input("[!] Go To Home (press Enter...) ")
            __main__()
      except:
            sys.exit() 
#############################
def RegularPolygons(): # چند ضلعی منتظم
      time.sleep(0.5)
      __banner__()
      
      try:
            oneside= float(input("Enter a side 卐 "))   # تعداد اضلاع را وارد کنید
            TedadSide= float(input("Enter Tedad side 卐 ")) ########################
      except:
            sys.exit()
            
      if (oneside == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (TedadSide == ""):
            time.sleep(0.5)
            __MohitMasaht__()

      time.sleep(2)
      print("")
      print("-"*40)
      print("[+] Environment: ",oneside * TedadSide)
      print("-"*40)

      try:
            print("")
            RegularPolygons= input("[!] Go To Home (press Enter...) ")
            __main__()
      except:
            sys.exit()       

#############################
def VolumeRectangularCube(): # حجم مکعب مستطیل
      time.sleep(0.5)
      __banner__()
      
      try:
            LenghtInput= float(input("Enter a Lenght 卐 ")) # طول
            heightInput= float(input("Enter a height 卐 ")) # ارتفاع
            widthInput= float(input("Enter a width 卐 "))  # عرض     
      except:
            sys.exit()
            
      if (LenghtInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (heightInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
      elif (widthInput == ""):
            time.sleep(0.5)
            __MohitMasaht__()
            
      time.sleep(2)
      print("")
      print("-"*40)
      print("[+] Hagm: ",(LenghtInput * widthInput) * heightInput) ############# حجم
      print("-"*40)

      try:
            print("")
            VolumeRectangularCube= input("[!] Go To Home (press Enter...) ")
            __main__()
      except:
            sys.exit()      

#############################
#############################
__main__()
