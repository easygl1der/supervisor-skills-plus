# Learning science behind the study protocol

## Contents
1. Principles and how each becomes a rule here
2. Why quizzes and spaced review are optional
3. Why no Manim by default
4. References (all verified 2026-10-16)

Every reference below was checked against the publisher, Crossref, arXiv or
ERIC on 2026-10-16 (`notes/11-learning-science-verified.md`). Claims we
could not verify are left out.

## 1. Principles and rules

| Principle | Rule in this skill | Reference |
|---|---|---|
| Unrestricted AI help can harm learning | Hints before answers by default; one question at a time. In a field experiment, practice grades rose 48% with plain GPT-4 and 127% with a hint-based tutor, but students who had the plain version scored 17% lower once access was removed; the tutor's safeguards largely removed that harm. | Bastani et al. 2025 |
| Pedagogy as explicit rules | The protocol and its checklist are the tutor's rules: active learning, manage cognitive load, adapt to the learner, stimulate curiosity, deepen metacognition. | Jurenka et al. 2024; LearnLM Team 2024 |
| Self-explanation | The learner restates in their own words (protocol step 6); in proofs, each step asks which fact it uses. | Chi et al. 1989; Chi et al. 1994 |
| Learning by explaining to others | The restatement is aimed at an outsider ("could you tell it to someone outside the field?"). | Fiorella & Mayer 2013, 2014 |
| Misconception types | Diagnosis labels each misconception as a false belief, a flawed mental model, or a category mistake, and repairs it accordingly. | Chi 2008; Chi, Slotta & de Leeuw 1994 |
| Conceptual change | Before replacing an idea, a counterexample creates dissatisfaction with it; the new idea must be intelligible, plausible and fruitful. | Posner et al. 1982 |
| Knowledge integration | Elicit the learner's ideas, add a new one, distinguish between them, let the learner sort them out: correction starts from the learner's associations. | Linn 2006; Linn & Eylon 2011 |
| Bridging analogies | Links to known concepts start from a correct anchor and go through intermediate cases when the gap is large; say where the analogy breaks. | Clement 1993 |
| Concreteness fading | Example, then general case, then formal definition. | Fyfe et al. 2014 |
| Cognitive load and expertise reversal | Short chunks and worked examples for new material; fade guidance and shorten rounds when the learner shows competence. | Sweller 1988; Kalyuga et al. 2003 |
| Dual coding and multimedia | Every concept gets a picture next to the words, with only the relations that matter. | Paivio 1986; Mayer 2020 |
| Generation and desirable difficulty | The learner produces the restatement before the tutor fills gaps; struggle is allowed, rereading is not mistaken for learning. | Slamecka & Graf 1978; Bjork 1994 |
| Realistic expectations | One-to-one tutoring helps, but the large "2 sigma" figure is not the norm; step-level tutoring reached about 0.8 sigma in a review. | Bloom 1984; VanLehn 2011 |
| Understanding in mathematics | Pair each formal step with its intuition or picture; aim for post-rigorous understanding (intuition checked by rigour). | Thurston 1994; Tao (blog, n.d.) |
| Genetic (historical) method | Motivation and history come before the definition. | Toeplitz 1963 |

## 2. Why quizzes and spaced review are optional

Retrieval practice and distributed practice have the strongest evidence for
long-term retention, and rereading, highlighting and summarizing the weakest
(Dunlosky et al. 2013; Roediger & Karpicke 2006; Karpicke & Blunt 2011).
The owner's goal is understanding for research, not exam recall, so the
default spends effort on restatement and correction (themselves retrieval
of a kind) and offers quizzes, confidence ratings and Anki export as
options. Notes-only mode is labelled as the low-value mode for this reason.
[src: user:2026-10-16] (confirmed)

## 3. Why no Manim by default

In TheoremExplainAgent, full Manim video generation succeeded for 93.8% of
theorems with o3-mini, 55.0% with GPT-4o, 14.6% with Gemini 2.0 Flash and
2.1% with Claude 3.5 Sonnet; layout scored 0.57 to 0.61 against 0.73 for
human-made videos (Ku et al. 2025). Code2Video improved layout with a
planner, coder and a critic that looks at rendered frames (arXiv
2510.01174). This kit takes the critic idea (render, look, fix) and uses
HTML steppers instead of video. [src: user:2026-10-16] (confirmed)

## 4. References

- Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS* 122(26), e2422633122. doi:10.1073/pnas.2422633122
- Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about Knowing* (pp. 185–205). MIT Press.
- Bloom, B. S. (1984). The 2 sigma problem. *Educational Researcher* 13(6), 4–16.
- Chi, M. T. H. (2008). Three types of conceptual change. In S. Vosniadou (Ed.), *International Handbook of Research on Conceptual Change* (pp. 61–82). Routledge.
- Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). Self-explanations. *Cognitive Science* 13(2), 145–182.
- Chi, M. T. H., de Leeuw, N., Chiu, M.-H., & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science* 18(3), 439–477.
- Chi, M. T. H., Slotta, J. D., & de Leeuw, N. (1994). From things to processes. *Learning and Instruction* 4(1), 27–43.
- Clement, J. (1993). Using bridging analogies and anchoring intuitions to deal with students' preconceptions in physics. *Journal of Research in Science Teaching* 30(10), 1241–1257.
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest* 14(1), 4–58.
- Fiorella, L., & Mayer, R. E. (2013). The relative benefits of learning by teaching and teaching expectancy. *Contemporary Educational Psychology* 38(4), 281–288.
- Fiorella, L., & Mayer, R. E. (2014). Role of expectations and explanations in learning by teaching. *Contemporary Educational Psychology* 39(2), 75–85.
- Fyfe, E. R., McNeil, N. M., Son, J. Y., & Goldstone, R. L. (2014). Concreteness fading in mathematics and science instruction. *Educational Psychology Review* 26(1), 9–25. doi:10.1007/s10648-014-9249-3
- Jurenka, I., et al. (2024). Towards responsible development of generative AI for education. arXiv:2407.12687.
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist* 38(1), 23–31.
- Karpicke, J. D., & Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. *Science* 331(6018), 772–775.
- Ku, M., et al. (2025). TheoremExplainAgent. *Proceedings of ACL 2025*, pp. 6663–6684. doi:10.18653/v1/2025.acl-long.332
- LearnLM Team (2024). LearnLM: Improving Gemini for learning. arXiv:2412.16429.
- Linn, M. C. (2006). The knowledge integration perspective on learning and instruction. In R. K. Sawyer (Ed.), *The Cambridge Handbook of the Learning Sciences* (pp. 243–264). Cambridge University Press.
- Linn, M. C., & Eylon, B.-S. (2011). *Science Learning and Instruction: Taking Advantage of Technology to Promote Knowledge Integration*. Routledge.
- Mayer, R. E. (2020). *Multimedia Learning* (3rd ed.). Cambridge University Press.
- Paivio, A. (1986). *Mental Representations: A Dual Coding Approach*. Oxford University Press.
- Posner, G. J., Strike, K. A., Hewson, P. W., & Gertzog, W. A. (1982). Accommodation of a scientific conception. *Science Education* 66(2), 211–227.
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science* 17(3), 249–255.
- Slamecka, N. J., & Graf, P. (1978). The generation effect. *Journal of Experimental Psychology: Human Learning and Memory* 4(6), 592–604.
- Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science* 12(2), 257–285.
- Tao, T. (n.d.). There's more to mathematics than rigour and proofs. Blog post, terrytao.wordpress.com; accessed 2026-10-16.
- Thurston, W. P. (1994). On proof and progress in mathematics. *Bulletin of the AMS* 30(2), 161–178.
- Toeplitz, O. (1963). *The Calculus: A Genetic Approach*. University of Chicago Press.
- VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist* 46(4), 197–221.
- Code2Video (2025). arXiv:2510.01174 (showlab; NeurIPS 2025 DL4C workshop; ICML 2026 per the authors' README).

Titles above are shortened where the subtitle adds nothing for our use;
full titles are in `notes/11-learning-science-verified.md`.
