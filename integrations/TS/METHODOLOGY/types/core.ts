/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

export interface FoundationalPhilosophy {
  architecturalMinimalism: boolean;
  deterministicReliability: boolean;
  measurableValue: boolean;
  productionFocus: boolean;
}

export interface SeparationOfConcerns {
  singleResponsibility: boolean;
  strictModularBoundaries: boolean;
  clearInterfaces: boolean;
  recognizeSeparationHarm: boolean;
  centralizedMainEntryPoints: boolean;
  modularProjectLayout: boolean;
}

export interface DeterministicOperations {
  synchronousBehavior: boolean;
  predictableOperations: boolean;
  longRuntimeStability: boolean;
  productionStability: boolean;
  crossPlatformConsiderations: boolean;
}

export interface PerformanceDrivenDecisions {
  workloadBasedChoices: boolean;
  optimizeProvenBottlenecks: boolean;
  avoidPrematureOptimization: boolean;
  maintainPerformanceBaselines: boolean;
  regressionDetection: boolean;
}

export interface CodeQualityStandards {
  maxFileLines: number;
  selfExplanatoryCode: boolean;
  avoidComments: boolean;
  preserveReadability: boolean;
  maintainMaintainability: boolean;
  followKISS: boolean;
  followDRY: boolean;
  reuseExistingFunctions: boolean;
}

export interface ErrorHandlingPhilosophy {
  robustWithoutOverEngineering: boolean;
  productionReliability: boolean;
  avoidOverHandling: boolean;
  gracefulFailureModes: boolean;
  resourceCleanup: boolean;
}

export interface FeatureControl {
  resistFeatureBloat: boolean;
  resistComplexityCreep: boolean;
  serveCoreProjectPurpose: boolean;
  surgicalApproach: boolean;
  targetExactProblem: boolean;
  minimalCode: boolean;
  multiLanguageJustified: boolean;
  measurableGains: boolean;
}

export interface WebDevelopmentAdaptations {
  noInlining: boolean;
  stylesToSeparateFiles: boolean;
  handlersToNamedFunctions: boolean;
  configurationsAsConstants: boolean;
  maxComponentLines: number;
  maxModuleLines: number;
  asyncOperationsAllowed: string[];
  errorBoundariesRequired: string[];
  fileColocation: string[];
  componentSplittingCriteria: string[];
  requestArchitecturalClarification: boolean;
}

export interface CodeArchitecturePrinciples {
  separationOfConcerns: SeparationOfConcerns;
  deterministicOperations: DeterministicOperations;
  performanceDrivenDecisions: PerformanceDrivenDecisions;
  codeQualityStandards: CodeQualityStandards;
  errorHandlingPhilosophy: ErrorHandlingPhilosophy;
  featureControl: FeatureControl;
  webDevelopmentAdaptations: WebDevelopmentAdaptations;
}

export interface CoreArchitecturalPrinciples {
  foundationalPhilosophy: FoundationalPhilosophy;
  codeArchitecturePrinciples: CodeArchitecturePrinciples;
}