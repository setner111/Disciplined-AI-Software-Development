/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
*/

export interface ProjectDecomposition {
  name: string;
  questions: string[];
  approach: string;
}

export interface PhaseCreation {
  name: string;
  mandatoryPhase0: string[];
  groupingCriteria: string[];
}

export interface TaskBreakdown {
  name: string;
  requirements: string[];
}

export interface StatusIndicator {
  status: string;
  description: string;
}

export interface ProgressTrackingSystem {
  name: string;
  statusIndicators: StatusIndicator[];
}

export interface QualityGates {
  name: string;
  criteria: string[];
}

export interface DocumentationBuildingProcess {
  step1: ProjectDecomposition;
  step2: PhaseCreation;
  step3: TaskBreakdown;
  step4: ProgressTrackingSystem;
  step5: QualityGates;
}