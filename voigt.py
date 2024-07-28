from manim import *
import numpy as np
import scipy.special

class VoigtProfile(Scene):
    def voigt_profile(self, x, sigma, gamma):
        z = (x + 1j * gamma) / (sigma * np.sqrt(2))
        return np.real(scipy.special.wofz(z)) / (sigma * np.sqrt(2 * np.pi))

    def construct(self):
        x_min = 0
        x_max = 10
        sigma = 1
        gamma = 4

        x_values = np.linspace(x_min, x_max, 300)
        y_values = self.voigt_profile(x_values-5, sigma, gamma)

        axes = Axes(
            x_range=[x_min, x_max, 1],
            y_range=[0, max(y_values) * 1.1, 0.1],
            axis_config={"color": WHITE},
        )
        labels = axes.get_axis_labels(Tex("wavelength $\lambda$"), Text("absorption").scale(0.5))

        voigt_graph = axes.plot_line_graph(
            x_values, y_values, line_color=RED, add_vertex_dots=False
        )
        self.add(axes, labels)

        self.play(AnimationGroup(Create(axes, lag_ratio=0.1), Create(voigt_graph, lag_ratio=0.1)), run_time=3.0)
        self.wait(2)

if __name__ == "__main__":
    from manim import *
    config.media_width = "100%"
    scene = VoigtProfile()
    scene.render()

