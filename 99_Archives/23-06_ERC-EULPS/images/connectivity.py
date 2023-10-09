import numpy as np
from nilearn import datasets
from nilearn import plotting
from nilearn import input_data
import matplotlib.pyplot as plt

from nilearn.connectome import ConnectivityMeasure


# Load the dataset
adhd_dataset = datasets.fetch_adhd(n_subjects=1)

# print basic information on the dataset
# dmn_coords = [(0, -52, 18), (-46, -68, 32), (46, -68, 32), (1, 50, -5)]
# labels = [
#           'Posterior Cingulate Cortex',
#           'Left Temporoparietal junction',
#           'Right Temporoparietal junction',
#           'Medial prefrontal cortex',
#          ]
dmn_coords = [(-20, -52, 18), (46, -68, 32), (1, 50, -5)]
K = len(dmn_coords)

masker = input_data.NiftiSpheresMasker(
    dmn_coords, radius=8,
    detrend=True, standardize=True,
    low_pass=0.1, high_pass=0.01, t_r=2.5,
    verbose=2)

func_filename = adhd_dataset.func[0]
confound_filename = adhd_dataset.confounds[0]

time_series = masker.fit_transform(func_filename,
                                   confounds=[confound_filename])
print(time_series.shape)

connectivity_measure = ConnectivityMeasure(kind='partial correlation')
partial_correlation_matrix = connectivity_measure.fit_transform(
    [time_series])[0]

node_color = ['C0', 'C1', 'C2']
plotting.plot_connectome(np.eye(K), dmn_coords, node_color=node_color,
                         node_size=150, display_mode='yz')
plt.savefig("connectivity_independent")

plotting.plot_connectome(-np.ones((K, K)), dmn_coords,
                         node_color=node_color, node_size=150,
                         edge_cmap='winter', edge_kwargs={'linewidth': 2},
                         display_mode='yz')
plt.savefig("connectivity_simultaneous")

plotting.plot_connectome(partial_correlation_matrix, dmn_coords,
                         node_color=node_color, node_size=150,
                         edge_cmap='winter',
                         display_mode='yz')
plt.savefig("connectivity_default_mode")
