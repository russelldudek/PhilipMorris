from pdf_common import *
def resume():
    s=[header("Russell Dudek","Business Process Excellence & Transformation Operator")]
    s+=section("Executive Profile")+[P("Operator-technologist who makes complex work visible, connects technical and business teams, and builds operating mechanisms that turn transformation into adopted, measurable outcomes. Career spans AI-first operations, manufacturing and quality systems, high-reliability technical programs, 24/7 logistics, distributed commercial operations, and agentic workflow design.","summary")]
    s+=section("Role-Aligned Capabilities")+[grid([(x,"") for x in ["End-to-End Process Redesign","Operating Model Design","Process Ownership & Decision Rights","Lean / Gemba / Root Cause","Quality Systems & Controls","Transformation Portfolio Prioritization","Adoption & Standard Work","ERP / Workflow Integration","AI-Assisted Process Design"]],3)]
    s+=section("Professional Experience")
    s+=[role("Vape-Jet","Director of Operations","2025–Present",[
        "Lead AI-first operating transformation across production, purchasing, quality, customer success, support, engineering issue flow, ERP/Odoo, Jira, HubSpot, Slack, telemetry, and AI-assisted workflows.",
        "Connect factory, field, customer, and machine-fleet signals into prioritized work, earlier risk detection, cleaner handoffs, dashboards, standard work, training, and accountability.",
        "Operate in a software-enabled robotics and machine-vision environment with approximately 1,000 fielded robots informing support and operating feedback loops."]),
        role("DudeWorth","Founder / AI and Automation Advisor","2017–Present",[
        "Develop AI-readiness and opportunity frameworks assessing value, feasibility, data readiness, governance, adoption burden, reuse, and time-to-value.",
        "Design agentic workflow patterns using structured context, retrieval, AI agents, human judgment, escalation, decision records, evaluation, and governance rails."]),
        role("Amazon","Operations Management / Site Leader","2014–2018",[
        "Led launch and execution for Amazon Prime Pittsburgh in a 24/7 customer-backward environment supporting approximately five million second-day orders annually.",
        "Built leadership routines, labor planning, throughput visibility, escalation paths, standard work, and operating mechanisms; applied Lean and Gemba practices across safety, quality, throughput, customer experience, and engagement."])]
    s+=[PageBreak(),header("Russell Dudek","Business Process Excellence & Transformation Operator","Candidate Vision · Resume")]
    s+=section("Professional Experience, Continued")
    s+=[role("Compunetics","Director of Operations and Engineering Management","2000–2013",[
        "Progressed through R&D program management, production management, strategic acquisition, operations management, and director-level leadership.",
        "Led engineering, manufacturing, quality, customer delivery, and complex technical programs in advanced electronics and high-reliability environments.",
        "Built quality systems, standard work, root-cause practices, performance measures, and process controls.",
        "Collaborated with high-consequence customers and partners including DoD, CERN, Intel, and AMD; published industry articles, delivered technical talks, and participated in the HyperTransport Consortium."]),
        role("Cardinal Building Products","Regional Director","2021–2023",[
        "Built the company’s first remote regional operation.",
        "Modernized distributed customer, CRM, commercial, fulfillment, logistics, digital marketing, SEO, and online-buying workflows."]),
        role("ZeusVu","Chief Pilot, Autonomous Systems and Aerial Data Operations","2018–2022",[
        "Led regulated drone operations across medical, energy, logistics, real-estate, and restricted-airspace contexts with a 100% safety record and no FAA incidents.",
        "Developed TensorFlow-based concepts for automated aerial inventory and designed medical drone delivery and chain-of-custody concepts."])]
    s+=section("Leadership, Education & Credentials")+[grid([
        ("Enviro Social Capital","Chairman of the Board, 2014–2017. Co-founded a public-private impact initiative and helped shape a $200 million Social Impact Bond feasibility concept."),
        ("IEEE Pittsburgh","CMPT and EDS Chapter Chair, 2012–2016. Led regional programming connecting industry, academia, manufacturing, and emerging technology."),
        ("University of Pittsburgh","Bachelor of Science; academic grounding includes materials science, physical chemistry, and biology-related studies."),
        ("Credentials","IBM Enterprise Design Thinking Practitioner · Six Sigma Certification · OSHA 10")],2)]
    s+=section("Technical Toolkit")+[P("Agentic AI · LLM workflows · RAG patterns · human-in-the-loop design · Python · SQL · JavaScript · TensorFlow · Tableau · ERP/Odoo · Jira · Confluence · HubSpot · Slack · GIS and mapping", "small")]
    build("Russell-Dudek-PMI-Resume.pdf",s,"Russell Dudek · PMI role-aligned resume")


def cover_letter():
    s=[header("Russell Dudek","Senior Manager, Business Process Excellence · PMI")]
    s += [Spacer(1,10),P("11 July 2026<br/><br/>Hiring Team<br/>Philip Morris International","body")]
    paras=[
    "PMI’s transformation creates a process-excellence problem that is more consequential than eliminating waste. A global enterprise is scaling a fast-growing smoke-free portfolio while still operating across different products, markets, channels, systems, and regulatory realities. The central question is how to know what must stay stable, what may legitimately vary, where process debt is hiding, and when evidence justifies changing the standard.",
    "That is the work I have spent my career doing from inside operations. At Vape-Jet, I lead AI-first operating transformation across production, purchasing, quality, customer success, support, engineering issue flow, ERP/Odoo, Jira, HubSpot, Slack, telemetry, and AI-assisted workflows. At Amazon, I built operating mechanisms and escalation paths in a 24/7 customer-backward environment supporting approximately five million second-day orders annually. At Compunetics, I led engineering, manufacturing, quality, customer delivery, and high-reliability technical programs.",
    "My thesis for the role is practical: Business Process Excellence should function as a <b>Process Genome</b>. Define the stable enterprise core of a process. Make legitimate market or regulatory variants explicit and reviewable. Expose harmful mutations such as workarounds, duplicate approvals, hidden queues, and zombie exceptions. Evolve the standard only when evidence shows a better way to create value, control risk, and sustain adoption.",
    "I would bring AI into the role with restraint. Automation is not the objective; better work is. Simplify and clarify the process first, then use AI or automation where context is sufficient, authority is explicit, economics are credible, and human judgment remains where consequence or ambiguity requires it.",
    "The obvious concern is that I have not spent my career inside tobacco or nicotine. That concern is fair. I would not confuse adjacent experience with domain mastery. What I bring is direct experience across manufacturing, quality, logistics, enterprise workflows, regulated operations, technical customer delivery, and AI-enabled work—plus a record of learning complex systems quickly and translating them into mechanisms people can use.",
    "I would welcome the opportunity to discuss where PMI’s greatest process friction sits today, how the organization distinguishes legitimate variation from process debt, and what success in this role must change for both executives and frontline users."
    ]
    s += [P(x,"letter") for x in paras] + [Spacer(1,5),P("Carpe diem,<br/><b>Russell Dudek</b>","letter")]
    build("Russell-Dudek-PMI-Cover-Letter.pdf",s,"Russell Dudek · PMI cover letter")


def brief():
    s=[header("Interview Thesis Brief","PMI · Senior Manager, Business Process Excellence")]
    s+=section("Mandate Hypothesis")+[P("Build an enterprise mechanism that turns cross-functional process friction into a governed portfolio of redesign interventions, separates necessary local variation from process debt, clarifies end-to-end ownership and decision rights, and proves whether redesigned work creates sustained business value.","summary")]
    s+=section("Company Moment")+[grid([("Portfolio transformation","PMI reports that its smoke-free business generated 43% of total global net revenues in Q1 2026, with more than 43 million estimated legal-age consumers across 108 markets."),("Transformation system","PMI describes transformation as powered by science, data, digital innovation, human judgment, and responsible decision-making.")])]
    s+=section("Operating Tensions")+[grid([(a,b) for a,b in [("Global vs local","Standardize enough to scale without flattening regulatory and market reality."),("Speed vs traceability","Transform quickly while preserving control logic and evidence."),("Ambition vs capacity","Prioritize against finite organizational change bandwidth."),("Visibility vs adoption","Data exposes friction; routines determine behavior."),("End-to-end vs function","Own outcomes without creating parallel bureaucracy.")]],2)]
    s+=section("White-Space Thesis")+[P("<b>Business Process Excellence should behave like a Process Genome:</b> define the stable core, make legitimate variants explicit, detect harmful mutations, and evolve standards from evidence.","summary")]
    s+=section("Strongest Objection")+[P("<b>Concern:</b> Russell has no direct tobacco/nicotine background. <b>Response:</b> acknowledge the gap, then make the adjacent-evidence argument across transformation, manufacturing and quality systems, high-reliability operations, regulated aviation, 24/7 logistics, and AI-enabled workflow design.","body")]
    s+=[PageBreak(),header("Thesis Brief · Proof & Discussion","Process excellence as a living enterprise system")]
    data=[[P("Evidence","h3"),P("Verified fact","h3"),P("Role relevance","h3")],
          [P("Vape-Jet","body"),P("Current AI-first operating transformation across business functions and systems.","small"),P("Direct redesign, handoffs, visibility, and adoption.","small")],
          [P("Amazon","body"),P("24/7 mechanisms supporting approximately five million second-day orders annually.","small"),P("Scale, cadence, flow, ownership, escalation.","small")],
          [P("Compunetics","body"),P("High-reliability engineering, manufacturing, quality systems, controls, and root cause.","small"),P("Technical/business translation and control discipline.","small")],
          [P("DudeWorth","body"),P("AI-readiness and agentic workflow patterns with human judgment and governance rails.","small"),P("AI tied to work, economics, governance, and adoption.","small")]]
    t=Table(data,colWidths=[28*mm,92*mm,60*mm]);t.setStyle(TableStyle([("GRID",(0,0),(-1,-1),.5,LINE),("BACKGROUND",(0,0),(-1,0),LIGHT),("VALIGN",(0,0),(-1,-1),"TOP"),("PADDING",(0,0),(-1,-1),6)]));s+=section("Proof Map")+[t]
    s+=section("First 120 Days")+[grid([("0–30 · Decode","Stakeholder map, taxonomy, two pilots, baseline scorecard, variant and exception inventory."),("31–60 · Make variation explicit","Process Genome maps, process contracts, decision rights, controls, and system seams."),("61–90 · Run targeted trials","Hypothesis-led interventions with outcome, flow, risk, economics, and behavior evidence."),("91–120 · Institutionalize learning","Portfolio governance, owner cadence, benefit validation, and scaling rules.")])]
    s+=section("Executive Questions")+bullets(["Where does PMI currently feel transformation friction most?","Which processes have true enterprise owners?","How does PMI distinguish required variation from process debt?","How are improvement benefits validated and sustained?","What decision authority does this role hold directly?","Where is process excellence experienced as overhead?"])
    s+=section("Research Basis")+[P("Official PMI corporate site and Q1 2026 progress indicators; PMI Value Report 2025 hub; PMI Careers overview; PMI ‘The human edge in the age of AI.’ The original job URL is preserved, but its body remained unavailable; no JD-specific responsibility or qualification was invented.","small")]
    build("PMI-Interview-Thesis-Brief.pdf",s,"Russell Dudek · PMI interview thesis brief")


def entry_plan():
    s=[header("120-Day Entry Plan","PMI · Senior Manager, Business Process Excellence")]
    s+=section("Entry Principle")+[P("<b>Earn the right to standardize.</b> Begin by learning where process truth lives, how variation is justified, where ownership breaks, and which measures already have credibility. Produce proof—not a theater of templates.","summary")]
    data=[[P("Window","h3"),P("Objective","h3"),P("Actions and output","h3")],
    [P("0–30","body"),P("Decode","body"),P("Map sponsors, owners, markets, functions, technology, governance, and frontline users. Select two pilots; baseline outcome, flow, control, economics, adoption, and learning. Output: accepted pilots and explicit data gaps.","small")],
    [P("31–60","body"),P("Make variation explicit","body"),P("Build Process Genome maps and process contracts. Classify variants as mandated, strategic, temporary, or unjustified. Output: agreement on legitimate variation versus inherited process debt.","small")],
    [P("61–90","body"),P("Run targeted trials","body"),P("Prioritize interventions by value, risk, feasibility, adoption burden, and reuse. Simplify before automating; instrument trials. Output: evidence of improvement, failure, or displaced burden.","small")],
    [P("91–120","body"),P("Institutionalize learning","body"),P("Establish portfolio governance, owner cadence, process-health scorecard, variant arbitration, exception review, and benefit validation. Output: aligned next-wave priorities and scaling logic.","small")]]
    t=Table(data,colWidths=[18*mm,38*mm,124*mm]);t.setStyle(TableStyle([("GRID",(0,0),(-1,-1),.5,LINE),("BACKGROUND",(0,0),(-1,0),LIGHT),("VALIGN",(0,0),(-1,-1),"TOP"),("PADDING",(0,0),(-1,-1),6)]));s+=section("Work Plan")+[t]
    s+=section("Guardrails")+[grid([("No improvement theater","Maps and workshops are inputs; changed decisions, handoffs, controls, flow, economics, and adoption are outcomes."),("No global uniformity fiction","Required market and regulatory variation stays visible and governed."),("No automation before clarity","Simplify, remove, and clarify first; automate only stable work with explicit authority."),("No benefit without sustainment","A change succeeds only when the business owns it after project support recedes.")])]
    build("PMI-120-Day-Entry-Plan.pdf",s,"Russell Dudek · PMI 120-day entry plan")


def objection():
    s=[header("Hard-Objection Analysis","PMI · Senior Manager, Business Process Excellence")]
    s+=section("The Objection, Plainly")+[P("PMI could hire a process leader who already understands tobacco or nicotine regulation, a global consumer-goods matrix, the company’s market structures, internal systems, and specific process language. Russell would have a real ramp.","summary")]
    s+=section("What Not to Claim")+[grid([("No direct nicotine expertise","Adjacent cannabis-tech operations, regulated drone operations, manufacturing, and chemistry grounding do not equal tobacco-domain mastery."),("No PMI-scale ownership claim","Amazon and Compunetics demonstrate scale and complexity; they should not be rewritten as ownership of a comparable global enterprise-transformation portfolio.")])]
    data=[[P("PMI need","h3"),P("Adjacent verified evidence","h3"),P("Transfer logic","h3")],
    [P("Cross-functional redesign","small"),P("Vape-Jet transformation spans operations, quality, support, systems, telemetry, and AI-assisted workflows.","small"),P("Direct practice across the seams where processes fail.","small")],
    [P("Operating mechanisms at scale","small"),P("Amazon 24/7 leadership supporting approximately five million second-day orders annually.","small"),P("Cadence, standard work, throughput visibility, and escalation.","small")],
    [P("Controls and consequence","small"),P("Compunetics high-reliability work; ZeusVu regulated operations with 100% safety and no FAA incidents.","small"),P("Change must respect control, traceability, and human authority.","small")],
    [P("Technology-enabled redesign","small"),P("DudeWorth AI-readiness and agentic workflow patterns with evaluation and governance rails.","small"),P("AI attached to specific work and decisions.","small")]]
    t=Table(data,colWidths=[42*mm,85*mm,53*mm]);t.setStyle(TableStyle([("GRID",(0,0),(-1,-1),.5,LINE),("BACKGROUND",(0,0),(-1,0),LIGHT),("VALIGN",(0,0),(-1,-1),"TOP"),("PADDING",(0,0),(-1,-1),5)]));s+=section("Transferability Case")+[t]
    s+=section("Best Interview Answer")+[P("“You should be concerned that I do not know PMI from the inside. My first job would be to learn the product, regulatory, market, and process realities from the people living them—not arrive with generic doctrine. What I bring is a career spent making complex work visible and redesigning the mechanisms around it: ownership, handoffs, controls, flow, escalation, systems, and adoption. I know how to learn a system without flattening it, then turn expert knowledge into work people can operate.”","summary")]
    build("PMI-Hard-Objection-Analysis.pdf",s,"Russell Dudek · PMI hard-objection analysis")
