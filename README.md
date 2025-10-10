# CyberTruck Project

Small-scale, vision-enabled RC Cybertruck prototype integrating physical design, 3D printing, ML perception, and control.

## Status
- Environment configured with PiCamera2
- Python pipeline live: object detection with bounding boxes and confidence scores
- Target demo: Christmas

## Scope
- Hardware: chassis, steering, propulsion
- Control: ESC and servo integration
- Vision: PiCamera2 capture → inference → control hooks
- Optics: windshield material tests (PETG HDglass vs resin)

## Hardware Quick Reference
- Steering: SG90/MG90S for light builds, MG996R/DS3218 for higher torque
- Propulsion: N20 (≤0.7 kg), 370/380 + 20–30 A ESC, 540 brushed or 3650 brushless + 45–60 A ESC, 2435 brushless for 1/18

## Vision Pipeline
- Capture: PiCamera2 stream
- Inference: object detection
- Output: bounding boxes + class + confidence
- Control: hooks for lane/obstacle cues to adjust speed/steer

## Getting Started
1) Define mass and wheelbase → pick servo and motor + ESC
2) Wire power tree to match servo and drive voltages
3) Run detection demo:
   - python ml/infer.py --source camera --show
4) Integrate control:
   - python control/run.py --mode assist

## Repo Layout
- hardware/ CAD, STLs, print notes
- electronics/ schematics, wiring, bom.csv
- control/ firmware and tuning scripts
- ml/ data, training, inference
- tests/ plans and logs
- demo/ runbook and media

## Optics Notes
- FDM is typically translucent; PETG HDglass clearer with post-processing
- Resin is clearest but consider durability and size limits
- Run vision A/B tests under glare and low light

## Milestones
- [ ] Finalize steering and drive
- [ ] Optics decision with vision results
- [ ] Control + vision closed-loop
- [ ] Full system test
- [ ] Christmas demo