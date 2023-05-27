
## EULPS - E.U.LPS.

0. Introduction:

Hello, I am Thomas Moreau and I am presenting my proposal EULPS, on event-based unsupervised learning for Physiological signals.

1. General anesthesia:

# Raw values are not meaningful

When you enter an Operating Room and undergo a General Anesthesia, the anesthesit uses many sensors to monitor your status: ECG for your heart, Plethysmography to make sure your blood has enough oxygen, and EEG to monitor your brain activity.
These raw signals are very complex.
To allow the anesthesiologist to take decision, many indicators have been developed to summarize them into actionable quantities: arterial pressure, heart rate...
While these indicators are useful, they are instantaneous summary for these signals, and do not allow for detecting early signs of degradation of the patient.

My collaborators in hospital Lariboisière in the north of Paris have been constructing a database with curated recordings thousands of patient undergoing GA procedure for the past few years, associated with clinical outcomes of the procedure. They use it to develop novel indicators, in particular for the EEG monitoring.




- Important and dangerous procedure
- Recordings are complex: ECG, REps. Pletho, EEG, ...
- Need for indicators, need for markers of potential issues
- Can we use stat for these complex signals?
and 

2. More general signals


A question could be: why not in a lifescience pannel? The answer is: because the problem is a general one for Machine learning on signal structured data.
Indeed, other physiological signals such as gait signals, or signal from neuroscience also have such structure, but also images in astronomy or output of large high energy particule simulations.

2. ML for complex signals: recent success stories:
- In common unsupervised learning
- In common interactions between identified parts of the signal.