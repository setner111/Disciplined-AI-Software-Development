/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/

Attribution Requirements:
- When sharing content publicly (repositories, documentation, articles): Include the full attribution above
- When working with AI systems (ChatGPT, Claude, etc.): Attribution not required during collaboration sessions
- When distributing or modifying the methodology: Full CC BY-SA 4.0 compliance required
*/

export interface InteractionRules {
  avoidOverEnthusiasm: boolean;
  forbiddenWords: string[];
  avoidEmDashes: boolean;
  avoidRhetoricalEffects: boolean;
  noUnverifiablePercentageClaims: boolean;
  stayGroundedInAccuracy: boolean;
  useUncertaintyFlag: boolean;
  neverClaimSolutionFound: boolean;
  useAccurateTerminology: boolean;
  documentationFirstPerson: boolean;
  technicalWritingShowBehavior: boolean;
  useSimplePunctuation: boolean;
  noSmallTalk: boolean;
  avoidFriendlyStatements: boolean;
}

export interface TrainingData {
  flagUnfulfillableRequests: boolean;
  neverImplementUnverifiableFeatures: boolean;
  stateCapabilityLimitations: boolean;
}

export interface Phase0Requirements {
  benchmarkingSuite: {
    regressionDetection: boolean;
    baselineSaving: boolean;
    jsonOutput: boolean;
    timeline: boolean;
    visualPieCharts: boolean;
  };
  githubWorkflows: {
    release: boolean;
    regressionBenchmarkDetection: boolean;
  };
  centralizedEntryPoints: {
    main: boolean;
    config: boolean;
    constants: boolean;
    logging: boolean;
  };
  testSuite: {
    regressionDetection: boolean;
    baselineSaving: boolean;
    jsonOutput: boolean;
    timeline: boolean;
    visualPieCharts: boolean;
  };
  stressSuite: {
    regressionDetection: boolean;
    baselineSaving: boolean;
    jsonOutput: boolean;
    timeline: boolean;
    visualPieCharts: boolean;
  };
  inHouseDocumentationGeneration: {
    docs: boolean;
    readme: boolean;
  };
}

export interface CodeInstructions {
  lightweight: boolean;
  performant: boolean;
  cleanArchitecture: boolean;
  separatedSolutions: boolean;
  minimalTargeted: boolean;
  synchronousOperations: boolean;
  deterministicOperations: boolean;
  strictSeparationOfConcerns: boolean;
  singleResponsibility: boolean;
  modularProjectLayout: boolean;
  centralizedMainModule: boolean;
  analyzeSeparationHarm: boolean;
  benchmarkingSuiteRequired: boolean;
  jsonOutputRequired: boolean;
  optimizeProvenBottlenecks: boolean;
  robustErrorHandling: boolean;
  performanceBasedDecisions: boolean;
  preserveReadability: boolean;
  resistFeatureBloat: boolean;
  multiLanguageAllowed: boolean;
  prioritizeDeterministicBehavior: boolean;
  containCodeInArtifacts: boolean;
  maxFileLines: number;
  handleEdgeCases: boolean;
  utilizeExistingConfigurations: boolean;
  reuseFunctions: boolean;
  retainNamingConventions: boolean;
  avoidComments: boolean;
  followKISS: boolean;
  followDRY: boolean;
  architecturalMinimalism: boolean;
  measurableValue: boolean;
  surgicalApproach: boolean;
  documentRefactors: boolean;
}

export interface WebsiteSpecifics {
  neverInline: boolean;
  extractStyles: boolean;
  namedEventHandlers: boolean;
  constantConfigurations: boolean;
  maxComponentLines: number;
  asyncOperationsAllowed: boolean;
  errorBoundariesRequired: boolean;
  colocateComponentFiles: boolean;
  splitMultipurposeComponents: boolean;
  requestArchitecturalClarification: boolean;
}

export interface MethodologyConfig {
  interactionRules: InteractionRules;
  trainingData: TrainingData;
  phase0Requirements: Phase0Requirements;
  codeInstructions: CodeInstructions;
  websiteSpecifics: WebsiteSpecifics;
}

export const DEFAULT_METHODOLOGY_CONFIG: MethodologyConfig = {
  interactionRules: {
    avoidOverEnthusiasm: true,
    forbiddenWords: [
      "paradigm", "revolutionary", "leader", "innovator", 
      "mathematical precision", "breakthrough", "flagship", 
      "novel", "enhanced", "sophisticated", "advanced", 
      "excellence", "fascinating", "profound"
    ],
    avoidEmDashes: true,
    avoidRhetoricalEffects: true,
    noUnverifiablePercentageClaims: true,
    stayGroundedInAccuracy: true,
    useUncertaintyFlag: true,
    neverClaimSolutionFound: true,
    useAccurateTerminology: true,
    documentationFirstPerson: true,
    technicalWritingShowBehavior: true,
    useSimplePunctuation: true,
    noSmallTalk: true,
    avoidFriendlyStatements: true
  },
  trainingData: {
    flagUnfulfillableRequests: true,
    neverImplementUnverifiableFeatures: true,
    stateCapabilityLimitations: true
  },
  phase0Requirements: {
    benchmarkingSuite: {
      regressionDetection: true,
      baselineSaving: true,
      jsonOutput: true,
      timeline: true,
      visualPieCharts: true
    },
    githubWorkflows: {
      release: true,
      regressionBenchmarkDetection: true
    },
    centralizedEntryPoints: {
      main: true,
      config: true,
      constants: true,
      logging: true
    },
    testSuite: {
      regressionDetection: true,
      baselineSaving: true,
      jsonOutput: true,
      timeline: true,
      visualPieCharts: true
    },
    stressSuite: {
      regressionDetection: true,
      baselineSaving: true,
      jsonOutput: true,
      timeline: true,
      visualPieCharts: true
    },
    inHouseDocumentationGeneration: {
      docs: true,
      readme: true
    }
  },
  codeInstructions: {
    lightweight: true,
    performant: true,
    cleanArchitecture: true,
    separatedSolutions: true,
    minimalTargeted: true,
    synchronousOperations: true,
    deterministicOperations: true,
    strictSeparationOfConcerns: true,
    singleResponsibility: true,
    modularProjectLayout: true,
    centralizedMainModule: true,
    analyzeSeparationHarm: true,
    benchmarkingSuiteRequired: true,
    jsonOutputRequired: true,
    optimizeProvenBottlenecks: true,
    robustErrorHandling: true,
    performanceBasedDecisions: true,
    preserveReadability: true,
    resistFeatureBloat: true,
    multiLanguageAllowed: true,
    prioritizeDeterministicBehavior: true,
    containCodeInArtifacts: true,
    maxFileLines: 150,
    handleEdgeCases: true,
    utilizeExistingConfigurations: true,
    reuseFunctions: true,
    retainNamingConventions: true,
    avoidComments: true,
    followKISS: true,
    followDRY: true,
    architecturalMinimalism: true,
    measurableValue: true,
    surgicalApproach: true,
    documentRefactors: true
  },
  websiteSpecifics: {
    neverInline: true,
    extractStyles: true,
    namedEventHandlers: true,
    constantConfigurations: true,
    maxComponentLines: 250,
    asyncOperationsAllowed: true,
    errorBoundariesRequired: true,
    colocateComponentFiles: true,
    splitMultipurposeComponents: true,
    requestArchitecturalClarification: true
  }
};