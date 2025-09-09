/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

export interface ArchitecturalCompliance {
  socValidation: boolean;
  deterministicBehavior: boolean;
  fileSizeCompliance: boolean;
  dryEnforcement: boolean;
  kissValidation: boolean;
  configCentralization: boolean;
  performanceIntegration: boolean;
  productionReadiness: boolean;
}

export interface CodeQualityGates {
  selfExplanatoryNaming: boolean;
  performanceCharacteristics: boolean;
  coreProjectPurpose: boolean;
  regressionDetection: boolean;
  resourceUtilization: boolean;
}

export interface MandatoryCheckpoints {
  architecturalCompliance: ArchitecturalCompliance;
  codeQualityGates: CodeQualityGates;
  progressionBlocker: boolean;
}

export interface DuringDevelopment {
  incrementalCompliance: boolean;
  benchmarkIntegration: boolean;
  dependencyAlignment: boolean;
  edgeCaseHandling: boolean;
  featureCreepCheck: boolean;
}

export interface BeforePhaseCompletion {
  fullArchitectureAudit: boolean;
  performanceRegression: boolean;
  integrationValidation: boolean;
  productionSimulation: boolean;
}

export interface MidPhaseValidation {
  duringDevelopment: DuringDevelopment;
  beforePhaseCompletion: BeforePhaseCompletion;
}

export interface ValidatePhaseScript {
  checkFileSizes: boolean;
  scanHardcodedValues: boolean;
  validateImportDependencies: boolean;
  runBenchmarkSuite: boolean;
  generateComplianceReport: boolean;
}

export interface DryAuditScript {
  detectDuplicateImplementations: boolean;
  findUnusedImports: boolean;
  findUnusedFunctions: boolean;
  identifyConstants: boolean;
  flagSeparationViolations: boolean;
}

export interface CICDWorkflowIntegration {
  runValidationOnCommit: boolean;
  blockFailedMerges: boolean;
  generateRegressionReports: boolean;
  maintainBaselineMeasurements: boolean;
}

export interface EnforcementAutomation {
  validatePhaseScript: ValidatePhaseScript;
  dryAuditScript: DryAuditScript;
  cicdWorkflowIntegration: CICDWorkflowIntegration;
}

export interface SystematicEnforcementFramework {
  mandatoryCheckpoints: MandatoryCheckpoints;
  midPhaseValidation: MidPhaseValidation;
  enforcementAutomation: EnforcementAutomation;
}