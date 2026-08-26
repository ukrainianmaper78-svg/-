# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle, Ellipse, Line
from kivy.metrics import dp

# Устанавливаем размер окна только для ПК
if platform not in ('android', 'ios'):
    Window.size = (380, 680)

# Глубокий темный премиальный фон
Window.clearcolor = (0.07, 0.08, 0.11, 1)

class GlassCard(BoxLayout):
    """Карточка с эффектом полупрозрачного стекла и неоновой обводкой"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(24)
        self.spacing = dp(16)
        
        with self.canvas.before:
            Color(0.12, 0.14, 0.20, 0.7)
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(20)])
            
            Color(0.3, 0.4, 0.8, 0.3)
            self.border = Line(rounded_rectangle=(self.x, self.y, self.width, self.height, dp(20)), width=1.2)

        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
        self.border.rounded_rectangle = (self.x, self.y, self.width, self.height, dp(20))

class ModernInput(TextInput):
    """Стилизованное поле ввода с мягким закруглением"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_active = ''
        self.background_color = (0, 0, 0, 0)
        self.foreground_color = (0.9, 0.95, 1, 1)
        self.cursor_color = (0.4, 0.6, 1, 1)
        self.hint_text_color = (0.4, 0.45, 0.55, 1)
        self.padding = [dp(16), dp(14), dp(16), dp(14)]
        self.font_size = '16sp'
        
        with self.canvas.before:
            Color(0.08, 0.09, 0.13, 0.9)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(12)])
            Color(0.2, 0.25, 0.35, 0.5)
            self.line = Line(rounded_rectangle=(self.x, self.y, self.width, self.height, dp(12)), width=1)
            
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.line.rounded_rectangle = (self.x, self.y, self.width, self.height, dp(12))

class GlowingButton(Button):
    """Яркая неоновая кнопка"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (0, 0, 0, 0)
        self.color = (1, 1, 1, 1)
        self.font_size = '16sp'
        self.bold = True
        
        with self.canvas.before:
            Color(0.35, 0.45, 0.95, 1)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(12)])
            
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class FollowedApp(App):
    def build(self):
        root = FloatLayout()

        # Фоновые декоративные свечения
        with root.canvas.before:
            Color(0.2, 0.3, 0.8, 0.25)
            Ellipse(pos=(dp(-50), Window.height - dp(250)), size=(dp(300), dp(300)))
            Color(0.6, 0.2, 0.8, 0.15)
            Ellipse(pos=(Window.width - dp(200), dp(50)), size=(dp(300), dp(300)))

        # 1. Заголовок "followed"
        title_label = Label(
            text='followed',
            font_size='36sp',
            bold=True,
            color=(0.95, 0.97, 1, 1),
            size_hint=(1, None),
            height=dp(60),
            pos_hint={'center_x': 0.5, 'top': 0.88}
        )
        root.add_widget(title_label)

        # 2. Стеклянная карточка с формой
        glass_card = GlassCard(
            size_hint=(0.88, None),
            height=dp(230),
            pos_hint={'center_x': 0.5, 'center_y': 0.52}
        )

        self.key_input = ModernInput(
            hint_text='Введите ключ...',
            multiline=False,
            size_hint_y=None,
            height=dp(52)
        )
        glass_card.add_widget(self.key_input)

        self.submit_btn = GlowingButton(
            text='Проверить',
            size_hint_y=None,
            height=dp(52)
        )
        self.submit_btn.bind(on_press=self.check_key)
        glass_card.add_widget(self.submit_btn)

        # Метка статуса
        self.status_label = Label(
            text='',
            font_size='14sp',
            color=(1, 0.35, 0.45, 1),
            size_hint_y=None,
            height=dp(30),
            halign='center'
        )
        glass_card.add_widget(self.status_label)

        root.add_widget(glass_card)

        # 3. Нижний текст покупки
        buy_label = Label(
            text='купить ключ [color=5599FF]@huperr[/color] или [color=5599FF]@moreplayed[/color]',
            font_size='13sp',
            color=(0.5, 0.55, 0.65, 1),
            markup=True,
            size_hint=(1, None),
            height=dp(40),
            pos_hint={'center_x': 0.5, 'y': 0.05}
        )
        root.add_widget(buy_label)

        return root

    def check_key(self, instance):
        user_text = self.key_input.text.strip()
        if user_text:
            self.status_label.text = '⚠️ неправильный ключ'
        else:
            self.status_label.text = '⚠️ введите ключ'

if __name__ == '__main__':
    FollowedApp().run()