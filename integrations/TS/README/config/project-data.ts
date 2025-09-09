/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

export const PROJECT_DATA = {
  exampleProjects: {
    projects: [
      {
        name: "Discord Bot Template",
        url: "https://github.com/Varietyz/discord-js-bot-template",
        description: "Production-ready bot foundation with plugin architecture, security, API management, and comprehensive testing. 46 files, all under 150 lines, with benchmarking suite and automated compliance checking.",
        structureLink: "example_project_structures/DISCORDJS_TEMPLATE_PROJECT.md"
      },
      {
        name: "PhiCode Runtime",
        url: "https://github.com/Varietyz/phicode-runtime",
        description: "Programming language runtime engine with transpilation, caching, security validation, and Rust acceleration. Complex system maintaining architectural discipline across 70+ modules.",
        structureLink: "example_project_structures/PHICODE_RUNTIME_PROJECT.md"
      },
      {
        name: "PhiPipe",
        url: "https://github.com/Varietyz/PhiPipe",
        description: "CI/CD regression detection system with statistical analysis, GitHub integration, and concurrent processing. Go-based service handling performance baselines and automated regression alerts.",
        structureLink: "example_project_structures/PHIPIPE_PROJECT.md"
      }
    ],
    note: "You can compare the methodology principles to the codebase structure to see how the approach translates to working code."
  },
  implementationSteps: {
    setup: {
      steps: [
        "Configure AI with AI-PREFERENCES.md as custom instructions",
        "Share METHODOLOGY.md for planning session",
        "Collaborate on project structure and phases",
        "Generate systematic development plan"
      ]
    },
    execution: {
      steps: [
        "Build Phase 0 benchmarking infrastructure first",
        "Work through phases sequentially",
        "Implement one component per interaction",
        "Run benchmarks and share results with AI",
        "Validate architectural compliance continuously"
      ]
    },
    qualityAssurance: {
      measures: [
        "Performance regression detection",
        "Architectural principle validation",
        "Code duplication auditing",
        "File size compliance checking",
        "Dependency boundary verification"
      ]
    }
  },
  projectStateExtraction: {
    description: "Use the included project extraction tool systematically to generate structured snapshots of your codebase",
    command: "python scripts/project_extract.py",
    configurationOptions: {
      options: [
        {
          name: "SEPARATE_FILES = False",
          description: "Single THE_PROJECT.md file (recommended for small codebases)",
          example: "scripts/output_example/THE_PROJECT.md"
        },
        {
          name: "SEPARATE_FILES = True",
          description: "Multiple files per directory (recommended for large codebases and focused folder work)",
          example: "scripts/output_example/.Project_Extraction"
        },
        {
            name: "INCLUDE_PATHS",
            description: "Directories and files to analyze",
            example: ""
        },
        {
            name: "EXCLUDE_PATTERNS",
            description: "Skip cache directories, build artifacts, and generated files",
            example: ""
        }
      ]
    },
    output: {
      features: [
        "Complete file contents with syntax highlighting",
        "File line counts with architectural warnings (⚠️ for 140-150 lines, ‼️ for >150 lines on code files)",
        "Tree structure visualization",
        "Ready-to-share"
      ]
    },
    usage: "Use the tool to share a complete or partial project state with the AI system, track architectural compliance, and create focused development context.",
    outputExamples: "scripts/output_example"
  }
};