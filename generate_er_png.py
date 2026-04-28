import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Rectangle


def draw_entity(ax, x, y, w, h, title, attrs):
    # Outer box
    ax.add_patch(Rectangle((x, y), w, h, linewidth=1.3, edgecolor="#6f6f6f", facecolor="white"))
    # Header
    head_h = 0.55
    ax.add_patch(Rectangle((x, y + h - head_h), w, head_h, linewidth=1.0, edgecolor="#2a708c", facecolor="#2fa4cf"))
    ax.text(x + w / 2, y + h - head_h / 2, title, ha="center", va="center", fontsize=11, color="white", fontweight="bold")
    # Attribute rows
    row_y = y + h - head_h - 0.18
    for attr in attrs:
        ax.text(x + w / 2, row_y, attr, ha="center", va="top", fontsize=9.6, color="#222")
        row_y -= 0.27
    return {
        "left": (x, y + h / 2),
        "right": (x + w, y + h / 2),
        "top": (x + w / 2, y + h),
        "bottom": (x + w / 2, y),
    }


def draw_attribute(ax, x, y, text, color):
    e = Ellipse((x, y), 1.9, 0.8, linewidth=1.2, edgecolor="#8a8a8a", facecolor=color)
    ax.add_patch(e)
    ax.text(x, y, text, ha="center", va="center", fontsize=9.2, color="#202020")
    return (x, y)


def draw_relationship(ax, x, y, w, h, text):
    cx, cy = x + w / 2, y + h / 2
    d = Polygon([[cx, y + h], [x + w, cy], [cx, y], [x, cy]], closed=True, edgecolor="#5f8f5f", facecolor="#84d39b", linewidth=1.2)
    ax.add_patch(d)
    ax.text(cx, cy, text, ha="center", va="center", fontsize=9.6, color="#114422", fontweight="bold")
    return (cx, cy)


def line(ax, p1, p2):
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color="#8b8f95", linewidth=1.2)


fig, ax = plt.subplots(figsize=(11.69, 8.27))  # A4 landscape ratio
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis("off")
ax.set_facecolor("white")

ax.text(8, 9.6, "Notown Records ER Diagram", fontsize=20, fontweight="bold", ha="center")
ax.text(8, 9.25, "Format aligned to provided sample style", fontsize=11, color="#555", ha="center")

# Core entities
mus = draw_entity(ax, 1.0, 5.6, 2.9, 2.0, "MUSICIAN", ["ssn (PK)", "name", "address", "phone"])
ins = draw_entity(ax, 5.8, 7.0, 2.9, 1.9, "INSTRUMENT", ["inst_id (PK)", "inst_name", "musical_key"])
alb = draw_entity(ax, 12.1, 6.0, 2.9, 2.2, "ALBUM", ["album_id (PK)", "title", "copyright_date", "format", "album_identifier (UNIQUE)"])
song = draw_entity(ax, 12.1, 2.2, 2.9, 1.9, "SONG", ["song_id (PK)", "title", "author"])

# Relationship diamonds
plays = draw_relationship(ax, 4.2, 6.8, 1.4, 1.0, "PLAYS")
produces = draw_relationship(ax, 10.0, 6.7, 1.5, 1.0, "PRODUCES")
contains = draw_relationship(ax, 10.0, 3.0, 1.5, 1.0, "CONTAINS")
performs = draw_relationship(ax, 6.0, 3.8, 1.6, 1.0, "PERFORMS")

# Entity-to-relationship connectivity (clear, sample-like)
line(ax, mus["right"], (4.2, 7.3))
line(ax, ins["left"], (5.6, 7.3))
ax.text(4.02, 7.52, "M", fontsize=9)
ax.text(5.62, 7.52, "N", fontsize=9)

line(ax, mus["right"], (6.0, 4.3))
line(ax, song["left"], (7.6, 4.3))
ax.text(5.8, 4.48, "M", fontsize=9)
ax.text(7.65, 4.48, "N", fontsize=9)

line(ax, mus["right"], (10.0, 7.2))
line(ax, alb["left"], (11.5, 7.2))
ax.text(9.82, 7.38, "1", fontsize=9)
ax.text(11.55, 7.38, "N", fontsize=9)

line(ax, alb["left"], (11.5, 3.5))
line(ax, song["left"], (11.5, 3.5))
line(ax, (11.5, 3.5), (10.0, 3.5))
ax.text(11.58, 3.72, "1", fontsize=9)
ax.text(11.58, 3.28, "N", fontsize=9)

# Attribute ovals around entities (sample-like visual)
attr_color_left = "#e98f76"
attr_color_right = "#d9a0d7"
line(ax, draw_attribute(ax, 0.9, 8.3, "ssn (PK)", attr_color_left), mus["top"])
line(ax, draw_attribute(ax, 0.9, 7.0, "name", attr_color_left), mus["left"])
line(ax, draw_attribute(ax, 0.9, 5.7, "address", attr_color_left), mus["left"])
line(ax, draw_attribute(ax, 0.9, 4.4, "phone", attr_color_left), mus["bottom"])

line(ax, draw_attribute(ax, 5.3, 9.2, "inst_id (PK)", attr_color_left), ins["top"])
line(ax, draw_attribute(ax, 7.2, 9.2, "inst_name", attr_color_left), ins["top"])
line(ax, draw_attribute(ax, 8.9, 9.2, "musical_key", attr_color_left), ins["top"])

line(ax, draw_attribute(ax, 15.1, 8.5, "album_id (PK)", attr_color_right), alb["top"])
line(ax, draw_attribute(ax, 15.1, 7.4, "title", attr_color_right), alb["right"])
line(ax, draw_attribute(ax, 15.1, 6.3, "copyright_date", attr_color_right), alb["right"])
line(ax, draw_attribute(ax, 15.1, 5.2, "format", attr_color_right), alb["right"])
line(ax, draw_attribute(ax, 12.8, 8.9, "album_identifier", attr_color_right), alb["top"])

line(ax, draw_attribute(ax, 15.1, 4.0, "song_id (PK)", attr_color_right), song["right"])
line(ax, draw_attribute(ax, 15.1, 3.0, "title", attr_color_right), song["right"])
line(ax, draw_attribute(ax, 15.1, 2.0, "author", attr_color_right), song["right"])

# Constraint notes
ax.text(7.0, 3.2, "Song total participation (>=1 performer)", fontsize=9.5, color="#333")
ax.text(10.15, 2.5, "Each song belongs to exactly one album", fontsize=9.5, color="#333")
ax.text(9.9, 6.35, "Each album has exactly one producer", fontsize=9.5, color="#333")

output = "Notown-ER-Diagram.png"
plt.tight_layout(pad=0.8)
plt.savefig(output, dpi=350, bbox_inches="tight")
print(output)
