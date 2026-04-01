import os
import re
import json
from pathlib import Path

class AgentRunner:
    """
    Loads and executes agent definitions from markdown files.
    Converts markdown agent specs into structured prompts for execution.
    """
    
    def __init__(self, agents_dir="agents"):
        self.agents_dir = agents_dir
        self.agents = {}
        self._load_agents()
    
    def _load_agents(self):
        """Load all markdown agent files from the agents directory."""
        print(f"\n📂 [Agent Runner] Loading agents from: {self.agents_dir}")
        
        if not os.path.exists(self.agents_dir):
            print(f"⚠️  Agent directory not found: {self.agents_dir}")
            return
        
        for filename in os.listdir(self.agents_dir):
            if filename.endswith(".md"):
                agent_name = filename.replace(".md", "")
                filepath = os.path.join(self.agents_dir, filename)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    self.agents[agent_name] = {
                        "name": agent_name,
                        "filepath": filepath,
                        "content": content,
                        "spec": self._parse_agent_spec(content)
                    }
                    print(f"  ✓ Loaded: {agent_name}")
                except Exception as e:
                    print(f"  ✗ Failed to load {agent_name}: {e}")
    
    def _parse_agent_spec(self, content):
        """
        Parse agent specification from markdown.
        Extracts role, instructions, input/output format.
        """
        spec = {
            "role": None,
            "instructions": None,
            "inputs": None,
            "outputs": None,
            "raw_content": content
        }
        
        # Extract role (look for Role: or ## Role sections)
        role_match = re.search(r'(?:^## Role|Role:)\s*\n(.+?)(?:\n##|\Z)', content, re.MULTILINE)
        if role_match:
            spec["role"] = role_match.group(1).strip()
        
        # Extract instructions
        instructions_match = re.search(r'(?:^## Instructions|Instructions:)\s*\n([\s\S]+?)(?:\n##|Inputs:|Outputs:|\Z)', content, re.MULTILINE)
        if instructions_match:
            spec["instructions"] = instructions_match.group(1).strip()
        
        # Extract input format
        inputs_match = re.search(r'(?:^## Inputs|Inputs:)\s*\n([\s\S]+?)(?:\n##|Outputs:|\Z)', content, re.MULTILINE)
        if inputs_match:
            spec["inputs"] = inputs_match.group(1).strip()
        
        # Extract output format
        outputs_match = re.search(r'(?:^## Outputs|Outputs:)\s*\n([\s\S]+?)(?:\n##|\Z)', content, re.MULTILINE)
        if outputs_match:
            spec["outputs"] = outputs_match.group(1).strip()
        
        return spec
    
    def get_agent(self, agent_name):
        """Retrieve a specific agent by name."""
        if agent_name in self.agents:
            return self.agents[agent_name]
        else:
            print(f"⚠️  Agent not found: {agent_name}")
            return None
    
    def list_agents(self):
        """Return list of available agents."""
        return list(self.agents.keys())
    
    def build_prompt(self, agent_name, task_context):
        """
        Build an LLM prompt from an agent specification.
        Combines agent role, instructions, and task context.
        """
        agent = self.get_agent(agent_name)
        if not agent:
            return None
        
        spec = agent["spec"]
        
        prompt = f"""# Agent: {agent_name.upper()}

## Role
{spec["role"] or "No role specified"}

## Instructions
{spec["instructions"] or "No instructions specified"}

## Task Context
{json.dumps(task_context, indent=2)}

## Expected Output Format
{spec["outputs"] or "Provide structured output"}

---
Please execute this task now:
"""
        
        return prompt
    
    def print_agent_info(self, agent_name):
        """Print detailed information about an agent."""
        agent = self.get_agent(agent_name)
        if not agent:
            return
        
        spec = agent["spec"]
        print(f"\n{'='*60}")
        print(f"AGENT: {agent_name}")
        print(f"{'='*60}")
        print(f"\n📋 Role:\n{spec['role'] or 'N/A'}")
        print(f"\n📝 Instructions:\n{spec['instructions'] or 'N/A'}")
        print(f"\n📥 Inputs:\n{spec['inputs'] or 'N/A'}")
        print(f"\n📤 Outputs:\n{spec['outputs'] or 'N/A'}")
        print(f"\n{'='*60}\n")


if __name__ == "__main__":
    # Example usage
    runner = AgentRunner()
    
    print(f"\n✓ Available agents: {runner.list_agents()}")
    
    # If you have agents, print their info
    for agent_name in runner.list_agents():
        runner.print_agent_info(agent_name)\n