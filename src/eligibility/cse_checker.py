"""Eligibility evaluation engine for B.Tech Computer Science & Engineering graduates.
Candidate Profile:
- Degree: B.Tech in Computer Science & Engineering
- Graduation: 2026 (Fresher / Early-career)
- Age: ~23
- Category: General (EWS potential)
- Skills: MERN stack, Java, SQL, REST APIs, Git
"""

import re
from typing import Dict, Any, Tuple


class CandidateProfile:
    def __init__(
        self,
        degree: str = "B.Tech",
        branch: str = "Computer Science & Engineering",
        graduation_year: int = 2026,
        age: int = 23,
        category: str = "General",
        ews_eligible: bool = True,
        years_experience: float = 0.0,
        has_gate_cs: bool = False
    ):
        self.degree = degree
        self.branch = branch
        self.graduation_year = graduation_year
        self.age = age
        self.category = category
        self.ews_eligible = ews_eligible
        self.years_experience = years_experience
        self.has_gate_cs = has_gate_cs


class CSEEligibilityChecker:
    CSE_KEYWORDS = [
        "computer science", "cse", "computer engineering", "information technology",
        "it", "software engineering", "computer applications", "mca",
        "data science", "artificial intelligence", "cyber security",
        "computer technology", "electronics & computer"
    ]

    ANY_GRAD_KEYWORDS = [
        "any degree", "any graduate", "bachelor's degree in any discipline",
        "graduation in any discipline", "degree of a recognized university",
        "any recognized bachelor's degree", "graduate in any discipline"
    ]

    ANY_ENG_KEYWORDS = [
        "any engineering", "degree in engineering", "b.e./b.tech in any branch",
        "bachelor of engineering in any discipline", "engineering graduate"
    ]

    EXP_REQUIRED_KEYWORDS = [
        "minimum 2 years", "min 2 years", "3 years experience", "5 years experience",
        "post qualification experience of", "mandatory experience"
    ]

    def __init__(self, candidate: CandidateProfile = None):
        self.candidate = candidate or CandidateProfile()

    def check_eligibility(
        self,
        job_title: str,
        degree_req: str,
        branch_req: str,
        exp_req: str,
        age_min: int,
        age_max: int,
        requires_gate: bool = False
    ) -> Dict[str, Any]:
        """Evaluates whether the candidate meets all eligibility criteria."""
        notes = []
        is_eligible = False
        eligibility_type = "NOT_ELIGIBLE"

        # 1. Age Check
        age_ok = True
        if age_min and self.candidate.age < age_min:
            age_ok = False
            notes.append(f"Candidate age ({self.candidate.age}) is below minimum age ({age_min}).")
        if age_max and self.candidate.age > age_max:
            age_ok = False
            notes.append(f"Candidate age ({self.candidate.age}) exceeds maximum unreserved age ({age_max}).")

        # 2. Experience Check
        fresher_ok = True
        exp_text = f"{exp_req} {degree_req}".lower()
        if any(keyword in exp_text for keyword in self.EXP_REQUIRED_KEYWORDS):
            fresher_ok = False
            notes.append("Post requires mandatory prior experience (Fresher not eligible).")

        # 3. Qualification Check
        combined_text = f"{job_title} {degree_req} {branch_req}".lower()

        # Check explicit CSE eligibility
        cse_match = any(re.search(r'\b' + re.escape(kw) + r'\b', combined_text) for kw in self.CSE_KEYWORDS)
        # Check Any Engineering Degree
        any_eng_match = any(kw in combined_text for kw in self.ANY_ENG_KEYWORDS)
        # Check Any Bachelor's Degree
        any_grad_match = any(kw in combined_text for kw in self.ANY_GRAD_KEYWORDS)

        if not age_ok:
            eligibility_type = "AGE_INELIGIBLE"
            reason = f"Candidate age ({self.candidate.age}) outside acceptable bracket ({age_min}-{age_max} yrs)."
        elif not fresher_ok:
            eligibility_type = "EXPERIENCE_REQUIRED"
            reason = f"Role requires mandatory prior full-time experience: '{exp_req}'."
        elif cse_match:
            is_eligible = True
            eligibility_type = "CSE_EXPLICITLY_ELIGIBLE"
            reason = "B.Tech in Computer Science / IT is explicitly specified as an eligible discipline."
        elif any_eng_match:
            is_eligible = True
            eligibility_type = "ANY_ENGINEERING_ELIGIBLE"
            reason = "Degree in any branch of Engineering / Technology is accepted."
        elif any_grad_match:
            is_eligible = True
            eligibility_type = "ANY_BACHELORS_ELIGIBLE"
            reason = "Graduation in any recognized discipline is accepted (CSE satisfies this)."
        else:
            eligibility_type = "ELIGIBILITY_UNCERTAIN"
            reason = "Educational qualification text requires manual notification clause verification."

        # GATE Check
        if requires_gate and not self.candidate.has_gate_cs:
            notes.append("Requires valid GATE CSE score. Recommended for candidates with valid GATE CS.")

        return {
            "is_eligible": is_eligible,
            "eligibility_type": eligibility_type,
            "reason": reason,
            "notes": "; ".join(notes) if notes else "Fully qualified as a fresher General/EWS graduate."
        }
