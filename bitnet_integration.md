# Evolution Phase 4: 1-Bit Neural Engine (BitNet)

## 1. Objective
Integrate the **BitNet b1.58** (1-bit LLM) framework into the Termux environment to enable ultra-fast, local autonomous reasoning. This upgrade will replace/supplement existing Ollama models with a specialized 1-bit engine optimized for ARM64.

## 2. Technical Stack
- **Framework:** Microsoft `bitnet.cpp` (optimized for ARM NEON/SIMD).
- **Environment:** Debian PRoot (for stable library dependencies like `torch` and `cmake`).
- **Model:** BitNet-b1.58-2B-4T (GGUF quantized).
- **Goal:** 5-10 tokens/sec on mobile ARM hardware with <2GB RAM usage.

## 3. Implementation Steps

### A. Environment Preparation
1.  **PRoot Setup:** Install and initialize `proot-distro` with Debian.
2.  **Toolchain:** Install `clang`, `cmake`, and `python3-venv` inside the Debian environment.

### B. BitNet Compilation
1.  **Clone:** Recursively clone `microsoft/BitNet` and its `llama.cpp` submodules.
2.  **Build:** Use `clang++` with `-march=armv8-a` optimizations.
3.  **Quantize:** Build the `i2_s` (1.58-bit) kernels specifically for ARM performance.

### C. Integration & Automation
1.  **API Bridge:** Create a Python wrapper to bridge the BitNet CLI output with my "Brain" (Gemini CLI).
2.  **Autonomous Launch:** Update `guardian.sh` to monitor the BitNet inference server.
3.  **Skill Update:** Add `bitnet-reasoning` to the `autonomous-evolution` skill.

## 4. Verification
- **Speed Test:** Measure tokens/sec against standard Ollama models.
- **Resource Test:** Verify RAM usage stays below 2GB during peak inference.
- **Accuracy Test:** Run a set of complex CLI planning tasks to ensure reasoning quality is maintained.

## 5. Rollback Strategy
- Keep the current Ollama/Moondream setup as a fallback "Secondary Brain."
- All BitNet artifacts will stay inside the `debian` proot to prevent host pollution.
