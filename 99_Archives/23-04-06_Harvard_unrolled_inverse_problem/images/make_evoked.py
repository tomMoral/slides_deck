import os
import mne

import matplotlib.pyplot as plt

sample_data_folder = mne.datasets.sample.data_path()
sample_data_raw_file = os.path.join(
    sample_data_folder, "MEG", "sample", "sample_audvis_raw.fif"
)
raw = mne.io.read_raw_fif(sample_data_raw_file, verbose=False).crop(tmax=120)
events = mne.find_events(raw, stim_channel="STI 014")
event_dict = {
    "auditory/left": 1,
    "auditory/right": 2,
    "visual/left": 3,
    "visual/right": 4,
    "face": 5,
    "button": 32,
}
epochs = mne.Epochs(
    raw, events, tmin=-0.2, tmax=0.5, event_id=event_dict, preload=True
)
ecg_proj_file = os.path.join(
    sample_data_folder, "MEG", "sample", "sample_audvis_ecg-proj.fif"
)
ecg_projs = mne.read_proj(ecg_proj_file)
epochs.add_proj(ecg_projs)
epochs.apply_proj()
fig, = epochs["auditory"].plot_image(picks="mag", combine="mean", show=False)
fig.set_figwidth(3.2)
fig.set_figheight(2.4)
fig.savefig("evoked_response.pdf")

e_mean = epochs["auditory"].pick_types(meg='grad').average()
t0 = e_mean.time_as_index(0.085)[0]
fig, axes = plt.subplots()
mne.viz.plot_topomap(e_mean.data[:, t0], e_mean.info, axes=axes, show=False)
fig.savefig("evoked_topo.pdf")
