# Roadmap

## MVP included
- Responsive React/TypeScript dashboard
- Selectable schematic-style component cards
- Concept PCB and chip previews
- Editable example SystemVerilog
- Local demo assistant and JSON project export
- FastAPI health and design-plan endpoints

## Not implemented yet
- Real symbol/footprint libraries or connectivity graph validation
- Real PCB routing, Gerber/drill/pick-and-place exports
- Three.js geometry derived from board geometry
- SPICE, RTL simulation, synthesis, timing or physical-design execution
- Authentication, cloud persistence, collaboration, rendering/video pipeline

## Next phases
1. Secure AI model integration with datasheet-grounded component data.
2. Canonical schematic JSON and connectivity checks.
3. KiCad integration for real ERC/DRC and manufacturing outputs.
4. ngspice and Verilator/Icarus/Yosys integrations in isolated workers.
5. Real PCB geometry and Three.js rendering.
6. OpenROAD/KLayout workflows, timing reports, reproducible logs.
