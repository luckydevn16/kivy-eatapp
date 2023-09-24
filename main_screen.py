import threading
import requests
import kivy
import folium
import webbrowser

# Import statements for other modules
# from splash_screen import SplashScreen
# from login import LoginScreen
# from signup import SignupScreen

from flask import Flask, jsonify
from kivy.config import Config
from kivy.uix.anchorlayout import AnchorLayout

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')

from kivy.app import App
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.webview import WebView
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Line
from kivy.uix.slider import Slider
from functools import partial
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.textfield import MDTextField
from datetime import datetime
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.uix.modalview import ModalView
import kivy.garden
from kivymd.uix.pickers import MDDatePicker
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivymd.uix.button import MDIconButton, MDRaisedButton, MDRoundFlatIconButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextFieldRect
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivymd.uix.button import MDFlatButton, MDFillRoundFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.toolbar import MDBottomAppBar
from kivy.uix.recycleview import RecycleView, RecycleDataAdapter
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivymd.uix.tab import MDTabs
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton, MDRectangleFlatIconButton


# Set the window size
Window.size = (350, 590)

############################################################################
# KV Code
############################################################################

restaurant_data = [
    {
        "img": "./assets/images/restaurants/r1.jpg",
        "name": "Noni",
        "address": "132, St. Dominic Street, Valletta VLT 1606, Malta",
        "special": "Fenek",
        "rating": 4.9,
        "price_level": "$$$-$$$$"
    },
    {
        "img": "./assets/images/restaurants/r2.jpg",
        "name": "Guze Bistro",
        "address": "22, Piazza San Gorg, Valletta VLT 1190, Malta",
        "special": "Pastizzi",
        "rating": 4.8,
        "price_level": "$$-$$$"
    },
    {
        "img": "./assets/images/restaurants/r3.jpg",
        "name": "De Mondion",
        "address": "Xara Palace Relais & Chateaux Hotel, Misrah il-Kunsill, Mdina, Malta",
        "special": "Bragioli",
        "rating": 4.7,
        "price_level": "$$$$"
    },
    {
        "img": "./assets/images/restaurants/r4.jpg",
        "name": "Tarragon",
        "address": "Qawra Palace Hotel, Qawra Road, St Paul's Bay SPB 1905, Malta",
        "special": "Bragioli",
        "rating": 4.7,
        "price_level": "$-$$"
    },
    {
        "img": "./assets/images/restaurants/r5.jpg",
        "name": "The Harbour Club",
        "address": "Strait Street, Valletta VLT 1432, Malta",
        "special": "Kapunata",
        "rating": 4.7,
        "price_level": "$"
    },
    {
        "img": "./assets/images/restaurants/r6.jpg",
        "name": "Barracuda",
        "address": "248, Tower Road, St Julian's STJ 1012, Malta",
        "special": "Aljotta",
        "rating": 4.6,
        "price_level": "$$"
    },
    {
        "img": "./assets/images/restaurants/r7.jpg",
        "name": "Rubino",
        "address": "53, Old Bakery Street, Valletta VLT 1450, Malta",
        "special": "Timpana",
        "rating": 4.6,
        "price_level": "$$$"
    },
    {
        "img": "./assets/images/restaurants/r8.jpg",
        "name": "The Summer Kitchen",
        "address": "Corinthia Palace Hotel & Spa, San Anton, Malta",
        "special": "Pastizzi",
        "rating": 4.6,
        "price_level": "$$$",
    },
    {
        "img": "./assets/images/restaurants/r9.jpg",
        "name": "The Boat House",
        "address": "Xatt l-Ahmar, Marsalforn Bay, Gozo Island, Malta",
        "special": "Bragioli",
        "rating": 4.5,
        "price_level": "$$-$$$"
    },
    {
        "img": "./assets/images/restaurants/r10.jpg",
        "name": "Medina Restaurant",
        "address": "Misrah il-Kunsill, Mdina MDN 1050, Malta",
        "special": "Fenek",
        "price_level": "$",
        "rating": 4.5,
    }
]

############################################################################
# KV Code
############################################################################

kv_code = """

# Footer
<Footer>:
    BoxLayout:
        orientation: 'vertical'

        MDBottomNavigation:
            text_color_normal: rgba(201, 103, 108, 255)
            text_color_active: rgba(181, 83, 88, 255)

            MDBottomNavigationItem:
                name: 'explore'
                text: "Explore"
                icon: 'silverware-fork-knife'
                on_tab_release: app.switch_to_screen('explore')
                active: False

            MDBottomNavigationItem:
                name: 'reservations'
                text: "Reservations"
                icon: 'calendar'
                on_tab_release: app.switch_to_screen('reservation')
                active: True

            MDBottomNavigationItem:
                name: 'more'
                text: "More"
                icon: 'dots-horizontal'
                on_tab_release: app.switch_to_screen('more')

# Splash Screen
<SplashScreen>:
    name: 'splash'
    id: splash_screen_content  

    FloatLayout:
        adaptive_height: True
                
        Button:
            text: 'Start'
            size_hint: 0.8, None
            height: dp(50)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            background_color: 0.8, 0, 0.5, 1
            on_release: app.switch_to_screen('explore')
            
# Explore Screen
<ExploreScreen>:
    name: 'explore'
    
    BoxLayout:
        orientation: 'vertical'
        adaptive_height: True
        spacing: dp(10)
        padding: dp(10)
        
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: "32dp"
            
            MDTextFieldRect:
                size_hint: 1, None
                height: "32dp"
                icon_left: "magnify"
                hint_text: 'Search for restaurant or location'
                
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: self.minimum_height
            
            Button:
                text: 'Restaurants'
                size_hint_y: None
                height: dp(32)
                background_color: 0.8, 0, 0.5, 1
                on_release: app.switch_to_tab('explore_restaurants')
            
            Button:
                text: 'Collections'
                size_hint_y: None
                height: dp(32)
                background_color: 0.8, 0, 0.5, 1
                on_release: app.switch_to_tab('explore_collections')
        
        ScrollView:
            id: explore_screen_content
            do_scroll_x: False
            do_scroll_y: True

        Footer:
            id: footer_navigation
            size_hint_y: None
            height: self.minimum_height

# Reservation Screen
<ReservationScreen>:
    name: 'reservation'
    
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)

        BoxLayout:
            size_hint_y: None
            height: dp(48)
            MDLabel:
                text: 'My Reservations'
                pos_hint: {'center_x': 0.5, 'top': 1}
                halign: 'center'
                font_size: '20sp'
                color: 0.5, 0, 0.5, 1

        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: self.minimum_height
            
            Button:
                text: 'Upcoming'
                size_hint_y: None
                height: dp(32)
                background_color: 0.8, 0, 0.5, 1
                on_release: app.switch_to_tab('reservation_upcoming')
                
            Button:
                text: 'Past'
                size_hint_y: None
                height: dp(32)
                background_color: 0.8, 0, 0.5, 1
                on_release: app.switch_to_tab('reservation_past')
                
        ScrollView:
            id: reservation_screen_content
            do_scroll_x: False
            do_scroll_y: True
        
        Footer:
            size_hint_y: None
            height: self.minimum_height
        
<MoreScreen>:
    name: 'more'
    
    BoxLayout:
        orientation: 'vertical'
        
        MDScrollView:
            MDList:
                OneLineAvatarIconListItem:
                    text: "Profile"
                    on_release: print("Profile Clicked!")        
                    IconLeftWidget:
                        icon: "account"        
                
                OneLineAvatarIconListItem:
                    text: "About Eat App"
                    on_release: print("About Eat App Clicked!")
                    IconLeftWidget:
                        icon: "information"
                        
                OneLineAvatarIconListItem:
                    text: "Region Selection"
                    on_release: print("Region Selection Clicked!")
                    IconLeftWidget:
                        icon: "map-marker"
        
        Footer:
            size_hint_y: None
            height: self.minimum_height


"""


############################################################################
# Common Widget
############################################################################


# Footer
class Footer(BoxLayout):
    pass

############################################################################
# Screens
############################################################################


# SplashScreen
class SplashScreen(Screen):
    splash_screen_content = ObjectProperty(None)

    def on_pre_enter(self, *args):
        print("Entering SplashScreen")


# ExploreScreen
class ExploreScreen(Screen):
    explore_screen_content = ObjectProperty(None)

    def on_pre_enter(self):
        print("Entering ExploreScreen")


# ReservationScreen
class ReservationScreen(Screen):
    reservation_screen_content = ObjectProperty(None)

    def on_pre_enter(self):
        print("Entering ReservationScreen")


class MoreScreen(Screen):
    more_screen_content = ObjectProperty(None)

    def on_pre_enter(self):
        print("Entering MoreScreen")

############################################################################
# Main Screen
############################################################################


class MainScreen(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.screen_manager = ScreenManager(transition=SlideTransition())

        # Load the root widget defined in the KV string
        root = Builder.load_string(kv_code)
        # root.app = self

        # Add the Splash, ExploreScreen, ReservationScreen and MoreScreen
        splash_screen = SplashScreen(name="splash")
        explore_screen = ExploreScreen(name="explore")
        reservation_screen = ReservationScreen(name="reservation")
        more_screen = MoreScreen(name="more")

        self.screen_manager.add_widget(splash_screen)
        self.screen_manager.add_widget(explore_screen)
        self.screen_manager.add_widget(reservation_screen)
        self.screen_manager.add_widget(more_screen)

        return self.screen_manager
        # return root

    def on_start(self):
        self.screen_manager.current = "splash"
        self.switch_to_tab("reservation_upcoming")
        self.switch_to_tab("explore_restaurants")

    def switch_to_screen(self, screen_name):
        self.screen_manager.current = screen_name

    def switch_to_tab(self, tab_name):
        if tab_name == "explore_restaurants":
            explore_screen = self.screen_manager.get_screen('explore')
            explore_screen_content = explore_screen.ids.explore_screen_content
            explore_screen_content.clear_widgets()

            parentLayout = GridLayout(cols=1, size_hint_y=None, spacing=dp(10), padding=[0, 0, 0, dp(55)])
            parentLayout.bind(minimum_height=parentLayout.setter('height'))

            for restaurant in restaurant_data:
                img = restaurant.get("img")
                name = restaurant.get("name")
                address = restaurant.get("address")
                special = restaurant.get("special")
                priceLevel = restaurant.get("price_level")
                rating = str(restaurant.get("rating"))

                relativeLayout = RelativeLayout(size_hint_x=1, size_hint_y=None, height=dp(200))

                image = Image(source=img, size_hint_y=None, height=dp(200), fit_mode="cover")

                floatLayout = FloatLayout(pos_hint={'x': 0, 'y': 0}, size_hint_x=1, size_hint_y=1)
                nameLabel = MDLabel(text=name, size_hint_x=1, size_hint_y=None, pos_hint={"x": 0.02, "center_y": 0.5}, theme_text_color="Custom", text_color=(1, 1, 1, 1), font_style="H6", font_size="20sp")
                addressLabel = MDLabel(text=address, size_hint_x=1, size_hint_y=None, pos_hint={"x": 0.02, "center_y": 0.35}, theme_text_color="Custom", text_color=(1, 1, 1, 1), font_style="Subtitle2", font_size="12sp")

                boxLayout = BoxLayout(orientation="horizontal", spacing=dp(8), pos_hint={"x": 0.02, 'center_y': 0.54})
                specialLabel = MDRectangleFlatButton(text=special, theme_text_color="Custom", text_color=(1, 1, 1, 1), line_color=(1, 1, 1, 1))
                priceLevelLabel = MDRectangleFlatButton(text=priceLevel, theme_text_color="Custom", text_color=(1, 1, 1, 1), line_color=(1, 1, 1, 1))
                boxLayout.add_widget(specialLabel)
                boxLayout.add_widget(priceLevelLabel)

                ratingButton = MDRectangleFlatIconButton(pos_hint={'right': 1, 'center_y': 0.90}, icon="star", theme_icon_color="Custom", icon_color=(1, 1, 1, 1), text=rating, theme_text_color="Custom", text_color=(1, 1, 1, 1), line_color=(0, 0, 0, 0))
                reserveButton = MDRaisedButton(text="Reserve Now", pos_hint={'right': 0.98, 'center_y': 0.13}, size_hint=(None, None), md_bg_color=(0.93, 0.49, 0.18, 1), theme_text_color="Custom", text_color=(1, 1, 1, 1))

                floatLayout.add_widget(nameLabel)
                floatLayout.add_widget(addressLabel)
                floatLayout.add_widget(boxLayout)
                floatLayout.add_widget(ratingButton)
                floatLayout.add_widget(reserveButton)

                relativeLayout.add_widget(image)
                relativeLayout.add_widget(floatLayout)

                parentLayout.add_widget(relativeLayout)

            explore_screen_content.add_widget(parentLayout)
            explore_screen_content.scroll_y = 1

        if tab_name == "explore_collections":
            explore_screen = self.screen_manager.get_screen('explore')
            explore_screen_content = explore_screen.ids.explore_screen_content
            explore_screen_content.clear_widgets()

            parentLayout = BoxLayout(orientation="vertical", adaptive_height=True)
            label = MDLabel(text="There are no active collections at the moment.", pos_hint={'center_x': 0.5, 'top': 1}, halign="center", font_size="16sp")
            parentLayout.add_widget(label)

            explore_screen_content.add_widget(parentLayout)

        if tab_name == "reservation_upcoming":
            reservation_screen = self.screen_manager.get_screen('reservation')
            reservation_screen_content = reservation_screen.ids.reservation_screen_content
            reservation_screen_content.clear_widgets()

            boxLayout = BoxLayout(orientation='vertical', adaptive_height=True)

            anchorLayout1 = AnchorLayout(anchor_x='center', anchor_y='center')
            subBoxLayout1 = BoxLayout(orientation='vertical', size_hint_x=1, size_hint_y=None)
            iconButton = MDIconButton(icon='calendar', pos_hint={"center_x": 0.5, "center_y": 0.5})
            label = MDLabel(text="You have no upcoming reservations!", halign='center', font_size='16sp')
            subBoxLayout1.add_widget(iconButton)
            subBoxLayout1.add_widget(label)
            anchorLayout1.add_widget(subBoxLayout1)

            anchorLayout2 = AnchorLayout(anchor_x='center', anchor_y='center')
            subBoxLayout2 = BoxLayout(orientation='vertical', size_hint_x=1, size_hint_y=None)
            label = MDLabel(text="Already booked? Import your reservation", halign='center', font_size='16sp')
            button = Button(text="Import", size_hint_y=None, height=dp(40), background_color=(0.8, 0, 0.5, 1))
            subBoxLayout2.add_widget(label)
            subBoxLayout2.add_widget(button)
            anchorLayout2.add_widget(subBoxLayout2)

            boxLayout.add_widget(anchorLayout1)
            boxLayout.add_widget(anchorLayout2)

            reservation_screen_content.add_widget(boxLayout)

        if tab_name == "reservation_past":
            reservation_screen = self.screen_manager.get_screen('reservation')
            reservation_screen_content = reservation_screen.ids.reservation_screen_content
            reservation_screen_content.clear_widgets()

            boxLayout = BoxLayout(orientation='vertical', adaptive_height=True)

            anchorLayout1 = AnchorLayout(anchor_x='center', anchor_y='center')
            subBoxLayout1 = BoxLayout(orientation='vertical', size_hint_x=1, size_hint_y=None)
            iconButton = MDIconButton(icon='calendar', pos_hint={"center_x": 0.5, "center_y":0.5})
            label = MDLabel(text="You have no past reservations!", halign='center', font_size='16sp')
            subBoxLayout1.add_widget(iconButton)
            subBoxLayout1.add_widget(label)
            anchorLayout1.add_widget(subBoxLayout1)

            anchorLayout2 = AnchorLayout(anchor_x='center', anchor_y='center')
            subBoxLayout2 = BoxLayout(orientation='vertical', size_hint_x=1, size_hint_y=None)
            label = MDLabel(text="Already booked? Import your reservation", halign='center', font_size='16sp')
            button = Button(text="Import", size_hint_y=None, height=dp(40), background_color=(0.8, 0, 0.5, 1))
            subBoxLayout2.add_widget(label)
            subBoxLayout2.add_widget(button)
            anchorLayout2.add_widget(subBoxLayout2)

            boxLayout.add_widget(anchorLayout1)
            boxLayout.add_widget(anchorLayout2)

            reservation_screen_content.add_widget(boxLayout)

############################################################################
# Main function
############################################################################


if __name__ == "__main__":
    MainScreen().run()
