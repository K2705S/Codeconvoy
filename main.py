import pyfiglet
import pyttsx3 
from winsound import Beep
from barcode import Code128 , PROVIDED_BARCODES , PZN
from barcode.writer import ImageWriter
import os
def remove(string):
    return string.replace(" ", "") 
x = writer=ImageWriter()
while True:
    u = input("Enter IMG format supported formats are SVG and PNG : ")
    if u == "SVG" or "svg":
        x = ""
        print("Done....")
        print(x)
        break
    if u == "PNG" or "png":
        print("Done....")
        print(x)
        break
    elif x:
        print("")
        print(x)
def PrintER(remove):
    global x
    pyfiglet.print_figlet("BARCODE",font = "banner3-D")
    class Print():
      def BAR():
            while True:
                os.system("color a ")
                
                Terminal = input("<: ")
                if Terminal == '':
                    print("<:")
                elif Terminal == 'BAR':
                        number = input("Enter to convert to barcode :")
                        if number == '':
                            number = 'NULL'
                        number = remove(number)

                        my_code = Code128(number, x)
                        my_code.save(number)
                        if x == "writer=ImageWriter()":
                            os.system(number+".png")
                        if x == "":
                            os.system(number+".svg")
               
                elif Terminal == "-cls":
                    os.system("cls")
                elif Terminal == "-exit":
                    os.system("color 7")
                    break
                elif Terminal == "help":
                    print("'BAR' - to make barcodes ")
                    print("'-cls' - clears the screen ")
                    print("'-exit' - to exit ")
                elif Terminal: 
                    print("")
    return Print

Print = PrintER(remove)
Print.BAR()
Beep(500,500)
pyttsx3.speak("Done")