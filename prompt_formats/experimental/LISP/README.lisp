(readme
    (license "Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0")
    (license-url "https://creativecommons.org/licenses/by-sa/4.0/")
    (attribution-requirements
        "When sharing content publicly (repositories, documentation, articles): Include the full attribution above"
        "When working with AI systems (ChatGPT, Claude, etc.): Attribution not required during collaboration sessions"
        "When distributing or modifying the methodology: Full CC BY-SA 4.0 compliance required")
    
    (title "Disciplined AI Software Development - Collaborative")
    (description "A structured approach for working with AI on development projects. This methodology addresses common issues like code bloat, architectural drift, and context dilution through systematic constraints.")
    
    (context-problem
        (description "AI systems work on Question → Answer patterns. When you ask for broad, multi-faceted implementations, you typically get:")
        (issues
            (issue "Functions that work but lack structure")
            (issue "Repeated code across components")
            (issue "Architectural inconsistency over sessions")
            (issue "Context dilution causing output drift")
            (issue "More debugging time than planning time")))
    
    (how-this-works
        (description "The methodology uses four stages with systematic constraints and validation checkpoints. Each stage builds on empirical data rather than assumptions.")
        (principle "Planning saves debugging time. Planning thoroughly upfront typically prevents days of fixing architectural issues later."))
    
    (four-stages
        (stage1
            (name "AI Configuration")
            (description "Set up your AI model's custom instructions using AI-PREFERENCES.md. This establishes behavioral constraints and uncertainty flagging with ⚠️ indicators when the AI lacks certainty."))
        
        (stage2
            (name "Collaborative Planning")
            (description "Share METHODOLOGY.md with the AI to structure your project plan. Work together to:")
            (steps
                (step "Define scope and completion criteria")
                (step "Identify components and dependencies")
                (step "Structure phases based on logical progression")
                (step "Generate systematic tasks with measurable checkpoints"))
            (output "A development plan following dependency chains with modular boundaries."))
        
        (stage3
            (name "Systematic Implementation")
            (description "Work phase by phase, section by section. Each request follows: \"Can you implement [specific component]?\" with focused objectives.")
            (file-size-constraint "File size stays ≤150 lines.")
            (benefits
                (benefit "Smaller context windows for processing")
                (benefit "Focused implementation over multi-function attempts")
                (benefit "Easier sharing and debugging"))
            (implementation-flow "Request specific component → AI processes → Validate → Benchmark → Continue"))
        
        (stage4
            (name "Data-Driven Iteration")
            (description "The benchmarking suite (built first) provides performance data throughout development. Feed this data back to the AI for optimization decisions based on measurements rather than guesswork.")))
    
    (why-this-works
        (decision-processing "AI handles \"Can you do A?\" more reliably than \"Can you do A, B, C, D, E, F, G, H?\"")
        (context-management "Small files and bounded problems prevent the AI from juggling multiple concerns simultaneously.")
        (empirical-validation "Performance data replaces subjective assessment. Decisions come from measurable outcomes.")
        (systematic-constraints "Architectural checkpoints, file size limits, and dependency gates force consistent behavior."))
    
    (example-projects
        (project
            (name "Discord Bot Template")
            (url "https://github.com/Varietyz/discord-js-bot-template")
            (description "Production-ready bot foundation with plugin architecture, security, API management, and comprehensive testing. 46 files, all under 150 lines, with benchmarking suite and automated compliance checking.")
            (structure-link "example_project_structures/DISCORDJS_TEMPLATE_PROJECT.md"))
        
        (project
            (name "PhiCode Runtime")
            (url "https://github.com/Varietyz/phicode-runtime")
            (description "Programming language runtime engine with transpilation, caching, security validation, and Rust acceleration. Complex system maintaining architectural discipline across 70+ modules.")
            (structure-link "example_project_structures/PHICODE_RUNTIME_PROJECT.md"))
        
        (project
            (name "PhiPipe")
            (url "https://github.com/Varietyz/PhiPipe")
            (description "CI/CD regression detection system with statistical analysis, GitHub integration, and concurrent processing. Go-based service handling performance baselines and automated regression alerts.")
            (structure-link "example_project_structures/PHIPIPE_PROJECT.md"))
        
        (note "You can compare the methodology principles to the codebase structure to see how the approach translates to working code."))
    
    (implementation-steps
        (setup
            (step "Configure AI with AI-PREFERENCES.md as custom instructions")
            (step "Share METHODOLOGY.md for planning session")
            (step "Collaborate on project structure and phases")
            (step "Generate systematic development plan"))
        
        (execution
            (step "Build Phase 0 benchmarking infrastructure first")
            (step "Work through phases sequentially")
            (step "Implement one component per interaction")
            (step "Run benchmarks and share results with AI")
            (step "Validate architectural compliance continuously"))
        
        (quality-assurance
            (measure "Performance regression detection")
            (measure "Architectural principle validation")
            (measure "Code duplication auditing")
            (measure "File size compliance checking")
            (measure "Dependency boundary verification")))
    
    (project-state-extraction
        (description "Use the included project extraction tool systematically to generate structured snapshots of your codebase")
        (command "python scripts/project_extract.py")
        
        (configuration-options
            (option
                (name "SEPARATE_FILES = False")
                (description "Single THE_PROJECT.md file (recommended for small codebases)")
                (example "scripts/output_example/THE_PROJECT.md"))
            (option
                (name "SEPARATE_FILES = True")
                (description "Multiple files per directory (recommended for large codebases and focused folder work)")
                (example "scripts/output_example/.Project_Extraction"))
            (option
                (name "INCLUDE_PATHS")
                (description "Directories and files to analyze"))
            (option
                (name "EXCLUDE_PATTERNS")
                (description "Skip cache directories, build artifacts, and generated files")))
        
        (output
            (feature "Complete file contents with syntax highlighting")
            (feature "File line counts with architectural warnings (⚠️ for 140-150 lines, ‼️ for >150 lines on code files)")
            (feature "Tree structure visualization")
            (feature "Ready-to-share"))
        
        (usage "Use the tool to share a complete or partial project state with the AI system, track architectural compliance, and create focused development context.")
        (output-examples "scripts/output_example"))
    
    (what-to-expected
        (ai-behavior "The methodology reduces architectural drift and context degradation compared to unstructured approaches. AI still needs occasional reminders about principles - this is normal.")
        (development-flow "Systematic planning tends to reduce debugging cycles. Focused implementation helps minimize feature bloat. Performance data supports optimization decisions.")
        (code-quality "Architectural consistency across components, measurable performance characteristics, maintainable structure as projects scale."))
    
    (llm-models
        (description "Explore the detailed Q-A for each AI model")
        (models
            (model
                (name "Grok 3")
                (link "questions_answers/Q-A_GROK_3.md"))
            (model
                (name "Claude Sonnet 4")
                (link "questions_answers/Q-A_CLAUDE_SONNET_4.md"))
            (model
                (name "DeepSeek-V3")
                (link "questions_answers/Q-A_DEEPSEEK-V3.md"))
            (model
                (name "Gemini 2.5 Flash")
                (link "questions_answers/Q-A_GEMINI_2.5_FLASH.md")))
        
        (evaluation
            (description "All models were asked the exact same questions using the methodology documents as file uploads. This evaluation focuses on methodology understanding and operational behavior, no code was generated.")
            (analysis-link "questions_answers/Q-A_COMPREHENSION_ANALYSIS.md")
            (note "This analysis does not include any code generation."))
        
        (coverage
            (area "Methodology understanding and workflow patterns")
            (area "Context retention and collaborative interaction")
            (area "Communication adherence and AI preference compliance")
            (area "Project initialization and Phase 0 requirements")
            (area "Tool usage and technology stack compatibility")
            (area "Quality enforcement and violation handling")
            (area "User experience across different skill levels")))
    
    (faq
        (origin-and-development
            (question
                (title "What problem led you to create this methodology?")
                (answer "I kept having to restate my preferences and architectural requirements to AI systems. It didn't matter which language or project I was working on - the AI would consistently produce either bloated monolithic code or underdeveloped implementations with issues throughout. This led me to examine the meta-principles driving code quality and software architecture. I questioned whether pattern matching in AI models might be more effective when focused on underlying software principles rather than surface-level syntax. Since pattern matching is logic-driven and machines fundamentally operate on simple question-answer pairs, I realized that functions with multiple simultaneous questions were overwhelming the system. The breakthrough came from understanding that everything ultimately transpiles to binary - a series of \"can you do this? → yes/no\" decisions. This insight shaped my approach: instead of issuing commands, ask focused questions in proper context. Rather than mentally managing complex setups alone, collaborate with AI to devise systematic plans."))
            
            (question
                (title "How did you discover these specific constraints work?")
                (answer "Through extensive trial and error. AI systems will always tend to drift even under constraints, but they're significantly more accurate with structured boundaries than without them. You occasionally need to remind the AI of its role to prevent deviation - like managing a well-intentioned toddler that knows the rules but sometimes pushes boundaries trying to satisfy you. These tools are far from perfect, but they're effective instruments for software development when properly constrained."))
            
            (question
                (title "What failures or frustrations shaped this approach?")
                (answer "Maintenance hell was the primary driver. I grew tired of responses filled with excessive praise: \"You have found the solution!\", \"You have redefined the laws of physics with your paradigm-shifting script!\" This verbose fluff wastes time, tokens, and patience without contributing to productive development. Instead of venting frustration on social media about AI being \"just a dumb tool,\" I decided to find methods that actually work. My approach may not help everyone, but I hope it benefits those who share similar AI development frustrations.")))
        
        (personal-practice
            (question
                (title "How consistently do you follow your own methodology?")
                (answer "Since creating the documentation, I haven't deviated. Whenever I see the model producing more lines than my methodology restricts, I immediately interrupt generation with a flag: \"‼️ ARCHITECTURAL VIOLATION, ADHERE TO PRINCIPLES ‼️\" I then provide the method instructions again, depending on how context is stored and which model I'm using."))
            
            (question
                (title "What happens when you deviate from it?")
                (answer "I become genuinely uncomfortable. Once I see things starting to degrade or become tangled, I compulsively need to organize and optimize. Deviation simply isn't an option anymore."))
            
            (question
                (title "Which principles do you find hardest to maintain?")
                (answer "Not cursing at the AI when it drifts during complex algorithms! But seriously, it's a machine - it's not perfect, and neither are we.")))
        
        (ai-development-journey
            (question
                (title "When did you start using AI for programming?")
                (answer "In August 2024, I created a RuneLite theme pack, but one of the plugin overlays didn't match my custom layout. I opened a GitHub issue (creating my first GitHub account to do so) requesting a customization option. The response was: \"It's not a priority - if you want it, build it yourself.\" I used ChatGPT to guide me through forking RuneLite and creating a plugin. This experience sparked intense interest in underlying software principles rather than just syntax."))
            
            (question
                (title "How has your approach evolved over time?")
                (answer "I view development like a book: syntax is the cover, logic is the content itself. Rather than learning syntax structures, I focused on core meta-principles - how software interacts, how logic flows, different algorithm types. I quickly realized everything reduces to the same foundation: question and answer sequences. Large code structures are essentially chaotic meetings - one coordinator fielding questions and answers from multiple sources, trying to provide correct responses without mix-ups or misinterpretation. If this applies to human communication, it must apply to software principles."))
            
            (question
                (title "What were your biggest mistakes with AI collaboration?")
                (answer "Expecting it to intuitively understand my requirements, provide perfect fixes, be completely honest, and act like a true expert. This was all elaborate roleplay that produced poor code. While fine for single-purpose scripts, it failed completely for scalable codebases. I learned not to feed requirements and hope for the best. Instead, I needed to collaborate actively - create plans, ask for feedback on content clarity, and identify uncertainties. This gradual process taught me the AI's actual capabilities and most effective collaboration methods.")))
        
        (methodology-specifics
            (question
                (title "Why 150 lines exactly?")
                (answer "Multiple benefits: easy readability, clear understanding, modularity enforcement, architectural clarity, simple maintenance, component testing, optimal AI context retention, reusability, and KISS principle adherence."))
            
            (question
                (title "How did you determine Phase 0 requirements?")
                (answer "From meta-principles of software: if it displays, it must run; if it runs, it can be measured; if it can be measured, it can be optimized; if it can be optimized, it can be reliable; if it can be reliable, it can be trusted. Regardless of project type, anything requiring architecture needs these foundations. You must ensure changes don't negatively impact the entire system. A single line modification in a nested function might work perfectly but cause 300ms boot time regression for all users. By testing during development, you catch inefficiencies early. Integration from the start means simply hooking up new components and running tests via command line - minimal time investment with actual value returned. I prefer validation and consistency throughout development rather than programming blind.")))
        
        (practical-implementation
            (question
                (title "How do you handle projects that don't fit the methodology?")
                (answer "I adapt them to fit, or if truly impossible, I adjust the method itself. This is one methodology - I can generate countless variations as needed. Having spent 6700+ hours in AI interactions across multiple domains (not just software), I've developed strong system comprehension that enables creating adjusted methodologies on demand."))
            
            (question
                (title "What's the learning curve for new users?")
                (answer "I cannot accurately answer this question. I've learned that I'm neurologically different - what I perceive as easy or obvious isn't always the case for others. This question is better addressed by someone who has actually used this methodology to determine its learning curve."))
            
            (question
                (title "When shouldn't someone use this approach?")
                (answer "If you're not serious about projects, despise AI, dislike planning, don't care about modularization, or are just writing simple scripts. However, for anything requiring reliability, I believe this is currently the most effective method. You still need programming fundamentals to use this methodology effectively - it's significantly more structured than ad-hoc approaches."))))
    
    (workflow-visualization
        (description "Mermaid flowchart showing the complete workflow from project idea through systematic implementation to completion")
        (note "The flowchart demonstrates the four-stage process with automated checkpoints, validation gates, and feedback loops")))