# CHIPFORGE AI — MVP starter

A starter Android-ready web app for AI-assisted VLSI and PCB workflows.

## Included
- React + TypeScript dashboard
- Interactive schematic-style canvas with selectable components
- Concept PCB view and chip preview
- Example SystemVerilog editor
- Local demo AI assistant
- Project JSON export
- FastAPI health and design-plan endpoints

## Run the frontend
Requirements: Node.js 20+
```bash
cd frontend
npm install
npm run dev
```

## Run the backend
Requirements: Python 3.10+
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
Windows activation: `.venv\\Scripts\\activate`

## Build an Android APK
The project starts as a responsive web app. Wrap it using Capacitor:
```bash
cd frontend
npm install
npm run build
npm install @capacitor/core @capacitor/cli @capacitor/android
npx cap init "CHIPFORGE AI" "com.chipforge.ai" --web-dir dist
npx cap add android
npx cap sync android
npx cap open android
```
In Android Studio, use **Build > Build Bundle(s) / APK(s) > Build APK(s)**. Debug APKs are typically created at `frontend/android/app/build/outputs/apk/debug/`.

For Play Store release, create a signed Android App Bundle (AAB), complete Play Console listing/privacy/data-safety requirements, test it, and submit for review. Store acceptance and publishing cannot be done automatically from this project.

## Important engineering limitations
This is an MVP, not a replacement for KiCad, Altium, Cadence, or Synopsys. The schematic and PCB views are starter demonstrations, not manufacturing-grade editors. No real ERC/DRC, SPICE, RTL simulation, synthesis, timing, physical design, or tape-out checks are run. Do not fabricate boards or chips based on this demo without proper EDA validation and engineering review.

## Roadmap
1. Secure AI model integration and datasheet-backed parts.
2. Canonical schematic data model and connectivity validation.
3. KiCad integration for real ERC/DRC and manufacturing outputs.
4. ngspice and Verilator/Icarus/Yosys integrations.
5. PCB geometry and Three.js viewer derived from real board data.
6. OpenROAD/KLayout workflows, timing reports, reproducible jobs.
