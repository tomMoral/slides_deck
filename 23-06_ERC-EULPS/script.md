
## EULPS - E.U.LPS.

Hello, it is my pleasure to present my project proposal E.U.LPS.

#### S2

Imagine you enter an Operating Room and undergo a surgical procedure under General Anesthesia.

The anesthetist won't just put you to sleep. He will actually monitor your status, to make sure you get a stable anesthesia and the best possible outcome.
Using various sensors, he will for instance track your cardiovascular system or your brain.
These sensors produce complex multimodal signals which are hard to directly process for the anesthetist.

To summarize these signals, many indicators have been developed over the years.
They help the anesthetist make decision about which drug to inject to get the best possible anesthesia trajectory.

However, these indicators are instantaneous snapshots of the signals, only giving information about the current status of the patient.
The anesthetist cannot really anticipate the evolution of the patient, and only react to status changes.
Moreover, these indicators are not personalized for the patient, and the anesthetist needs to adapt its reading depending on the patient's history.

<!-- In order to propose personalized and predictive indicators to summarize the signal, AI is a powerful approach. -->


#### S3

Be it to understand the functioning of physical systems like the brain, or to control and stir a large physical system, summarizing signals is a critical step.
It allows the practitioner to make sense of the data and draw conclusions.


---

The overarching goal of my project is to provide an automated way to summarize complex physical signals using AI, to be able to easily answer questions about their structures.


#### S4

When looking at recent breakthrough in AI, being the technologies that lead to ChatGPT or Midjourney, they rely on two common ingredients:

---

- First, they don't consider the full signals directly but tokens, which correspond to parts of words for language models or small patches for images.
   In these applications, the signal is transformed in a stream of tokens, and then processed using transformer architectures, which compute interactions between the tokens.

- Second, these powerful models rely on self-supervised pretraining that captures the distribution of the input of the model X by solving some pretext tasks, defined directly from the data.
    Typical tasks consist in next-token prediction, which also helps characterizing the interaction between tokens.
    These models are then fined-tune to tackle specific tasks, by further training then on small annotated databases to produce high quality predictions.

These two ingredients allow to capture the distribution of the model input X by modeling the interaction between the tokens it contains, and then use it to summarize the signal or to solve specific tasks.

---

There are various challenges in applying similar approach to physical signals.
The notion of tokens for the signals is not well-defined for signals, unlike in language and image application.
Another constraint is that the provided summary needs to be interpretable, unlike black-box models produce through deep learning.



#### S5

Looking back at the general anesthesia, a key observation is that the signals are often mostly driven by physical phenomenon:
    - either physiological events that underly the signal such as an heartbeat for the ECG or
    - external events that impact the signal such as drug injection that will modify the patient state.
Physical events are present both in and around the recorded signals.
But physiological events are not directly observed.
They produce characteristic patterns, which often constitute the building block for the overall signal's structure.
Finding these recurring patterns and considering their apparition as specific physiological events yields punctual representations of the signal, as a stream of events.
<!-- The duality between the recurring patterns and the events allow to transform the continuous signal into a stream of events. -->

The notion of events can thus is thus a natural candidate to tokenize signals.


#### S6

And this observation can apply to other domains.
Characteristic patterns highlight brain responses in neuroscience or the presence of stars and galaxy in astronomical images.
They can also be turned into punctual events by considering the time or place they occur instead of the full extent of the pattern.
Moreover, the events can be interpreted by practitioners, as they have physical meaning.

These stream of events, joined with known external events recorded with the signal, produce informative signal representations.


#### S7

The goal of the E.U.LPS project is to propose new unsupervised methods to process jointly physiological signals and their associated external events.

My approach is to turn them into events' streams and model the events' distribution, similarly to the stream of tokens processed for language models.
The core hypothesis is that the distribution of the events in time and space is much simpler than the original signals' distribution.

One difficulty of this approach compared to existing works is that the physiological events from the signals are not known a priori.
The project will aim at developping methods that can identify the recurring patterns as well as model their distribution and the distribution of external events jointly.

---

To tackle this goal, I will focus on three tasks:
- first, considering that I have access to all events, I will develop models able to describe physiological events' distribution.
- then, building on these models, I will propose methods that are able to simultaneously extract events from the signal and model their distribution jointly  with external events.
<!-- propose some fine-tuning methods to leverage these novel signal representation to tackle tasks in practice -->
- Finally, I will propose some fine-tuning methods to leverage these novel signal description to tackle practical tasks.

#### S8





#### S11

To summarize, my project aims at providing a new way to summarize complex physical signals.
It will allow to answer questions about the signal's structure and to solve tasks in practice.
It will also help to develop new indicators for the anesthetist, to better monitor the patient during surgery.



<!-- A question could be: why not in a lifescience pannel? The answer is: because the problem is a general one for Machine learning on signal structured data.
Indeed, other physiological signals such as gait signals, or signal from neuroscience also have such structure, but also images in astronomy or output of large high energy particule simulations. -->
