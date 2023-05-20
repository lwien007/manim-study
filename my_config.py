from manim import *
c_black = "#343434"
c_blue = '#3174f0'
c_red  = '#e53125'
c_gold = '#fbb003'
c_green = '#269a43'
c_white = '#ece6e2'
Text.set_default(color=c_black,font="sans-serif",font_size=35)
MathTex.set_default(color=c_black,font_size=35)
DecimalNumber.set_default(color=c_black,font_size=35)
Integer.set_default(color=c_black,font_size=35)
Brace.set_default(color=c_black)
MarkupText.set_default(color=c_black,font_size=35)
Tex.set_default(color=c_black,font_size=35)


def foot(c='假设检验的基本思想'):
    bottom_rectangle = Rectangle(width=15,height=0.4,fill_color=GOLD_B,fill_opacity=1,stroke_width=0).to_edge(DOWN,buff=0)
    footnote3 = Text('流行病与卫生统计学教研室',font_size=20).to_edge(DR,buff=0.07)
    footnote2 = Text('公共卫生学院',font_size=20).next_to(footnote3,LEFT,buff=1)
    footnote1 = Text('佳木斯大学',font_size=20).next_to(footnote2,LEFT,buff=1)
    footnote4 = Text(c,font_size=20,color=BLUE_E).to_edge(LEFT*0.2+DOWN*0.15)
    footnote = VGroup(bottom_rectangle,footnote1,footnote2,footnote3,footnote4)
    return footnote
