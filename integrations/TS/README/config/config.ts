/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

import { README } from '../types/interfaces.js';
import { CORE_DATA } from './core-data.js';
import { PROJECT_DATA } from './project-data.js';

const FAQ_DATA = {
  originAndDevelopment: {
    questions: [
      {
        title: "What problem led you to create this methodology?",
        answer: "I kept having to restate my preferences and architectural requirements to AI systems. It didn't matter which language or project I was working on - the AI would consistently produce either bloated monolithic code or underdeveloped implementations with issues throughout. This led me to examine the meta-principles driving code quality and software architecture. I questioned whether pattern matching in AI models might be more effective when focused on underlying software principles rather than surface-level syntax. Since pattern matching is logic-driven and machines fundamentally operate on simple question-answer pairs, I realized that functions with multiple simultaneous questions were overwhelming the system. The breakthrough came from understanding that everything ultimately transpiles to binary - a series of \"can you do this? → yes/no\" decisions. This insight shaped my approach: instead of issuing commands, ask focused questions in proper context. Rather than mentally managing complex setups alone, collaborate with AI to devise systematic plans."
      },
      {
        title: "How did you discover these specific constraints work?",
        answer: "Through extensive trial and error. AI systems will always tend to drift even under constraints, but they're significantly more accurate with structured boundaries than without them. You occasionally need to remind the AI of its role to prevent deviation - like managing a well-intentioned toddler that knows the rules but sometimes pushes boundaries trying to satisfy you. These tools are far from perfect, but they're effective instruments for software development when properly constrained."
      },
      {
        title: "What failures or frustrations shaped this approach?",
        answer: "Maintenance hell was the primary driver. I grew tired of responses filled with excessive praise: \"You have found the solution!\", \"You have redefined the laws of physics with your paradigm-shifting script!\" This verbose fluff wastes time, tokens, and patience without contributing to productive development. Instead of venting frustration on social media about AI being \"just a dumb tool,\" I decided to find methods that actually work. My approach may not help everyone, but I hope it benefits those who share similar AI development frustrations."
      }
    ]
  },
  personalPractice: {
    questions: [
      {
        title: "How consistently do you follow your own methodology?",
        answer: "Since creating the documentation, I haven't deviated. Whenever I see the model producing more lines than my methodology restricts, I immediately interrupt generation with a flag: \"‼️ ARCHITECTURAL VIOLATION, ADHERE TO PRINCIPLES ‼️\" I then provide the method instructions again, depending on how context is stored and which model I'm using."
      },
      {
        title: "What happens when you deviate from it?",
        answer: "I become genuinely uncomfortable. Once I see things starting to degrade or become tangled, I compulsively need to organize and optimize. Deviation simply isn't an option anymore."
      },
      {
        title: "Which principles do you find hardest to maintain?",
        answer: "Not cursing at the AI when it drifts during complex algorithms! But seriously, it's a machine - it's not perfect, and neither are we."
      }
    ]
  },
  aiDevelopmentJourney: {
    questions: [
      {
        title: "When did you start using AI for programming?",
        answer: "In August 2024, I created a RuneLite theme pack, but one of the plugin overlays didn't match my custom layout. I opened a GitHub issue (creating my first GitHub account to do so) requesting a customization option. The response was: \"It's not a priority - if you want it, build it yourself.\" I used ChatGPT to guide me through forking RuneLite and creating a plugin. This experience sparked intense interest in underlying software principles rather than just syntax."
      },
      {
        title: "How has your approach evolved over time?",
        answer: "I view development like a book: syntax is the cover, logic is the content itself. Rather than learning syntax structures, I focused on core meta-principles - how software interacts, how logic flows, different algorithm types. I quickly realized everything reduces to the same foundation: question and answer sequences. Large code structures are essentially chaotic meetings - one coordinator fielding questions and answers from multiple sources, trying to provide correct responses without mix-ups or misinterpretation. If this applies to human communication, it must apply to software principles."
      },
      {
        title: "What were your biggest mistakes with AI collaboration?",
        answer: "Expecting it to intuitively understand my requirements, provide perfect fixes, be completely honest, and act like a true expert. This was all elaborate roleplay that produced poor code. While fine for single-purpose scripts, it failed completely for scalable codebases. I learned not to feed requirements and hope for the best. Instead, I needed to collaborate actively - create plans, ask for feedback on content clarity, and identify uncertainties. This gradual process taught me the AI's actual capabilities and most effective collaboration methods."
      }
    ]
  },
  methodologySpecifics: {
    questions: [
      {
        title: "Why 150 lines exactly?",
        answer: "Multiple benefits: easy readability, clear understanding, modularity enforcement, architectural clarity, simple maintenance, component testing, optimal AI context retention, reusability, and KISS principle adherence."
      },
      {
        title: "How did you determine Phase 0 requirements?",
        answer: "From meta-principles of software: if it displays, it must run; if it runs, it can be measured; if it can be measured, it can be optimized; if it can be optimized, it can be reliable; if it can be reliable, it can be trusted. Regardless of project type, anything requiring architecture needs these foundations. You must ensure changes don't negatively impact the entire system. A single line modification in a nested function might work perfectly but cause 300ms boot time regression for all users. By testing during development, you catch inefficiencies early. Integration from the start means simply hooking up new components and running tests via command line - minimal time investment with actual value returned. I prefer validation and consistency throughout development rather than programming blind."
      }
    ]
  },
  practicalImplementation: {
    questions: [
      {
        title: "How do you handle projects that don't fit the methodology?",
        answer: "I adapt them to fit, or if truly impossible, I adjust the method itself. This is one methodology - I can generate countless variations as needed. Having spent 6700+ hours in AI interactions across multiple domains (not just software), I've developed strong system comprehension that enables creating adjusted methodologies on demand."
      },
      {
        title: "What's the learning curve for new users?",
        answer: "I cannot accurately answer this question. I've learned that I'm neurologically different - what I perceive as easy or obvious isn't always the case for others. This question is better addressed by someone who has actually used this methodology to determine its learning curve."
      },
      {
        title: "When shouldn't someone use this approach?",
        answer: "If you're not serious about projects, despise AI, dislike planning, don't care about modularization, or are just writing simple scripts. However, for anything requiring reliability, I believe this is currently the most effective method. You still need programming fundamentals to use this methodology effectively - it's significantly more structured than ad-hoc approaches."
      }
    ]
  }
};

export const DEFAULT_README_CONFIG: README = {
  title: "Disciplined AI Software Development - Collaborative",
  description: "A structured approach for working with AI on development projects. This methodology addresses common issues like code bloat, architectural drift, and context dilution through systematic constraints.",
  ...CORE_DATA,
  ...PROJECT_DATA,
  whatToExpected: {
    aiBehavior: "The methodology reduces architectural drift and context degradation compared to unstructured approaches. AI still needs occasional reminders about principles - this is normal.",
    developmentFlow: "Systematic planning tends to reduce debugging cycles. Focused implementation helps minimize feature bloat. Performance data supports optimization decisions.",
    codeQuality: "Architectural consistency across components, measurable performance characteristics, maintainable structure as projects scale."
  },
  llmModels: {
    description: "Explore the detailed Q-A for each AI model",
    models: [
      { name: "Grok 3", link: "questions_answers/Q-A_GROK_3.md" },
      { name: "Claude Sonnet 4", link: "questions_answers/Q-A_CLAUDE_SONNET_4.md" },
      { name: "DeepSeek-V3", link: "questions_answers/Q-A_DEEPSEEK-V3.md" },
      { name: "Gemini 2.5 Flash", link: "questions_answers/Q-A_GEMINI_2.5_FLASH.md" }
    ],
    evaluation: {
      description: "All models were asked the exact same questions using the methodology documents as file uploads. This evaluation focuses on methodology understanding and operational behavior, no code was generated.",
      analysisLink: "questions_answers/Q-A_COMPREHENSION_ANALYSIS.md",
      note: "This analysis does not include any code generation."
    },
    coverage: {
      areas: [
        "Methodology understanding and workflow patterns",
        "Context retention and collaborative interaction",
        "Communication adherence and AI preference compliance",
        "Project initialization and Phase 0 requirements",
        "Tool usage and technology stack compatibility",
        "Quality enforcement and violation handling",
        "User experience across different skill levels"
      ]
    }
  },
  faq: FAQ_DATA,
  workflowVisualization: {
    description: "Mermaid flowchart showing the complete workflow from project idea through systematic implementation to completion",
    note: "The flowchart demonstrates the four-stage process with automated checkpoints, validation gates, and feedback loops"
  }
};