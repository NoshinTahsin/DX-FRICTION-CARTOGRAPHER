# Single source of truth for DX dimensions and frameworks
DIMENSIONS = {
    "flow_state": {
        "name": "Flow State",
        "framework": "DevEx",
        "citation": "Noda, Greiler, Forsgren et al. — 'DevEx: What Actually Drives Productivity', ACM Queue, 2023",
        "definition": "Flow state refers to the optimal mental state where developers are fully immersed and focused on their work, leading to high productivity and satisfaction. It occurs when tasks match skill level and provide clear goals with immediate feedback. Interruptions and unclear objectives break this state, reducing overall developer effectiveness.",
        "friction_signals": [
            "Frequent context switching between tasks",
            "Unclear task requirements requiring constant clarification",
            "Long wait times for code reviews or CI feedback",
            "Mid-sprint requirement changes forcing work restarts",
            "Slow development environment setup or tool loading"
        ],
        "prompt_description": "state of deep focus and immersion in development work"
    },
    "feedback_loops": {
        "name": "Feedback Loops",
        "framework": "DevEx",
        "citation": "Noda, Greiler, Forsgren et al. — 'DevEx: What Actually Drives Productivity', ACM Queue, 2023",
        "definition": "Feedback loops measure how quickly developers receive information about their work quality and progress. Fast, actionable feedback enables rapid iteration and learning. Slow or unclear feedback creates uncertainty and reduces development velocity.",
        "friction_signals": [
            "Pull requests waiting days for review",
            "Test failures without clear error messages",
            "CI pipelines taking 30+ minutes to complete",
            "Unclear code review feedback focusing on style over substance",
            "Delayed deployment feedback from production monitoring"
        ],
        "prompt_description": "speed and quality of feedback on development work"
    },
    "cognitive_load": {
        "name": "Cognitive Load",
        "framework": "DevEx",
        "citation": "Noda, Greiler, Forsgren et al. — 'DevEx: What Actually Drives Productivity', ACM Queue, 2023",
        "definition": "Cognitive load represents the mental effort required to understand and work with the codebase and development processes. High cognitive load from complex architectures or unclear processes reduces problem-solving capacity. Well-designed systems minimize unnecessary mental overhead.",
        "friction_signals": [
            "Complex branching strategies causing confusion",
            "Inconsistent coding standards across the team",
            "Outdated documentation requiring extensive research",
            "Manual deployment checklists with many error-prone steps",
            "Multiple tools requiring different mental models"
        ],
        "prompt_description": "mental effort required for development tasks"
    },
    "satisfaction": {
        "name": "Satisfaction",
        "framework": "SPACE",
        "citation": "Forsgren, Storey et al. — 'The SPACE of Developer Productivity', ACM Queue, 2021",
        "definition": "Satisfaction measures developers' overall contentment with their work environment and processes. High satisfaction correlates with better retention and productivity. Factors include work-life balance, meaningful work, and positive team dynamics.",
        "friction_signals": [
            "Excessive overtime or crunch periods",
            "Lack of recognition for completed work",
            "Toxic team communication or blame culture",
            "Unclear career progression paths",
            "Repetitive, unengaging tasks"
        ],
        "prompt_description": "overall contentment with development work"
    },
    "efficiency": {
        "name": "Efficiency",
        "framework": "SPACE",
        "citation": "Forsgren, Storey et al. — 'The SPACE of Developer Productivity', ACM Queue, 2021",
        "definition": "Efficiency measures how productively developers use their time and resources. It includes both individual productivity and system-level optimizations that reduce wasted effort. Efficient processes allow developers to focus on value-creating activities.",
        "friction_signals": [
            "Time spent on manual processes that could be automated",
            "Waiting for other teams or approvals",
            "Debugging issues that recur due to lack of fixes",
            "Context switching between multiple projects",
            "Excessive meetings reducing coding time"
        ],
        "prompt_description": "productive use of time and resources"
    },
    "collaboration": {
        "name": "Collaboration",
        "framework": "SPACE",
        "citation": "Forsgren, Storey et al. — 'The SPACE of Developer Productivity', ACM Queue, 2021",
        "definition": "Collaboration assesses how effectively team members work together on shared goals. Strong collaboration enables knowledge sharing and collective problem-solving. Poor collaboration leads to duplicated effort and inconsistent solutions.",
        "friction_signals": [
            "Inconsistent tool adoption across team members",
            "Lack of code review knowledge sharing",
            "Siloed teams with poor communication",
            "Conflicting priorities between teams",
            "Difficulty finding expertise within the organization"
        ],
        "prompt_description": "effectiveness of team knowledge sharing and cooperation"
    },
    "performance": {
        "name": "Performance",
        "framework": "SPACE",
        "citation": "Forsgren, Storey et al. — 'The SPACE of Developer Productivity', ACM Queue, 2021",
        "definition": "Performance evaluates the outcomes and results of development work. It includes both individual achievements and team-level delivery metrics. High performance requires clear goals, proper tooling, and supportive processes.",
        "friction_signals": [
            "Unrealistic deadlines causing rushed work",
            "Lack of clear success metrics",
            "Technical debt slowing down new feature development",
            "Frequent production incidents reducing stability",
            "Inadequate testing leading to bug escapes"
        ],
        "prompt_description": "quality and success of development outcomes"
    },
    "activity": {
        "name": "Activity",
        "framework": "SPACE",
        "citation": "Forsgren, Storey et al. — 'The SPACE of Developer Productivity', ACM Queue, 2021",
        "definition": "Activity measures the volume and pace of development work completed. While not the only measure of productivity, consistent activity indicates healthy development processes. Low activity may signal bottlenecks or demotivation.",
        "friction_signals": [
            "Blocked work waiting for other teams",
            "Long review queues delaying merges",
            "Slow CI/CD pipelines reducing iteration speed",
            "Complex approval processes for deployments",
            "Lack of clear priorities causing task paralysis"
        ],
        "prompt_description": "pace and volume of completed development work"
    },
    "deploy_frequency": {
        "name": "Deploy Frequency",
        "framework": "DORA",
        "citation": "Forsgren, Humble, Kim — 'Accelerate', IT Revolution, 2018",
        "definition": "Deploy frequency measures how often code changes are successfully released to production. High deploy frequency enables rapid iteration and quick customer feedback. Low frequency often indicates risky or complex release processes.",
        "friction_signals": [
            "Manual deployment processes requiring checklists",
            "Fear of breaking production limiting releases",
            "Complex branching strategies delaying merges",
            "Lack of automated testing confidence",
            "Approval bottlenecks in release process"
        ],
        "prompt_description": "frequency of successful production deployments"
    },
    "lead_time": {
        "name": "Lead Time",
        "framework": "DORA",
        "citation": "Forsgren, Humble, Kim — 'Accelerate', IT Revolution, 2018",
        "definition": "Lead time measures the time from code commit to successful production deployment. Short lead times enable rapid response to customer needs and quick validation of ideas. Long lead times indicate process inefficiencies.",
        "friction_signals": [
            "Slow code review turnaround times",
            "Long CI pipeline execution times",
            "Manual testing phases delaying releases",
            "Complex merge and release processes",
            "Dependencies on other teams for deployments"
        ],
        "prompt_description": "time from commit to production deployment"
    },
    "change_failure_rate": {
        "name": "Change Failure Rate",
        "framework": "DORA",
        "citation": "Forsgren, Humble, Kim — 'Accelerate', IT Revolution, 2018",
        "definition": "Change failure rate measures the percentage of deployments that cause production incidents requiring remediation. Low failure rates indicate reliable deployment processes and good testing practices. High rates signal quality or process issues.",
        "friction_signals": [
            "Flaky automated tests leading to false failures",
            "Manual deployment steps prone to human error",
            "Lack of staging environment testing",
            "Insufficient monitoring for post-deploy issues",
            "Complex systems making failure prediction difficult"
        ],
        "prompt_description": "percentage of deployments causing production failures"
    },
    "time_to_restore": {
        "name": "Time to Restore",
        "framework": "DORA",
        "citation": "Forsgren, Humble, Kim — 'Accelerate', IT Revolution, 2018",
        "definition": "Time to restore measures how quickly the team can recover from production incidents. Fast restoration minimizes customer impact and maintains trust. Slow recovery times indicate inadequate monitoring or complex systems.",
        "friction_signals": [
            "Lack of automated rollback capabilities",
            "Poor production monitoring and alerting",
            "Complex system architectures slowing diagnosis",
            "Manual recovery processes requiring multiple people",
            "Insufficient incident response training"
        ],
        "prompt_description": "time to recover from production incidents"
    },
    "intrinsic_load": {
        "name": "Intrinsic Load",
        "framework": "CLT",
        "citation": "Sweller — 'Cognitive Load Theory', 1988, applied to DX",
        "definition": "Intrinsic load is the mental effort required to understand the inherent complexity of the task itself. This load cannot be eliminated as it relates to the fundamental difficulty of the work. However, poor tool design can increase intrinsic load unnecessarily.",
        "friction_signals": [
            "Working with legacy codebases lacking documentation",
            "Complex business logic requiring deep domain knowledge",
            "Highly interconnected systems making changes risky",
            "Learning new programming paradigms or languages",
            "Debugging complex multi-threaded or distributed systems"
        ],
        "prompt_description": "mental effort from task complexity itself"
    },
    "extraneous_load": {
        "name": "Extraneous Load",
        "framework": "CLT",
        "citation": "Sweller — 'Cognitive Load Theory', 1988, applied to DX",
        "definition": "Extraneous load is unnecessary mental effort caused by poor tool design, confusing interfaces, or inefficient processes. This load can and should be eliminated through better design. High extraneous load reduces available cognitive capacity for actual work.",
        "friction_signals": [
            "Confusing IDE interfaces requiring extensive searching",
            "Inconsistent keyboard shortcuts across tools",
            "Poor error messages requiring extensive debugging",
            "Manual processes that could be automated",
            "Complex deployment checklists prone to mistakes"
        ],
        "prompt_description": "unnecessary mental effort from poor design"
    },
    "germane_load": {
        "name": "Germane Load",
        "framework": "CLT",
        "citation": "Sweller — 'Cognitive Load Theory', 1988, applied to DX",
        "definition": "Germane load is the productive mental effort invested in learning and skill development. This load builds long-term cognitive capacity and expertise. Supportive learning environments maximize germane load while minimizing extraneous load.",
        "friction_signals": [
            "Lack of mentorship or knowledge sharing opportunities",
            "Code reviews that don't provide learning feedback",
            "Inadequate documentation for onboarding",
            "No time allocated for learning new technologies",
            "Isolated work preventing skill development through collaboration"
        ],
        "prompt_description": "productive mental effort in learning and growth"
    },
    "codebase_health": {
        "name": "Codebase Health",
        "framework": "DX Framework",
        "citation": "Greiler, Storey & Noda — 'An Actionable Framework for Understanding and Improving Developer Experience', IEEE TSE, Vol.49 No.4, 2023",
        "definition": "Codebase health measures the maintainability and quality of the code itself. Healthy codebases are easy to understand, modify, and extend. Poor health increases development time and introduces bugs.",
        "friction_signals": [
            "High technical debt slowing new development",
            "Inconsistent code formatting and style",
            "Lack of automated testing coverage",
            "Complex inheritance hierarchies or dependencies",
            "Outdated libraries with security vulnerabilities"
        ],
        "prompt_description": "maintainability and quality of codebase"
    },
    "development_environment": {
        "name": "Development Environment",
        "framework": "DX Framework",
        "citation": "Greiler, Storey & Noda — 'An Actionable Framework for Understanding and Improving Developer Experience', IEEE TSE, Vol.49 No.4, 2023",
        "definition": "Development environment encompasses the tools, setup, and infrastructure developers use daily. Consistent, reliable environments reduce setup time and context switching. Poor environments create constant friction and reduce productivity.",
        "friction_signals": [
            "Inconsistent tool versions across team members",
            "Slow development machine performance",
            "Complex environment setup requiring multiple tools",
            "Lack of standardized development workflows",
            "Frequent environment-related bugs or issues"
        ],
        "prompt_description": "quality and consistency of development tools and setup"
    },
    "automated_testing": {
        "name": "Automated Testing",
        "framework": "DX Framework",
        "citation": "Greiler, Storey & Noda — 'An Actionable Framework for Understanding and Improving Developer Experience', IEEE TSE, Vol.49 No.4, 2023",
        "definition": "Automated testing measures the effectiveness and reliability of test suites in catching bugs and providing confidence. Good automated testing enables safe refactoring and rapid development. Poor testing creates fear of change and slows development.",
        "friction_signals": [
            "Flaky tests that fail randomly without code changes",
            "Slow test execution times blocking development",
            "Low test coverage leaving bugs undetected",
            "Tests that are hard to understand or maintain",
            "False positive test failures requiring investigation"
        ],
        "prompt_description": "effectiveness and reliability of automated test suites"
    },
    "frictionless_releases": {
        "name": "Frictionless Releases",
        "framework": "DX Framework",
        "citation": "Greiler, Storey & Noda — 'An Actionable Framework for Understanding and Improving Developer Experience', IEEE TSE, Vol.49 No.4, 2023",
        "definition": "Frictionless releases measure how smoothly code moves from development to production. Automated, reliable release processes enable frequent deployments and quick feedback. Manual or error-prone releases create bottlenecks and risk.",
        "friction_signals": [
            "Manual deployment checklists with many steps",
            "Complex branching strategies complicating releases",
            "Lack of staging environments for testing",
            "Approval processes delaying deployments",
            "Fear of production deployments due to past failures"
        ],
        "prompt_description": "smoothness of code release to production"
    },
    "goal_clarity": {
        "name": "Goal Clarity",
        "framework": "DX Framework",
        "citation": "Greiler, Storey & Noda — 'An Actionable Framework for Understanding and Improving Developer Experience', IEEE TSE, Vol.49 No.4, 2023",
        "definition": "Goal clarity measures how well-defined and understood project objectives and requirements are. Clear goals enable focused work and reduce wasted effort. Unclear goals lead to confusion, rework, and low motivation.",
        "friction_signals": [
            "Vague user stories or requirements",
            "Changing priorities mid-sprint",
            "Lack of product vision communication",
            "Unclear acceptance criteria for tasks",
            "Conflicting goals between stakeholders"
        ],
        "prompt_description": "clarity and stability of project goals and requirements"
    },
    "timeline_pressure": {
        "name": "Timeline Pressure",
        "framework": "DX Framework",
        "citation": "Greiler, Storey & Noda — 'An Actionable Framework for Understanding and Improving Developer Experience', IEEE TSE, Vol.49 No.4, 2023",
        "definition": "Timeline pressure measures the stress caused by unrealistic deadlines and time constraints. Appropriate pressure can motivate, but excessive pressure leads to burnout, rushed work, and quality issues. Sustainable pacing enables high-quality output.",
        "friction_signals": [
            "Unrealistic sprint commitments",
            "Last-minute requirement changes",
            "Cramped project timelines",
            "Constant deadline pressure from stakeholders",
            "Lack of buffer time for unexpected issues"
        ],
        "prompt_description": "stress from deadlines and time constraints"
    },
    "psychological_safety": {
        "name": "Psychological Safety",
        "framework": "DX Framework",
        "citation": "Greiler, Storey & Noda — 'An Actionable Framework for Understanding and Improving Developer Experience', IEEE TSE, Vol.49 No.4, 2023",
        "definition": "Psychological safety measures the team's ability to take risks and speak up without fear of negative consequences. Safe environments enable innovation, learning from failures, and open communication. Unsafe environments suppress creativity and hide problems.",
        "friction_signals": [
            "Blame culture for production incidents",
            "Fear of asking questions or admitting confusion",
            "Punitive responses to mistakes",
            "Lack of trust between team members",
            "Leadership that doesn't encourage experimentation"
        ],
        "prompt_description": "team's ability to take risks and speak openly"
    },
    "team_support": {
        "name": "Team Support",
        "framework": "DX Framework",
        "citation": "Greiler, Storey & Noda — 'An Actionable Framework for Understanding and Improving Developer Experience', IEEE TSE, Vol.49 No.4, 2023",
        "definition": "Team support measures the availability of help and resources within the development team. Strong support enables knowledge sharing, problem-solving, and career growth. Poor support leaves developers isolated and slows progress.",
        "friction_signals": [
            "Lack of mentorship for junior developers",
            "No pair programming or knowledge sharing practices",
            "Siloed work preventing collaboration",
            "Inadequate documentation for complex systems",
            "No clear escalation paths for blockers"
        ],
        "prompt_description": "availability of help and resources within the team"
    },
    "code_review_quality": {
        "name": "Code Review Quality",
        "framework": "DX Framework",
        "citation": "Greiler, Storey & Noda — 'An Actionable Framework for Understanding and Improving Developer Experience', IEEE TSE, Vol.49 No.4, 2023",
        "definition": "Code review quality measures the effectiveness of peer review processes in improving code quality and sharing knowledge. Good reviews provide actionable feedback and learning opportunities. Poor reviews become bottlenecks or provide little value.",
        "friction_signals": [
            "Reviews focusing on style rather than substance",
            "Long wait times for review feedback",
            "Nitpicky comments without constructive guidance",
            "Lack of review guidelines or standards",
            "Reviews that don't facilitate knowledge transfer"
        ],
        "prompt_description": "effectiveness of peer code review processes"
    },
    "autonomy": {
        "name": "Autonomy",
        "framework": "DX Framework",
        "citation": "Greiler, Storey & Noda — 'An Actionable Framework for Understanding and Improving Developer Experience', IEEE TSE, Vol.49 No.4, 2023",
        "definition": "Autonomy measures the freedom developers have to make decisions about their work approach and solutions. Appropriate autonomy enables ownership and creativity. Excessive control or micromanagement reduces motivation and slows decision-making.",
        "friction_signals": [
            "Micromanagement of implementation details",
            "Rigid processes that don't allow flexibility",
            "Lack of decision-making authority",
            "Excessive approval requirements for changes",
            "No ownership of code or features"
        ],
        "prompt_description": "freedom to make decisions about work approach"
    },
    "meaningful_work": {
        "name": "Meaningful Work",
        "framework": "DX Framework",
        "citation": "Greiler, Storey & Noda — 'An Actionable Framework for Understanding and Improving Developer Experience', IEEE TSE, Vol.49 No.4, 2023",
        "definition": "Meaningful work measures the sense of purpose and value developers find in their tasks. Work that aligns with personal values and provides visible impact increases motivation and satisfaction. Routine or disconnected work reduces engagement.",
        "friction_signals": [
            "Working on features with no clear user benefit",
            "Lack of understanding of project impact",
            "Repetitive tasks without learning opportunities",
            "Work that conflicts with personal values",
            "No connection between individual work and company mission"
        ],
        "prompt_description": "sense of purpose and value in development work"
    },
    "uninterrupted_time": {
        "name": "Uninterrupted Time",
        "framework": "DX Framework",
        "citation": "Greiler, Storey & Noda — 'An Actionable Framework for Understanding and Improving Developer Experience', IEEE TSE, Vol.49 No.4, 2023",
        "definition": "Uninterrupted time measures the ability to focus deeply on complex tasks without distractions. Deep work enables creative problem-solving and high-quality output. Frequent interruptions reduce productivity and increase errors.",
        "friction_signals": [
            "Constant notifications and alerts",
            "Frequent meetings breaking focus",
            "Open office environments with noise",
            "Context switching between multiple projects",
            "Interruptions from urgent but unimportant requests"
        ],
        "prompt_description": "ability to focus deeply without distractions"
    }
}

FRAMEWORK_GROUPS = {
    "DevEx": ["flow_state", "feedback_loops", "cognitive_load"],
    "SPACE": ["satisfaction", "efficiency", "collaboration", "performance", "activity"],
    "DORA": ["deploy_frequency", "lead_time", "change_failure_rate", "time_to_restore"],
    "CLT": ["intrinsic_load", "extraneous_load", "germane_load"],
    "DX Framework": ["codebase_health", "development_environment", "automated_testing", "frictionless_releases", "goal_clarity", "timeline_pressure", "psychological_safety", "team_support", "code_review_quality", "autonomy", "meaningful_work", "uninterrupted_time"]
}

FRAMEWORK_CITATIONS = {
    "DevEx": "Noda, Greiler, Forsgren et al. — 'DevEx: What Actually Drives Productivity', ACM Queue, 2023",
    "SPACE": "Forsgren, Storey et al. — 'The SPACE of Developer Productivity', ACM Queue, 2021",
    "DORA": "Forsgren, Humble, Kim — 'Accelerate', IT Revolution, 2018",
    "CLT": "Sweller — 'Cognitive Load Theory', 1988, applied to DX",
    "DX Framework": "Greiler, Storey & Noda — 'An Actionable Framework for Understanding and Improving Developer Experience', IEEE TSE, Vol.49 No.4, 2023"
}
