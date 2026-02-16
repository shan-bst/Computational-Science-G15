import matplotlib.pyplot as plt
import numpy as np

# --- 1. DARK THEME & COLOR CONFIGURATION (REPEATED FOR INDEPENDENCE) ---
color_bg = "#121926"
color_heads = "#3b82f6"
color_tails = "#059669"
color_pink = "#f472b6"
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
    tosses = list(range(1, len(h_cum) + 1))
    ax.plot(tosses, h_cum, color=color_heads, linewidth=2.5, label='Heads (H)')
    ax.plot(tosses, t_cum, color=color_tails, linewidth=2.5, label='Tails (T)')
    ax.set_title(title, fontsize=11, fontweight='bold', pad=15)
    ax.set_xlabel('No. of Attempts')
    ax.set_ylabel('Cumulative Count')
    ax.grid(True, alpha=0.2)
    ax.legend(loc='upper left', facecolor="#1f2937", fontsize='x-small')

    f_h, f_t = h_cum[-1], t_cum[-1]
    total = f_h + f_t
    t_data = [
        ["Outcome", "Count", "Prob."],
        ["Heads (H)", f"{f_h}", f"{(f_h/total)*100:.1f}%"],
        ["Tails (T)", f"{f_t}", f"{(f_t/total)*100:.1f}%"],
        ["Total", f"{total}", "100.0%"]
    ]
    bbox_val = [0.15, -0.45, 0.7, 0.3]
    tbl = ax.table(cellText=t_data, loc='bottom', bbox=bbox_val, cellLoc='center')
    
    for (r, c), cell in tbl.get_celld().items():
        cell.set_edgecolor("#444b5a")
        cell.set_facecolor(color_bg)
        if r == 0: cell.set_facecolor("#1f2937") 
        if r == 3: cell.set_facecolor("#1a2233") 
        if c == 2 and r > 0: cell.get_text().set_color(color_pink)
        if r == 1 and c < 2: cell.get_text().set_color(color_heads)
        if r == 2 and c < 2: cell.get_text().set_color(color_tails)

# --- 2. RAW DATA ---
h1b_raw = [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1]
t1b_raw = [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0]

h5b_raw = [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]
t5b_raw = [1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0]

# --- 3. COMBINED CALCULATIONS ---
comb_h_cum = np.cumsum([h1b_raw[i] + h5b_raw[i] for i in range(100)])
comb_t_cum = np.cumsum([t1b_raw[i] + t5b_raw[i] for i in range(100)])

# --- 4. RENDERING COMBINED DATA ---
fig2, ax_c = plt.subplots(figsize=(10, 7))
apply_custom_style(ax_c, 'Combined Running Totals (1B + 5B)', comb_h_cum, comb_t_cum)
plt.subplots_adjust(bottom=0.35)
plt.show()