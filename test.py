import numpy as np
import scipy.special
from scipy.optimize import curve_fit
import matplotlib
import matplotlib.pyplot as plt

def voigt_profile_wofz(x, sigma, gamma, x_offset):
    z = ((x - x_offset) + 1j * gamma) / (sigma * np.sqrt(2))
    return np.real(scipy.special.wofz(z)) / (sigma * np.sqrt(2 * np.pi))

def voigt_profile(x, sigma, gamma, x_offset, magnitude):
    return magnitude * scipy.special.voigt_profile(x - x_offset, sigma, gamma)

def periodic_scan(t, lb, ub, freq, phase):
    amplitude = (ub - lb) / 2
    offset = (ub + lb) / 2
    return amplitude * np.sin(2 * np.pi * freq * t + phase) + offset

if __name__ == "__main__":
    lambdas_raw = np.genfromtxt("lambdas0.csv", delimiter=",")
    absorps_raw = np.genfromtxt("absorptions0.csv", delimiter=",")
    print(np.shape(lambdas_raw))
    print(np.shape(absorps_raw))
    stellen = np.where(np.isclose(absorps_raw, 1e-6, atol=1e-7))
    print(stellen)
    lambdas = lambdas_raw[2453:2892]
    absorps = absorps_raw[2453:2892]
    stelle = np.argmax(absorps)
    print("Index mit Max-Wert: ", lambdas[stelle])
    sine_max = np.where(np.isclose(absorps, 4e-7, atol=3e-8))
    print("Index Sine Max: ", sine_max)
    print("Wavelengths Sine Bounds: ", lambdas[sine_max])
    x_values = np.linspace(lambdas[0], lambdas[2792 - 2553-1], np.shape(lambdas)[0])
    sigma = .68
    gamma = .14
    z_values = 10**(-6) * voigt_profile_wofz(x_values, sigma, gamma, lambdas[stelle])
    y_values = 10**(-6) * voigt_profile(lambdas, sigma, gamma, lambdas[stelle], 1.0)
    seed = [0.03,0.03,1392.5,1e-6]
    popt, pcov = curve_fit(voigt_profile, lambdas, absorps, p0=seed)
    fitted_sigma, fitted_gamma, fitted_x_offset, fitted_magnitude = popt
    print("Fitted parameters:")
    print(f"Sigma: {fitted_sigma}")
    print(f"Gamma: {fitted_gamma}")
    print(f"X Offset: {fitted_x_offset}")
    print(f"Magnitude: {fitted_magnitude}")
    t = np.arange(0, 0.005, 1e-6)
    vals = periodic_scan(t, 1392.457, 1392.614, 500, np.pi/2)
    scanned_voigt = voigt_profile(vals, fitted_sigma, fitted_gamma, fitted_x_offset, fitted_magnitude)
    # plt.plot(x_values, z_values)
    # plt.plot(x_values, y_values)
    plt.plot(lambdas, absorps)
    plt.plot(lambdas, voigt_profile(lambdas, *popt), label="Fitted Voigt Profile")
    plt.legend()
    plt.grid(alpha=0.5)
    plt.xlabel("wavlength in nm")
    plt.ylabel("absorption")
    plt.title("Voigt Profile Fitting")
    plt.show()

    plt.plot(t, np.max(scanned_voigt) - scanned_voigt, label="absorption over time")
    plt.legend()
    plt.grid(alpha=0.5)
    plt.xlabel("time in s")
    plt.ylabel("absorption")
    plt.title("Input for Scan")
    plt.show()
