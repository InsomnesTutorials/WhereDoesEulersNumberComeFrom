from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class Test(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dollars = {f"dollar_{i}" : ImageMobject(f"images/dollar_{i}.png").scale(0.2)
                        for i in [33, 44, 50, 58, 75]
                       }
        self.dollars["dollar"] = ImageMobject("images/dollar.png").scale(0.2)

        self.expressions = Group(Group(self.dollars["dollar"].copy(), Text("+"), self.dollars["dollar"].copy(), Text("="), Text("2")).arrange(RIGHT),
                                 Group(self.dollars["dollar"].copy(), Text("+"), self.dollars["dollar_50"].copy(), Text("+"), self.dollars["dollar_75"].copy(), Text("="), Text("2.25")).arrange(RIGHT),
                                 Group(self.dollars["dollar"].copy(), Text("+"), self.dollars["dollar_33"].copy(), Text("+"), self.dollars["dollar_44"].copy(), Text("+"), self.dollars["dollar_58"].copy(), Text("="), Text("2.37")).arrange(RIGHT)
                                ).arrange(DOWN, aligned_edge= LEFT, buff= 1.3)

        self.math_expressions = Group(*[MathTex(i).move_to(j, coor_mask= [0,1,0]).shift(RIGHT * 8)
                                        for i,j in zip([r"1\left( 1 + \frac{1}{1} \right)^1 = 2",
                                                        r"1\left( 1 + \frac{1}{2} \right)^2 = 2.25",
                                                        r"1\left( 1 + \frac{1}{3} \right)^3 = 2.37"
                                                       ],
                                                       self.expressions
                                                      )
                                       ]
                                     )

        self.e = {"p" : MathTex("P", "=", "principle", "=", "1").shift(UP * 2),
                  "compound" : MathTex(r"Compound\\infinitey\\(x\to \infty)").shift(UP * 2),
                  "p_formula" : VGroup(MathTex("P"), MathTex(r"\left(1+\frac{1}{x}\right)")).arrange(),
                  "limit_formula" : VGroup(MathTex(r"\lim_{x \to \infty}"), MathTex(r"\left(1+\frac{1}{x}\right)")).arrange(),
                  "e" : MathTex("e")
                 }

    def construct(self):
        # Expression 1
        self.play(FadeIn(self.expressions[0]))
        self.wait()

        # Expression 2
        self.play(FadeIn(self.expressions[1][0]))
        self.wait()
        self.play(FadeIn(self.expressions[1][1:3]))
        self.wait()
        self.play(Indicate(self.expressions[1][:3]))
        self.wait()
        self.play(FadeIn(self.expressions[1][3:]))
        self.wait()

        # Expression 3
        self.play(FadeIn(self.expressions[2]))
        self.wait()

        # Math Expressions
        self.add(self.math_expressions)

        self.play(self.expressions.animate.shift(LEFT * 10),
                  self.math_expressions.animate.move_to(ORIGIN)
                 )
        self.wait()
        self.play(FadeOut(self.math_expressions))

        # Main Formula
        self.play(Write(self.e["p_formula"]))
        self.wait()
        self.play(Write(self.e["p"][:3]))
        self.wait()
        self.play(Write(self.e["p"][3:]))
        self.wait()
        self.play(ReplacementTransform(self.e["p"], self.e["compound"]))
        self.wait()
        self.play(ReplacementTransform(self.e["p_formula"][0], self.e["limit_formula"][0]),
                  self.e["p_formula"][1].animate.move_to(self.e["limit_formula"][1])
                 )
        self.wait()
        self.play(ReplacementTransform(VGroup(self.e["limit_formula"][0], self.e["p_formula"][1]), self.e["e"]),
                  FadeOut(self.e["compound"])
                 )
        self.wait()