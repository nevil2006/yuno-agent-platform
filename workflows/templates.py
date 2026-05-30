from runtime.crew_runtime import run_crew


def run_workflow(workflow_type, query):

    if workflow_type == "research":
        return run_crew(query)

    elif workflow_type == "blog":
        return (
            f"Blog Workflow\n\n"
            f"Topic: {query}\n\n"
            f"Generated draft blog structure."
        )

    elif workflow_type == "finance":
        return (
            f"Finance Workflow\n\n"
            f"Topic: {query}\n\n"
            f"Generated finance analysis template."
        )

    else:
        return "Workflow not found"