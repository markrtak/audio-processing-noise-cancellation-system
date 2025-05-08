# Signals Project

## Overview

This project implements an audio signal processing pipeline in Python. It generates a custom piano-inspired signal, adds synthetic noise, and performs noise cancellation via frequency-domain filtering. The workflow follows four key parts:

1. **Signal Generation (The Pianist)**

   * Create `N` pairs of piano notes from the 3rd and 4th octaves.
   * Each note is represented as a sine wave active over a specified time window.
   * Sum all note pairs to form the original signal.

2. **Song Composition**

   * Superimpose individual note signals to form a short song (e.g., 3 seconds).
   * Visualize the time-domain waveform and listen to the composition.

3. **Noise Addition**

   * Generate two sinusoidal noise components with random frequencies.
   * Add the noise to the original signal to simulate disturbances.
   * Plot and playback the noisy signal.

4. **Noise Cancellation**

   * Transform the noisy signal to the frequency domain using FFT.
   * Identify noise peaks and zero out corresponding frequency bins.
   * Reconstruct the filtered signal via inverse FFT.
   * Plot and playback the denoised signal.

---

## Repository Structure

```
├── signals_project.py      # Main Python script implementing all parts
└── README.md               # Project documentation (this file)
```

## Requirements

* Python 3.7+
* NumPy
* SciPy
* MatPlotLib
* SoundDevice

## Usage

1. **Adjust Parameters**

   * In `signals_project.py`, modify:

     * `N`: number of note pairs
     * `notes`, `ti`, `Ti`: chosen notes and their start times/durations
     * `Fs`, duration: sampling rate and overall signal length

2. **Run the Script**

   ```bash
   python signals_project.py
   ```

   This will:

   * Plot the original, noisy, and filtered signals (both time and frequency domains).
   * Play each signal in sequence, with a 1-second pause between.

3. **Interpret Results**

   * Verify that the noise peaks are removed in the filtered signal’s spectrum.
   * Listen to the audio to appreciate the noise cancellation effect.

---

## Example Output

* **Figures (6 total)**:

  1. Original signal (time domain)
  2. Original signal (frequency domain)
  3. Noisy signal (time domain)
  4. Noisy signal (frequency domain)
  5. Filtered signal (time domain)
  6. Filtered signal (frequency domain)

* **Audio Playback**:

  * Original → \[1s pause] → Noisy → \[1s pause] → Filtered

---

## Notes

* The noise frequencies `fn1` and `fn2` are randomly chosen per run. For reproducible results, set a random seed at the top of the script:

  ```python
  np.random.seed(0)
  ```
* Ensure your audio output is configured correctly to hear playback via `sounddevice`.
