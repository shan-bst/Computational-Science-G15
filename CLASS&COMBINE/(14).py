import matplotlib.pyplot as plt

# --- 1. RAW DATA (Group 14) ---
h1a_raw = [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]  # 100 elements (heads sum 42)
t1a_raw = [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1]  # 100 elements (tails sum 58)

h20a_raw = [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1]  # 100 elements (heads sum 42)
t20a_raw = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0]  # 100 elements (tails sum 58)

# --- 2. CALCULATION ---
def calc_running_total(data):
    res, s = [], 0
    for x in data: 
        s += x; res.append(s)
    return res

# Activity 2 Data: Add 1A and 20A together for each toss
comb_h = [h1a_raw[i] + h20a_raw[i] for i in range(100)]
comb_t = [t1a_raw[i] + t20a_raw[i] for i in range(100)]

tosses = list(range(1, 101))

# --- FIGURE 1: 1A ---
plt.figure(figsize=(10, 6))
h1a_cum = calc_running_total(h1a_raw)
t1a_cum = calc_running_total(t1a_raw)
plt.plot(tosses, h1a_cum, label=f'1A Heads (Total: {h1a_cum[-1]})', color='blue')
plt.plot(tosses, t1a_cum, label=f'1A Tails (Total: {t1a_cum[-1]})', color='green')
plt.title('1A Coin Running Totals (Group 14)', fontweight='bold')
plt.legend(); plt.grid(True); plt.tight_layout()
print("Showing Graph 1 (1A). Close window to continue.")
plt.show()

# --- FIGURE 2: 20A ---
plt.figure(figsize=(10, 6))
h20a_cum = calc_running_total(h20a_raw)
t20a_cum = calc_running_total(t20a_raw)
plt.plot(tosses, h20a_cum, label=f'20A Heads (Total: {h20a_cum[-1]})', color='blue')
plt.plot(tosses, t20a_cum, label=f'20A Tails (Total: {t20a_cum[-1]})', color='green')
plt.title('20A Coin Running Totals (Group 14)', fontweight='bold')
plt.legend(); plt.grid(True); plt.tight_layout()
print("Showing Graph 2 (20A). Close window to continue.")
plt.show()

# --- FIGURE 3: ACTIVITY 2 (COMBINED) ---
plt.figure(figsize=(10, 6))
comb_h_cum = calc_running_total(comb_h)
comb_t_cum = calc_running_total(comb_t)
plt.plot(tosses, comb_h_cum, label=f'Combined Heads (Total: {comb_h_cum[-1]})', color='blue', linewidth=2.5)
plt.plot(tosses, comb_t_cum, label=f'Combined Tails (Total: {comb_t_cum[-1]})', color='green', linewidth=2.5)
plt.title('Combined Running Totals (1A + 20A)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Toss Number')
plt.ylabel('Cumulative Count')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
print("Showing Graph 3 (Combined).")
plt.show()