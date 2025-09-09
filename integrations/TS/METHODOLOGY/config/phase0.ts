/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

import { Phase0Requirements, DocumentationBuildingProcess } from '../types';

export const PHASE0_REQUIREMENTS: Phase0Requirements = {
  title: "Basic Must-Haves (Phase 0 - Always First)",
  description: "Every project, regardless of size, must establish these foundational systems before any feature development",
  benchmarkingSuite: {
    coreFramework: true,
    performanceMeasurement: true,
    componentIsolation: true,
    regressionDetection: true,
    compareAgainstPrevious: true,
    failOnPerformanceDrops: true,
    baselineManagement: true,
    saveBaselines: true,
    trackBaselinesOverTime: true,
    jsonOutput: true,
    structuredData: true,
    automatedAnalysis: true,
    ciIntegration: true,
    timelineTracking: true,
    historicalPerformanceData: true
  },
  cicdInfrastructure: {
    releaseWorkflows: true,
    automatedVersioning: true,
    automatedBuilding: true,
    automatedDeployment: true,
    regressionDetection: true,
    benchmarkComparison: true,
    qualityGates: true,
    blockMergesOnFailure: true,
    automatedTesting: true,
    runFullTestSuite: true
  },
  coreArchitecture: {
    centralizedEntryPoints: true,
    singleMainModule: true,
    configurationManagement: true,
    externalizedSettings: true,
    settingsValidation: true,
    centralizedLogging: true,
    errorHandling: true,
    diagnosticOutput: true,
    jsonIntegration: true,
    dependencyInjection: true,
    cleanSeparation: true,
    testableComponents: true
  },
  testingInfrastructure: {
    testSuite: true,
    unitTests: true,
    integrationTests: true,
    stressTesting: true,
    loadValidation: true,
    boundaryConditionValidation: true,
    testDataManagement: true,
    reproducibleTestScenarios: true,
    testCleanup: true,
    coverageTracking: true,
    adequateCoverage: true
  },
  documentationSystem: {
    automatedGeneration: true,
    extractFromCode: true,
    extractFromStructure: true,
    architectureDocumentation: true,
    systemDesign: true,
    componentRelationships: true,
    apiDocumentation: true,
    interfaceSpecifications: true,
    usageExamples: true,
    performanceDocumentation: true,
    benchmarkResults: true,
    optimizationGuides: true
  },
  criticalNote: "These systems must be operational before writing any application logic. They become the foundation that enables rapid, confident development."
};

export const DOCUMENTATION_BUILDING_PROCESS: DocumentationBuildingProcess = {
  step1: {
    name: "Project Decomposition",
    questions: [
      "What does \"finished\" look like?",
      "What are the major pieces that need to exist?",
      "What depends on what?",
      "Where are the natural stopping points?"
    ],
    approach: "Create sections based on dependencies: Major Piece A → Major Piece B → Major Piece C with corresponding sub-tasks"
  },
  step2: {
    name: "Phase Creation",
    mandatoryPhase0: [
      "Benchmarking suite with regression detection",
      "GitHub workflows for releases and quality gates",
      "Test infrastructure (unit + stress testing)",
      "Documentation generation system",
      "Centralized architecture setup"
    ],
    groupingCriteria: [
      "Dependency chains: Things that must happen in sequence",
      "Logical groupings: Related functionality that makes sense together",
      "Natural checkpoints: Places where you can validate progress"
    ]
  },
  step3: {
    name: "Task Breakdown",
    requirements: [
      "Specific action: What exactly needs to be done",
      "Output: What will exist when complete",
      "Success criteria: How to verify completion",
      "Integration points: How it connects to other work"
    ]
  },
  step4: {
    name: "Progress Tracking System",
    statusIndicators: [
      { status: "COMPLETED", description: "Done and validated" },
      { status: "BLOCKED", description: "Cannot proceed due to dependency" },
      { status: "READY", description: "Dependencies met, can start" },
      { status: "UNCERTAIN", description: "Need clarification or decision" }
    ]
  },
  step5: {
    name: "Quality Gates",
    criteria: [
      "Does the output match what was specified?",
      "Can the next phase actually use this output?",
      "Is there enough documentation for future reference?",
      "Are there any obvious issues that need fixing?"
    ]
  }
};