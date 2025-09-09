/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

export interface FileAndModuleConstraints {
  maxFileLines: number;
  singlePurposeModule: boolean;
  noRedundantCode: boolean;
  reuseExistingFunctions: boolean;
  consistentNaming: boolean;
}

export interface ArchitectureValidation {
  centralizedConfiguration: boolean;
  constantsReferenced: boolean;
  noMagicNumbers: boolean;
  modularSeparation: boolean;
  clearBoundaries: boolean;
  alignedDependencies: boolean;
  synchronousPreferred: boolean;
}

export interface PerformanceIntegration {
  benchmarkingSuiteIntegrated: boolean;
  regressionDetectionOperational: boolean;
  jsonOutputAvailable: boolean;
  performanceGatesDefined: boolean;
  performanceGatesEnforced: boolean;
  timelineTracking: boolean;
  historicalComparison: boolean;
}

export interface ProductionReadiness {
  crossPlatformDeployment: boolean;
  realWorldConstraints: boolean;
  resourceCleanupOnShutdown: boolean;
  deterministicBehaviorUnderLoad: boolean;
  appropriateErrorHandling: boolean;
}

export interface ImplementationEnforcement {
  fileAndModuleConstraints: FileAndModuleConstraints;
  architectureValidation: ArchitectureValidation;
  performanceIntegration: PerformanceIntegration;
  productionReadiness: ProductionReadiness;
}

export interface SingleFileScripts {
  socWithinFunctions: boolean;
  benchmarkCoreOperation: boolean;
  validateLineLimitSimple: boolean;
  selfExplanatoryNames: boolean;
}

export interface SmallApplications {
  strictModularBoundaries: boolean;
  centralizedConfigConstants: boolean;
  synchronousFlow: boolean;
  performanceBaseline: boolean;
}

export interface ProductionSystems {
  fullArchitecturalCompliance: boolean;
  comprehensiveBenchmarking: boolean;
  crossPlatformDeployment: boolean;
  productionGradeErrorHandling: boolean;
  resourceManagement: boolean;
}

export interface MultiLanguageProjects {
  languageJustifiedByPerformance: boolean;
  architecturalPrinciplesAcrossBoundaries: boolean;
  unifiedBenchmarkingSystem: boolean;
  consistentErrorHandlingPatterns: boolean;
}

export interface ScalingAdaptationGuidelines {
  singleFileScripts: SingleFileScripts;
  smallApplications: SmallApplications;
  productionSystems: ProductionSystems;
  multiLanguageProjects: MultiLanguageProjects;
}

export interface WebDevelopmentProjects {
  noInlining: boolean;
  stylesToSeparateFiles: boolean;
  handlersToNamedFunctions: boolean;
  configsAsConstants: boolean;
  componentMaxLines: number;
  moduleMaxLines: number;
  asyncPermitted: string[];
  errorBoundaries: string[];
  fileColocation: string[];
  componentSplitting: string[];
}

export interface DomainSpecificAdaptations {
  webDevelopmentProjects: WebDevelopmentProjects;
}

export interface PrincipleIntegration {
  implementationEnforcement: ImplementationEnforcement;
  scalingAdaptationGuidelines: ScalingAdaptationGuidelines;
  domainSpecificAdaptations: DomainSpecificAdaptations;
}