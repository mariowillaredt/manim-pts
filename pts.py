from manim import *

class PhotothermalSpectroscopy(Scene):
    def construct(self):
        # Title
        title = Text("Photothermal Spectroscopy").scale(1.2).to_edge(UP)
        self.play(FadeIn(title))

        # Absorption Profile (Voigt)
        absorption_axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1, 0.2],
            axis_config={"color": BLUE},
            tips=False
        ).scale(0.7).to_edge(UP + LEFT)
        voigt_profile = absorption_axes.plot(
            lambda x: 0.7 * np.exp(-((x - 5) ** 2) / 2) + 0.3 * np.exp(-((x - 5) ** 2) / 1),
            color=YELLOW
        )
        absorption_label = Text("Absorption (Voigt Profile)").next_to(absorption_axes, DOWN)

        # Refractive Index Change
        refractive_index_axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-1, 1, 0.5],
            axis_config={"color": GREEN},
            tips=False
        ).scale(0.7).next_to(absorption_axes, RIGHT, buff=1.5)
        refractive_index_graph = refractive_index_axes.plot(lambda x: 0.5 * np.sin(x), color=PURPLE)
        refractive_index_label = Text("Change in Refractive Index").next_to(refractive_index_axes, DOWN)

        # Resonance Curve Displacement
        resonance_axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 1, 0.2],
            axis_config={"color": RED},
            tips=False
        ).scale(0.7).next_to(refractive_index_axes, RIGHT, buff=1.5)
        resonance_curve_initial = resonance_axes.plot(lambda x: np.exp(-((x - 1) ** 2)), color=BLUE)
        resonance_curve_shifted = resonance_axes.plot(lambda x: np.exp(-((x + 1) ** 2)), color=ORANGE)
        resonance_label = Text("Resonance Curve Displacement").next_to(resonance_axes, DOWN)

        # Reflected Intensity
        reflected_intensity_axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1, 0.2],
            axis_config={"color": PURPLE},
            tips=False
        ).scale(0.7).next_to(resonance_axes, DOWN, buff=1.5)
        reflected_intensity_graph = reflected_intensity_axes.plot(lambda x: 0.5 * (np.sin(x) + 1), color=PINK)
        reflected_intensity_label = Text("Reflected Intensity").next_to(reflected_intensity_axes, DOWN)

        # Photothermal Signal
        signal_axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-1, 1, 0.5],
            axis_config={"color": PINK},
            tips=False
        ).scale(0.7).next_to(reflected_intensity_axes, RIGHT, buff=1.5)
        signal_graph = signal_axes.plot(lambda x: 0.5 * np.sin(x), color=PURPLE)
        signal_label = Text("Photothermal Signal").next_to(signal_axes, DOWN)

        # Show Components
        self.play(FadeIn(absorption_axes), FadeIn(voigt_profile), FadeIn(absorption_label))
        self.play(FadeIn(refractive_index_axes), FadeIn(refractive_index_graph), FadeIn(refractive_index_label))
        self.play(FadeIn(resonance_axes), FadeIn(resonance_curve_initial), FadeIn(resonance_label))
        self.play(FadeIn(reflected_intensity_axes), FadeIn(reflected_intensity_graph), FadeIn(reflected_intensity_label))
        self.play(FadeIn(signal_axes), FadeIn(signal_graph), FadeIn(signal_label))

        self.wait(1)

        # Animate Processes
        absorption_anim = voigt_profile.animate(rate_func=linear, run_time=8).shift(LEFT * 2).shift(RIGHT * 2).repeat(2)
        refractive_index_anim = refractive_index_graph.animate(rate_func=linear, run_time=8).shift(UP * 0.2).shift(DOWN * 0.2).repeat(2)
        resonance_anim = Transform(resonance_curve_initial, resonance_curve_shifted, run_time=8, rate_func=there_and_back).repeat(2)
        reflected_intensity_anim = reflected_intensity_graph.animate(rate_func=linear, run_time=8).shift(UP * 0.2).shift(DOWN * 0.2).repeat(2)
        signal_anim = signal_graph.animate(rate_func=linear, run_time=8).shift(UP * 0.2).shift(DOWN * 0.2).repeat(2)

        self.play(absorption_anim, refractive_index_anim, resonance_anim, reflected_intensity_anim, signal_anim)

        self.wait(2)

        # End of animation
        self.play(
            FadeOut(absorption_axes), FadeOut(voigt_profile), FadeOut(absorption_label),
            FadeOut(refractive_index_axes), FadeOut(refractive_index_graph), FadeOut(refractive_index_label),
            FadeOut(resonance_axes), FadeOut(resonance_curve_initial), FadeOut(resonance_curve_shifted), FadeOut(resonance_label),
            FadeOut(reflected_intensity_axes), FadeOut(reflected_intensity_graph), FadeOut(reflected_intensity_label),
            FadeOut(signal_axes), FadeOut(signal_graph), FadeOut(signal_label),
            FadeOut(title)
        )
        self.wait(1)

