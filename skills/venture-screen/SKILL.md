---
name: venture-screen
description: >
  Use when the user is looking for, proposing, or evaluating a business idea:
  "what should I build", "here's an idea", "is this worth doing", "find me a startup
  idea", or /venture-screen. Generates candidates from several kinds of source, runs
  cheap structural checks before any long write-up, scores survivors on what makes an
  idea worth building, and always ends with a ranked list and one recommendation.
---

# Venture Screen

**The goal is to leave the session with something to build.** Screening orders and
de-risks candidates; it is not the output. A session that kills every idea has failed,
and the failure is almost always in how the ideas were generated, not in the market.

## Why this exists

Idea evaluation with an AI assistant tends to fail in one of two opposite ways. This
skill prevents both.

**Deep work before cheap checks.** A session writes a long concept note, a pricing
table, a validation plan and an outreach playbook, then kills the idea on a question
that could have been answered in five minutes. A typical case: a product that audits a
vendor's performance, where the vendor itself controls access to the data the audit
needs. The answer was fatal from the first message. The fix is order of operations.

**A screen with no way to say yes.** Candidates are found by searching what already
exists in a space, then rejected because it exists. Anything you can find with desk
research is already occupied, so a filter tuned on occupancy rejects everything it is
fed. Ten ways to fail an idea and none to pass one is not a screen. Both halves are
specified below.

## The prime directive

> **Nothing longer than one page until the idea survives Gate 1.**

No concept note, roadmap, pricing table, translation or validation spec. A killed idea
should cost twenty minutes, not a day. If the user asks for a full write-up before the
screen is done, run the screen first and say why: it takes minutes and may save the
write-up entirely.

## Step 0: the founder profile

Ideas are only good or bad for someone. Before generating anything, establish the
founder's position. If the user keeps a profile file (for example `founder-profile.md`
in the project), read it; otherwise ask, in one message:

1. **Assets:** money, team, skills, existing customers, audience, network, a company
   already registered, payment setup.
2. **Gaps:** what does *not* exist. Be blunt here; most people overstate their network.
3. **Constraints:** regulation they will or won't touch, time horizon, budget, whether a
   sales-led motion is acceptable.
4. **Shape:** must the outcome be a software product, or is a service business fine?
5. **Distribution:** which channels they can actually run (content, paid ads, outbound,
   community, search/AI search).
6. **Already killed:** ideas they have dropped before, and why.

Then apply the profile as filters. Common implications:

- **With no network, chase existing demand, never created demand.** The buyer has to be
  looking already: searching, asking an AI assistant, complaining in public. Anything
  that needs market education is unreachable from a cold start.
- **A team is not a differentiator.** Anyone can hire developers. The advantage has to
  come from distribution, accumulated data, or a niche too small for incumbents.
- **Reachability, not purchase mechanics, is the binding constraint.** Cold outbound,
  paid acquisition, content and demo-led sales all count as reachable. Needing warm
  introductions does not.

Constraints change. When the user reverses one ("a sales call is fine now"), stop
citing the old rule, and recheck earlier kills that rested on it.

## Where candidates come from

**This half decides the outcome; the gates cannot rescue a bad batch.** Ideas assembled
from listicles, "top N tools" pages and market overviews are pre-filtered to the
obvious, and the obvious is taken.

Every batch draws from at least **three** of these sources, never only the first:

1. **Desk research:** market analysis, category searches. Cheap and the weakest. At most
   a third of any batch.
2. **Something that changed recently:** a platform capability newly opened or closed, a
   price that collapsed, a standard that shipped. Change creates gaps before the market
   notices. Date the change and check it is under about 12 months old.
3. **Direct exposure:** what the founder, their team, or people they can cold-reach
   actually complain about. Ten conversations with operators in one industry beat
   another afternoon of searching.
4. **Deliberate un-legibility:** problems with no search volume because the people who
   have them have no vocabulary for them. They fail "existing searchable demand" and may
   still be right. Flag the reachability cost rather than auto-rejecting.
5. **An adjacent market's solved pattern:** a mechanism that works in one industry and
   has not crossed to another. Name both industries and why it hasn't crossed.
6. **Reframes of dead ideas:** the second-order finding from a kill is often the real
   business. Example: a "software for repair shops" idea dies on incumbents, but the
   kill shows the money sits in a countable recovered outcome that can be sold on
   contingency instead.

If a batch comes entirely from source 1, **do not gate it.** Say so and regenerate.

## Gate 1: structural (instant kill, ~10 minutes)

Any **NO** kills the idea. Do not design around it.

**1. Who controls the pipe to the data?**
If the party being measured, audited or cut out controls access to the data the product
needs, stop. One root like this usually produces several blockers at once: access
revocable at their discretion, terms that bar aggregation or competitive analysis, an
app-approval gate they hold. The marketing that makes such a product attractive is
exactly what gets it refused.
*Pass: the data sits on the customer's own systems, or the customer can export it as of
right.*

**2. Can the founder reach the buyer without a network?**
Ask whether the buyer is *reachable*, not whether they buy self-serve. Plans that need
warm introductions, an existing industry position, or pilots sourced from a network the
founder doesn't have fail here.

**3. Is there a claim to contradict, or a decision that changes?**
Information alone does not sell. A dashboard that changes no decision and challenges no
specific assertion is a "so what?" machine.

**4. Regulated?**
Anything that needs a licence the founder doesn't hold, or has a licensing timeline,
stops here unless the profile says otherwise.

## Gate 2: economic (~20 minutes, back-of-envelope arithmetic)

**5. Are you optimising the big number or the small one?**
List every cost in the customer's workflow and rank them. A common trap: building around
a $1 software fee when the human labour behind it costs $4–12.

**6. Can the customer act on the finding alone, and does acting pay?**
Model the recommendation. Advice that sounds obviously right ("switch off the part that
underperforms") can lose the customer money once you price the alternative. **Do the
break-even before writing the pitch.**

**7. Is the money recoverable, or only forward-looking?**
Contingency and success-fee pricing need something to claw back. If nothing can be
recovered, the value is future savings and the pricing should be flat.

Do the money arithmetic per customer, per year, before anything else. An idea can pass
every structural test and still be worth a few hundred dollars per customer.

## Gate 3: competitive (~20 minutes, web search required)

**8. Is the method already public?**
Search for the technique itself, not just company names. If the core insight is
published, maybe in a vendor's own help centre, differentiation has to come from
something other than the insight.

**9. Is an incumbent one feature away?**
**Competition is a headwind, not a verdict.** "Somebody already does this" is not a kill.
A crowded market is usually evidence of demand.

This is a kill **only** when all four hold at once:
1. an incumbent holds the same buyer *and* the same install path,
2. they already ship the thing, not merely could,
3. they can give it away as a feature of something the buyer already pays for, and
4. the founder has no distribution advantage and no niche the incumbent would decline.

Fewer than four: record it as a headwind, size it, keep the idea in the ranking, and say
which of the four apply. "Three of four" is a real answer and it is not a kill.

**10. Is the market actually sized?**
Count the customers who have the problem *and* can buy, not total companies in the
category. If this stays open through the whole analysis, that is a finding: nobody
checked the denominator.

## What a YES looks like

The gates say what sinks an idea. These say what makes one worth the next six months.
Score every survivor and recommend the highest, even when none is perfect.

- **A. Someone already pays for a worse version.** Existing budget beats estimated
  demand. Name the line item the money comes out of.
- **B. The first customer is reachable this month.** A named list, a search term with
  intent, or ten operators who will take a cold call.
- **C. The founder can be genuinely good at it within a quarter.** Not "we can build
  it"; anyone can build. Something where doing the work compounds into an advantage.
- **D. It compounds with what the founder already has.** An idea that strengthens their
  distribution is worth more than one that merely earns.
- **E. There is a cheap first proof.** One customer, one paid pilot, or one landing page
  with real conversions, inside four weeks, without building the whole thing.
- **F. Failure is affordable and instructive.** If it dies, the founder keeps a skill, a
  list, an audience or a dataset.

**Three of six is a build candidate. Five is a strong one.** Don't demand a moat on day
one: distribution, data and a niche too small to bother with are earned after launch,
not proven before it.

### Correct for the service bias

A service scores on A, B, E and F on day one; a software product scores on none of them
until it exists. Left alone, the top candidate will **always** be a service, and that is
an artefact of the scoring, not a finding about the market.

If the founder wants a product (Step 0, question 4):
- Score A, B, E and F against the **product**, not a service wrapped around it.
  "We could sell consulting into this demand" earns nothing.
- Hand-delivery to the first 5–10 customers is fine as **scaffolding with an expiry
  date**. Name when it expires. Scaffolding with no expiry is an agency.
- A candidate that needs humans in the loop permanently **fails**. Ask what accrues: a
  dataset, a workflow, a distribution position. If the answer is "a client list", it is
  a service.

## Patterns that look good and usually aren't

**Regulation-deadline ideas.** A dated, legally forced purchase looks irresistible.
These fail for the same reasons again and again: the deadline slips; free or bundled
compliance tools set the price floor; whoever already holds the customer when the rule
lands (the accountant, the bank, the incumbent software) owns distribution; and one or
two touches a year means no habit and heavy churn. If a regulation is the only reason a
product exists, it is not a product.

**Measurement products.** Products that report on work rather than do it. Demand is
real but served free by consultants' calculators and incumbents' dashboards, and the
honest version usually needs data the customer doesn't capture yet, which turns
onboarding into a behaviour-change project. Ask what it *does*, not what it *shows*.

**Problems sized only by vendors.** If every number quantifying a problem comes from
companies selling the fix, treat the problem as unsized. A real, large, countable loss
usually has someone independent counting it: an insurer, a regulator, a trade body, a
researcher.

**Over-solicited buyers.** Before generating ideas for a buyer type, screen the buyer:
is demand searchable, is their budget growing rather than shrinking, and is every tool
vendor already courting them with partner programmes and referral fees? Thin-margin
buyers whose model is under pressure (many small agencies, for example) are a red flag
in themselves.

**Credentials read as validation.** An accelerator admission or a standard-deal raise is
not proof the idea works; every company in the batch shows the same number. Check team
size, date and named traction before treating someone's startup as a proven business.

## Check facts before building on them

Company and platform facts go stale in weeks: renames, acquisitions, pricing changes,
API terms. Before an idea rests on a named company or platform, verify in one search its
current name, owner, funding, pricing model, and whether its API and terms still allow
what the plan assumes. Cite the date you checked.

## Batch, don't serialise

Generate **8–10 candidates** from at least three sources and run all of them through
Gate 1 before deep-diving any. A ranked shortlist after two hours beats one dead plan
after a day. Deep work is earned by ranking highest, not by being interesting and not by
being the last one standing.

## Artefact discipline

| Stage | Maximum artefact |
|---|---|
| Before Gate 1 | A few lines in chat |
| Passed Gate 1 | One page, in chat |
| Passed Gates 2 and 3 | One-page note saved to the project |
| Evidence of demand from a real buyer | Full concept note, roadmap, specs |
| Explicitly requested by the user | Translations, playbooks, pitches |

Never translate, never build a validation protocol, and never write a roadmap for an
idea that has not passed all three gates.

## Never end empty-handed

Close every session with a **ranked list and one named recommendation**: the best
available option even if every candidate has an open problem, plus *what would have to
be true* for it to work and the cheapest test of that.

"Everything died" is not a deliverable. If it happens:
1. Say plainly that the generator failed, not the market.
2. Regenerate from different sources before gating anything else.
3. If two batches in a row die, stop screening and change the input: go get direct
   exposure. More desk research will not help.

Record every kill with its structural reason (in the user's killed-ideas file if they
keep one), so the next session doesn't re-propose it.

## Session checklist

1. Read the founder profile and the killed list. Don't re-tread kills, but check whether
   any rested on a constraint the founder has since dropped; those may deserve a second
   look.
2. Ask the Step 0 questions the profile doesn't answer.
3. Generate 8–10 candidates **from at least three sources**. All desk research means
   regenerate before gating.
4. Gate 1 on everything, in chat, in minutes.
5. Verify company and platform facts, with a date.
6. State kill criteria *before* looking at evidence and don't renegotiate them after. A
   kill names a **structural** reason: arithmetic that doesn't work, a gatekeeper, an
   adversarial incentive, an unmeasurable input. "It exists already" is not one.
7. Write nothing long until all three gates pass.
8. **Close with a ranked list, one recommendation, what would have to be true, and the
   cheapest test.** Never an empty list.
