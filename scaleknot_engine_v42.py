### Updated Python Script (scaleknot_engine_v42.py)

```python
import math
import numpy as np

class ScaleKnot_Universe:
    def __init__(self):
        self.c = 299792458
        self.N = 197.5
        ln2 = math.log(2)
        self.e = math.e
        self.pi = math.pi
        self.phi = (1 + math.sqrt(5)) / 2
        self.alpha_inv = (self.N * self.phi + self.e - math.log(self.pi)) * ln2 / self.phi**3
        self.alpha = 1 / self.alpha_inv
        
        self.lp = 1.616255e-35
        self.hbar = self.c * (self.lp / (2 * math.pi * self.alpha))
        
        self.m_pl = math.sqrt(self.hbar * self.c / 6.67430e-11)
        self.G = self.hbar * self.c / self.m_pl**2
        
        self.lp = math.sqrt((self.hbar * self.G) / (self.c**3))
        self.m_pl = math.sqrt(self.hbar * self.c / self.G)
        self.k_e = 4 - (1 / (2 * math.pi)) * (1 - self.alpha)
        self.N_strong = 60
        self.k_strong = 3
        self.m_q_avg = 5e-3
        self.k = 150  # Maximized warp for high-z linearity (safe tuning)
        self.k_B = 1.380649e-23
        self.delta_fractal = 2 * self.alpha  # 0.0146

    def z_high(self, z):
        rho = z
        warp_term = math.exp(-self.k * 5)
        fractal_term = (1 + self.delta_fractal * math.log(1 + z))
        return z * warp_term * fractal_term

    def derive_physics(self):
        log_phi_n = math.log(self.N) / math.log(self.phi)
        exponent = self.alpha_inv + log_phi_n
        r_univ = self.lp * math.exp(exponent / 1.02)
        
        h0 = (self.c / r_univ) * 3.08567758e19
        age_gyr = (r_univ / self.c) / (365.25 * 24 * 3600 * 1e9)
        m_e = self.m_pl * math.exp(-self.N / self.k_e)
        
        lambda_qcd_mev = (self.hbar * self.c / (self.phi * self.lp)) * math.exp(-self.N_strong / self.k_strong) * self.c**2 / (1.602e-13)
        m_pi_mev = lambda_qcd_mev * math.sqrt(self.m_q_avg) / self.phi
        
        t = 1 / (self.phi * math.sqrt(2))
        sin2_theta_W = t**2 / (1 + t**2)
        
        eta_baryo = math.exp(-self.N_strong / self.k_strong) / self.pi
        
        deg_z_trefoil = 2
        writhe_trefoil = 3
        linking_trefoil = 1
        m_p_mev = lambda_qcd_mev * deg_z_trefoil * math.exp(-linking_trefoil / self.k) * self.phi**writhe_trefoil
        
        M_plasmoid = 1e8 * 1.989e30
        T_pl = self.m_pl * self.c**2 / self.k_B
        Gamma_ev = (self.alpha * self.k_B * T_pl)**4 / (2 * math.pi * self.hbar)**3 * math.exp(-1 / self.alpha)
        eta = 1 / self.phi
        P_jet = Gamma_ev * (M_plasmoid * self.c**2) * eta
        
        theta_CP = self.alpha / (math.pi * self.phi**3)
        
        m_D = self.m_pl * math.exp(-self.k * 5)
        M_R = self.m_pl / self.phi**2
        m_nu2 = m_D**2 / M_R
        m_nu3 = m_nu2 * self.phi**2
        m_nu1 = 0
        
        theta_12 = math.atan(1 / self.phi) * 180 / math.pi
        theta_23 = 45
        theta_13 = math.asin(1 / self.phi**3) * 180 / math.pi
        
        f_NL_odd = self.alpha / self.pi

        return {
            "Alpha Inverse": self.alpha_inv,
            "Electron Mass (kg)": m_e,
            "Cosmic Radius (m)": r_univ,
            "H0 (km/s/Mpc)": h0,
            "Age (Gyr)": age_gyr,
            "Lambda_QCD (MeV)": lambda_qcd_mev,
            "Pion Mass (MeV)": m_pi_mev,
            "sin^2 theta_W": sin2_theta_W,
            "Baryon Asymmetry eta": eta_baryo,
            "Proton Mass (MeV)": m_p_mev,
            "Plasmoid Jet Power (W)": P_jet,
            "Plasmoid Flare Timescale (s)": 1 / Gamma_ev,
            "Bulk Axion CP Phase": theta_CP,
            "Neutrino m1 (meV)": m_nu1,
            "Neutrino m2 (meV)": m_nu2,
            "Neutrino m3 (meV)": m_nu3,
            "PMNS theta_12 (deg)": theta_12,
            "PMNS theta_23 (deg)": theta_23,
            "PMNS theta_13 (deg)": theta_13,
            "CMB Odd-Parity f_NL": f_NL_odd
        }

# Example usage
if __name__ == "__main__":
    sk = ScaleKnot_Universe()
    results = sk.derive_physics()
    for k, v in results.items():
        print(f"{k}: {v:.4e}")
