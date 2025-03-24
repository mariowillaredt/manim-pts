import numpy as np
import scipy.special
import matplotlib
import matplotlib.pyplot as plt

def voigt_profile(x, sigma, gamma):
    z = (x + 1j * gamma) / (sigma * np.sqrt(2))
    return np.real(scipy.special.wofz(z)) / (sigma * np.sqrt(2 * np.pi))

if __name__ == "__main__":
    x_values = np.linspace(1392.5 - 5,1392.5 + 5, 1000)
    sigma = .68
    gamma = .14
    y_values = scipy.special.voigt_profile(x_values - 1392.5, sigma, gamma)
    plt.plot(x_values, y_values)
    plt.grid(alpha=0.5)
    plt.xlabel("wavlength in nm")
    plt.ylabel("absorption")
    plt.show()
    print(matplotlib.matplotlib_fname())
