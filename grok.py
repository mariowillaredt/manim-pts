from manim import *

class PhotothermalSpectroscopyPrinciple(Scene):
    def construct(self):
        # Step 1: Display the title
        title = Text("Photothermal Spectroscopy Measurement Principle").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Step 2: Create the sample
        sample = Rectangle(width=2, height=4, fill_opacity=0.2, color=WHITE)
        self.play(Create(sample))
        self.wait(1)

        # Step 3: Introduce the heating laser beam
        heating_start = LEFT * 5 + UP * 1
        heating_end = RIGHT * 5 + UP * 1
        heating_beam = Arrow(heating_start, heating_end, color=RED)
        heating_spot = Dot(color=RED).move_to(sample.get_center())
        heating_label = Text("Heating laser beam").next_to(heating_beam, UP)
        self.play(Create(heating_beam), FadeIn(heating_spot), Write(heating_label))
        self.wait(1)

        # Step 4: Show the sample absorbing light and heating up
        absorption_label = Text("Sample absorbs light and heats up").next_to(sample, DOWN, buff=0.5)
        self.play(
            sample.animate.set_fill(RED, opacity=0.5),
            Write(absorption_label),
            run_time=2
        )
        self.wait(1)

        # Step 5: Introduce the probe laser beam before the sample
        probe_start = LEFT * 5 + DOWN * 1
        probe_end_before = sample.get_left() + DOWN * 1
        probe_beam_before = Arrow(probe_start, probe_end_before, color=BLUE)
        probe_label = Text("Probe laser beam").next_to(probe_beam_before, DOWN)
        self.play(Create(probe_beam_before), Write(probe_label))
        self.wait(1)

        # Step 6: Show the probe beam diverging due to the thermal lens effect
        sample_right = sample.get_right() + DOWN * 1
        diverging_points = [
            sample_right + RIGHT * 2 + UP * 0.5,
            sample_right + RIGHT * 2,
            sample_right + RIGHT * 2 + DOWN * 0.5
        ]
        diverging_beams = VGroup(
            *[Arrow(sample_right, point, color=BLUE) for point in diverging_points]
        )
        lens_effect_label = Text("Thermal lens effect causes probe beam to diverge").next_to(diverging_beams, RIGHT)
        self.play(Create(diverging_beams), Write(lens_effect_label))
        self.wait(2)

        # Step 7: Add a detector to measure the change
        detector = Circle(radius=0.5, color=YELLOW).move_to(RIGHT * 4 + DOWN * 1)
        detector_label = Text("Detector measures the change").next_to(detector, DOWN)
        self.play(Create(detector), Write(detector_label))
        self.wait(1)

        # Step 8: Display the conclusion
        conclusion = Text("The change in the probe beam is used to infer the sample's absorption").to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(3)

