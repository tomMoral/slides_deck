
## EULPS - E.U.LPS.

Hello everyone, it is my pleasure to present my project proposal E.U.LPS.

#### S2

Imagine you enter an Operating Room and undergo a surgical procedure under General Anesthesia.

The anesthetist won't just put you to sleep. He will actually monitor your status, to make sure you get a stable anesthesia and the best possible outcome.
Using various sensors, he will for instance track your cardiovascular system or your brain.
These sensors produce complex multimodal signals which are hard to directly process for the anesthetist.

To summarize these signals and help the anesthetist make decision, many indicators have been developed over the years.
However, these indicators are instantaneous snapshots of the signals, only giving information about the current status of the patient.
They don't allow the anesthetist to anticipate the status change of the patient, and only react to them.
Moreover, these indicators are usually not personalized for the patient.

<!-- In order to propose personalized and predictive indicators to summarize the signal, AI is a powerful approach. -->


#### S3

Summarizing multivariate signals in predictive and personalized ways is a critical step in many pipelines, be it to understand the functioning of the brain, or to control and stir large physical systems like a tokamak.
It allows the practitioner to understand the underlying system, and make decisions.


---

The overarching goal of my project is to provide an automated way to summarize complex physical signals using AI, to be able to easily answer questions about the system that produced them.


#### S4

When looking at recent breakthrough in AI for complex inputs, in particular the technologies that led to ChatGPT or Midjourney, they rely on two common ingredients:

---

- First, these models don't process their input directly.
  They first transformed it as a stream of tokens, which correspond to parts of words for language models or small patches for images. 
  These streams are then processed using transformer architectures, which compute interactions between the tokens.

- The second ingredient is the use of self-supervised pretraining to train the model.
  This step allows to capture the distribution of the input of the model X by learnig to solve some pretext tasks, defined directly from the data.
  Typical example are the prediction of the next token in the stream.

These models are then fined-tune, to specialize them to tackle specific tasks.


---

In order to apply similar approaches to multivariate signals, various challenges need to be overcome.
First, the notion of tokens for the signals is not well-defined, unlike in language and image application.
Also, a particular focus is on the interpretability of the method, needed to understand the signal or make decisions.



#### S5

For general anesthesia recordings, a key observation is that the signals are often mostly driven by physical phenomenon.
    - Indeed, external events such as drug injection impact the signal as they modify the patient state.
    - Moreover, physiological events such as a heartbeat, produce characteristic patterns, which often constitute the building block for the overall signal's structure
While external events are directly observed, physiological events are only visible through the proxy recurring patterns.
Finding these recurring patterns and considering their apparition as specific physiological events yields punctual representations of the signal, as a stream of events.
<!-- The duality between the recurring patterns and the events allow to transform the continuous signal into a stream of events. -->


#### S6

And this observation applies to many other domains.
Characteristic patterns highlight brain responses in neuroscience or the presence of stars and galaxy in astronomical images.
They can also be turned into punctual events by considering the time or place they occur instead of the full extent of the pattern, in order to tokenize the signals.

The notion of events is thus a natural candidate to tokenize signals.


An advantage of these events over random patches is that they can be interpreted by practitioners, as they have physical meaning.


#### S7

The goal of the E.U.LPS project is to propose new unsupervised methods to summarize physiological signals jointly with external events.

My approach is to turn them into events' streams and model the events' distribution, similarly to the stream of tokens processed for language models.
The core hypothesis is that the distribution of the events in time and space is much simpler than the original signals' distribution.

A challenge in this approach is that unlike existing works, the tokens a.k.a the physiological events are not known a priori and need to be identified.
<!-- The project will aim at developing methods for their  identify the recurring patterns as well as model their distribution and the distribution of external events jointly. -->

---

To tackle this goal, I will focus on three tasks:
- First, considering that we have identified the events, I will develop models able to describe physiological events' distribution.
- Then, building on these models, I will propose methods that are able to simultaneously extract events from the signal and model their distribution.
- Finally, I will propose some fine-tuning methods to leverage these novel signal descriptions to tackle practical tasks.

#### S8

In a first work package, I will consider the case where the events have already been identified in the signal, and we want to model their distribution.

I propose to rely on the framework of point processes, which is a classical framework to model the distribution of events in space and time.


However, most existing models in this framework are restricted to non-parametric or Markovian kernels, which do not capture well the latency between interacting events, and are limited to specific types of interactions.
Based on preliminary work that will be published with my postdoc in IMCL23, we will propose a novel inference framework that will unlock using more general models for point processes, with generic parametric kernels, unlocking novel use of the framework to model more complex interactions between events, such as pseudo-periodicity or thresholding effects, but also spatial dependencies with uncertainty.


#### S9

Then, I will propose joint methods to process signals and events.

In order to keep limited parametrization space and improve interpretability, I will take an approach that goes from low parametrization models to deep models.

First, I will consider small parametric models base on event detection algorithms, such as convolutional dictionary learning or change point detection, and extend them to take into account the distribution of the detected events.
The models will be fitted to the data using alternate minimization or bilevel optimization algorithms, which I have been working on in the last five years.

Then, I will consider more expressive models based on deep learning and traditional approaches in self supervised learning. These models are often considered more powerful as they can easily be adapted to the task considered, as they are fully differentiable. However, they tend to suffer from a lack of interpretability due to their massive parametrization. In order to keep benefit of a low parametrization models, the considered architectures will be based on the unrolling of the smaller models, which tend to limit the parameter explosion.

#### S10

Finally, to validate the proposed representations, we will develop methods that can leverage them to answer machine learning questions about physiological signals.

In order to take concrete examples, I will consider adverse event prediction for general anesthesia, to demonstrate the predictivness of the proposed signal summaries, as well as causal analysis in neuroscience recordings to highlight their interpretability.

The core idea will be to leverage either the likelihood for small parametric models and the differentiable architectures for deep network.



#### S11

To summarize, my project aims at providing a new signal processing tool to summarize complex physical signals based on events.
It will allow answering questions about the signal's structure and to solve tasks in practice.
It will also help to develop new indicators for the anesthetist, to better monitor the patient during surgery.

This project will benefit from my expertise in core machine learning and signals processing tools and will aim to have impact in various domain, in particular the one of GA, as my colleague Fabrice Vallée from Paris hospital will help me get access to a database of 46 thousands GA recordings to evaluate the methods resulting from the project.

Finally, the tools developed during this project will be disseminated as open source software, relying on my experience in the domain, as the maintainer of packages downloaded millions of times a month and the creator of domain specific software that are progressively gaining attention.
