import numpy as np
import pandas as pd

def Calculo_de_Gravidade(Massa_corpo,
                         raio_corpo,
                         periodo_rotacional,
                         precisao_angulo):
  G = 6.6743e-11                                            # Constante Gravitacional (m³/(kg*s²))
  g = (G * Massa_corpo) / (raio_corpo**2)                   # Massa em kg
  T = periodo_rotacional * 60 * 60                          # Período (s)
  V = 2 * np.pi * d_terra/ T                                # Velocidade de Translação sem Coneso
  angulos = np.arange(0, 90, precisao_angulo) * np.pi / 180 # Lista de ângulos
  a = (V * np.cos(angulos)) ** 2 / d_terra                  # Aceleração Centrípeta
  gravidade_corrigida = g - a                               # Correção da Gravidade pela rotação do corpo
  df = pd.DataFrame({'Latitudes (rad)': angulos,            # DataFrame
                                  'Latitudes (°)': angulos * 180 / np.pi,
                                  'Aceleracao Centripeta (m/s²)': a,
                                  'Gravidade (m/s²)': gravidade_corrigida})
  return df
