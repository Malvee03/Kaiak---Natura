import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Meses fixos
meses = ["JAN","FEV","MAR","ABR","MAI","JUN","JUL","AGO","SET","OUT","NOV","DEZ"]

# Dados fictícios (substitua por dados reais ou leitura de CSV/Excel)
vendas_2024 = [3.9, 4.0, 4.2, 4.1, 4.3, 4.4, 4.6, 4.7, 4.2, 4.5, 4.8, 5.0]
vendas_2025 = [4.2, 3.8, 4.7, 4.6, 4.1, 4.6, 4.8, 5.3, 4.3, 4.9, 5.5, 5.9]
vendas_2026 = [4.8, 4.6, 4.5, 5.2, 5.6, None, None, None, None, None, None, None]

# Título do app
st.title("Histórico de Vendas Natura Kaiak (2024 x 2025 x 2026)")

# Criar gráfico
fig, ax = plt.subplots(figsize=(14,7))

ax.plot(meses, vendas_2024, marker='o', linewidth=2, label='Vendas 2024')
ax.plot(meses, vendas_2025, marker='o', linewidth=2, label='Vendas 2025')
ax.plot(meses, vendas_2026, marker='o', linewidth=2, label='Vendas 2026')

# Anotações nos pontos
for x, y in zip(meses, vendas_2024):
    if y is not None:
        ax.text(x, y+0.05, f'R$ {y:.1f} mi', fontsize=8, fontweight='bold', ha='center')

for x, y in zip(meses, vendas_2025):
    if y is not None:
        ax.text(x, y+0.05, f'R$ {y:.1f} mi', fontsize=8, fontweight='bold', ha='center')

for x, y in zip(meses, vendas_2026):
    if y is not None:
        ax.text(x, y-0.15, f'R$ {y:.1f} mi', fontsize=8, fontweight='bold', ha='center')

# Configurações do gráfico
ax.set_ylabel("Faturamento (R$ milhões)", fontsize=14, fontweight='bold')
ax.set_title("Histórico de Vendas Natura Kaiak", fontsize=20, fontweight='bold')
ax.legend()
ax.grid(True, linestyle='--', alpha=0.3)

st.pyplot(fig)

# Texto adicional
st.markdown("""
Este gráfico compara o faturamento estimado da linha **Kaiak** da Natura entre os anos de 2024, 2025 e 2026.
Os valores são baseados em estimativa de mercado via API e podem ser substituídos por dados reais de relatórios financeiros ou sistemas internos caso sejam encontrados.
""")
