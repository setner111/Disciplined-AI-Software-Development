/*
Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
https://creativecommons.org/licenses/by-sa/4.0/
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