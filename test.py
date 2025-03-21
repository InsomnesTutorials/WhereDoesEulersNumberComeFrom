from manim import * 

class Test(Scene):
    def construct(self):
        svg = SVGMobject("images/dollar.svg")
        svg.set_color(WHITE)
        svg.scale(2)
        svg.move_to(ORIGIN)

        # Get center x position and filter only left-side elements
        center_x = svg.get_center()[0]
        left_half = VGroup(*[sm for sm in svg.submobjects if sm.get_center()[0] < center_x])

        # Show original SVG briefly
        self.play(FadeIn(svg))
        self.wait(1)

        # Replace with only left half
        self.play(ReplacementTransform(svg, left_half))
        self.wait(2)