camclick = '''
ScreenManager:
    MenuScreen:
    LogedinScreen:
    CameraClickScreen:

<CameraClickScreen>:
    name: 'CameraClick'
    orientation: 'vertical'

    Camera:
        id: camera
        resolution: (640, 480)
        play: True

    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'

    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()

<MenuScreen>:
    name: 'menu'

    MDIcon: 
        icon: 'bg_edit.png'

    MDTextField:
        hint_text: "Enter username"
        helper_text: "or click on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "account"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.55}
        size_hint_x:None
        size_hint_y:None
        width:500
        height: 200
        font_size: 50

    MDTextField:
        password: True
        hint_text: "Enter password"
        helper_text: "or click on forgot password"
        helper_text_mode: "on_focus"
        icon_right: "textbox-password"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.35}
        size_hint_x:None
        size_hint_y:None
        width:500
        height: 200
        font_size: 50

    MDRaisedButton:
        text: 'Login'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'logedin'

<LogedinScreen>:
    name: 'logedin'

    MDIcon: 
        icon: 'bg.jpg'

    MDLabel:
        text: 'Welcome to Steag App @Vipin'
        font_style: "H3"
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.9}

    MDLabel:
        text: 'You can reach to asset SOP/SMP or other OEM manuals by entering asset no or by scaning the Qr-code.'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.75}
        size_hint_y: None
        size_hint_x: None
        width:500
        height:self.height

    MDTextField:
        hint_text: "Enter equipment no"
        helper_text: "or scan the Qr-Code"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        size_hint_y:None
        width:500
        height: 200
        font_size: 50

    MDLabel:
        text: 'or scan Qr-Code'
        font_style: "H6"
        halign: 'center'
        valign: 'center'

    MDFloatingActionButton:
        icon: "camera"
        pos_hint: {'center_x':0.5,'center_y':0.35}
        md_bg_color: app.theme_cls.primary_color
        elevation_normal: 

        on_press: root.manager.current = 'CameraClick'


    MDRaisedButton:
        text: 'Logout'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
'''