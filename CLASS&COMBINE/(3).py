import matplotlib.pyplot as plt

# --- 1. RAW DATA (Group 3) ---
h1b_raw = [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
t1b_raw = [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

h10a_raw = [0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0]
t10a_raw = [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1]

# --- 2. CALCULATION ---
def calc_running_total(data):
    res, s = [], 0
    for x in data: 
        s += x; res.append(s)
    return res

# Activity 2 Data: Add 1B and 10A together for each toss
comb_h = [h1b_raw[i] + h10a_raw[i] for i in range(100)]
comb_t = [t1b_raw[i] + t10a_raw[i] for i in range(100)]

tosses = list(range(1, 101))

# --- FIGURE 1: 1B ---
plt.figure(figsize=(10, 6))
h1b_cum = calc_running_total(h1b_raw)
t1b_cum = calc_running_total(t1b_raw)
plt.plot(tosses, h1b_cum, label=f'1B Heads (Total: {h1b_cum[-1]})', color='blue')
plt.plot(tosses, t1b_cum, label=f'1B Tails (Total: {t1b_cum[-1]})', color='green')
plt.title('1B Coin Running Totals (Group 3)', fontweight='bold')
plt.legend(); plt.grid(True); plt.tight_layout()
print("Showing Graph 1 (1B). Close window to continue.")
plt.show()

# --- FIGURE 2: 10A ---
plt.figure(figsize=(10, 6))
h10a_cum = calc_running_total(h10a_raw)
t10a_cum = calc_running_total(t10a_raw)
plt.plot(tosses, h10a_cum, label=f'10A Heads (Total: {h10a_cum[-1]})', color='blue')
plt.plot(tosses, t10a_cum, label=f'10A Tails (Total: {t10a_cum[-1]})', color='green')
plt.title('10A Coin Running Totals (Group 3)', fontweight='bold')
plt.legend(); plt.grid(True); plt.tight_layout()
print("Showing Graph 2 (10A). Close window to continue.")
plt.show()

# --- FIGURE 3: ACTIVITY 2 (COMBINED) ---
plt.figure(figsize=(10, 6))
comb_h_cum = calc_running_total(comb_h)
comb_t_cum = calc_running_total(comb_t)
plt.plot(tosses, comb_h_cum, label=f'Combined Heads (Total: {comb_h_cum[-1]})', color='blue', linewidth=2.5)
plt.plot(tosses, comb_t_cum, label=f'Combined Tails (Total: {comb_t_cum[-1]})', color='green', linewidth=2.5)
plt.title('Combined Running Totals (1B + 10A)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Toss Number')
plt.ylabel('Cumulative Count')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
print("Showing Graph 3 (Combined).")
plt.show()