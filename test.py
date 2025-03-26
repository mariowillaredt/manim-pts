import numpy as np
import scipy.special
import matplotlib
import matplotlib.pyplot as plt

def voigt_profile(x, sigma, gamma):
    z = (x + 1j * gamma) / (sigma * np.sqrt(2))
    return np.real(scipy.special.wofz(z)) / (sigma * np.sqrt(2 * np.pi))

if __name__ == "__main__":
    lambdas = np.genfromtxt("lambdas0.csv", delimiter=",")
    absorps = np.genfromtxt("absorptions0.csv", delimiter=",")
    print(np.shape(lambdas))
    print(np.shape(absorps))
    stellen = np.where(np.isclose(absorps, 1e-6, atol=1e-7))
    print(stellen)
    lambdas = lambdas[2553:2792]
    absorps = absorps[2553:2792]
    stelle = np.argmax(absorps)
    x_values = np.linspace(lambdas[0], lambdas[2792 - 2553-1], np.shape(lambdas)[0])
    sigma = .68
    gamma = .14
    y_values = 10**(-6) * scipy.special.voigt_profile(x_values - lambdas[stelle], sigma, gamma)
    plt.plot(x_values, y_values)
    plt.plot(lambdas, absorps)
    plt.grid(alpha=0.5)
    plt.xlabel("wavlength in nm")
    plt.ylabel("absorption")
    plt.show()
    print(matplotlib.matplotlib_fname())
