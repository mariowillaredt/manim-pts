from manim import *
import numpy as np
import scipy.special
import matplotlib.pyplot as plt

class VoigtProfile(Scene):
    def voigt_profile(self, x, sigma, gamma):
        z = (x + 1j * gamma) / (sigma * np.sqrt(2))
        return np.real(scipy.special.wofz(z)) / (sigma * np.sqrt(2 * np.pi))

    def construct(self):
        x_min = 0
        x_max = 10
        sigma = 0.1
        gamma = 0.1
        voigt_func = FunctionGraph(
        lambda x: self.voigt_profile(x, sigma, gamma), x_range=np.array([-1,1]), color=RED,)
        # lambda x: x, color=GREEN,
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
        #self.add(axes, labels)

        #self.play(AnimationGroup(Create(axes, lag_ratio=0.1), Create(voigt_func, lag_ratio=0.1)), run_time=3.0)
        self.play(Create(voigt_func, lag_ratio=0.1), run_time=3.0)
        d1 = Dot().set_color(RED)
        self.play(MoveAlongPath(d1, voigt_func), rate_func=linear)
        self.wait(3)

if __name__ == "__main__":
    '''
    from manim import *
    config.media_width = "100%"
    scene = VoigtProfile()
    scene.render()
    '''
    x_values = np.linspace(-5, 5, 1000)
    sigma = .68
    gamma = .34
    y_values = scipy.special.voigt_profile(x_values, sigma, gamma)
    plt.plot(x_values, y_values)
    plt.show()
