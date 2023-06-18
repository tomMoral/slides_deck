
## EULPS - E.U.LPS.

Hello everyone, it is my pleasure to present my project proposal E.U.LPS.
<!-- Maybe  -->

#### S2

Imagine you enter an Operating Room for a surgery under General Anesthesia.

The anesthetist won't just put you to sleep. He will monitor your status to ensure that your condition remains stable: your heart, your brain and others.
As you can see with this picture from my collaborators in Paris hospital Lariboisiere, these multivariate signals are complex and hard to interpret.
That is why many indicators have been developed to support decisions.

Yet, they are an instantaneous snapshot of the patient's condition at time T.
They don't allow to anticipate what is going to happen, but only react to status changes.


#### S3

Summarizing large scale multivariate signals in predictive ways is a critical step in many scientific fields.
In Neuroscience, it is used to understand the brain responses to a stimuli or in Physical Simulations, to stir large systems like a tokamak.


---

The overarching goal of my project is to provide an automated way to process complex physical signals using AI, to be able to easily answer questions about the system that produced them.


#### S4

When looking at recent breakthrough in AI for complex inputs, in particular the technologies that led to ChatGPT for language or Midjourney for vision, they rely on two common ingredients:

---

- First, these models don't process their input directly.
  They transform it as a stream of tokens, which correspond to parts of words for language models or small patches for images. 
  These streams are then processed using transformer architectures, which compute interactions between the tokens.

- The second ingredient is the use of self-supervised pretraining.
  This step allows to capture the distribution of the input by learning to solve some pretext tasks, typically predicting the next token in a stream.

These models are then fine-tuned, to specialize for specific tasks, document summarization or just chatting.


---

In order to apply similar approaches to multivariate signals, various challenges need to be overcome.
First, the notion of tokens for the signals is not well-defined, unlike in language and image applications.
Also, for critical decision making, we need these model to be interpretable, which is not the case with current black-box models.



#### S5

In my project, I propose to view the signals as streams of events: the tokens of the signals are events. But what are events exactly?
They are characterized by their nature and associated with a precise time T.

I consider two types of events:
  - First, observed events, which are recorded with the signal, such as drug injection. Their precise time and nature are known, and they modify the dynamic of the signal. 
  - Then, the latent events. Their time is unknown but can be inferred by locating characteristic patterns they produce in the signal. For example, the beginning of a heartbeat pattern, here framed in white, can be considered as the time associated with a heartbeat event.
  Finding these characteristic patterns and considering their apparition as specific latent events yields punctual representations of the signal, as a stream of events.
<!-- The duality between the recurring patterns and the events allow to transform the continuous signal into a stream of events. -->


#### S6

And this tokenization based on events applies to various other domains.
Characteristic patterns stem from brain responses in neuroscience or the presence of stars and galaxies in astronomical images.
<!-- check astro image? -->
They can also be turned into punctual events by considering the time or place they occur instead of the full extent of the pattern.


An advantage of this tokenization over random patches is that the tokens 
are more compact, as they are selected part of the signal, and they can be interpreted by practitioners, as they have physical meaning.


#### S7

The goal of the E.U.LPS project is to propose new unsupervised methods to characterize physiological signals jointly with observed events, by turning them into stream of events as you understood.

<!-- My approach is to turn them into events' streams and model the events' distribution, similarly to the stream of tokens processed for language models. -->

<!-- The core hypothesis is that the distribution of the events in time and space is much simpler to model than the original signals' distribution. -->

The main challenge, is that unlike language models, the event tokens are not known a priori and need to be identified

<!-- A challenge in this approach is that unlike existing works, the tokens are not known a priori and need to be identified. -->

---

To address this goal, I will focus on three tasks:
- First, considering that we have identified the events, I will develop models able to describe physiological events' distribution.
- Then, building on these models, I will propose methods that can simultaneously extract events from the signal and model their distribution.
- Finally, I will validate these novel signal representations by fine-tuning them to solve specific tasks.

#### S8

In a first work package, I will consider the case where the events have already been identified in the signal, and we want to model their distribution.

I propose to rely on the framework of point processes, which is a classical framework to model the distribution of events in space and time.


Most existing parametric models in this framework are restricted to Markovian kernels, which favor short latencies between events while we would like to capture the longer range interactions of physiological events.


Based on preliminary work published this year in IMCL, I propose a novel inference method that unlocks general models for point processes.
It opens the way to capture more complex interactions between events, such as pseudo-periodicity or thresholding effects, but also spatial dependencies with uncertainty.


#### S9

Then, I will propose joint methods to identify and model events from signals.

To trade off interpretability and expressivity, I will take an approach that goes from dictionary based representations to deep models.

First, I will consider statistical models based on event detection algorithms, such as convolutional dictionary learning or change point detection, and extend them to take into account the distribution of the detected events, leveraging event models from WP1.
The models will be fitted to the data using alternate minimization or bilevel optimization, which I am an expert of.

Then, I will consider the unrolled version of these algorithms to create more expressive deep models that can be trained through self-supervised learning. 
These models are interesting because they remain partially interpretable thanks to the unrolled architecture.
And compared to dictionary based approach, they have the advantage of being more powerful as they can be fine-tuned easily to answer specific questions about the signals.

#### S10

Finally, to validate the proposed representations, I will develop methods that can leverage them to answer machine learning questions about physiological signals.

Let me give you an example.
In general anesthesia, avoiding long alpha suppression phases in the brain allows to reduce the risk of post-operative cognitive impairments.
So we plan to predict such adverse events in real time using the developed representations, to allow the anesthetist to anticipate them.
We will also focus on anomaly detection as well as causal analysis to understand response of the brain to stimuli.

These developments will leverage either the fine-tuning of deep network, or the likelihood for dictionary-based models.



#### S11

To summarize, my project aims at providing new signal processing tools based on events.

This project will benefit from my expertise in core machine learning and signals processing.
It aims to have impact in various domains, in particular the one of GA. It is important to mention that Paris hospital already granted me access to a database of 46 thousands GA recordings which is huge in the domain.

Finally, the tools developed during this project will be disseminated as open source software, relying on my experience in the domain. I am currently maintainer of packages downloaded millions of times a month and creator of software currently gaining traction with more than a thousand download a month.

Thank you very much for your attention, and I am happy to take any question.
