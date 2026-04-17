import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rcParams
import os

BG = '#1a1b27'
ACCENT_BLUE = '#7c83fd'
ACCENT_GREEN = '#26a641'
ACCENT_RED = '#e05c5c'
TEXT_COLOR = '#888888'
GRID_COLOR = '#2a2b3a'

rcParams['font.family'] = 'monospace'
os.makedirs('assets', exist_ok=True)

# ORDERBOOK
def gen_orderbook():
    fig, ax = plt.subplots(figsize=(4, 2.8))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    bids = [320, 280, 210, 160, 90]
    asks = [150, 240, 290, 330, 380]
    levels = [0,1,2,3,4]

    ax.barh(levels, [-b for b in bids], color=ACCENT_GREEN, alpha=0.85)
    ax.barh(levels, asks, color=ACCENT_RED, alpha=0.85)

    ax.axvline(0, color='white', linewidth=0.5, alpha=0.3)
    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color('#2a2b3a')
        spine.set_linewidth(0.5)

    ax.text(0, 5.2, '// order book', color=TEXT_COLOR, fontsize=7, ha='center')

    plt.tight_layout(pad=0.1)
    plt.savefig('assets/orderbook.svg', facecolor=BG)
    plt.close()

# PRICE
def gen_price():
    fig, ax = plt.subplots(figsize=(4, 2.8))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    x = np.linspace(0,10,200)
    y = np.cumsum(np.random.randn(200))*0.1 + x*0.2

    ax.plot(x,y,color=ACCENT_BLUE)
    ax.fill_between(x,y,alpha=0.15,color=ACCENT_BLUE)

    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color('#2a2b3a')
        spine.set_linewidth(0.5)

    ax.text(0, max(y)*1.05, '// price action', color=TEXT_COLOR, fontsize=7)

    plt.tight_layout(pad=0.1)
    plt.savefig('assets/priceaction.svg', facecolor=BG)
    plt.close()

# BELL CURVE
def gen_bell():
    fig, ax = plt.subplots(figsize=(4, 2.8))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    x = np.linspace(-4,4,300)
    y = np.exp(-0.5*x**2)

    ax.plot(x,y,color=ACCENT_BLUE)
    ax.fill_between(x,y,alpha=0.15,color=ACCENT_BLUE)

    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color('#2a2b3a')
        spine.set_linewidth(0.5)

    ax.text(-3.5, max(y)*1.05, '// distribution', color=TEXT_COLOR, fontsize=7)

    plt.tight_layout(pad=0.1)
    plt.savefig('assets/bellcurve.svg', facecolor=BG)
    plt.close()

# SCATTER
def gen_scatter():
    fig, ax = plt.subplots(figsize=(4, 2.8))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    risk = np.random.rand(20)
    alpha = risk*0.6 + np.random.randn(20)*0.1

    ax.scatter(risk, alpha, c=alpha, cmap='RdYlGn')

    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color('#2a2b3a')
        spine.set_linewidth(0.5)

    ax.text(0, max(alpha)*1.05, '// alpha vs risk', color=TEXT_COLOR, fontsize=7)

    plt.tight_layout(pad=0.1)
    plt.savefig('assets/scatter.svg', facecolor=BG)
    plt.close()

if __name__ == "__main__":
    gen_orderbook()
    gen_price()
    gen_bell()
    gen_scatter()
