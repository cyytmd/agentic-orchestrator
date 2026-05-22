# Agentic Orchestrator
# Multi-Agent Task Decomposition & Orchestration Engine

"""
Example: Submitting a complex task to the orchestrator.

The orchestrator automatically:
1. Decomposes high-level goals into sub-tasks
2. Assigns sub-tasks to specialized agents
3. Merges results and resolves conflicts
4. Returns a unified final output
"""

import asyncio
from orchestrator.core import Orchestrator
from orchestrator.agents import CodeReviewer, DevOpsOperator, DataAnalyst


async def main():
    orchestrator = Orchestrator(
        primary_model="mimo-v2.5-pro",
        fallback_models=["deepseek-v4-pro", "gpt-5.4"],
    )

    # Register specialized agents
    orchestrator.register(CodeReviewer())
    orchestrator.register(DevOpsOperator())
    orchestrator.register(DataAnalyst())

    # Submit a complex task — the orchestrator handles decomposition
    result = await orchestrator.execute(
        task="Review all Python files in src/ for security issues, "
             "fix them, run tests, and deploy to staging if all pass.",
        context={
            "repo": "backend-api",
            "branch": "main",
            "deploy_target": "staging.k8s.internal",
        }
    )

    print(f"Status: {result.status}")
    print(f"Sub-tasks: {len(result.sub_tasks)}")
    print(f"Duration: {result.duration:.2f}s")
    print(f"Tokens Used: {result.token_usage}")

    for fix in result.fixes_applied:
        print(f"  ✓ {fix.file}: {fix.description}")


if __name__ == "__main__":
    asyncio.run(main())
