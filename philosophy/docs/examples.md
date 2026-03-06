# Examples & Patterns

This document provides sample philosophical rules and common patterns to help you get started with adding your own rules.

## Sample Rules

### Classical Philosophers

#### Socrates - The Socratic Method
```json
{
  "id": "socrates",
  "name": "Socrates",
  "rule": "Question Everything",
  "axes": {
    "conflict": -0.3,
    "truth": 1,
    "order": 0.2,
    "will": -0.5,
    "risk": 0.3,
    "time": 0.5
  },
  "whenWorks": "When seeking deeper understanding through dialogue.",
  "whenFails": "When immediate action is required or time is limited.",
  "relationships": [
    {"target": "plato", "type": "support"}
  ],
  "influenceWeight": 0.95,
  "notes": "Use systematic questioning to examine beliefs and expose contradictions."
}
```

#### Aristotle - Virtue Ethics
```json
{
  "id": "aristotle",
  "name": "Aristotle",
  "rule": "Golden Mean",
  "axes": {
    "conflict": -0.7,
    "truth": 0.8,
    "order": 0.9,
    "will": -0.3,
    "risk": -0.4,
    "time": 0.6
  },
  "whenWorks": "When seeking balanced, sustainable approaches to life.",
  "whenFails": "In crisis situations requiring decisive action.",
  "relationships": [
    {"target": "plato", "type": "support"},
    {"target": "epictetus", "type": "similar"}
  ],
  "influenceWeight": 0.9,
  "notes": "Virtue lies in finding the balance between extremes."
}
```

### Modern Thinkers

#### Jordan Peterson - Order From Chaos
```json
{
  "id": "peterson",
  "name": "Jordan Peterson",
  "rule": "Clean Your Room",
  "axes": {
    "conflict": -0.2,
    "truth": 0.7,
    "order": 0.8,
    "will": -0.6,
    "risk": -0.3,
    "time": 0.4
  },
  "whenWorks": "When personal responsibility and meaningful action are possible.",
  "whenFails": "When systemic issues require collective action.",
  "relationships": [
    {"target": "nietzsche", "type": "oppose"}
  ],
  "influenceWeight": 0.75,
  "notes": "Take responsibility for your immediate sphere of influence before seeking broader change."
}
```

#### Naval Ravikant - Leverage and Specific Knowledge
```json
{
  "id": "naval",
  "name": "Naval Ravikant",
  "rule": "Specific Knowledge Beats General",
  "axes": {
    "conflict": -0.4,
    "truth": 0.9,
    "order": 0.3,
    "will": -0.7,
    "risk": 0.2,
    "time": 0.8
  },
  "whenWorks": "When deep expertise in a specific domain creates value.",
  "whenFails": "When broad generalist skills are needed.",
  "relationships": [
    {"target": "buffett", "type": "similar"}
  ],
  "influenceWeight": 0.8,
  "notes": "Escape competition through specific, valuable knowledge."
}
```

### Contemporary Figures

#### Taylor Swift - Reputation Management
```json
{
  "id": "taylor_swift",
  "name": "Taylor Swift",
  "rule": "Control the Narrative",
  "axes": {
    "conflict": 0.6,
    "truth": -0.2,
    "order": 0.7,
    "will": 0.8,
    "risk": 0.5,
    "time": -0.3
  },
  "whenWorks": "When public perception and media presence matter.",
  "whenFails": "When authenticity and genuine connection are required.",
  "relationships": [],
  "influenceWeight": 0.7,
  "notes": "Strategic communication and reputation management through storytelling."
}
```

## Common Patterns

### The Stoic Pattern
Rules focused on internal discipline and accepting what cannot be controlled:

```json
{
  "axes": {
    "conflict": -0.3,
    "truth": 0.6,
    "order": 0.8,
    "will": 0,
    "risk": -0.6,
    "time": 0.5
  }
}
```

**Examples**: Marcus Aurelius, Epictetus

### The Pragmatic Pattern
Rules focused on practical outcomes and what works:

```json
{
  "axes": {
    "conflict": 0,
    "truth": 0.5,
    "order": 0.2,
    "will": 0,
    "risk": 0,
    "time": 0
  }
}
```

**Examples**: Sun Tzu, Machiavelli

### The Disruptive Pattern
Rules focused on breaking existing structures and creating new values:

```json
{
  "axes": {
    "conflict": 0.8,
    "truth": -0.7,
    "order": 0.5,
    "will": -1,
    "risk": 0.9,
    "time": 0.3
  }
}
```

**Examples**: Nietzsche, Trump

### The Collaborative Pattern
Rules focused on harmony and avoiding conflict:

```json
{
  "axes": {
    "conflict": -0.8,
    "truth": 0.8,
    "order": -0.5,
    "will": 0.8,
    "risk": -0.3,
    "time": 0.7
  }
}
```

**Examples**: Gandhi, MLK

### The Innovation Pattern
Rules focused on breakthrough thinking and high-risk approaches:

```json
{
  "axes": {
    "conflict": 0.4,
    "truth": 0.6,
    "order": -0.2,
    "will": -0.6,
    "risk": 1,
    "time": 0.9
  }
}
```

**Examples**: Musk, Einstein

## Relationship Patterns

### Teacher-Student
```json
{"target": "student_id", "type": "support"}
```

### Complementary Philosophies
```json
{"target": "complement_id", "type": "similar"}
```

### Direct Opposition
```json
{"target": "opponent_id", "type": "oppose"}
```

## Scoring Tips

### Comparative Scoring
When adding a new rule, compare it to existing similar philosophies:

1. **Find 2-3 similar rules** in the existing dataset
2. **Score your rule relative to them**
3. **Check the visualization** to ensure it makes sense

### Consistency Checks
- **Conflict axis**: Collaborative rules should have negative scores, dominant rules positive
- **Truth axis**: Scientific approaches should trend positive, postmodern approaches negative
- **Time axis**: Long-term thinkers should have positive scores, reactive thinkers negative

### Edge Cases
- **Extreme scores**: Use -1 or 1 sparingly for truly exceptional cases
- **Balanced scores**: Most rules should cluster around 0 on most axes
- **Influence weights**: Reserve 0.9+ for historically transformative figures

## Adding Your First Rule

1. **Start simple** - Choose a clear, well-known philosophy
2. **Research thoroughly** - Understand the core principles and context
3. **Score conservatively** - Use moderate scores initially, adjust based on visualization
4. **Add relationships** - Connect to 2-3 existing philosophies
5. **Test and iterate** - Run the visualization and adjust as needed

## Common Mistakes to Avoid

1. **Inconsistent scoring** - Mixing up the direction of axes
2. **Missing relationships** - Forgetting to connect similar philosophies
3. **Extreme influence weights** - Giving new rules too much importance
4. **Vague descriptions** - Notes should be specific and helpful
5. **Ignoring the spectrum** - Treating axes as binary instead of continuous

Remember: The goal is to create meaningful philosophical comparisons, not to "win" the scoring.
