import math
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Conceptual comparison plot: Compression Ratio vs. Decompression Throughput
# ------------------------------------------------------------
# Notes:
# - Use throughput in GB/s for decompression, if reported.
# - Use compression ratio as "uncompressed_size / compressed_size" (x-times).
# - If papers report different metrics (e.g., MB/s, ns/byte, bpc), convert first.
#
# Values below:
# - FSST / GSST are taken from the uploaded GSST paper (see citations in your text).
# - Other entries are placeholders because a single directly comparable metric
#   isn't uniquely extractable without choosing a specific dataset/setup.
# ------------------------------------------------------------

data = [
    # name, compression_ratio (x), decompression_throughput_gbs (GB/s), marker
    ("FSST (CPU)", 2.71, None, "o"),   # CR from GSST paper; throughput not specified in the snippet we extracted
    ("GSST (GPU, A100)", 2.74, 191.0, "s"),  # CR and throughput reported in abstract

    # ---- TODO: Fill these if you decide to plot numeric values from each paper ----
    # ("Order-preserving dict (Binnig et al.)",  None, None, "^"),
    # ("Fast & Strong (Lasch et al.)",           None, None, "D"),
    # ("ALPHAZIP (Narasimhan et al.)",           None, None, "v"),
]

# Optional: If you still want to show papers without numeric throughput,
# assign them a conceptual position (ranked) instead of real GB/s, e.g.:
# "low=1, medium=2, high=3, very high=4"
USE_CONCEPTUAL_Y = False

conceptual_y = {
    "FSST (CPU)": 4,                 # very high (CPU-side fast decompression)
    "GSST (GPU, A100)": 5,           # extremely high (GPU)
    # "Order-preserving dict (Binnig et al.)": 3,
    # "Fast & Strong (Lasch et al.)": 2,
    # "ALPHAZIP (Narasimhan et al.)": 1,
}

# Build plot points
xs, ys, labels, markers = [], [], [], []
for name, cr, thr, m in data:
    if cr is None:
        continue
    if USE_CONCEPTUAL_Y:
        y = conceptual_y.get(name, None)
        if y is None:
            # skip entries without a conceptual mapping
            continue
    else:
        if thr is None:
            # skip entries without numeric throughput
            continue
        y = thr

    xs.append(cr)
    ys.append(y)
    labels.append(name)
    markers.append(m)

# Plot
plt.figure(figsize=(8, 5))

for x, y, label, m in zip(xs, ys, labels, markers):
    plt.scatter(x, y, marker=m, s=80)
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(6, 6), ha="left", fontsize=9)

plt.xlabel("Compression ratio (x = uncompressed / compressed)")
plt.ylabel("Decompression throughput (conceptual scale)" if USE_CONCEPTUAL_Y else "Decompression throughput [GB/s]")
plt.title("Compression ratio vs. decompression throughput")

# Helpful grid
plt.grid(True, linestyle="--", linewidth=0.5)

# If using conceptual scale, add ticks
if USE_CONCEPTUAL_Y:
    plt.yticks([1, 2, 3, 4, 5], ["low", "medium-low", "medium", "high", "very high"])

plt.tight_layout()
plt.show()
