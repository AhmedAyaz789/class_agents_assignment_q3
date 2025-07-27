## 🚀 How This Project Works

- The user gives input like: "I want to become a web developer".
- The **MainAgent** activates three sub-agents:
  1. **CareerAgent** → provides a career roadmap  
  2. **JobAgent** → gives job search tips  
  3. **SkillsAgent** → suggests a skill development plan  
- The **CareerAgent** uses a tool called `get_career_roadmap` which contains predefined roadmaps for common careers.
- Everything runs on the **Gemini 2.0 Flash model** using the **OpenAI Agents SDK**.
- In the end, the system prints a final response that includes a mix of roadmap, job advice, and skill suggestions.
