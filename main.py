from typing import Literal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="CHIPFORGE AI API", version="0.1.0",
              description="MVP API. Engineering checks require external validated EDA tools.")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=False, allow_methods=["GET", "POST"], allow_headers=["*"],
)

class DesignPrompt(BaseModel):
    prompt: str = Field(min_length=1, max_length=4000)
    project_type: Literal["circuit", "pcb", "rtl", "general"] = "general"

@app.get("/health")
def health():
    return {"status": "ok", "app": "CHIPFORGE AI", "version": "0.1.0",
            "eda_tools_connected": False}

@app.post("/api/design-plan")
def design_plan(req: DesignPrompt):
    """Return a cautious starter plan, not a validated design."""
    p = req.prompt.lower()
    if req.project_type == "rtl" or "verilog" in p or "rtl" in p:
        steps = [
            "Clarify interface, clock, reset polarity, and latency requirements.",
            "Draft synthesizable RTL and a self-checking testbench.",
            "Run Icarus Verilog or Verilator and preserve logs.",
            "Run Yosys synthesis and inspect warnings and inferred hardware.",
            "Use OpenROAD only after selecting a compatible platform/PDK."
        ]
        warnings = ["No RTL simulation or synthesis was run by this API."]
    elif req.project_type in ("circuit", "pcb") or "pcb" in p or "circuit" in p:
        steps = [
            "List functional blocks, supply rails, interfaces, and constraints.",
            "Choose parts from verified datasheets and record manufacturer part numbers.",
            "Create a schematic and assign reviewed footprints.",
            "Define stack-up, board outline, clearances, and net classes.",
            "Run ERC/DRC in KiCad; use ngspice for supported analog simulations.",
            "Review fabrication outputs and BOM before manufacturing."
        ]
        warnings = ["This is a checklist, not a generated or validated schematic."]
    else:
        steps = [
            "Specify function, voltage, interfaces, size, power budget, and environment.",
            "Create a block diagram and identify uncertain requirements.",
            "Select datasheet-backed components and define test criteria.",
            "Validate in appropriate EDA tools before implementation."
        ]
        warnings = ["No external LLM, component database, or EDA tool is connected."]
    return {"status": "plan_only", "project_type": req.project_type,
            "steps": steps, "warnings": warnings, "validated": False}
