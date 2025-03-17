
from manim import *

class PTSPrinciple(Scene):
    def construct(self):
        # Title
        title = Text("Photothermal Spectroscopy: Gas Sensing Principle", font_size=36)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Gas chamber (simplified as a rectangle)
        chamber = Rectangle(width=6, height=2, color=BLUE, fill_opacity=0.2)
        chamber_label = Text("Gas Sample (Acetylene)", font_size=24).next_to(chamber, DOWN)
        self.play(Create(chamber), Write(chamber_label))
        
        # Pump laser (red arrow from left)
        pump = Arrow(start=LEFT * 4, end=RIGHT * 2, color=RED, buff=0)
        pump_label = Text("Pump Laser (1532 nm)", font_size=24, color=RED).next_to(pump, UP)
        self.play(GrowArrow(pump), Write(pump_label))
        
        # Gas molecules (dots) excited by pump
        molecules = VGroup(*[Dot(radius=0.1, color=WHITE) for _ in range(10)])
        molecules.arrange_in_grid(2, 5, buff=0.5).move_to(chamber.get_center())
        self.play(FadeIn(molecules))
        self.play(molecules.animate.set_color(YELLOW), run_time=1)  # Excitation
        
        # Heat wave (expanding circles)
        heat_waves = VGroup(*[Circle(radius=r, color=ORANGE, fill_opacity=0.2).move_to(chamber.get_center()) 
                              for r in [0.5, 1, 1.5]])
        heat_label = Text("Heat (Thermal Wave)", font_size=24, color=ORANGE).next_to(chamber, UP, buff=0.5)
        self.play(LaggedStart(*[Create(wave) for wave in heat_waves], lag_ratio=0.3), Write(heat_label))
        self.play(FadeOut(heat_waves))
        
        # Refractive index change (gradient effect)
        ri_label = Text("Refractive Index Change", font_size=24).move_to(chamber_label.get_center() + DOWN * 1)
        self.play(Transform(chamber_label, ri_label), chamber.animate.set_fill(GREEN, opacity=0.4))
        
        # Probe laser (green arrow from left)
        probe = Arrow(start=LEFT * 4, end=RIGHT * 4, color=GREEN, buff=0).shift(DOWN * 0.5)
        probe_label = Text("Probe Laser (1550 nm)", font_size=24, color=GREEN).next_to(probe, DOWN)
        self.play(GrowArrow(probe), Write(probe_label))
        
        # Wavefront distortion (sine wave bending)
        straight_wave = FunctionGraph(lambda x: 0.5 * np.sin(2 * x), x_range=[-4, 4], color=GREEN).shift(DOWN * 0.5)
        bent_wave = FunctionGraph(lambda x: 0.5 * np.sin(2 * x + 0.5 * np.exp(-x**2)), x_range=[-4, 4], color=GREEN).shift(DOWN * 0.5)
        self.play(Create(straight_wave))
        self.play(Transform(straight_wave, bent_wave), run_time=1)  # Phase shift
        
        # Interferometer (simplified as a box)
        interferometer = Rectangle(width=2, height=1, color=GREY).shift(RIGHT * 4)
        int_label = Text("Interferometer", font_size=24).next_to(interferometer, UP)
        self.play(Create(interferometer), Write(int_label))
        
        # Signal output (oscillating line)
        signal = FunctionGraph(lambda x: 0.3 * np.sin(5 * x), x_range=[0, 2], color=YELLOW).next_to(interferometer, RIGHT)
        signal_label = Text("Detected Signal", font_size=24).next_to(signal, UP)
        self.play(Create(signal), Write(signal_label))
        
        # Fade out everything except title
        self.play(*[FadeOut(obj) for obj in self.mobjects if obj != title])
        self.wait(1)

# Run with: manim -pql pts_animation.py PTSPrinciple