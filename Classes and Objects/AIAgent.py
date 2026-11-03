class AIAgent:
    def __init__(self, name, task):
        self.name = name
        self.task = task

    def execute(self):
        print(self.name, "is executing", self.task)

agent1 = AIAgent(
    "Requirement Analysis Agent",
    "Analyze the uploaded requirement"
)

agent2 = AIAgent(
    "Test Case Generator",
    "Generate end to end test cases based on requirement"
)

agent1.execute()
agent2.execute()

