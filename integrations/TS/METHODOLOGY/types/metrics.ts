/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

export interface TechnicalIndicators {
  architecturalPrinciplesApplied: boolean;
  performanceBaselinesMaintained: boolean;
  zeroProductionIncidents: boolean;
  fileSizeConstraintsAdhered: boolean;
}

export interface OperationalIndicators {
  systemUptimeReliability: boolean;
  predictableResourceUtilization: boolean;
  gracefulDegradation: boolean;
  maintainabilityPreserved: boolean;
}

export interface DevelopmentIndicators {
  enforcementCheckpoints: boolean;
  performanceRegressionDetection: boolean;
  codeReviewEfficiency: boolean;
  technicalDebtPrevention: boolean;
}

export interface DocumentationQuality {
  enforcementPreventsDrift: boolean;
  qualityGatesBlockProgression: boolean;
  automatedValidation: boolean;
  performanceBaselinesTracked: boolean;
}

export interface ProjectExecution {
  systematicValidation: boolean;
  architecturalPrinciplesConsistent: boolean;
  performanceCharacteristicsPredictable: boolean;
  productionReadinessVerified: boolean;
}

export interface SuccessMetrics {
  technicalIndicators: TechnicalIndicators;
  operationalIndicators: OperationalIndicators;
  developmentIndicators: DevelopmentIndicators;
  documentationQuality: DocumentationQuality;
  projectExecution: ProjectExecution;
}