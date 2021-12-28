from manim import *

class Limits(Scene):
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
        
        axes = Axes(x_range=[-1, 10], y_range=[-1, 10], tips=False)
        axes.add_coordinates()
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        def LinearFunc(x):
            return x**2
        linearGraph = axes.plot(LinearFunc, color=GREEN)
        group1 = VGroup(axes, labels, linearGraph)
        self.play(FadeIn(group1))
        self.wait()
        
        # Dot portion
        dot1 = Dot(color=RED).move_to(axes.c2p(2, 4))
        dot2 = Dot(color=RED).move_to(axes.c2p(3, 9))
        self.play(FadeIn(dot1))
        self.play(FadeIn(dot2))
        # Dotted line portion
        horizontalLine1 = axes.get_horizontal_line(dot1.get_left(), color=BLUE)
        verticalLine1 = axes.get_vertical_line(dot1.get_bottom(), color=BLUE)
        horizontalLine2 = axes.get_horizontal_line(dot2.get_left(), color=BLUE)
        verticalLine2 = axes.get_vertical_line(dot2.get_bottom(), color=BLUE)
        dottedLinesGroup1 = VGroup(horizontalLine1, verticalLine1)
        dottedLinesGroup2 = VGroup(horizontalLine2, verticalLine2)
        self.play(FadeIn(dottedLinesGroup1))
        self.play(FadeIn(dottedLinesGroup2))
        self.wait()
        dXLine = Line(dot1.get_right(), axes.c2p(3, 4)).set_color(ORANGE)
        dYLine = Line(dot2, dXLine.get_right()).set_color(ORANGE)
        dXBrace = Brace(dXLine, direction=dXLine.copy().rotate((PI / 2) * -1).get_unit_vector())
        xBraceText = dXBrace.get_tex("dx")
        dYBrace = Brace(dYLine, direction=dYLine.copy().rotate(PI / 2).get_unit_vector())
        yBraceText = dYBrace.get_tex("dy")
        self.add(dXLine, dYLine)
        self.play(FadeOut(dottedLinesGroup1, dottedLinesGroup2))
        dBraceGroup = VGroup(dXBrace, xBraceText, dYBrace, yBraceText)
        self.play(FadeIn(dBraceGroup))
        self.wait()

class TestyMode(Scene):
    def construct(self):
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line)
        b1Text = b1.get_text("Horizontal")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2Text = b2.get_tex("x=x_1")
        self.add(line, dot, dot2, b1, b2, b1Text, b2Text) # Use brace and line to make a brace and line update to show tan line
        line2 = Line(b1.get_right(), dot2).set_color(YELLOW) # line made from 
        b3 = Brace(line2, direction=line2.copy().rotate((PI / 2) * -1).get_unit_vector()) # Adding the brace from the line and *-1 to mirror it
        self.add(line2, b3)
        
        # Create linear function, get a point, draw 2 dotted lines, add another point and add their dotted lines
        # Then add +x to the x difference and +h to the y difference, take the slope function and convert the y to f(x) and the change in y to f(x+h)
        # Simplify and cancel out the terms to get the difference quotient, once there introduce the limit and drag the top point down as the difference between the points approaches zero
        # With that take the difference quotient, add the limit portion and call it the limit definition of the derivative, then introduce the other ways to write the derivative