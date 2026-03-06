# Rules & Axes

This document explains how to add philosophical rules and score them on the conceptual axes.

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

### Conflict Orientation
**How does the rule approach conflict and disagreement?**

- **-1.0** = **Collaborative** - Seeks consensus, avoids confrontation
- **-0.5** = **Diplomatic** - Prefers negotiation over direct conflict
- **0.0** = **Strategic** - Treats conflict as a tool to be managed
- **0.5** = **Competitive** - Engages in controlled conflict
- **1.0** = **Dominant** - Uses force, intimidation, or overwhelming pressure

**Examples:**
- Gandhi's nonviolence = -1.0 (avoids conflict entirely)
- Trump's negotiation = 1.0 (uses overwhelming pressure)
- Sun Tzu's strategy = 0.0 (conflict as a calculated tool)

### Truth Orientation
**How does the rule treat truth and reality?**

- **-1.0** = **Subjective** - Truth is determined by personal belief or perspective
- **-0.5** = **Relativistic** - Multiple valid truths exist, context-dependent
- **0.0** = **Pluralistic** - Multiple valid truths coexist
- **0.5** = **Pragmatic** - Truth serves practical outcomes
- **1.0** = **Objective** - Single discoverable reality exists independently

**Examples:**
- Nietzsche's will to power = -1.0 (creates own values/truth)
- Einstein's science = 1.0 (objective reality exists)
- Confucius's harmony = 0.0 (multiple truths for different contexts)

### Order Orientation
**How does the rule approach structure and systems?**

- **-1.0** = **Structured** - Follows established systems, hierarchies, and traditions
- **-0.5** = **Organized** - Creates order through planning and coordination
- **0.0** = **Balanced** - Mixes structure and flexibility as needed
- **0.5** = **Adaptive** - Adjusts structure based on circumstances
- **1.0** = **Improvised** - Creates order spontaneously, rejects rigid structures

**Examples:**
- Confucius = -1.0 (strict hierarchical order)
- Bruce Lee = 1.0 (fluid, improvised approach)
- Marcus Aurelius = 0.0 (balanced inner/outer order)

### Will Direction
**Where does the rule direct effort and energy?**

- **-1.0** = **Inward** - Focuses on self-discipline, internal change
- **-0.5** = **Reflective** - Balances internal and external focus
- **0.0** = **Integrated** - Coordinates internal and external efforts
- **0.5** = **Expressive** - Projects will outward into the world
- **1.0** = **Outward** - Seeks to change external conditions and others

**Examples:**
- Epictetus = -1.0 (master internal judgments)
- Muhammad Ali = 1.0 (project confidence outward)
- Buffett = 0.0 (balanced internal discipline with external action)

### Risk Tolerance
**How does the rule handle uncertainty and risk?**

- **-1.0** = **Risk-Averse** - Minimizes exposure, seeks security
- **-0.5** = **Cautious** - Prefers known paths, limits downside
- **0.0** = **Calculated** - Takes risks when expected return justifies
- **0.5** = **Opportunistic** - Seeks favorable risk/reward opportunities
- **1.0** = **Risk-Seeking** - Embraces uncertainty, high-risk/high-reward approach

**Examples:**
- Buffett = -1.0 (minimizes risk through patience)
- Musk = 1.0 (embraces extreme risks for breakthrough)
- Marcus Aurelius = -0.5 (cautious about what can't be controlled)

### Time Horizon
**What time frame does the rule prioritize?**

- **-1.0** = **Short-Term** - Focuses on immediate results and present moment
- **-0.5** = **Reactive** - Responds to current conditions, limited future planning
- **0.0** = **Present-Balanced** - Balances immediate needs with future considerations
- **0.5** = **Strategic** - Plans for medium-term outcomes and positioning
- **1.0** = **Long-Term** - Prioritizes future benefits, compounding effects, legacy

**Examples:**
- Trump = -1.0 (immediate wins, short-term focus)
- Buffett = 1.0 (long-term compounding, patience)
- Bruce Lee = 0.0 (present-focused adaptability)

## Adding New Rules

1. **Choose a unique ID** - Use lowercase, underscores instead of spaces
2. **Score all 6 axes** - Be consistent with the scale definitions above
3. **Add relationships** - Connect to existing rules using the `relationships` array
4. **Test the result** - Run `python scripts/render_graph.py` to see positioning

## Relationship Types

- **support** - One philosophy supports or reinforces another
- **oppose** - Philosophies are fundamentally incompatible or in conflict
- **similar** - Philosophies share core principles or approaches
- **contextual** - Relationship depends on specific circumstances

## Tips for Consistent Scoring

- **Compare with existing rules** - Look at similar philosophies before scoring
- **Consider the extremes** - Use the full -1 to 1 scale meaningfully
- **Think in spectra** - Each axis represents a spectrum, not just binary choices
- **Test with visualization** - The graph will reveal if your scoring makes sense philosophically
