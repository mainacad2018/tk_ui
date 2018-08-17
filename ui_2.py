
import sys

a = sys.argv[1]

k = "kkk"

# coding:utf-8

obj_text27_list = []

def look_for(quest, objname):
    global obj_text27_list
    # obj_text27_list = []
    k = quest                                                                   
                                                                           
    #if 'QPushButton' in k:                                                     
    if objname in k:                                                            
        btn01 = k.split('.')                                                    
        btn02var = btn01[1].split(' = ')                                        
        obj_name = btn02var[0] # имя переменной Button                          
    
        print("obj_name = ",obj_name)                                                               
        # открываем заново и читаем все строки, в которых есть этот объект      
        # по таким темам:                                                       
        obj_text27 = ''                                                         
        btn_x = ''                                                              
        btn_y = ''                                                              
        obj_x = ''                                                              
        obj_y = ''                                                              

        with open(a, "r") as f4:
                 k5 = 'k5'
                 while len(k5):
                    k5 = f4.readline()                       
                    k5_str = k5.split('.')
                    # print('k5_str = ', k5_str)

                    if obj_name in k5:                            
                       """
                       print('k5_str = ', k5_str)
                       print('k5 = ', k5)
                       input('==press key==')
                       """
                       #if 'setGeometry' in k5_str:  # !!! так не найдет !!!
                       if 'setGeometry' in k5:                        
                           btn02geom = k5_str[3].split(',')            
                           btn_x = int(btn02geom[0][6:]) # X              
                           btn_y = int(btn02geom[1].strip()) # Y          
                           obj_x = int(btn02geom[2].strip())      # rel x 
                           btn02geom[3] = btn02geom[3].split(')')         
                           obj_y = int(btn02geom[3][0].strip())  # rel y  
                           """
                           print('k5_str = ', k5_str) 
                           print('btn_x = ', btn_x) 
                           print('btn_y = ', btn_y) 
                           print('obj_x = ', obj_x) 
                           print('obj_y = ', obj_y) 


                           input('==press key==')     
                           """

                       # ===>>>>
                       """
                       if 'setObjectName' in k5:                 
                           btn01text[2] = btn01text[2].split("\"")   
                           obj_text = btn01text[2][1]                
                       """
                           # !!! =================================================   
                           
                       #obj_text27_list = []
                       with open(a, "r") as f3:                                      
                           k4 = 'k4'                                                 
                           while len(k4):                                            
                              k4 = f3.readline()                                     
                              if obj_name in k4:                                     
                                   if 'setText'  in k4:                   
                                      obj_text22 = k4.split('.')                        
                                      obj_text23 = obj_text22[2].split(',')          
                                      #print('obj_text23 = ', obj_text23)            
                                      obj_text24 = obj_text23[1]                     
                                      #print('obj_text24 = ', obj_text24)            
                                      obj_text25 = obj_text24.split('"')             
                                      # print('obj_text25 = ', obj_text25)           
                                      obj_text27 = obj_text25[1]                     
                                      # print('obj_text27 = ', obj_text27)
                                      if not obj_text27 in obj_text27_list:
                                             obj_text27_list.append(obj_text27)


        #self.pushButton.setText(_translate("MainWindow", "PushButton"))

        obj_text27_list = [0,] + obj_text27_list # оно global !!!
        print('obj_text27_list = ', obj_text27_list)

        return obj_name, obj_text27_list, str(btn_x), str(btn_y), str(obj_x), str(obj_y)
    return None

class WidgetStorage():

    def __init__(self, obj_name, obj_text, btn_x, btn_y, obj_x, obj_y):

       self.obj_name = []
       self.obj_text = obj_text
       self.btn_x  = []
       self.btn_y  = []
       self.obj_x  = []
       self.obj_y  = []

       self.obj_name.append(obj_name)
       # self.obj_text.append(obj_text)
       self.btn_x.append(btn_x)
       self.btn_y.append(btn_y)
       self.obj_x.append(obj_x)
       self.obj_y.append(obj_y)




spisok = []    

shapka = """

from tkinter import *;
root = Tk();

"""
podval = """
root.mainloop()

"""

name = str(a.split('.')[0]) + "_tk_" + '.py'


win_geom = False

btn_store = WidgetStorage(0,0,0,0,0,0)


with open(name, "a+") as ff:  
   ff.write(shapka)         

   with open(a, "r") as f:
      while len(k):
         k = f.readline()

         if not win_geom:
            if 'MainWindow.resize' in k:
                win_geom01 = k.split('(')
                win_geom02 = win_geom01[1].split(',') 
                # print('win_geom02 = ', win_geom02) 
                # win_geom02 =  ['800', ' 600)\n']
                win_x = win_geom02[0] #               
                win_y = win_geom02[1][:-2] #      
                #print('win_y = ', win_y)                
                win_y = win_y.strip()
                #print('win_y = ', win_y)                
                # print('win_x, win_y = ', win_x, win_y)
                root_geometry = "('" + win_x + "x" + win_y + "')"
                ff.write("root.geometry"+root_geometry+"\n")
         #MainWindow.resize(800, 600)
         #root.geometry('800x600')


         spisok = look_for(k, 'QPushButton')
         
         if spisok:
            btn_store.obj_name.append(spisok[0]) #obj_name
            #btn01 = btn_store.obj_name[-1]

            btn_store.obj_text = spisok[1]
            #btn_store.obj_text.append(spisok[1]) #obj_text
            #btn01_text = btn_store.obj_text[-1]

            btn_store.btn_x.append(spisok[2]) #obj_name
            btn_store.btn_y.append(spisok[3]) #obj_name
            btn_store.obj_x.append(spisok[4]) #obj_name
            btn_store.obj_y.append(spisok[5]) #obj_name

            
            spisok = look_for(k, 'QLabel')

         if spisok:
            ff.write("label01 = Label(bg='green', text='"+spisok[1]+"').place(x = "+\
                 spisok[2]+", y="+spisok[3]+", width="+spisok[4]+", height="+spisok[5]+")")
            ff.write('\n')

   for z in range(1, len(btn_store.obj_name)):
      print('z = ', z)
      print('len btn_store.obj_name = ', len(btn_store.obj_name) )
      print('btn_store.obj_name = ', btn_store.obj_name )
      print('btn_store.obj_text = ', btn_store.obj_text )
      print('btn_store.btn_x = ', btn_store.btn_x )
      print('btn_store.btn_y = ', btn_store.btn_y )
      print('btn_store.obj_x = ', btn_store.obj_x )
      print('btn_store.obj_y = ', btn_store.obj_y )



      ff.write(str(btn_store.obj_name[z]) + " = Button(bg='red', text='"+ \
               str(btn_store.obj_text[z])+"').place(x = "+\
               str(btn_store.btn_x[z]) +", y="+str(btn_store.btn_y[z])+", \
               width="+str(btn_store.obj_x[z])+", height="+str(btn_store.obj_y[z])+")")
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





