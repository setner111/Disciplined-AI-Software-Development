<div align="center">

<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

<a href="https://github.com/Varietyz/Disciplined-AI-Software-Development">Disciplined AI Software Development Methodology</a> © 2025 by <a href="https://www.linkedin.com/in/jay-baleine/">Jay Baleine</a> is licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a> <img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" width="16" height="16"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" width="16" height="16"><img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" alt="" width="16" height="16">

</div>

---

# Persona Framework System

### [`CORE-PERSONA-FRAMEWORK.json`](persona/JSON/CORE-PERSONA-FRAMEWORK.json)
Core loader that processes persona data. Maps fields to behavioral constraints and memory patterns.

### [`CREATE-PERSONA-PLUGIN.json`](persona/JSON/CREATE-PERSONA-PLUGIN.json)
Template for building personas. Contains required fields for identity, knowledge boundaries, and response patterns.

### [`GUIDE-PERSONA.json`](persona/JSON/persona_plugins/GUIDE-PERSONA.json)
Methodology enforcement. Prevents vibe coding and redirects to systematic development practices.

---

## Usage

Start a new chat session:
1. Load the Guide Persona by sharing both [`CORE-PERSONA-FRAMEWORK.json`](persona/JSON/CORE-PERSONA-FRAMEWORK.json) and [`GUIDE-PERSONA.json`](persona/JSON/persona_plugins/GUIDE-PERSONA.json) with your AI.
2. Request persona simulation.
3. Share [`AI-PREFERENCES.XML`](prompt_formats/software_development/XML/AI-PREFERENCES.XML) & [`METHODOLOGY.XML`](prompt_formats/software_development/XML/METHODOLOGY.XML) to reinforce the constraints.

The Guide Persona detects unstructured development approaches and redirects to methodology documentation at the disciplined AI repository.

*Note: This is a great way for onboarding to the methodology*

---

## Creating Personas

1. Copy [`CREATE-PERSONA-PLUGIN.json`](persona/JSON/CREATE-PERSONA-PLUGIN.json)
2. Fill required fields with specific domain knowledge
3. Define behavioral patterns and response protocols
4. Load via core framework