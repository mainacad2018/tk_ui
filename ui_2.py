# coding: utf-8
import sys

a = sys.argv[1]

k = "kkk"

def look_for(quest, objname):

         k = quest

         #if 'QPushButton' in k:
         if objname in k:
             btn01 = k.split('.')
             btn02var = btn01[1].split(' = ')
             obj_name = btn02var[0] # имя переменной Button

             # тогда читаем след. строку
             k2 = f.readline()
             btn01geom = k2.split('.')
             if 'setGeometry' in btn01geom[2]:
                 btn02geom = btn01geom[3].split(',')

                 btn_x = int(btn02geom[0][6:]) # X
                 btn_y = int(btn02geom[1].strip()) # Y
                 obj_x = int(btn02geom[2].strip())      # rel x

                 btn02geom[3] = btn02geom[3].split(')')
                 obj_y = int(btn02geom[3][0].strip())  # rel y

             # тогда читаем еще след. строку
             k3 = f.readline()
             btn01text = k3.split('.')
             if 'setObjectName' in btn01text[2]:
                 btn01text[2] = btn01text[2].split("\"")
                 obj_text = btn01text[2][1]

             # !!! =================================================

             with open(a, "r") as f3:
                 k4 = 'k4'
                 while len(k4):
                    k4 = f3.readline()                       
                    if obj_text in k4:                            
                         obj_text22 = k4.split('.')          
                         # print("obj_text22 = ", obj_text22) #
                         # print("obj_text = ", obj_text)     #

                         if 'setText'  in obj_text22[2]:            
                            obj_text23 = obj_text22[2].split(',') 
                            #print('obj_text23 = ', obj_text23)      
                            obj_text24 = obj_text23[1]              
                            #print('obj_text24 = ', obj_text24) 
                            obj_text25 = obj_text24.split('"')
                            print('obj_text25 = ', obj_text25) 
                            obj_text27 = obj_text25[1]


        #self.pushButton.setText(_translate("MainWindow", "PushButton"))

             return obj_name, obj_text27, str(btn_x), str(btn_y), str(obj_x), str(obj_y)
         return None

class BigSpisok():

    def __init__(self, obj_name, obj_text, obj_x, obj_y):
       self.obj_name = obj_name 
       self.obj_text = obj_text
       self.obj_x =  obj_x     
       self.obj_y =  obj_y

spisok = []    

shapka = """

from tkinter import *;
root = Tk();

"""
podval = """
root.mainloop()

"""

name = str(a.split('.')[0]) + "_tk_" + '.py'


with open(name, "a+") as ff:  
   ff.write(shapka)         


   with open(a, "r") as f:
      while len(k):
         k = f.readline()

         #MainWindow.resize(800, 600)
         #root.geometry('800x600')
         spisok = look_for(k, 'QPushButton')
         if spisok:
            ff.write("btn01 = Button(bg='red', text='"+spisok[1]+"').place(x = "+\
            spisok[2]+", y="+spisok[3]+", width="+spisok[4]+", height="+spisok[5]+")")
            ff.write('\n')

         spisok = look_for(k, 'QLabel')
         if spisok:
            ff.write("label01 = Label(bg='green', text='"+spisok[1]+"').place(x = "+\
                 spisok[2]+", y="+spisok[3]+", width="+spisok[4]+", height="+spisok[5]+")")
            ff.write('\n')

   ff.write(podval)
"""
lab01 = Label(root, image=pylogo, text="это метка", font="Arial 18").pack(side="right")
label.pack(padx = 20, pady = 50)
Основными параметрами place() являются:
anchor (якорь) – определяет часть виджета, для которой задаются координаты. Принимает значения N, NE, E, SE, SW, W, NW или CENTER. По умолчанию NW (верхний левый угол).

relwidth, relheight (относительные ширина и высота) – определяют размер виджета в долях его родителя.

relx, rely – определяют относительную позицию в родительском виджете. Координата (0; 0) – у левого верхнего угла, (1; 1) – у правого нижнего.

width, height – абсолютный размер виджета в пикселях. Значения по умолчанию (когда данные опции опущены) приравниваются к естественному размеру виджета, то есть к тому, который определяется при его создании и конфигурировании.

x, y – абсолютная позиция в пикселях. Значения по умолчанию приравниваются к нулю.

"""
   
   



"""
# from pprint import pprint
# pprint(zzz)

btn_width = str(btn_width+btn_x)
btn_height = str(btn_height+btn_y)



btn_width = str(btn_width)
btn_height = str(btn_height)
btn_x = str(btn_x)
btn_y = str(btn_y)

lab_width = str(lab_width+lab_x)
lab_height = str(lab_height+lab_y)


lab_width = str(lab_width)
lab_height = str(lab_height)
lab_x = str(lab_x)
lab_y = str(lab_y)
"""





