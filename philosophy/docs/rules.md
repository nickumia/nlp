# Rules & Axes

This document explains how to add philosophical rules and score them on the 6 conceptual axes.

## Rule Structure

Each philosophical rule follows this JSON structure:

```json
{
  "id": "unique_identifier",
  "name": "Person's Name",
  "rule": "Name of the Rule",
  "axes": {
    "conflict": -1.0,
    "truth": 1.0,
    "order": -0.5,
    "will": 1.0,
    "risk": 0.4,
    "time": 0.8
  },
  "whenWorks": "When this approach is effective",
  "whenFails": "When this approach fails",
  "relationships": [
    {"target": "other_rule_id", "type": "support|oppose|similar|contextual"}
  ],
  "influenceWeight": 0.9,
  "notes": "Detailed description or context"
}
```

## Core Axes (Quantified)

All axes use a **-1 to 1 scale** unless otherwise noted.

| Axis | Question | -1.0 (Min) | 1.0 (Max) |
|-------|----------|------------|------------|
| **Conflict** | How does the rule approach conflict and disagreement? | Collaborative | Dominant |
| **Truth** | How does the rule treat truth and reality? | Subjective | Objective |
| **Order** | How does the rule approach structure and systems? | Structured | Improvised |
| **Will** | Where does the rule direct effort and energy? | Inward | Outward |
| **Risk** | How does the rule handle uncertainty and risk? | Risk-Averse | Risk-Seeking |
| **Time** | What time frame does the rule prioritize? | Short-Term | Long-Term |

## Detailed Scoring Guide

| Score | Axis | Approach | Description |
|-------|------|----------|-----------|
| **-1.0** | Conflict | Collaborative | Seeks consensus, avoids confrontation, prioritizes harmony |
| **-0.5** | Conflict | Diplomatic | Prefers negotiation over direct conflict, uses strategic engagement |
| **0.0** | Conflict | Strategic | Treats conflict as a tool to be managed, calculates costs/benefits |
| **0.5** | Conflict | Competitive | Engages in controlled conflict, seeks advantage through competition |
| **1.0** | Conflict | Dominant | Uses force, intimidation, or overwhelming pressure to achieve goals |
||||
| **-1.0** | Truth | Subjective | Truth determined by personal belief, intuition, or inner conviction |
| **-0.5** | Truth | Relativistic | Multiple valid truths exist, truth depends on context or perspective |
| **0.0** | Truth | Pragmatic | Truth serves practical outcomes and real-world effectiveness |
| **0.5** | Truth | Empirical | Truth based on observable evidence and data |
| **1.0** | Truth | Objective | Truth exists independently of personal beliefs or perspectives |
||||
| **-1.0** | Order | Structured | Follows established systems, hierarchies, and traditions |
| **-0.5** | Order | Organized | Creates order through planning and coordination |
| **0.0** | Order | Balanced | Mixes structure and flexibility as needed |
| **0.5** | Order | Adaptive | Adjusts structure based on circumstances |
| **1.0** | Order | Improvised | Creates order spontaneously, rejects rigid structures |
||||
| **-1.0** | Will | Inward | Focuses on self-discipline, internal change, and personal development |
| **-0.5** | Will | Reflective | Balances internal and external focus, considers multiple perspectives |
| **0.0** | Will | Integrated | Coordinates internal and external efforts, seeks harmony |
| **0.5** | Will | Expressive | Projects will outward into the world, seeks to change others |
| **1.0** | Will | Outward | Seeks to change external conditions and other people |
||||
| **-1.0** | Risk | Risk-Averse | Minimizes exposure, seeks security, prefers known paths |
| **-0.5** | Risk | Cautious | Prefers known approaches, limits downside, careful planning |
| **0.0** | Risk | Calculated | Takes risks when expected return justifies |
| **0.5** | Risk | Opportunistic | Seeks favorable risk/reward opportunities |
| **1.0** | Risk | Risk-Seeking | Embraces uncertainty, high-risk/high-reward approach |
||||
| **-1.0** | Time | Short-Term | Focuses on immediate results and present moment |
| **-0.5** | Time | Reactive | Responds to current conditions, limited future planning |
| **0.0** | Time | Present-Balanced | Balances immediate needs with future considerations |
| **0.5** | Time | Strategic | Plans for medium-term outcomes and positioning |
| **1.0** | Time | Long-Term | Prioritizes future benefits, compounding effects, legacy |

## Adding New Rules

1. **Choose a unique ID** - Use lowercase, underscores instead of spaces
2. **Score all 6 axes** - Be consistent with the scale definitions above
3. **Add relationships** - Connect to existing rules using the `relationships` array
4. **Test the result** - Run `python scripts/render_graph.py` to see positioning

## Relationship Types

| Type | Description |
|-------|-----------|
| **support** | One philosophy supports or reinforces another |
| **oppose** | Philosophies are fundamentally incompatible or in conflict |
| **similar** | Philosophies share core principles or approaches |
| **contextual** | Relationship depends on specific circumstances |

## Tips for Consistent Scoring

- **Compare with existing rules** - Look at similar philosophies before scoring
- **Consider the extremes** - Use the full -1 to 1 scale meaningfully
- **Think in spectra** - Each axis represents a spectrum, not just binary choices
- **Test with visualization** - The graph will reveal if your scoring makes sense philosophically

## Common Scoring Patterns

| Pattern | Typical Scores | Examples |
|---------|----------------|----------|
| **Stoic** | conflict: -0.3, truth: 0.6, order: 0.8, will: 0, risk: -0.6, time: 0.5 | Marcus Aurelius, Epictetus |
| **Pragmatic** | conflict: 0, truth: 0.5, order: 0.2, will: 0, risk: 0, time: 0 | Sun Tzu, Machiavelli |
| **Collaborative** | conflict: -0.8, truth: 0.9, order: -0.3, will: 0.8, risk: 0.4, time: 0.7 | Gandhi, MLK |
| **Dominant** | conflict: 0.8, truth: 0.3, order: 0.6, will: -1, risk: 0.8, time: -0.2 | Trump, Nietzsche |
| **Balanced** | conflict: 0, truth: 0.5, order: 0, will: 0, risk: 0, time: 0 | Bruce Lee |
| **Innovative** | conflict: 0.4, truth: 0.6, order: -0.2, will: -0.6, risk: 1, time: 0.9 | Musk, Einstein |
