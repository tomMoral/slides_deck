
## EULPS - E.U.LPS.

Hello everyone, it is my pleasure to present my project proposal E.U.LPS.

#### S2

Imagine you enter an Operating Room for a surgery under General Anesthesia.

The anesthetist won't just put you to sleep. He will monitor your status to ensure that your condition remains stable: your heart, your brain and others.
These signals are complex and hard to interpret.
That is why many indicators have been developed to support decisions.

Yet, they are an instantaneous snapshot of the patient's condition at time T,they don't allow to anticipate what is going to happen, but only react to status changes.

<!-- In order to propose personalized and predictive indicators to summarize the signal, AI is a powerful approach. -->


#### S3

Summarizing lage scale multivariate signals in predictive ways is a critical step in many pipelines.
In Neuroscience, it is used to understand the brain responses to a stimuli or in Physical simulations, to stir large physical systems like a tokamak.


---

The overarching goal of my project is to provide an automated way to summarize complex physical signals using AI, to be able to easily answer questions about the system that produced them.


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
Also, for critical decision making, we need these model to be interpretable, unlike current black-box models.



#### S5

In my project, I propose to view the signals as streams of events: the tokens are events. But what are these events exactly?
They are represented by a precise time T and the nature of the event.

I consider two types of events:
  - First, observed events such as drug injection. They modify the dynamic of the signal. Their precise time and nature are known.
  - Then, the underlying events. Their time is unknown but can be inferred by locating characteristic patterns they produce in the signal. For example, the beginning of a heartbeat pattern can be considered as the time associated to this heartbeat event.
  Finding these characteristic patterns and considering their apparition as specific underlying events yields punctual representations of the signal, as a stream of events.
<!-- The duality between the recurring patterns and the events allow to transform the continuous signal into a stream of events. -->


#### S6

And this tokenization based on events applies to many other domains.
Characteristic patterns stem from brain responses in neuroscience or the presence of stars and galaxies in astronomical images.
<!-- check astro image? -->
They can also be turned into punctual events by considering the time or place they occur instead of the full extent of the pattern.


An advantage of these events over random patches is that they can be interpreted by practitioners, as they have physical meaning.


#### S7

The goal of the E.U.LPS project is to propose new unsupervised methods to summarize physiological signals jointly with observed events.

My approach is to turn them into events' streams and model the events' distribution, similarly to the stream of tokens processed for language models.

The core hypothesis is that the distribution of the events in time and space is much simpler to model than the original signals' distribution.

A challenge in this approach is that unlike existing works, the tokens are not known a priori and need to be identified.

---

To tackle this goal, I will focus on three tasks:
- First, considering that we have identified the events, I will develop models able to describe physiological events' distribution.
- Then, building on these models, I will propose methods that can simultaneously extract events from the signal and model their distribution.
- Finally, I will propose some fine-tuning methods to leverage these novel signal descriptions and tackle specific tasks.

#### S8

In a first work package, I will consider the case where the events have already been identified in the signal, and we want to model their distribution.

I propose to rely on the framework of point processes, which is a classical framework to model the distribution of events in space and time.


Most existing parametric models in this framework are restricted to Markovian kernels, which favor short latencies between events while we would like to capture the longer range interactions of physiological events.

Based on preliminary work published this year in IMCL, we propose a novel inference framework that unlocks more general models for point processes.
It opens the way to develop more complex interaction models between events, such as pseudo-periodicity or thresholding effects, but also spatial dependencies with uncertainty.


#### S9

Then, I will propose joint methods to identify and model events from signals.

To trade off interpretability and expressivity, I will take an approach that goes from dictionary based representations to deep models.

First, I will consider statistical models based on event detection algorithms, such as convolutional dictionary learning or change point detection, and extend them to take into account the distribution of the detected events, leveraging event models from WP1.
The models will be fitted to the data using alternate minimization or bilevel optimization, which I am an expert of.

Then, I will consider the unrolled version of these algorithms to create more expressive deep models that can be trained through self-supervised learning. 
These models are interesting because they remain partially interpretable thanks to the unrolled architecture.
And compared to dictionary based approach, they have the advantage of being more powerful as they can be fine-tuned easily for specific tasks.

#### S10

Finally, to validate the proposed representations, I will develop methods that can leverage them to answer machine learning questions about physiological signals.

Let me give you an example.
In general anesthesia, avoiding long alpha suppression phases in the brain allows to reduce the risk of post-operative cognitive impairments.
So we plan to detect such adverse events in real time using the developed representations.
We will also focus on anomaly detection as well as causal analysis to understand response of the brain to stimuli.

These developments will leverage either the fine-tuning of deep network, or the likelihood for dictionary-based models.



#### S11

To summarize, my project aims at providing new signal processing tools based on events.

This project will benefit from my expertise in core machine learning and signals processing.
It aims to have impact in various domains, in particular the one of GA. It is important to mention that Paris hospital already granted me access to a database of 46 thousands GA recordings which is huge in the domain.

Finally, the tools developed during this project will be disseminated as open source software, relying on my experience in the domain. I am currently maintainer of packages downloaded millions of times a month and creator of software currently gaining traction with more than a thousand download a month.

Thank you very much for your attention, and I am happy to take any question.
