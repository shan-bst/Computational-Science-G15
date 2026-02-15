import matplotlib.pyplot as plt

# --- 1. RAW DATA (Group 9) ---
h5b_raw = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1]
t5b_raw = [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0]

h1b_raw = [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0]
t1b_raw = [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1]

h20a_raw = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0]
t20a_raw = [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1]

# --- 2. CALCULATION ---
def calc_running_total(data):
    res, s = [], 0
    for x in data: 
        s += x; res.append(s)
    return res

tosses = list(range(1, 101))

# --- FIGURE 1: 5B ---
plt.figure(figsize=(10, 6))
h5b_cum = calc_running_total(h5b_raw)
t5b_cum = calc_running_total(t5b_raw)
plt.plot(tosses, h5b_cum, label=f'5B Heads (Total: {h5b_cum[-1]})', color='blue')
plt.plot(tosses, t5b_cum, label=f'5B Tails (Total: {t5b_cum[-1]})', color='green')
plt.title('5B Coin Running Totals (Group 9)', fontweight='bold')
plt.legend(); plt.grid(True); plt.tight_layout()
print("Showing Graph 1 (5B). Close window to continue.")
plt.show()

# --- FIGURE 2: 1B ---
plt.figure(figsize=(10, 6))
h1b_cum = calc_running_total(h1b_raw)
t1b_cum = calc_running_total(t1b_raw)
plt.plot(tosses, h1b_cum, label=f'1B Heads (Total: {h1b_cum[-1]})', color='blue')
plt.plot(tosses, t1b_cum, label=f'1B Tails (Total: {t1b_cum[-1]})', color='green')
plt.title('1B Coin Running Totals (Group 9)', fontweight='bold')
plt.legend(); plt.grid(True); plt.tight_layout()
print("Showing Graph 2 (1B). Close window to continue.")
plt.show()

# --- FIGURE 3: 20A ---
plt.figure(figsize=(10, 6))
h20a_cum = calc_running_total(h20a_raw)
t20a_cum = calc_running_total(t20a_raw)
plt.plot(tosses, h20a_cum, label=f'20A Heads (Total: {h20a_cum[-1]})', color='blue')
plt.plot(tosses, t20a_cum, label=f'20A Tails (Total: {t20a_cum[-1]})', color='green')
plt.title('20A Coin Running Totals (Group 9)', fontweight='bold')
plt.legend(); plt.grid(True); plt.tight_layout()
print("Showing Graph 3 (20A). Close window to continue.")
plt.show()

# --- FIGURE 4: ACTIVITY 2 (COMBINED: Overall Heads and Tails) ---
plt.figure(figsize=(10, 6))
comb_h = [h5b_raw[i] + h1b_raw[i] + h20a_raw[i] for i in range(100)]
comb_t = [t5b_raw[i] + t1b_raw[i] + t20a_raw[i] for i in range(100)]
comb_h_cum = calc_running_total(comb_h)
comb_t_cum = calc_running_total(comb_t)
plt.plot(tosses, comb_h_cum, label=f'Overall Heads (Total: {comb_h_cum[-1]})', color='blue', linewidth=2)
plt.plot(tosses, comb_t_cum, label=f'Overall Tails (Total: {comb_t_cum[-1]})', color='green', linewidth=2)
plt.title('Combined Running Totals (Overall Heads + Tails from 5B, 1B, 20A)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Toss Number')
plt.ylabel('Cumulative Count')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
print("Showing Graph 4 (Combined with 2 lines: Overall Heads and Tails).")
plt.show()