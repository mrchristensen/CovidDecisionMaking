# CovidDescisionMaking

## Model
A simple computer program (in any language that you want) that decides whether or not it would be best for the goverment to mandate vaccines.
Takes into account beliefs about the vaccine's efficacy (e.g., number of deaths avoided), beliefs about how a mandate will impact the number
of people that get the vaccine, as well as other information related to utilities (loss/gain of freedom), etc.
Ideally, the program takes as input a variety of different parameters and decide whether to recommend that mandate based on the parameters input to it.

### Actions
- Vaccine mandate
- No vaccine mandate

### States
- Deadly pandemic
- Non-deadly pandemic
- Fake news


### Belief
- How deadly it is

### Consequences
- Deaths
- Sickness
- Freedom

### Goals
- Health
- Freedom

### Utilities
-

Actions and States that map to consiquences:
| | Mandate | No mandate |
| --- | --- | --- |
| **No pandemic** |  deaths per 1000, X sick per 1000, No freedom to choose |  deaths per 1000, X sick per 1000, Freedom to choose |
| **Non-Deadly pandemic** |  deaths per 1000, X sick per 1000, No freedom to choose |  deaths per 1000, X sick per 1000, Freedom to choose |
| **Deadly pandemic** | 3 deaths per 1000, X sick per 1000, No freedom to choose | 5 deaths per 1000, X sick per 1000, Freedom to choose |
