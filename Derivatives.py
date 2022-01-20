from manim import *

class Intro(Scene):
    def construct(self):
        title = Text("Limit Definition of the Derivative")
        title.to_corner(UP + LEFT)
        self.play(Write(title)) #Creates the title
        derivativeLimit = MathTex("\\lim_{h\\to 0}\\frac{f(x+h)-f(x)}{h}")
        derivativeNotation = MathTex("\\frac{d}{dx}")
        self.play(Write(derivativeLimit))
        self.play(Write(derivativeNotation.next_to(derivativeLimit, DOWN * 3)))
        self.wait()
        box1 = SurroundingRectangle(derivativeLimit, buff=0.1)
        self.play(Create(box1), FadeOut(derivativeNotation, title))
        self.wait()
        self.play(FadeOut(box1, derivativeLimit))

class Limits(Scene):
    def construct(self):
        axes = Axes(x_range=[-1, 10], y_range=[-1, 10], tips=False, axis_config={"include_numbers": False})
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        parabolaGraph = axes.plot(lambda x: x**2, color=GREEN)
        group1 = VGroup(axes, labels, parabolaGraph)
        self.play(FadeIn(group1))
        self.wait()
        
        # Dot portion
        dot1 = Dot(color=RED).move_to(axes.c2p(2, 4))
        dot2 = Dot(color=RED).move_to(axes.c2p(3, 9))
        self.play(FadeIn(dot1))
        self.play(FadeIn(dot2))
        
        # Dotted line portion
        horizontalLine1 = axes.get_horizontal_line(dot1.get_left(), color=YELLOW)
        verticalLine1 = axes.get_vertical_line(dot1.get_bottom(), color=YELLOW)
        horizontalLine2 = axes.get_horizontal_line(dot2.get_left(), color=YELLOW)
        verticalLine2 = axes.get_vertical_line(dot2.get_bottom(), color=YELLOW)
        dottedLinesGroup1 = VGroup(horizontalLine1, verticalLine1)
        dottedLinesGroup2 = VGroup(horizontalLine2, verticalLine2)
        # Secant line portion
        secantSlope = axes.get_secant_slope_group(x=2.0, graph=parabolaGraph, dx=1.0, dx_line_color=ORANGE, dy_line_color=ORANGE, secant_line_length=5, secant_line_color=BLUE)
        self.play(FadeIn(secantSlope))
        self.wait()
        self.play(FadeIn(dottedLinesGroup1))
        self.play(FadeIn(dottedLinesGroup2))
        self.wait() # add new slope formula, fade out lines, move dots to zero, apply limit to slope formula, change to dy/dx
        
        # Brace and dot labels section
        bottomLine = Line(axes.c2p(2, 0), axes.c2p(3, 0))
        bottomBrace = Brace(bottomLine, direction=bottomLine.copy().rotate(PI / 2).get_unit_vector())
        bottomBraceText = bottomBrace.get_tex("h")
        self.add(bottomBrace, bottomBraceText)
        xText = Tex("x").move_to(axes.c2p(2, -1))
        xhText = Tex("x+h").move_to(axes.c2p(3, -0.9))
        fxText = Tex("f(x)").move_to(axes.c2p(-1, 4))
        fxhText = Tex("f(x+h)").move_to(axes.c2p(-1, 9))
        self.add(xText, xhText, fxText, fxhText)
        #self.play(FadeOut(dottedLinesGroup1, dottedLinesGroup2))
        self.wait()
        
        
class ConstantFunctionScene(Scene):
    def construct(self):
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        ax.add_coordinates()
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")
        constantFunction = ax.plot(lambda x: x, color=BLUE)
        constantFunctionGroup = VGroup(labels, constantFunction, ax)
        self.play(FadeIn(constantFunctionGroup))
        dot1 = Dot(color=RED).move_to(ax.c2p(2, 2))
        dot2 = Dot(color=RED).move_to(ax.c2p(4, 4))
        
        # Fades in the dots for the first time
        self.play(FadeIn(dot1))
        self.play(FadeIn(dot2))
        self.wait()
        
        # Fades out the dots so they can be moved and then re-faded in
        self.play(FadeOut(dot1, dot2))
        self.wait()
        
        # Dot fade in again
        dot1.move_to(ax.c2p(3, 3))
        dot2.move_to(ax.c2p(5, 5))
        self.play(FadeIn(dot1, dot2))
        self.wait()
        
        # Dots are faded out to be moved again
        self.play(FadeOut(dot1, dot2))
        self.wait()
        
        # Dots move and are re-faded back in
        dot1.move_to(ax.c2p(2, 2))
        dot2.move_to(ax.c2p(4, 4))
        slopeLine = ax.plot(lambda x: x, color=GREEN)
        self.play(FadeIn(slopeLine, dot1, dot2))
        self.wait()
        
        # Fades out the slope line
        self.play(FadeOut(slopeLine))
        self.wait()
        
        # Shows coords and then begins formula sequence
        coordinate1 = MathTex("(2 , 2)").next_to(dot1, UP)
        coordinate2 = MathTex("(4 , 4)").next_to(dot2, UP)
        self.play(FadeIn(coordinate1))
        self.play(FadeIn(coordinate2))
        self.wait()
        
        # Creates dy/dx line
        xLine = Line(dot1.get_right(), ax.c2p(4, 2)).set_color(ORANGE)
        yLine = Line(dot2.get_bottom(), xLine.get_right()).set_color(ORANGE)
        lineGroup1 = VGroup(xLine, yLine)
        self.play(FadeIn(lineGroup1))
        self.wait()
        
        # Animations of the math formula sequence
        slopeFormula = MathTex("m = \\frac{y_2-y_1}{x_2-x_1}").next_to(ax.c2p(4, 2), RIGHT * 3)
        self.play(FadeIn(slopeFormula))
        self.wait()
        slopeFormulaWithNumbers = MathTex("m = \\frac{4 - 2}{4 - 2}").next_to(ax.c2p(4, 2), RIGHT * 3)
        slopeFormulaCompleted = MathTex("m = 1").next_to(ax.c2p(4, 2), RIGHT * 3)
        self.play(ReplacementTransform(slopeFormula, slopeFormulaWithNumbers))
        self.wait()
        self.play(ReplacementTransform(slopeFormulaWithNumbers, slopeFormulaCompleted))
        self.wait()
        endGroup = VGroup(slopeFormulaCompleted, lineGroup1, coordinate1, coordinate2, dot1, dot2, constantFunctionGroup)
        self.play(FadeOut(endGroup))
        self.wait()
        
        # Create linear function, get a point, draw 2 dotted lines, add another point and add their dotted lines
        # Then add +x to the x difference and +h to the y difference, take the slope function and convert the y to f(x) and the change in y to f(x+h)
        # Simplify and cancel out the terms to get the difference quotient, once there introduce the limit and drag the top point down as the difference between the points approaches zero
        # With that take the difference quotient, add the limit portion and call it the limit definition of the derivative, then introduce the other ways to write the derivative