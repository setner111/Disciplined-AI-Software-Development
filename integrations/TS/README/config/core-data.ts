/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

export const CORE_DATA = {
  contextProblem: {
    description: "AI systems work on Question → Answer patterns. When you ask for broad, multi-faceted implementations, you typically get:",
    issues: [
      "Functions that work but lack structure",
      "Repeated code across components",
      "Architectural inconsistency over sessions",
      "Context dilution causing output drift",
      "More debugging time than planning time"
    ]
  },
  howThisWorks: {
    description: "The methodology uses four stages with systematic constraints and validation checkpoints. Each stage builds on empirical data rather than assumptions.",
    principle: "Planning saves debugging time. Planning thoroughly upfront typically prevents days of fixing architectural issues later."
  },
  fourStages: {
    stage1: {
      name: "AI Configuration",
      description: "Set up your AI model's custom instructions using AI-PREFERENCES.md. This establishes behavioral constraints and uncertainty flagging with ⚠️ indicators when the AI lacks certainty."
    },
    stage2: {
      name: "Collaborative Planning",
      description: "Share METHODOLOGY.md with the AI to structure your project plan. Work together to:",
      steps: [
        "Define scope and completion criteria",
        "Identify components and dependencies",
        "Structure phases based on logical progression",
        "Generate systematic tasks with measurable checkpoints"
      ],
      output: "A development plan following dependency chains with modular boundaries."
    },
    stage3: {
      name: "Systematic Implementation",
      description: "Work phase by phase, section by section. Each request follows: \"Can you implement [specific component]?\" with focused objectives.",
      fileSizeConstraint: "File size stays ≤150 lines.",
      benefits: [
        "Smaller context windows for processing",
        "Focused implementation over multi-function attempts",
        "Easier sharing and debugging"
      ],
      implementationFlow: "Request specific component → AI processes → Validate → Benchmark → Continue"
    },
    stage4: {
      name: "Data-Driven Iteration",
      description: "The benchmarking suite (built first) provides performance data throughout development. Feed this data back to the AI for optimization decisions based on measurements rather than guesswork."
    }
  },
  whyThisWorks: {
    decisionProcessing: "AI handles \"Can you do A?\" more reliably than \"Can you do A, B, C, D, E, F, G, H?\"",
    contextManagement: "Small files and bounded problems prevent the AI from juggling multiple concerns simultaneously.",
    empiricalValidation: "Performance data replaces subjective assessment. Decisions come from measurable outcomes.",
    systematicConstraints: "Architectural checkpoints, file size limits, and dependency gates force consistent behavior."
  }
};