import Std

/-!
Original project proposal: source memory in assisted self-assessment.
This is a finite-count model, not a verified model of human behavior.
Compare equally sized low- and high-initial-confidence bands.
Corrected errors improve final task outcomes. A remembered correction is
not credited to the unaided judgment; an unremembered correction is.
The psychological credit rule is an explicit, empirically unvalidated premise.
-/
namespace ClinicalModels.AssistedSelfAssessment

structure Band where
  size : Int
  initialCorrect : Int
  rescued : Int
  rememberedRescues : Int
  deriving DecidableEq, Repr

def Valid (b : Band) : Prop :=
  0 < b.size ∧ 0 ≤ b.initialCorrect ∧ 0 ≤ b.rescued ∧
  b.initialCorrect + b.rescued ≤ b.size ∧
  0 ≤ b.rememberedRescues ∧ b.rememberedRescues ≤ b.rescued

def finalCorrect (b : Band) : Int := b.initialCorrect + b.rescued

/-- Model-assumed numerator used to estimate unaided correctness. -/
def creditedCorrect (b : Band) : Int :=
  b.initialCorrect + b.rescued - b.rememberedRescues

def initialGap (low high : Band) : Int := high.initialCorrect - low.initialCorrect
def creditedGap (low high : Band) : Int := creditedCorrect high - creditedCorrect low
def rescueExcess (low high : Band) : Int := low.rescued - high.rescued
def memoryExcess (low high : Band) : Int := low.rememberedRescues - high.rememberedRescues

theorem credited_bounds (b : Band) (valid : Valid b) :
    b.initialCorrect ≤ creditedCorrect b ∧ creditedCorrect b ≤ finalCorrect b ∧
    0 ≤ creditedCorrect b ∧ finalCorrect b ≤ b.size := by
  simp only [Valid, creditedCorrect, finalCorrect] at *
  omega

/-- The exact threshold for reversing the two credited numerators.
Equal band sizes are needed to interpret numerator order as rate order. -/
theorem reversal_threshold (low high : Band) :
    creditedCorrect high < creditedCorrect low ↔
      initialGap low high + memoryExcess low high < rescueExcess low high := by
  simp only [creditedCorrect, initialGap, memoryExcess, rescueExcess]
  omega

/-- Remembering all rescues removes the model's attribution distortion. -/
theorem full_memory_recovers_gap (low high : Band)
    (hl : low.rememberedRescues = low.rescued)
    (hh : high.rememberedRescues = high.rescued) :
    creditedGap low high = initialGap low high := by
  simp only [creditedGap, creditedCorrect, initialGap]
  omega

/-- At the same original outcomes and rescue counts, the memory imbalance
alone determines the difference between the two credited gaps. -/
theorem memory_changes_gap (low high low' high' : Band)
    (cl : low.initialCorrect = low'.initialCorrect)
    (ch : high.initialCorrect = high'.initialCorrect)
    (rl : low.rescued = low'.rescued)
    (rh : high.rescued = high'.rescued) :
    creditedGap low' high' - creditedGap low high =
      memoryExcess low' high' - memoryExcess low high := by
  simp only [creditedGap, creditedCorrect, memoryExcess]
  omega

/-- Reallocating a fixed number of rescues preserves total final success. -/
theorem matched_rescues_match_total (low high low' high' : Band)
    (cl : low.initialCorrect = low'.initialCorrect)
    (ch : high.initialCorrect = high'.initialCorrect)
    (r : low.rescued + high.rescued = low'.rescued + high'.rescued) :
    finalCorrect low + finalCorrect high = finalCorrect low' + finalCorrect high' := by
  simp only [finalCorrect]
  omega

def targetedLow : Band := ⟨100, 60, 35, 0⟩
def targetedHigh : Band := ⟨100, 80, 5, 0⟩
def balancedLow : Band := ⟨100, 60, 20, 0⟩
def balancedHigh : Band := ⟨100, 80, 20, 0⟩

/-- A constructed, feasible contrast at identical total final success.
These counts are synthetic; no participant data were used to choose them. -/
theorem matched_success_different_order :
    Valid targetedLow ∧ Valid targetedHigh ∧
    Valid balancedLow ∧ Valid balancedHigh ∧
    finalCorrect targetedLow + finalCorrect targetedHigh = 180 ∧
    finalCorrect balancedLow + finalCorrect balancedHigh = 180 ∧
    initialGap targetedLow targetedHigh = 20 ∧
    creditedGap targetedLow targetedHigh = -10 ∧
    creditedGap balancedLow balancedHigh = 20 := by decide

def taggedLow : Band := ⟨100, 60, 35, 11⟩
def boundaryLow : Band := ⟨100, 60, 35, 10⟩

/-- Eleven remembered low-confidence rescues restore strict order;
ten yield a tie, with final task outcomes unchanged. -/
theorem selective_memory_threshold_example :
    Valid taggedLow ∧ Valid boundaryLow ∧
    finalCorrect taggedLow = finalCorrect targetedLow ∧
    finalCorrect boundaryLow = finalCorrect targetedLow ∧
    creditedGap taggedLow targetedHigh = 1 ∧
    creditedGap boundaryLow targetedHigh = 0 := by decide

/-- Forgetting source information can cross the model's reversal boundary
without any change to original answers or final task outcomes. -/
theorem forgetting_crosses_boundary :
    taggedLow.initialCorrect = targetedLow.initialCorrect ∧
    taggedLow.rescued = targetedLow.rescued ∧
    finalCorrect taggedLow = finalCorrect targetedLow ∧
    0 < creditedGap taggedLow targetedHigh ∧
    creditedGap targetedLow targetedHigh < 0 := by decide

end ClinicalModels.AssistedSelfAssessment
