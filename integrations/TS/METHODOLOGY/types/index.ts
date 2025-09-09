/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

import { CoreArchitecturalPrinciples } from './core';
import { Phase0Requirements } from './phase0';
import { DocumentationBuildingProcess } from './process';
import { SystematicEnforcementFramework } from './enforcement';
import { PrincipleIntegration } from './integration';
import { SuccessMetrics } from './metrics';

export interface ProjectDocumentationMethodology {
  title: string;
  coreArchitecturalPrinciples: CoreArchitecturalPrinciples;
  phase0Requirements: Phase0Requirements;
  documentationBuildingProcess: DocumentationBuildingProcess;
  systematicEnforcementFramework: SystematicEnforcementFramework;
  principleIntegration: PrincipleIntegration;
  successMetrics: SuccessMetrics;
  conclusion: string;
}

export * from './core';
export * from './phase0';
export * from './process';
export * from './enforcement';
export * from './integration';
export * from './metrics';