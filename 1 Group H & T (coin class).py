import matplotlib.pyplot as plt
import numpy as np

# --- 1. DARK THEME & COLOR CONFIGURATION ---
color_bg = "#121926"     # Dark Navy background
color_heads = "#3b82f6"  # Blue for Heads
color_tails = "#059669"  # Green for Tails
color_pink = "#f472b6"   # Pink for Probability highlighting
color_grid = "#2d3748"

plt.rcParams.update({
    "figure.facecolor": color_bg, 
    "axes.facecolor": color_bg,
    "axes.edgecolor": "#444b5a", 
    "axes.labelcolor": "#ffffff",
    "xtick.color": "#aeb4c1", 
    "ytick.color": "#aeb4c1",
    "grid.color": color_grid, 
    "text.color": "#ffffff"
})

def apply_custom_style(ax, title, h_cum, t_cum, is_subplot=False):
    """Applies themed lines, labels, and the summary table with Totals."""
    tosses = list(range(1, len(h_cum) + 1))
    ax.plot(tosses, h_cum, color=color_heads, linewidth=2.5, label='Heads (H)')
    ax.plot(tosses, t_cum, color=color_tails, linewidth=2.5, label='Tails (T)')
    
    ax.set_title(title, fontsize=11, fontweight='bold', pad=15)
    ax.set_xlabel('No. of Attempts')
    ax.set_ylabel('Cumulative Count')
    ax.grid(True, alpha=0.2)
    ax.legend(loc='upper left', facecolor="#1f2937", fontsize='x-small')

    # Summary Table Logic
    f_h, f_t = h_cum[-1], t_cum[-1]
    total = f_h + f_t
    t_data = [
        ["Outcome", "Count", "Prob."],
        ["Heads (H)", f"{f_h}", f"{(f_h/total)*100:.1f}%"],
        ["Tails (T)", f"{f_t}", f"{(f_t/total)*100:.1f}%"],
        ["Total", f"{total}", "100.0%"]
    ]
    
    # Adjust table position based on layout
    bbox_val = [0.1, -0.6, 0.8, 0.4] if is_subplot else [0.15, -0.45, 0.7, 0.3]
    tbl = ax.table(cellText=t_data, loc='bottom', bbox=bbox_val, cellLoc='center')
    
    for (r, c), cell in tbl.get_celld().items():
        cell.set_edgecolor("#444b5a")
        cell.set_facecolor(color_bg)
        if r == 0: cell.set_facecolor("#1f2937") 
        if r == 3: cell.set_facecolor("#1a2233") 
        if c == 2 and r > 0: cell.get_text().set_color(color_pink)
        if r == 1 and c < 2: cell.get_text().set_color(color_heads)
        if r == 2 and c < 2: cell.get_text().set_color(color_tails)

# --- 2. RAW DATA (Group 15) ---
h1b_raw = [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1]
t1b_raw = [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0]

h5b_raw = [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]
t5b_raw = [1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0]

# --- 3. CALCULATIONS ---
h1b_cum = np.cumsum(h1b_raw); t1b_cum = np.cumsum(t1b_raw)
h5b_cum = np.cumsum(h5b_raw); t5b_cum = np.cumsum(t5b_raw)

# --- 4. RENDERING INDIVIDUAL COINS ---
fig1, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(15, 8))
apply_custom_style(ax_l, 'Graph 1: 1B Coin (Group 15)', h1b_cum, t1b_cum, is_subplot=True)
apply_custom_style(ax_r, 'Graph 2: 5B Coin (Group 15)', h5b_cum, t5b_cum, is_subplot=True)
plt.subplots_adjust(wspace=0.3, bottom=0.35)
plt.show()