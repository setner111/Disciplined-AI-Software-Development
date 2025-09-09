/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

import { SystematicEnforcementFramework, PrincipleIntegration } from '../types';

export const SYSTEMATIC_ENFORCEMENT_FRAMEWORK: SystematicEnforcementFramework = {
  mandatoryCheckpoints: {
    architecturalCompliance: {
      socValidation: true,
      deterministicBehavior: true,
      fileSizeCompliance: true,
      dryEnforcement: true,
      kissValidation: true,
      configCentralization: true,
      performanceIntegration: true,
      productionReadiness: true
    },
    codeQualityGates: {
      selfExplanatoryNaming: true,
      performanceCharacteristics: true,
      coreProjectPurpose: true,
      regressionDetection: true,
      resourceUtilization: true
    },
    progressionBlocker: true
  },
  midPhaseValidation: {
    duringDevelopment: {
      incrementalCompliance: true,
      benchmarkIntegration: true,
      dependencyAlignment: true,
      edgeCaseHandling: true,
      featureCreepCheck: true
    },
    beforePhaseCompletion: {
      fullArchitectureAudit: true,
      performanceRegression: true,
      integrationValidation: true,
      productionSimulation: true
    }
  },
  enforcementAutomation: {
    validatePhaseScript: {
      checkFileSizes: true,
      scanHardcodedValues: true,
      validateImportDependencies: true,
      runBenchmarkSuite: true,
      generateComplianceReport: true
    },
    dryAuditScript: {
      detectDuplicateImplementations: true,
      findUnusedImports: true,
      findUnusedFunctions: true,
      identifyConstants: true,
      flagSeparationViolations: true
    },
    cicdWorkflowIntegration: {
      runValidationOnCommit: true,
      blockFailedMerges: true,
      generateRegressionReports: true,
      maintainBaselineMeasurements: true
    }
  }
};

export const PRINCIPLE_INTEGRATION: PrincipleIntegration = {
  implementationEnforcement: {
    fileAndModuleConstraints: {
      maxFileLines: 150,
      singlePurposeModule: true,
      noRedundantCode: true,
      reuseExistingFunctions: true,
      consistentNaming: true
    },
    architectureValidation: {
      centralizedConfiguration: true,
      constantsReferenced: true,
      noMagicNumbers: true,
      modularSeparation: true,
      clearBoundaries: true,
      alignedDependencies: true,
      synchronousPreferred: true
    },
    performanceIntegration: {
      benchmarkingSuiteIntegrated: true,
      regressionDetectionOperational: true,
      jsonOutputAvailable: true,
      performanceGatesDefined: true,
      performanceGatesEnforced: true,
      timelineTracking: true,
      historicalComparison: true
    },
    productionReadiness: {
      crossPlatformDeployment: true,
      realWorldConstraints: true,
      resourceCleanupOnShutdown: true,
      deterministicBehaviorUnderLoad: true,
      appropriateErrorHandling: true
    }
  },
  scalingAdaptationGuidelines: {
    singleFileScripts: {
      socWithinFunctions: true,
      benchmarkCoreOperation: true,
      validateLineLimitSimple: true,
      selfExplanatoryNames: true
    },
    smallApplications: {
      strictModularBoundaries: true,
      centralizedConfigConstants: true,
      synchronousFlow: true,
      performanceBaseline: true
    },
    productionSystems: {
      fullArchitecturalCompliance: true,
      comprehensiveBenchmarking: true,
      crossPlatformDeployment: true,
      productionGradeErrorHandling: true,
      resourceManagement: true
    },
    multiLanguageProjects: {
      languageJustifiedByPerformance: true,
      architecturalPrinciplesAcrossBoundaries: true,
      unifiedBenchmarkingSystem: true,
      consistentErrorHandlingPatterns: true
    }
  },
  domainSpecificAdaptations: {
    webDevelopmentProjects: {
      noInlining: true,
      stylesToSeparateFiles: true,
      handlersToNamedFunctions: true,
      configsAsConstants: true,
      componentMaxLines: 250,
      moduleMaxLines: 150,
      asyncPermitted: ["API calls", "user interactions", "data fetching"],
      errorBoundaries: ["network operations", "user inputs", "third-party integrations"],
      fileColocation: ["Component.jsx", "Component.module.css", "Component.test.js"],
      componentSplitting: ["multiple purposes", "testing difficulty"]
    }
  }
};