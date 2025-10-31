from manim import *
from utils import styles

class Intro(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/bk_name_en.png")
        self.add(logo)