import matplotlib.pyplot as plt

# --- 1. RAW DATA (Group 12) ---
h5b_raw = [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
t5b_raw = [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0]

h5a_raw = [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0]  
t5a_raw = [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1]  

# --- 2. CALCULATION ---
def calc_running_total(data):
    res, s = [], 0
    for x in data: 
        s += x; res.append(s)
    return res

# Activity 2 Data: Add 5B and 5A together for each toss
comb_h = [h5b_raw[i] + h5a_raw[i] for i in range(100)]
comb_t = [t5b_raw[i] + t5a_raw[i] for i in range(100)]

tosses = list(range(1, 101))

# --- FIGURE 1: 5B ---
plt.figure(figsize=(10, 6))
h5b_cum = calc_running_total(h5b_raw)
t5b_cum = calc_running_total(t5b_raw)
plt.plot(tosses, h5b_cum, label=f'5B Heads (Total: {h5b_cum[-1]})', color='blue')
plt.plot(tosses, t5b_cum, label=f'5B Tails (Total: {t5b_cum[-1]})', color='green')
plt.title('5B Coin Running Totals (Group 12)', fontweight='bold')
plt.legend(); plt.grid(True); plt.tight_layout()
print("Showing Graph 1 (5B). Close window to continue.")
plt.show()

# --- FIGURE 2: 5A ---
plt.figure(figsize=(10, 6))
h5a_cum = calc_running_total(h5a_raw)
t5a_cum = calc_running_total(t5a_raw)
plt.plot(tosses, h5a_cum, label=f'5A Heads (Total: {h5a_cum[-1]})', color='blue')
plt.plot(tosses, t5a_cum, label=f'5A Tails (Total: {t5a_cum[-1]})', color='green')
plt.title('5A Coin Running Totals (Group 12)', fontweight='bold')
plt.legend(); plt.grid(True); plt.tight_layout()
print("Showing Graph 2 (5A). Close window to continue.")
plt.show()

# --- FIGURE 3: ACTIVITY 2 (COMBINED) ---
plt.figure(figsize=(10, 6))
comb_h_cum = calc_running_total(comb_h)
comb_t_cum = calc_running_total(comb_t)
plt.plot(tosses, comb_h_cum, label=f'Combined Heads (Total: {comb_h_cum[-1]})', color='blue', linewidth=2.5)
plt.plot(tosses, comb_t_cum, label=f'Combined Tails (Total: {comb_t_cum[-1]})', color='green', linewidth=2.5)
plt.title('Combined Running Totals (5B + 5A)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Toss Number')
plt.ylabel('Cumulative Count')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
print("Showing Graph 3 (Combined).")
plt.show()