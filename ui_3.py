
import sys

a = sys.argv[1]

k = "kkk"

from colorutils import Color

# coding:utf-8

# obj_text27_list = [] # !!! это будет обязательно, но ниже

def look_for_textname(name, quest, objname): # принимает строку в которой искать, и что ищем
                              # наприм. QPushButton
    k = quest                                                                   
    obj_text27 = ''      
    count = 0
                                                                 
    #if 'QPushButton' in k:                                                     
    if objname in k:                                                            
        btn01 = k.split('.')                                                    
        btn02var = btn01[1].split(' = ')                                        
        obj_name = btn02var[0] # имя переменной Button                          
    
        with open(a, "r") as f4:
                 k5 = 'k5'
                 while k5:
                    k5 = f4.readline()                       
                    """
                    print('k5 = ', k5)
                    print('obj_name = ', obj_name)
                    print('objname = ', objname)
                    input('-------------')
                    # print('k5_str = ', k5_str)
                    """

                    if obj_name in k5:                        
                        if 'setText' in k5:                        
                            if count > 0: break
                            count += 1
                            obj_text22 = k5.split('.')               
                            obj_text23 = obj_text22[2].split(',')    
                            #print('obj_text23 = ', obj_text23)      
                            obj_text24 = obj_text23[1]               
                            #print('obj_text24 = ', obj_text24)      
                            obj_text25 = obj_text24.split('"')       
                            # print('obj_text25 = ', obj_text25)     
                            obj_text27 = obj_text25[1]               

    return obj_text27


def look_for(name, obj_text27, quest, objname): # принимает строку в которой искать, и что ищем
                              # наприм. QPushButton
    k = quest                                    
    count = 0                           
                                                                           
    #if 'QPushButton' in k:                                                     
    if objname in k:                                                            
        btn01 = k.split('.')                                                    
        btn02var = btn01[1].split(' = ')                                        
        obj_name = btn02var[0] # имя переменной Button                          
    
        # print("obj_name = ",obj_name)                                                               
        # открываем заново и читаем все строки, в которых есть этот объект      
        # по таким темам:                                                       

        obj_text27 = ''                                                         
        btn_x = ''                                                              
        btn_y = ''                                                              
        obj_x = ''                                                              
        obj_y = ''                                                              
        fg_color = ''
        bg_color = ''
        zz2 = ''

        flag = 0
        with open(a, "r") as f4:
                 k5 = 'k5'
                 while k5:

                    if flag == 0:
                       k5 = f4.readline() 

                    flag = 0
                    if obj_name in k5:                            
                       #if 'setGeometry' in k5_str:  # !!! так не найдет !!!
                       if 'setGeometry' in k5:                    
                           if count > 0: break
                           print('setGeometry')
                           count += 1
                           k5_str = k5.split('.')
                           btn02geom = k5_str[3].split(',')            
                           btn_x = int(btn02geom[0][6:]) # X              
                           btn_y = int(btn02geom[1].strip()) # Y          
                           obj_x = int(btn02geom[2].strip())      # rel x 
                           btn02geom[3] = btn02geom[3].split(')')         
                           obj_y = int(btn02geom[3][0].strip())  # rel y  

                           print('========== obj_name = ', obj_name)

                       if 'setStyleSheet' in k5:
                           # отдельная функц.
                           k6_str = k5.split('.')
                           k6_style = k6_str[2]
                           if '"color:' in k6_style:
                               k6_style = k6_style.split(':')
                               k6_rgb = k6_style[1].split(';')
                               rgb01 = k6_rgb[0].split('rgb(')
                               #rgb01 =  [' ', '255, 0, 0)']
                               rgb01 = rgb01[1]
                               rgb01 = rgb01.split(',')
                               gb01 = rgb01[2].split(")")
                               rgb01[2] = int(gb01[0])
                               rgb01[0] = int(rgb01[0])
                               rgb01[1] = int(rgb01[1])
                               rgb = rgb01
                               #print('rgb01 = ', rgb01)
                               #k6_rgb =  rgb(85, 255, 255);
                               #k6_rgb =  rgb(255, 0, 255);

                               # from colorutils import Color  # в самом верху есть
                               # zz = 'rgb(255, 0, 0)'         
                               zz = "rgb = ("+str(rgb[0])+',' + str(rgb[1])+\
                                     ',' +str(rgb[2])+")"
                               zz2 = zz

                               k5 = f4.readline()
                               flag = 1
                               if 'background-color' in k5:

                                   bg_color = k5.split(':')
                                   bg_color = bg_color[1][:-3]
                                   print('inner bg_color = ', bg_color)
                                   # inner bg_color =   rgb(255, 255, 0);

                                   rgb02 = bg_color.split('rgb(')
                                   qaz = rgb02[1]
                                   qaz = qaz.split(')')
                                   qaz = qaz[0]
                                   rgb02 = [int(k) for k in qaz.split(',')]

                                   print('rgb02 = ',rgb02)
                                   zz = "rgb = ("+str(rgb02[0])+',' + str(rgb02[1])+\
                                     ',' +str(rgb02[2])+")"
                                   bg_color = zz

        return obj_name, str(btn_x), str(btn_y), str(obj_x),\
               str(obj_y), fg_color, bg_color, zz2
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

# ===================================

with open(name, "a+") as ff:  
   ff.write(shapka)         

with open(a, "r") as f:
   while k:
       k = f.readline()
       if not win_geom:
         if 'MainWindow.resize' in k:
                win_geom01 = k.split('(')
                win_geom02 = win_geom01[1].split(',') 
                win_x = win_geom02[0] #               
                win_y = win_geom02[1][:-2] #      
                win_y = win_y.strip()
                root_geometry = "('" + win_x + "x" + win_y + "')"
                with open(name, "a+") as ff:  
                     ff.write("root.geometry"+root_geometry+"\n")
         #MainWindow.resize(800, 600)
         #root.geometry('800x600')

         #======================
       if 'QPushButton' in k:
          #print('=======> if QPushButon <<==========')
          #print('count =  ',count)
          #count += 1

          obj_27 = look_for_textname(name, k, 'QPushButton')
          #print('obj_27 = ', obj_27)

          obj_name, btn_x, btn_y, obj_x, obj_y, fg_color, bg_color, zz2 = look_for(name, 
                    obj_27, k, 'QPushButton')

          if fg_color:
              exec("c = Color("+zz2+")")                  
              fg_color = c.hex        
              qa = "fg = '" + fg_color +"',"
              fg_color = qa
              print('fg_color = ', fg_color)

          if bg_color:
              #qa = bg_color[:-1]                    
              #qa = qa[:4] + " = " + qa[4:]          
              #bg_color = qa                         
                                                    
              print('bg_color(2) = ', bg_color)          
                                                    
              exec("d = Color(" + bg_color + ")")              
              bg_color = d.hex                      
              qa = "bg = '" + bg_color +"',"
              bg_color = qa

              #print('bg_color = ', bg_color)       
                                                    
              #print('fg_color = ',fg_color)                  
              # хоть тут работает !!!               
              #========== obj_name =  pushButton    
              #k6_rgb =  rgb(255, 0, 0);            
              #c.hex =  #ff0000                     


          obj_name_text = obj_name+ "= Button("+bg_color+fg_color+" text='"+obj_27+"').place("
          obj_place = "x ="+btn_x+",y="+btn_y+", width="+obj_x+", height="+obj_y+")"

          with open(name, "a+") as ff:                          
             ff.write(obj_name_text+obj_place)
             ff.write('\n')                                                      
                           

       if 'QLabel' in k:

          obj_27 = look_for_textname(name, k, 'QLabel')
          obj_name, btn_x, btn_y, obj_x, obj_y, fg_color, bg_color, zz2 = look_for(name, 
                    obj_27, k, 'QLabel')

          if fg_color:
              exec("c = Color("+zz2+")")                  
              fg_color = c.hex        
              qa = "fg = '" + fg_color +"',"
              fg_color = qa


          if bg_color:
              qa = bg_color[:-1]                   
              qa = qa[:4] + " = " + qa[4:]         
              bg_color = qa                        
                                                   
              exec("d = Color(" + bg_color + ")")              
              bg_color = d.hex               
              qa = "bg = '" + bg_color +"',"
              bg_color = qa

          obj_name_text = obj_name+ "= Label("+bg_color+fg_color+" text='"+obj_27+"').place("
          obj_place = "x ="+btn_x+",y="+btn_y+", width="+obj_x+", height="+obj_y+")"

          with open(name, "a+") as ff:                          
             ff.write(obj_name_text+obj_place)
             ff.write('\n')                                                      
                           

       if 'QCheckBox' in k:
          obj_27 = look_for_textname(name, k, 'QCheckBox')
          obj_name, btn_x, btn_y, obj_x, obj_y, fg_color, bg_color, zz2 = look_for(name, 
                    obj_27, k, 'QCheckBox')

          if fg_color:
              exec("c = Color("+zz2+")")                  
              fg_color = c.hex        
              qa = "fg = '" + fg_color +"',"
              fg_color = qa


          if bg_color:
              qa = bg_color[:-1]                   
              qa = qa[:4] + " = " + qa[4:]         
              bg_color = qa                        
                                               
              print('checkbox bg_color = ',bg_color)
              exec("d = Color(" + bg_color + ")")              
              bg_color = d.hex                     
              qa = "bg = '" + bg_color +"',"
              bg_color = qa


          obj_name_text = obj_name+ "= Checkbutton("+bg_color+fg_color+" text='"+obj_27+"').place("
          obj_place = "x ="+btn_x+",y="+btn_y+", width="+obj_x+", height="+obj_y+")"

          with open(name, "a+") as ff:                          
             ff.write(obj_name_text+obj_place)
             ff.write('\n')                                                      


       if 'QRadioButton' in k:
          obj_27 = look_for_textname(name, k, 'QRadioButton')
          obj_name, btn_x, btn_y, obj_x, obj_y, fg_color, bg_color, zz2 = look_for(name, 
                    obj_27, k, 'QRadioButton')

          if fg_color:
              exec("c = Color("+zz2+")")                  
              fg_color = c.hex        
              qa = "fg = '" + fg_color +"',"
              fg_color = qa


          if bg_color:
              qa = bg_color[:-1]                       
              qa = qa[:4] + " = " + qa[4:]             
              bg_color = qa                            
                                                       
              exec("d = Color(" + bg_color + ")")              
              bg_color = d.hex                         
              qa = "bg = '" + bg_color +"',"
              bg_color = qa


          obj_name_text = obj_name+ "= Radiobutton("+bg_color+fg_color+" text='"+obj_27+"').place("
          obj_place = "x ="+btn_x+",y="+btn_y+", width="+obj_x+", height="+obj_y+")"

          with open(name, "a+") as ff:                          
             ff.write(obj_name_text+obj_place)
             ff.write('\n')                                                      


#QRadioButton
#QCheckBox


with open(name, "a+") as ff:  
    ff.write(podval)

