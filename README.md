# Covid Decision Making

## Model

A simple computer program (in any language that you want) that decides whether or not it would be best for the government to mandate vaccines.
Takes into account beliefs about the vaccine's efficacy (e.g., number of deaths avoided), beliefs about how a mandate will impact the number
of people that get the vaccine, as well as other information related to utilities (loss/gain of freedom), etc.

The program takes as input a variety of different parameters (such as believes about the probability of a pandemic) and decide whether to recommend that mandate based on the parameters input to it. To do this, we find the deaths, sicknesses, and freedom affect by each possible combination of actions and states and then find the given utility. This is done by weighing deaths, sicknesses and loss of freedom (as described below).

We then weigh the utility given the belief probability and find that the best action to take (given our believes of the world) to be to mandate vaccines. This can be seen in the final table below, which shows that the highest possible weighed utility (with probability factored in) would be to assume we are in a deadly pandemic and would be maximizing utility with a mandate.

### Actions

- Vaccine mandate
- No vaccine mandate

### States

- Deadly pandemic
- Non-deadly pandemic
- No Pandemic

### Belief

- Is there a pandemic? (p = .9)
- If there is a pandemic, is it deadly? (p = .7)
- Vaccine mandates affect personal freedom (resistance to authority)

### Consequences

- Deaths
- Sickness
- Freedom

### Goals

- Health
- Freedom

### Utilities

| Consequence        | Utility |
| ------------------ | ------- |
| Death              | -200    |
| Sickness           | -10     |
| Vaccine Mandate    | -100    |
| No Vaccine Mandate | 100     |

### Actions and States that map to consequences:

|                         | Mandate                                                   | No mandate                                               |
| ----------------------- | --------------------------------------------------------- | -------------------------------------------------------- |
| **No pandemic**         | 2 deaths per 1000, 5 sick per 1000, No freedom to choose  | 2 deaths per 1000, 5 sick per 1000, Freedom to choose    |
| **Non-Deadly pandemic** | 3 deaths per 1000, 70 sick per 1000, No freedom to choose | 3 deaths per 1000, 100 sick per 1000, Freedom to choose  |
| **Deadly pandemic**     | 5 deaths per 1000, 70 sick per 1000, No freedom to choose | 25 deaths per 1000, 100 sick per 1000, Freedom to choose |

### Utility with probability:

|                         | Mandate | No mandate |
| ----------------------- | ------- | ---------- |
| **No pandemic**         | -54999  | -34999     |
| **Non-Deadly pandemic** | -4666   | -4999      |
| **Deadly pandemic**     | -2571   | -8428      |
