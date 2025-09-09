/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

import { ProjectDocumentationMethodology, SuccessMetrics } from '../types';
import { CORE_ARCHITECTURAL_PRINCIPLES } from './core';
import { PHASE0_REQUIREMENTS, DOCUMENTATION_BUILDING_PROCESS } from './phase0';
import { SYSTEMATIC_ENFORCEMENT_FRAMEWORK, PRINCIPLE_INTEGRATION } from './enforcement';

export const SUCCESS_METRICS: SuccessMetrics = {
  technicalIndicators: {
    architecturalPrinciplesApplied: true,
    performanceBaselinesMaintained: true,
    zeroProductionIncidents: true,
    fileSizeConstraintsAdhered: true
  },
  operationalIndicators: {
    systemUptimeReliability: true,
    predictableResourceUtilization: true,
    gracefulDegradation: true,
    maintainabilityPreserved: true
  },
  developmentIndicators: {
    enforcementCheckpoints: true,
    performanceRegressionDetection: true,
    codeReviewEfficiency: true,
    technicalDebtPrevention: true
  },
  documentationQuality: {
    enforcementPreventsDrift: true,
    qualityGatesBlockProgression: true,
    automatedValidation: true,
    performanceBaselinesTracked: true
  },
  projectExecution: {
    systematicValidation: true,
    architecturalPrinciplesConsistent: true,
    performanceCharacteristicsPredictable: true,
    productionReadinessVerified: true
  }
};

export const DEFAULT_PROJECT_DOCUMENTATION_CONFIG: ProjectDocumentationMethodology = {
  title: "Project Documentation Methodology",
  coreArchitecturalPrinciples: CORE_ARCHITECTURAL_PRINCIPLES,
  phase0Requirements: PHASE0_REQUIREMENTS,
  documentationBuildingProcess: DOCUMENTATION_BUILDING_PROCESS,
  systematicEnforcementFramework: SYSTEMATIC_ENFORCEMENT_FRAMEWORK,
  principleIntegration: PRINCIPLE_INTEGRATION,
  successMetrics: SUCCESS_METRICS,
  conclusion: "This methodology enforces discipline through automated checking and explicit validation points, preventing the gradual erosion of architectural principles during development."
};

export * from './core';
export * from './phase0';
export * from './enforcement';