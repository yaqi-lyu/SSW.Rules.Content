---
type: rule
title: Do you know how to avoid design debt?
seoDescription: Making ad-hoc UI changes without a designer leads to design
  debt. Learn how to prevent inconsistencies and poor UX by following a better
  workflow.
uri: design-debt
authors:
  - title: Micaela Blank
    url: https://www.ssw.com.au/people/micaela-blank
  - title: Betty Bondoc
    url: https://www.ssw.com.au/people/betty-bondoc
  - title: Tiago Araujo
    url: https://www.ssw.com.au/people/tiago-araujo
created: 2025-04-23T11:45:00.000Z
related:
  - design-system
  - less-is-more
  - request-a-test-please
  - technical-debt
archivedreason: null
guid: e0d0ea3b-9b9f-465a-8da8-54f6f7280790
---

It’s tempting to fix small UI issues on the fly - change a button size, adjust some spacing, or tweak a color. But those “quick wins” often turn into long-term losses, leading to a messy, inconsistent UI that confuses users and slows development.

<!--endintro-->

Design debt is like technical debt: shortcuts that seem efficient in the moment create chaos down the line. Without a shared system, visual inconsistencies multiply, developers second-guess design intent, and user experience suffers.

## What causes design debt?

It usually starts with innocent intentions:

* "Just added a quick icon"
* "Tightened the padding a bit"
* "Didn't want to bother design - it's small"

We’ve all done it. But enough of these add up fast. Before you know it, the product starts to feel inconsistent, design is out of sync, and developers redo work they thought was already done.

## Why design debt matters

### 🚨 Why it happens

* Rushed timelines or MVP mindset ("we'll fix it later")
* No shared design system
* Designers and developers working in silos
* Unclear product direction or pivots

### 📉 Why it’s a problem

* Hurts user trust and usability
* Makes the product feel messy or inconsistent
* Slows future development and design
* Causes rework and team friction

### 🧹 How to manage it

* Run regular UX audits and design reviews
* Maintain a living design system or component library
* Include UI refactoring in your roadmap
* Document design decisions with clear rationale

## How to prevent design debt

### What to do before you code

Check if the change is already in the design system.  
✅ **If yes**: use it.  
❌ **If no**: ask yourself:

- Will users see this change?  
- Does it affect layout, spacing, interaction, or visuals?  

If the answer is **yes** (or you’re unsure), it involves design.  
👉 Ask for a **"Test Please"** and tag a designer on the PBI.
📌 *If it's a bigger change, create a PBI.*
If no designer is available or you're under time pressure, **log the Design Debt** and tag a designer for visibility.



## Example – The SSW Mega Menu

::: greybox
A stakeholder requested these dotted underlines, and they were implemented without design review.
:::

::: bad
![Figure: Bad example – Dotted lines added without design approval or alignment with the design system](https://github.com/user-attachments/assets/42b35115-99cc-4d31-9726-07c20ca36ae2)
:::

::: greybox
In this version, the developer tagged a designer for review before implementation.
:::

::: good
![Figure: Good example – A designer was tagged, reviewed the proposed dotted line, and flagged it as inconsistent with the product and design standards](https://github.com/user-attachments/assets/4c6eb728-084d-4b4f-874b-96a70255762b)
:::

## More ways to prevent design debt

* Screenshot your change and post it in the PBI before merging
* Ask for a quick "test please" from a designer 👀 on spacing, alignment, and component use
* Loop in design early on bigger stuff (e.g. layout or feature changes)
* After merge, let design know if you created something reusable

## Treat design like code

Every visual tweak changes the product - just like changing a line of code. So follow process, get the right people involved, and respect the system. 🤖
