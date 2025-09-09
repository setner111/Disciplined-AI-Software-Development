/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

import { InteractionRules, TrainingData } from '../types/interaction';
import { Phase0Requirements } from '../types/requirements';
import { CodeInstructions, WebsiteSpecifics } from '../types/code_instructions';

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