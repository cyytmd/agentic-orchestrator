"""
Specialized AI Agents for the Orchestrator

Each agent is a domain-specific AI worker capable of:
- Autonomous decision making within its domain
- Tool invocation (file ops, web, code execution, GitHub API)
- Result reporting back to the Orchestrator
"""


class CodeReviewer:
    """Security-focused code review agent.
    
    Capabilities:
    - Static analysis (SQL injection, XSS, CSRF, auth bypass)
    - Automated fix generation
    - Test suite validation
    - PR creation with inline comments
    """
    tools = ["read_file", "search_files", "patch", "terminal"]
    preferred_model = "mimo-v2.5-pro"


class DevOpsOperator:
    """Infrastructure & deployment automation agent.
    
    Capabilities:
    - Server health checks (CPU, memory, disk, network)
    - Docker/K8s management
    - Auto-scaling decisions
    - CronJob scheduling & monitoring
    """
    tools = ["terminal", "web_search", "cronjob", "process"]
    preferred_model = "deepseek-v4-pro"


class DataAnalyst:
    """Data analysis & visualization agent.
    
    Capabilities:
    - SQL query generation & execution
    - Chart & dashboard creation
    - Anomaly detection
    - Report generation (PDF/HTML)
    """
    tools = ["terminal", "execute_code", "web_search", "write_file"]
    preferred_model = "mimo-v2.5-pro"
