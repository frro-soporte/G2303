import time
from kivy.app import App
# from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty,BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from business import NegocioSocio
from model import Socio
# import window 
from kivy.core.window import Window


class UsersList(GridLayout):
    dni  = StringProperty('')
    nombre  = StringProperty('')
    apellido  = StringProperty('')
    def __init__(self, **kwargs):
        super(UsersList,self).__init__(**kwargs)
        self.clear_widgets()
        self.cols = 1
        self.padding = dp(10)
        self.spacing = dp(10)
        self.size_hint_y = None
        users = NegocioSocio().todos()
        for user in users: 
            self.dni = str(user.dni)
            self.nombre = str(user.nombre)
            self.apellido = str(user.apellido)
            boxLy = BoxLayout(orientation='horizontal', size_hint_y=None,  height=dp(30),padding=5)
            boxLy.clear_widgets()
            btnEdit = Button(text='Editar ' + str(user.id), size_hint_x=None, width=dp(70),height=dp(50),background_color=(248/255, 205/255, 29/255, 0.8))
            btnDelete = Button(text='Eliminar ' + str(user.id), size_hint_x=None, width=dp(80),height=dp(50),background_color=(248/255, 29/255, 29/255, 0.8))
            btnDelete.bind(on_press= lambda x : self.delete_user(user.id,x))
            btnEdit.bind(on_press= lambda x : self.edit_user(x))
            label = Label(text=f"{self.dni}  /  {self.nombre}  /  {self.apellido} ",halign='left', markup=True,font_size=dp(15),size_hint_y=None,height=dp(25),color=(7/255, 12/255, 32/255, 0.95)) 
            # label.text = f"{user.dni} - {user.nombre} - {user.apellido}"
            boxLy.add_widget(label)
            boxLy.add_widget(btnEdit)
            boxLy.add_widget(btnDelete)            
            self.add_widget(boxLy)
        

    def delete_user(self, id,x):
        try:
            id = int(x.text.split(' ')[1])
            NegocioSocio().baja(id)
            print('User deleted')

        except Exception as e:
            print('Error :: ',e)

    def edit_user(self,x):
        id = int(x.text.split(' ')[1])
        MyMainApp.currentUser = int(id)
        sm.current = 'edituser'
        sm.transition.direction = 'right'


class UserList(Screen):
    # pass
    # SHOW USER LIST 
    def on_pre_enter(self):
        print('on_pre_enter.................................................................')
        # get the current screen y clear the content
        # self.clear_widgets()
        # self.ids.users_list.add_widget(UsersList())
        UsersList()
        # self.ids.add_widget(v)
        # self.rootWindow().refresh_from_layout()
        # self.ids.users_list.add_widget(UsersList())

    def refresh(self):
        pass
        # Window.request_update()
        # clear the screen content 
        # self.ids.users_list.clear_widgets()
        # add the new content
        # self.ids.users_list.add_widget(UsersList())

class AddUser(Screen):
    error  = StringProperty('')
    success  = StringProperty('')
    def on_pre_enter(self):
        self.success = ''
        self.error = ''
    def add_user(self,dni,nombre,apellido):
        socio = Socio(dni=dni, nombre=nombre, apellido=apellido)
        # save the socio
        try :
            res = NegocioSocio().alta(socio)
            if res :
                self.error = ''
                self.success = 'Socio guardado con exito'
                self.ids.dni.text = ''
                self.ids.nombre.text = ''
                self.ids.apellido.text = ''

            else:
                print('error')
                self.error = str(e)
        except Exception as e:
            self.success = ''
            self.error = str(e)

class EditUser(Screen):
    error  = StringProperty('')
    success  = StringProperty('')
    cid =StringProperty('')
    def on_pre_enter(self):
        c = MyMainApp()
        self.success = ''
        self.error = ''
        self.cid = str(c.currentUser)
        soc = NegocioSocio().buscar(c.currentUser)
        if soc == None:
            print('no se encontro el socio')
            return       
        # set the dni 
        self.ids.dni.text = str(soc.dni)
        self.ids.nombre.text = str(soc.nombre)
        self.ids.apellido.text = str(soc.apellido)
        print('GLOBAL CURRENT USER :::::',c.currentUser )
    def edit_user(self,dni,nombre,apellido):
        socio = Socio(dni=dni, nombre=nombre, apellido=apellido,id=self.cid)
        try :
            res = NegocioSocio().modificacion(socio)
            if res :
                self.error = ''
                self.success = 'Socio modificado con exito'
                self.ids.dni.text = ''
                self.ids.nombre.text = ''
                self.ids.apellido.text = ''
            else:
                print('error')
                self.error = str(e)
        except Exception as e:
            self.success = ''
            self.error = str(e)

class MainWindowManager(ScreenManager):
    pass

sm = Builder.load_file('abm.kv')

class MyMainApp(App):
    currentUser = 444
    def build(self):
        Window.clearcolor = (245/255, 245/255, 245/255, 1)
        Window.size = (450, 600)
        return sm       

MyMainApp().run()