# 11 — Learning-science references, verified (2026-10-16)

Method: every bibliographic field below was read from a page opened during this check. Sources were the Crossref API (`api.crossref.org/works/<doi>`), the arXiv API and arXiv HTML pages, the ACL Anthology DOI as recorded in Crossref, ERIC (`api.ies.ed.gov/eric`), PubMed, Open Library, publisher pages (Princeton UP, U Chicago Press, Cambridge), the ASU Chi-lab publication page, the showlab/Code2Video GitHub README, and the WordPress public API for Tao's blog.
Status key: **VERIFIED** = matches the brief. **CORRECTED** = the brief had something wrong, and the fix is stated. **PARTIAL** = the reference exists, but one detail could only be confirmed from secondary pages. **NOT FOUND** = could not be confirmed.

---

## A. AI tutoring and video-generation evidence

### Bastani et al. 2025 (PNAS) — VERIFIED (numbers exact)
- Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*, 122(26), e2422633122. https://doi.org/10.1073/pnas.2422633122 (PMID 40560616)
- Note: the full title includes the subtitle "Evidence from high school mathematics". This is an article number (e2422633122), not a page range.
- The abstract (from Crossref) gives these figures:
  - "48% improvement in grades for GPT Base and 127% for GPT Tutor", for practice while students had access.
  - "17% reduction in grades for GPT Base" once access was taken away, compared with students who never had access.
  - Mitigation, quoted (8 words): "These negative learning effects are largely mitigated by the safeguards in GPT Tutor."
- The brief left out the +127% practice gain for GPT Tutor. The study had nearly a thousand high-school math students in a field experiment.
- Tutor relevance: an unrestricted answer engine raises practice scores but lowers unaided performance ("crutch"). Hint-first, answer-withholding guardrails remove most of that harm.

### TheoremExplainAgent (Ku et al., ACL 2025) — VERIFIED, with one clarification
- Ku, M., Chong, T., Leung, J., Shah, K., Yu, A., & Chen, W. (2025). TheoremExplainAgent: Towards video-based multimodal explanations for LLM theorem understanding. In *Proceedings of the 63rd Annual Meeting of the ACL (Vol. 1: Long Papers)*, pp. 6663–6684. https://doi.org/10.18653/v1/2025.acl-long.332 ; arXiv:2502.19400 (v2, "accepted to ACL 2025 main, camera ready").
- Table 1 (overall success rate for complete videos): o3-mini (medium) **93.8%**, GPT-4o **55.0%**, Gemini 2.0-Flash **14.6%**, Claude 3.5-Sonnet v1 **2.1%**. All four match the brief.
  - Watch-out: Claude 3.5-Sonnet + RAG also scores 14.6%, the same as Gemini without RAG.
  - RAG variants: GPT-4o 45.8%, Gemini 20.4%, o3-mini 82.1%.
- Table 2, "Element Layout", scored only on videos that were generated successfully: GPT-4o 0.59, Claude 0.57, Gemini 0.57, o3-mini 0.61. Human-made Manim videos: **0.73**.
  - So the brief's "~0.59–0.61" should read **0.57–0.61**. The human 0.73 is correct.
  - Overall scores: o3-mini 0.77, human 0.77.
  - Human videos score 0.70 on Logical Flow, below every non-RAG agent (0.80–0.89).
- Tutor relevance: agentic planning is needed for long-form visual explanations. Layout is the weakest dimension. Multimodal explanations expose reasoning flaws that text alone hides.

### Code2Video (showlab) — CORRECTED (venue and numbers)
- Chen, Y., et al. (3 authors) (2025). Code2Video: A code-centric paradigm for educational video generation. arXiv:2510.01174 (v1, 1 Oct 2025; only v1 exists). https://arxiv.org/abs/2510.01174 ; code: https://github.com/showlab/Code2Video
- Venue, per the README: accepted to the **DL4C workshop at NeurIPS 2025** (2025-09-22), then to **ICML 2026** (2026-05-01). There is no DOI or proceedings page yet, so cite it as arXiv + "ICML 2026" per the authors.
- Numbers, from Table 1 of the arXiv HTML (VLM-judge, **100-point scale**, not 0–1):
  - Element Layout (EL) for Code2Video: 70.3 (Gemini-2.5 Pro, GPT-4o), 77.0 (o4-mini), 75.5 (GPT-5), 82.8 (GPT-4.1), **90.6** (Claude Opus 4.1). Human 3B1B: 98.3.
  - The brief's "layout 0.88–0.91" matches only the best backbone (90.6/100). It does not hold as a range.
  - "+40%" is the abstract's wording: "40% improvement over direct code generation".
  - The table actually reports point gains over the same backbone used for plain code generation: Avg +39.5 / +44.8 / +50.1 and TeachQuiz +43.5 / +45.0 / +46.0 for GPT-5 / GPT-4.1 / Claude Opus 4.1.
  - My table read came from a garbled HTML extraction. Check against the PDF before quoting individual cells.
- Tutor relevance: Planner → Coder → Critic, with visual-anchor layout critique, roughly doubles quality over one-shot code. "TeachQuiz" measures whether a video actually transfers knowledge.

### LearnLM — VERIFIED
- Jurenka, I., et al. (74 authors) (2024). Towards responsible development of generative AI for education: An evaluation-driven approach. arXiv:2407.12687 (v4).
  - Named principles (§4.3.1, pedagogy rubrics): "encourage active learning", "manage cognitive load", "deepen metacognition", "motivate and stimulate curiosity", "adapt to learners' goals and needs".
  - Critic headings (App. M): "Don't reveal the answer", "Guide towards the answer", "Promote active engagement", "Identify and address misconceptions", "Adapt to learner's level", and others.
- LearnLM Team (first-listed author; 46 names) (2024). LearnLM: Improving Gemini for learning. arXiv:2412.16429 (v3).
  - Framing: "pedagogical instruction following".
  - Rubric categories visible in §4: "inspiring active learning", "deepening metacognition", "stimulating curiosity".
  - Experts preferred LearnLM by +31% over GPT-4o, +11% over Claude 3.5 Sonnet, and +13% over Gemini 1.5 Pro.
- Tutor relevance: express pedagogy as explicit system-level instructions, and evaluate against named rubric dimensions.

### Bloom 1984 — VERIFIED
- Bloom, B. S. (1984). The 2 sigma problem: The search for methods of group instruction as effective as one-to-one tutoring. *Educational Researcher*, 13(6), 4–16. https://doi.org/10.3102/0013189X013006004
- Claim: under tutoring plus mastery learning, the average tutored student was above about 98% of the conventional-class students (≈2σ). Mastery learning alone was ≈1σ (84%). Detail from secondary pages that quote the paper.

### VanLehn 2011 — VERIFIED
- VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist*, 46(4), 197–221. https://doi.org/10.1080/00461520.2011.611369 (ERIC EJ946764)
- The ERIC abstract says human tutoring "d = 0.79" (not 2.0), and intelligent tutoring systems "0.76, so they are nearly as effective as human tutoring".
- Tutor relevance: realistic ceiling about 0.8σ. Step-level interaction is what matters, not finer granularity.

---

## B. Memory and study strategies

### Dunlosky et al. 2013 — VERIFIED
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques: Promising directions from cognitive and educational psychology. *Psychological Science in the Public Interest*, 14(1), 4–58. https://doi.org/10.1177/1529100612453266
  - Crossref gives only the main title. The subtitle is from the standard citation and was not seen on the page.
- Abstract ratings:
  - **High** utility: practice testing, distributed practice.
  - **Moderate**: elaborative interrogation, self-explanation, interleaved practice.
  - **Low**: the remaining five, which are summarization, highlighting, keyword mnemonic, imagery for text, and rereading. These are listed among the 10 techniques; the "low" label comes from the abstract continuation, which was truncated in my fetch.

### Roediger & Karpicke 2006 — VERIFIED
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science*, 17(3), 249–255. https://doi.org/10.1111/j.1467-9280.2006.01693.x
  - The subtitle is not in Crossref's title field.
- Claim: restudying wins at 5 minutes, but prior testing gives much better retention at 2 days and 1 week, even though restudy raised students' confidence.

### Karpicke & Blunt 2011 — VERIFIED
- Karpicke, J. D., & Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. *Science*, 331(6018), 772–775. https://doi.org/10.1126/science.1199327
- Claim: retrieval practice beat concept mapping on meaningful learning of science texts. Note the published methodological critique: Mintzes et al. 2011, *Science* 334:453.

### Slamecka & Graf 1978 — VERIFIED
- Slamecka, N. J., & Graf, P. (1978). The generation effect: Delineation of a phenomenon. *Journal of Experimental Psychology: Human Learning and Memory*, 4(6), 592–604. https://doi.org/10.1037/0278-7393.4.6.592
- Claim: across 5 experiments, self-generated words were remembered better than words that were only read, on recognition and on recall.

### Bjork 1994 — VERIFIED (minor page discrepancy)
- Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. P. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press. https://doi.org/10.7551/mitpress/4561.003.0011
  - Crossref gives pp. 185–206. SERC and the scanned copy give 185–205.
- Claim: conditions that speed acquisition can hurt long-term retention. "Desirable difficulties" (spacing, interleaving/variation, reduced feedback) help it. Learners misread their own fluency as learning.

### Fiorella & Mayer 2013 / 2014 — VERIFIED
- Fiorella, L., & Mayer, R. E. (2013). The relative benefits of learning by teaching and teaching expectancy. *Contemporary Educational Psychology*, 38(4), 281–288. https://doi.org/10.1016/j.cedpsych.2013.06.001
  - Claim, from the matching UCSB thesis abstract: preparing to teach helps on an immediate test. Actually teaching (explaining on video) helps on a delayed test (d = .79, .90).
- Fiorella, L., & Mayer, R. E. (2014). Role of expectations and explanations in learning by teaching. *Contemporary Educational Psychology*, 39(2), 75–85. https://doi.org/10.1016/j.cedpsych.2014.01.001
- Broader: Fiorella & Mayer (2016). Eight ways to promote generative learning. *Educational Psychology Review*, 28(4), 717–741. https://doi.org/10.1007/s10648-015-9348-9
  - Crossref's online date is 2015-11-21; the issue is 2016.

---

## C. Understanding and conceptual change

### Chi, Bassok, Lewis, Reimann & Glaser 1989 — VERIFIED
- *Cognitive Science*, 13(2), 145–182. "Self-explanations: How students study and use examples in learning to solve problems." https://doi.org/10.1207/s15516709cog1302_1
- Claim: "Good" students generate many self-explanations that tie example steps to principles, and they monitor their own understanding accurately. "Poor" students do not, and end up leaning on the examples.

### Chi, de Leeuw, Chiu & LaVancher 1994 — VERIFIED
- *Cognitive Science*, 18(3), 439–477. "Eliciting self-explanations improves understanding." https://doi.org/10.1207/s15516709cog1803_3
- Claim: simply prompting 8th-graders to self-explain each line gave larger gains. High explainers all reached the correct mental model.

### Chi, Slotta & de Leeuw 1994 — CORRECTED (venue)
- Chi, M. T. H., Slotta, J. D., & de Leeuw, N. (1994). From things to processes: A theory of conceptual change for learning science concepts. ***Learning and Instruction***, 4(1), 27–43. https://doi.org/10.1016/0959-4752(94)90017-5
  - This is not a *Cognitive Science* paper.
- Claim: robust misconceptions are ontological category mistakes (treating a process as matter), and fixing them needs a category shift.

### Chi 2008 — CORRECTED (book title)
- Chi, M. T. H. (2008). Three types of conceptual change: Belief revision, mental model transformation, and categorical shift. In S. Vosniadou (Ed.), ***International Handbook of Research on Conceptual Change*** (pp. 61–82). New York: Routledge.
  - Pages are from the ASU Chi-lab record. Book title and publisher are from Open Library (Routledge, 2008).
  - ASU's own record says "Handbook of research on conceptual change … Hillsdale, NJ: Erlbaum". Prefer the Routledge title.
  - Author PDF: https://education.asu.edu/lcl/publications/chi-m-t-h-2008-three-types-conceptual-change-belief-revision-mental-model
- This is the canonical source for the three misconception levels: false beliefs → belief revision; flawed mental models → mental-model transformation; category mistakes → categorical shift.

### Posner, Strike, Hewson & Gertzog 1982 — VERIFIED
- Accommodation of a scientific conception: Toward a theory of conceptual change. *Science Education*, 66(2), 211–227. https://doi.org/10.1002/sce.3730660207
- Conditions: dissatisfaction with the current conception, and a new conception that is intelligible, plausible, and fruitful. Condition names are from secondary summaries and the paper's first page.

### Linn — knowledge integration — CORRECTED (process labels)
- Canonical chapter: Linn, M. C. (2006). The knowledge integration perspective on learning and instruction. In R. K. Sawyer (Ed.), *The Cambridge Handbook of the Learning Sciences* (pp. 243–264). Cambridge University Press. https://doi.org/10.1017/CBO9780511816833.016
  - Crossref's online date is 2005-04-24. The print year is 2006 (Open Library).
- Book: Linn, M. C., & Eylon, B.-S. (2011). *Science learning and instruction: Taking advantage of technology to promote knowledge integration*. New York: Routledge. ISBN 9780805860542 (hb) / 9780805860559 (pb).
- The four processes are named "Elicit ideas, Add ideas, Distinguish ideas, **Sort out ideas**" in Linn, Slotta, Terashima, Stone & Madhok (2010), APFSLT 11(2) foreword, which cites Linn 2006 and Eylon & Linn.
  - The fourth label is **"sort out"**, not "reflect". Reflection is how students do the sorting out.

### Clement 1993 — VERIFIED
- Clement, J. (1993). Using bridging analogies and anchoring intuitions to deal with students' preconceptions in physics. *Journal of Research in Science Teaching*, 30(10), 1241–1257. https://doi.org/10.1002/tea.3660301007
- Claim: start from a correct "anchoring" intuition, then use a chain of bridging analogies to reach the target case. This produced large pre/post gains. Students' useful prior knowledge deserves as much attention as their misconceptions.

### Fyfe, McNeil, Son & Goldstone 2014 — CORRECTED (DOI)
- Concreteness fading in mathematics and science instruction: A systematic review. *Educational Psychology Review*, 26(1), 9–25. https://doi.org/10.1007/s10648-014-9249-3 (ERIC EJ1036777)
  - The DOI is s10648-**014**-9249-3. The "013" form does not resolve.
- Claim: begin concrete, then explicitly and gradually fade to the abstract. This grounds symbols and helps learners strip away irrelevant surface details.

### Sweller 1988 — VERIFIED
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257–285. https://doi.org/10.1207/s15516709cog1202_4
- Claim: means-ends problem solving uses up the capacity needed to build schemas, so plain problem solving is an inefficient way to learn.

### Kalyuga, Ayres, Chandler & Sweller 2003 — VERIFIED
- The expertise reversal effect. *Educational Psychologist*, 38(1), 23–31. https://doi.org/10.1207/S15326985EP3801_4
- Claim: guidance that helps novices can become useless or harmful for more expert learners, so instruction must adapt to expertise.

### Paivio — dual coding — VERIFIED (both books)
- Paivio, A. (1971). *Imagery and verbal processes*. New York: Holt, Rinehart and Winston. Confirmed by the Science 1972 review record (10.1126/science.176.4035.628-b) and Open Library; reprinted by Erlbaum in 1979.
- Paivio, A. (1986). *Mental representations: A dual coding approach*. Oxford University Press. Open Library has first publication 1986; Crossref has OUP's 1990 Oxford Psychology Series edition, https://doi.org/10.1093/acprof:oso/9780195066661.001.0001
- Cite 1986 for the mature theory.

### Mayer — Multimedia Learning — VERIFIED
- Mayer, R. E. (2020). *Multimedia learning* (3rd ed.). Cambridge University Press. https://doi.org/10.1017/9781316941355
  - Earlier editions: 2001 (1st) and 2009 (2nd), per Open Library.
- Claim: 15 evidence-based design principles for multimedia instruction. Examples are coherence, signaling, and modality. Names other than the count are not checked here.

---

## D. Mathematics-specific

### Thurston 1994 — VERIFIED
- Thurston, W. P. (1994). On proof and progress in mathematics. *Bulletin of the AMS*, 30(2), 161–178. https://doi.org/10.1090/S0273-0979-1994-00502-6 ; arXiv:math/9404236
  - Pages are from Crossref (161–178). The AMS landing page was not opened.
- Claim: progress in mathematics is mainly about human understanding (pictures, intuitions, ways of thinking), and formal proofs do not capture all of it.

### Tao — three stages — PARTIAL (date)
- Tao, T. "There's more to mathematics than rigour and proofs." *What's new* (blog), Career advice. https://terrytao.wordpress.com/career-advice/theres-more-to-mathematics-than-rigour-and-proofs/
- Date:
  - The page itself shows no date.
  - The WordPress API gives `date` 2007-05-06 (the same timestamp as sibling career-advice pages, so probably a container date) and `modified` 2024-01-21.
  - The earliest Wayback capture at this URL is 2018-02-01.
  - A web summary claiming "26 Nov 2022" is inconsistent with all of this.
  - Cite as "n.d., accessed 2026-10-16".
- Stages: pre-rigorous (intuition, examples), rigorous (precise and formal), post-rigorous (intuition re-grounded in rigour). Rigour is meant to destroy bad intuition and sharpen good intuition.

### Pólya 1945 — VERIFIED
- Pólya, G. (1945). *How to solve it*. Princeton University Press. Current Princeton edition 2014, foreword by John H. Conway.
- The four-phase list (understand, plan, carry out, look back) was **not** visible on the opened page. Treat the phase names as unverified until checked against the book.

### Toeplitz 1963 — VERIFIED
- Toeplitz, O. (1963). *The calculus: A genetic approach* (G. Köthe, Ed.; L. Lange, Trans.). University of Chicago Press. Reissued with a foreword by D. Bressoud.
- Claim: present calculus as the historical evolution of problems that motivated each idea, starting from the Greeks, not as finished technique.

### Swales 1990 — VERIFIED (book); CARS from secondary pages
- Swales, J. M. (1990). *Genre analysis: English in academic and research settings*. Cambridge University Press (Cambridge Applied Linguistics series). ISBN 0521328691 / 0521338131.
  - Confirmed by Open Library and the Crossref records for reviews in *Language* 69(1) and *SSLA* 15(1).
- CARS: Move 1 establish a territory, Move 2 establish a niche, Move 3 occupy the niche. These names come from secondary writing-centre pages.

---

## learning-science.md ready

| principle | rule for the tutor (one line) | verified reference |
|---|---|---|
| Guardrails over answer-giving | Default to hints and questions; never hand over the final answer on graded or practice items unless the learner has attempted it. | Bastani et al. 2025, PNAS 122(26) e2422633122 |
| Pedagogical instruction following | Encode pedagogy as explicit system rules (active learning, cognitive load, metacognition, curiosity, adaptivity) and evaluate turns against them. | Jurenka et al. 2024 arXiv:2407.12687; LearnLM Team 2024 arXiv:2412.16429 |
| Realistic tutoring ceiling | Aim for step-level interaction (feedback per step); expect ~0.8σ, not 2σ. | VanLehn 2011 EP 46(4):197–221; Bloom 1984 ER 13(6):4–16 |
| Retrieval practice | End each unit with closed-book recall of key ideas before any re-explanation. | Roediger & Karpicke 2006 PS 17(3):249–255; Karpicke & Blunt 2011 Science 331:772–775 |
| Spacing / interleaving | Schedule revisits across sessions and mix problem types. Do not mass-practice one type. | Dunlosky et al. 2013 PSPI 14(1):4–58; Bjork 1994 (MIT Press, pp. 185–205) |
| Low-utility habits | Do not suggest rereading, highlighting or summarizing as main study moves. | Dunlosky et al. 2013 |
| Generation | Ask the learner to produce the next step, definition or example before showing it. | Slamecka & Graf 1978 JEP:HLM 4(6):592–604 |
| Desirable difficulty | Allow productive struggle; warn that fluent rereading feels like learning but is not. | Bjork 1994 |
| Self-explanation | After each worked step, prompt "why does this step follow / what principle?" | Chi et al. 1989 CogSci 13(2):145–182; Chi et al. 1994 CogSci 18(3):439–477 |
| Diagnose misconception type | Classify the error as false belief, flawed mental model, or category mistake, and pick refutation, model repair, or re-categorization. | Chi 2008 (Vosniadou, Intl Handbook of Research on Conceptual Change, pp. 61–82); Chi, Slotta & de Leeuw 1994 L&I 4(1):27–43 |
| Conceptual change conditions | Before replacing an idea, create dissatisfaction with it, then make the new idea intelligible, plausible and fruitful. | Posner et al. 1982 Sci Ed 66(2):211–227 |
| Knowledge integration | Elicit the learner's ideas → add a new idea → distinguish between ideas → have the learner sort them out. | Linn 2006 Cambridge Handbook LS pp. 243–264; Linn & Eylon 2011 (Routledge) |
| Bridging analogies | Start from a correct anchoring intuition and bridge to the target through intermediate cases. | Clement 1993 JRST 30(10):1241–1257 |
| Concreteness fading | Concrete example → visual/iconic → symbolic, with explicit fading. | Fyfe et al. 2014 EPR 26(1):9–25 |
| Cognitive load | Use worked examples and goal-free subproblems for novices; avoid unguided search early on. | Sweller 1988 CogSci 12(2):257–285 |
| Expertise reversal | Fade guidance as competence shows; drop redundant explanation for advanced learners. | Kalyuga et al. 2003 EP 38(1):23–31 |
| Dual coding / multimedia | Pair each key idea with a picture or diagram plus words; cut decoration that is not essential. | Paivio 1986 (OUP); Mayer 2020 *Multimedia Learning* 3rd ed. (CUP) |
| Video explanations | Generate visuals by plan → code → critique, and check layout explicitly; layout is the weakest dimension. | Ku et al. 2025 ACL pp. 6663–6684; Code2Video arXiv:2510.01174 (ICML 2026 per authors) |
| Learning by teaching | Have the learner explain the idea back as if teaching someone else; this helps delayed retention. | Fiorella & Mayer 2013 CEP 38(4):281–288; 2014 CEP 39(2):75–85 |
| Understanding over formal proof | Pair each formal step with the intuition or picture behind it. | Thurston 1994 BAMS 30(2):161–178 |
| Rigour stages | Detect pre-rigorous, rigorous or post-rigorous mode and do not force formalism too early or too late. | Tao, blog "There's more to mathematics than rigour and proofs" (n.d.) |
| Genetic method | Introduce a concept through the historical problem that forced it. | Toeplitz 1963 (U Chicago Press) |
| Problem-solving heuristics | Use heuristic questions (related problem? work backwards?). | Pólya 1945 (Princeton) — four-phase names **unverified — do not cite** the phase list |
| Paper-introduction moves (CARS) | When tutoring academic writing, check the territory → niche → occupy moves. | Swales 1990 (CUP) — move names from secondary pages; check against the book before quoting |
