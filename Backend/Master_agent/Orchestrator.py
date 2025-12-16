from worker_agents.sales_agent import SalesAgent
from worker_agents.verification_agent import VerificationAgent
from worker_agents.underwriting_agent import UnderwritingAgent
from worker_agents.sanction_agent import SanctionAgent

class MasterAgent:
    def __init__(self):
        self.sales = SalesAgent()
        self.verify = VerificationAgent()
        self.underwrite = UnderwritingAgent()
        self.sanction = SanctionAgent()

        self.stage = "sales"
        self.context = {}

    def handle_message(self, message: str) -> str:
        if self.stage == "sales":
            self.context.update(self.sales.process(message))
            self.stage = "verification"
            return "Thanks. Proceeding with KYC verification."

        if self.stage == "verification":
            ok = self.verify.verify(self.context)
            if not ok:
                return "KYC failed."
            self.stage = "underwriting"
            return "KYC successful. Checking eligibility."

        if self.stage == "underwriting":
            decision = self.underwrite.evaluate(self.context)
            self.context.update(decision)
            if decision["approved"]:
                self.stage = "sanction"
                return "Loan approved. Generating sanction letter."
            return "Loan rejected due to eligibility."

        if self.stage == "sanction":
            path = self.sanction.generate(self.context)
            self.stage = "done"
            return f"🎉 Approved! Sanction letter generated at {path}"

        return "Conversation complete."
