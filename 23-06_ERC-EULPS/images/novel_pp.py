import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from tick.hawkes import SimuHawkes, HawkesKernelSumExp


# Arrow style
ARROW_STYLE = dict(
    arrowstyle="Simple, tail_width=0.5, head_width=4, head_length=8",
    color="C2"
)


# simulate the Hawkes kernel
run_time = 10

# seed = np.random.randint(2**31)
# print(seed)
seed = 293476211

hawkes = SimuHawkes(n_nodes=1, end_time=run_time, verbose=False, seed=seed)
kernel = HawkesKernelSumExp([.7], [.8])
hawkes.set_kernel(0, 0, kernel)
hawkes.set_baseline(0, .2)

dt = 0.01
hawkes.track_intensity(dt)
hawkes.simulate()
timestamps = hawkes.timestamps
intensity = hawkes.tracked_intensity
intensity_times = hawkes.intensity_tracked_times


# Create the figure
fig, axes = plt.subplots(
    # nrows=2, ncols=1, figsize=(4.8, 2.7),
    nrows=2, ncols=1, figsize=(6, 3.2),
    gridspec_kw={'width_ratios': [3]},
    squeeze=False
)

T_max = 5.5
sfreq = 100
L = int(T_max * sfreq)

z = np.array(hawkes.timestamps[0][:20]) * (5 / 6) * sfreq
intensity_times = np.array(intensity_times) * (5 / 6) * sfreq

markerline, stemlines, baseline = axes[0, 0].stem(z, np.ones(len(z)))
plt.setp(stemlines, 'color', 'k', linewidth=1, linestyle='--')
plt.setp(markerline, 'color', 'k', linewidth=2)
axes[0, 0].set_xlim(0, L)
axes[0, 0].plot([0, L], [0, 0], 'k', lw=2)
axes[0, 0].set_xticks([0, 200, 500])
axes[0, 0].set_xticklabels(['0s', '2s', '5s'])
axes[0, 0].set_yticks([])
# import IPython; IPython.embed(colors='neutral')
axes[0, 0].fill_between(
    intensity_times, intensity[0],
    alpha=0.3, color='C2', lw=0
)
axes[0, 0].hlines(hawkes.baseline, 0, L, ls='--', lw=2, color='C3')
axes[0, 0].set_title("Current models (Markovian kernels)", fontsize=20)
axes[0, 0].text(2, 0.3, 'baseline', color='C3', rotation=-60, fontsize=10)
axes[0, 0].text(465, 0.55, 'induced', color='C2', rotation=-10, fontsize=10)

for i, j in [(0, 2), (3, 4)]:
    xi, xj = z[i] + 5, z[j] - 5
    arrow = patches.FancyArrowPatch(
        (xi, 1.05), (xj, 1.05),
        connectionstyle="arc3,rad=-.5", **ARROW_STYLE
    )
    axes[0, 0].add_patch(arrow)

# z = np.array([
#     v[0] for v in ex.steps_annotation[0] if v[0] > T0 and v[0] < T1
# ]) - T0
z = (np.array([0.9, 2, 3.1, 4.3, 5.4])*100).astype(int)

z_val = np.array([0.4] + [1] * (len(z) - 1)) * .7
z_bar = np.zeros(L)
jitter = np.array([+5, -10, 5, 0, 0])
z_bar[z + jitter] = 1


markerline, stemlines, baseline = axes[1, 0].stem(z, z_val)
plt.setp(stemlines, 'color', 'k', linewidth=1, linestyle='--')
plt.setp(markerline, 'color', 'k', linewidth=2)
axes[1, 0].set_xlim(0, L)
axes[1, 0].plot([0, L], [0, 0], 'k', lw=2)
axes[1, 0].set_xticks([0, 200, 500])
axes[1, 0].set_xticklabels(['0s', '2s', '5s'])
axes[1, 0].set_yticks([])
axes[1, 0].set_title("Novel models", y=-0, pad=-40, fontsize=20)


T_ker = 60
baseline = 0.1
mean_period = int(np.diff(z).mean() - T_ker // 2)
ker = np.cos(np.pi * np.linspace(-0.5, .5, 60))
axes[1, 0].fill_between(
    np.arange(L),
    np.convolve(z_bar, np.pad(ker, (mean_period, 0)))[:L] + baseline,
    alpha=0.3, color='C2', lw=0
)
axes[1, 0].hlines(baseline, 0, L, ls='--', lw=2, color='C3')
axes[1, 0].text(2, 0.2, 'baseline', color='C3', rotation=-60, fontsize=10)
axes[1, 0].text(220, 0.2, 'induced', color='C2', rotation=-60, fontsize=10)

for zz, zv in zip(z, z_val):
    arrow = patches.FancyArrowPatch(
        (zz + 4, zv + 0.05), (zz + mean_period + 10, zv + 0.05),
        connectionstyle="arc3,rad=-.5", **ARROW_STYLE
    )
    axes[1, 0].add_patch(arrow)


# legend = {
#     'Activation': plt.Line2D([], [], color='k', ls='--'),
#     'Intensity': plt.Rectangle((0, 0), 1, 1, color='C2', alpha=0.3, lw=0)
# }
# axes[1, 1].set_axis_off()
# axes[1, 1].legend(legend.values(), legend.keys(), loc='center',
#                   fontsize=12)

fig.tight_layout()
fig.savefig('novel_pp.pdf', dpi=300)

plt.show()
