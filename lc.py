#!/usr/bin/env python3
"""lc.py — LeetCode Practice Manager

A CLI tool for spaced repetition, progress tracking, concept grouping,
hint generation, and git automation for LeetCode practice.

Usage:
    python lc.py sync                       Parse roadmap & scan notes
    python lc.py status                     One-line summary
    python lc.py dash                       Progress dashboard
    python lc.py review                     Show today's review queue
    python lc.py review start <num|--all>   Start tracking for review
    python lc.py review done <num> <1-5>    Record review result
    python lc.py hint <num> [--level 1-4]   Generate AI-agnostic hint prompts
    python lc.py note <num>                 Display a problem's note
    python lc.py group [name]               List or show concept groups
    python lc.py group add <name> <nums..>  Create custom group
    python lc.py git init                   Initialize git repo
    python lc.py git save [--push]          Auto-commit & optionally push
    python lc.py git remote <url>           Set GitHub remote
"""

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timedelta, date
from pathlib import Path

NOTES_DIR = Path(__file__).parent.resolve()
TRACKER = NOTES_DIR / "tracker.json"
ROADMAP = NOTES_DIR / "00 - Roadmap.md"
YEAR = 2026  # Default year for M.DD dates

# ─── Data Layer ────────────────────────────────────────────────────────────────

def load_tracker():
    if TRACKER.exists():
        with open(TRACKER, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "version": 1,
        "problems": {},
        "categories": {},
        "custom_groups": {},
        "git": {"initialized": False, "remote_url": None},
    }


def save_tracker(tracker):
    with open(TRACKER, "w", encoding="utf-8") as f:
        json.dump(tracker, f, indent=2, ensure_ascii=False)


def today_iso():
    return date.today().isoformat()


def today_date():
    return date.today()


# ─── Roadmap Parser ───────────────────────────────────────────────────────────

def parse_date_field(text):
    """Parse 'M.DD' dates like '3.18' → '2026-03-18'."""
    text = text.strip()
    if not text:
        return None
    m = re.match(r"(\d{1,2})\.(\d{1,2})", text)
    if m:
        month, day = int(m.group(1)), int(m.group(2))
        try:
            return date(YEAR, month, day).isoformat()
        except ValueError:
            return None
    return None


def parse_table_row(line):
    """Parse a markdown table row into cells."""
    line = line.strip()
    if not line.startswith("|"):
        return None
    cells = [c.strip() for c in line.split("|")]
    # Split produces empty strings at start/end
    return cells[1:-1] if len(cells) > 2 else None


def is_separator_row(cells):
    """Check if row is a --- separator."""
    return all(re.match(r"^-+$", c.strip()) for c in cells if c.strip())


def parse_roadmap():
    """Parse 00 - Roadmap.md and return (problems, categories)."""
    if not ROADMAP.exists():
        print(f"Error: {ROADMAP} not found")
        sys.exit(1)

    content = ROADMAP.read_text(encoding="utf-8")
    lines = content.split("\n")

    problems = {}
    categories = {}
    current_category = None
    current_phase = None
    current_description = None
    header_indices = {}
    phase_num = 0

    i = 0
    while i < len(lines):
        line = lines[i]

        # Detect phase headers: ## Phase N: ...
        phase_match = re.match(r"^## Phase (\d+):", line)
        if phase_match:
            phase_num = int(phase_match.group(1))

        # Detect category headers: ### N. Category Name
        cat_match = re.match(r"^### \d+\.\s+(.+)$", line)
        if cat_match:
            current_category = cat_match.group(1).strip()
            # Look for description in next lines (> Core skill: ...)
            desc = ""
            for j in range(i + 1, min(i + 4, len(lines))):
                desc_match = re.match(r"^>\s*(.+)$", lines[j])
                if desc_match:
                    desc = desc_match.group(1).strip()
                    break
            categories[current_category] = {
                "phase": phase_num,
                "description": desc,
            }
            header_indices = {}
            i += 1
            continue

        # Detect table header row
        cells = parse_table_row(line)
        if cells and current_category:
            # Check if this is a header row (contains '#' and 'Problem')
            cell_lower = [c.lower().strip() for c in cells]
            if "#" in cell_lower and "problem" in cell_lower:
                header_indices = {}
                for idx, name in enumerate(cell_lower):
                    if name == "#":
                        header_indices["num"] = idx
                    elif name == "problem":
                        header_indices["problem"] = idx
                    elif name == "difficulty":
                        header_indices["difficulty"] = idx
                    elif name == "list":
                        header_indices["list"] = idx
                    elif name == "finish":
                        header_indices["finish"] = idx
                    elif name == "date":
                        header_indices["date"] = idx
                    elif name == "review":
                        header_indices["review"] = idx
                i += 1
                continue

            # Skip separator rows
            if is_separator_row(cells):
                i += 1
                continue

            # Data row
            if header_indices and "num" in header_indices and "problem" in header_indices:
                num_idx = header_indices["num"]
                prob_idx = header_indices["problem"]
                if num_idx < len(cells) and prob_idx < len(cells):
                    num = cells[num_idx].strip()
                    title = cells[prob_idx].strip()

                    # Skip empty rows
                    if not num or not num.isdigit():
                        i += 1
                        continue

                    # Clean title: remove wiki-links [[...]]
                    title = re.sub(r"\[\[(.+?)\]\]", r"\1", title)

                    # Parse difficulty
                    difficulty = ""
                    if "difficulty" in header_indices and header_indices["difficulty"] < len(cells):
                        difficulty = cells[header_indices["difficulty"]].strip()

                    # Parse list membership
                    lists = []
                    if "list" in header_indices and header_indices["list"] < len(cells):
                        list_text = cells[header_indices["list"]].strip()
                        if "Blind 75" in list_text:
                            lists.append("Blind 75")
                        if "Top 100" in list_text:
                            lists.append("Top 100")

                    # Parse finish status
                    finished = False
                    finish_text = ""
                    if "finish" in header_indices and header_indices["finish"] < len(cells):
                        finish_text = cells[header_indices["finish"]].strip()
                        finished = "✅" in finish_text

                    # Parse date
                    finish_date = None
                    if "date" in header_indices and header_indices["date"] < len(cells):
                        finish_date = parse_date_field(cells[header_indices["date"]])

                    # Parse review notes
                    review_notes = ""
                    if "review" in header_indices and header_indices["review"] < len(cells):
                        review_notes = cells[header_indices["review"]].strip()

                    # Preserve existing review data if problem already tracked
                    existing = problems.get(num, {})
                    problems[num] = {
                        "title": title,
                        "difficulty": difficulty,
                        "category": current_category,
                        "lists": lists,
                        "finished": finished,
                        "finish_date": finish_date,
                        "note_file": existing.get("note_file"),
                        "review": existing.get("review"),
                    }

        i += 1

    return problems, categories


# ─── Note Scanner ──────────────────────────────────────────────────────────────

def scan_notes():
    """Scan .md files and return (note_map, custom_groups).

    note_map: {problem_id: filename}
    custom_groups: {group_name: {"problem_ids": [...], "note_file": filename}}
    """
    note_map = {}
    custom_groups = {}

    for f in NOTES_DIR.glob("*.md"):
        name = f.name
        # Skip non-problem files
        if name.startswith("00 ") or name.startswith("01 ") or name.startswith("02 "):
            continue
        if name.startswith("IELTS") or name.startswith("Avoiding"):
            continue

        # Multi-problem group: "1 & 167 & 15 - Two Sum Three Sum 系列.md"
        group_match = re.match(r"^([\d\s&]+)\s*-\s*(.+)\.md$", name)
        if group_match and "&" in group_match.group(1):
            nums_part = group_match.group(1)
            group_title = group_match.group(2).strip()
            nums = [n.strip() for n in nums_part.split("&") if n.strip().isdigit()]
            if nums:
                for n in nums:
                    note_map[n] = name
                custom_groups[group_title] = {
                    "problem_ids": nums,
                    "note_file": name,
                }
            continue

        # Single problem: "704 - Binary Search.md"
        single_match = re.match(r"^(\d+)\s*-\s*.+\.md$", name)
        if single_match:
            num = single_match.group(1)
            note_map[num] = name
            continue

        # Date-based practice files: "2026.3.18 practice leetcode.md"
        # Files like "LeetCode questions 217.md"
        # These are ignored

    return note_map, custom_groups


def parse_note_file(filepath):
    """Extract structured data from a note markdown file."""
    if not filepath or not (NOTES_DIR / filepath).exists():
        return {}

    content = (NOTES_DIR / filepath).read_text(encoding="utf-8")
    data = {}

    # Difficulty
    m = re.search(r"\*\*Difficulty:\*\*\s*(\w+)", content)
    if m:
        data["difficulty"] = m.group(1)

    # Tags
    m = re.search(r"\*\*Tags:\*\*\s*(.+)", content)
    if m:
        data["tags"] = [t.strip() for t in m.group(1).split(",")]

    # Key Insight / Approach section
    sections = re.split(r"^##\s+", content, flags=re.MULTILINE)
    for section in sections:
        header_line = section.split("\n", 1)[0].strip()
        body = section.split("\n", 1)[1].strip() if "\n" in section else ""
        if any(kw in header_line.lower() for kw in ["key insight", "approach", "核心"]):
            # Take first paragraph, skip lines that are just headers
            lines = [l for l in body.split("\n\n")[0].strip().split("\n")
                     if l.strip() and not l.strip().startswith("**Key Insight")]
            para = " ".join(lines).strip()
            # Strip markdown bold
            para = re.sub(r"\*\*(.+?)\*\*", r"\1", para)
            if para:
                data["key_insight"] = para
                break

    # Code blocks
    code_blocks = re.findall(r"```(?:python)?\n(.+?)```", content, re.DOTALL)
    if code_blocks:
        data["code_blocks"] = code_blocks

    return data


# ─── Sync Command ─────────────────────────────────────────────────────────────

def cmd_sync(args):
    tracker = load_tracker()
    problems, categories = parse_roadmap()
    note_map, custom_groups = scan_notes()

    # Merge note files into problems
    for pid, filename in note_map.items():
        if pid in problems:
            problems[pid]["note_file"] = filename

    # Merge with existing tracker (preserve review data)
    for pid, pdata in problems.items():
        if pid in tracker["problems"]:
            existing = tracker["problems"][pid]
            pdata["review"] = existing.get("review")
            # Don't overwrite note_file if already set and new is None
            if not pdata["note_file"] and existing.get("note_file"):
                pdata["note_file"] = existing["note_file"]

    tracker["problems"] = problems
    tracker["categories"] = categories

    # Merge custom groups (preserve existing, add new)
    for gname, gdata in custom_groups.items():
        tracker["custom_groups"][gname] = gdata

    save_tracker(tracker)

    n_problems = len(problems)
    n_cats = len(categories)
    n_finished = sum(1 for p in problems.values() if p["finished"])
    n_notes = sum(1 for p in problems.values() if p.get("note_file"))
    n_groups = len(tracker["custom_groups"])

    print(f"Synced: {n_problems} problems, {n_cats} categories, "
          f"{n_finished} finished, {n_notes} with notes, {n_groups} custom groups")


# ─── Status Command ───────────────────────────────────────────────────────────

def cmd_status(args):
    tracker = load_tracker()
    if not tracker["problems"]:
        print("No data. Run: python lc.py sync")
        return

    problems = tracker["problems"]
    total = len(problems)
    finished = sum(1 for p in problems.values() if p["finished"])
    blind75 = sum(1 for p in problems.values() if "Blind 75" in p.get("lists", []))
    blind75_done = sum(1 for p in problems.values()
                       if "Blind 75" in p.get("lists", []) and p["finished"])

    # Review stats
    due = 0
    for p in problems.values():
        r = p.get("review")
        if r and r.get("next_review"):
            if r["next_review"] <= today_iso():
                due += 1

    print(f"{finished}/{total} solved ({finished*100//total}%) | "
          f"Blind 75: {blind75_done}/{blind75} | "
          f"{due} reviews due today")


# ─── Spaced Repetition ────────────────────────────────────────────────────────

def new_review():
    return {
        "confidence": 0,
        "ease_factor": 2.5,
        "interval_days": 0,
        "next_review": (today_date() + timedelta(days=1)).isoformat(),
        "review_count": 0,
        "last_reviewed": None,
        "history": [],
    }


def update_review(review, confidence):
    """SM-2 spaced repetition algorithm."""
    if confidence < 3:
        review["interval_days"] = 1
        review["review_count"] = 0
    else:
        if review["review_count"] == 0:
            review["interval_days"] = 1
        elif review["review_count"] == 1:
            review["interval_days"] = 3
        else:
            review["interval_days"] = round(
                review["interval_days"] * review["ease_factor"]
            )
        review["review_count"] += 1

    # Adjust ease factor (bounded 1.3 to 2.5)
    review["ease_factor"] = max(1.3, min(2.5,
        review["ease_factor"]
        + 0.1 - (5 - confidence) * (0.08 + (5 - confidence) * 0.02)
    ))

    review["confidence"] = confidence
    review["last_reviewed"] = today_iso()
    review["next_review"] = (
        today_date() + timedelta(days=review["interval_days"])
    ).isoformat()
    review["history"].append({"date": today_iso(), "confidence": confidence})


def get_review_queue(tracker):
    """Get problems due for review, sorted by priority."""
    today = today_iso()
    queue = []

    for pid, p in tracker["problems"].items():
        r = p.get("review")
        if not r or not r.get("next_review"):
            continue
        if r["next_review"] <= today:
            days_overdue = (today_date() - date.fromisoformat(r["next_review"])).days
            queue.append((pid, p, days_overdue))

    # Sort: most overdue first, then lowest confidence
    queue.sort(key=lambda x: (-x[2], x[1].get("review", {}).get("confidence", 5)))
    return queue


CONFIDENCE_LABELS = {
    1: "Again (forgot)",
    2: "Hard (struggled)",
    3: "Okay (some difficulty)",
    4: "Good (minor hesitation)",
    5: "Easy (instant recall)",
}


def cmd_review(args):
    tracker = load_tracker()
    if not tracker["problems"]:
        print("No data. Run: python lc.py sync")
        return

    queue = get_review_queue(tracker)

    if not queue:
        # Check if any problems are being tracked
        tracked = sum(1 for p in tracker["problems"].values() if p.get("review"))
        if tracked == 0:
            print("No problems tracked for review yet.")
            print("Start with: python lc.py review start <number>")
            print("Or track all finished: python lc.py review start --all")
        else:
            print("No reviews due today! You're all caught up.")
            # Show next upcoming
            upcoming = []
            for pid, p in tracker["problems"].items():
                r = p.get("review")
                if r and r.get("next_review") and r["next_review"] > today_iso():
                    upcoming.append((pid, p, r["next_review"]))
            upcoming.sort(key=lambda x: x[2])
            if upcoming:
                pid, p, nxt = upcoming[0]
                print(f"Next review: #{pid} {p['title']} on {nxt}")
        return

    print(f"Review Queue for {today_iso()} ({len(queue)} due):\n")
    for i, (pid, p, days_overdue) in enumerate(queue, 1):
        r = p["review"]
        overdue_str = f" (overdue {days_overdue}d)" if days_overdue > 0 else ""
        conf_str = f"Confidence: {r['confidence']}/5" if r["confidence"] else "Never reviewed"
        last = r.get("last_reviewed", "never")
        print(f"  {i}. [#{pid}] {p['title']} ({p['difficulty']}) — {p['category']}")
        print(f"     Last: {last} | {conf_str} | Interval: {r['interval_days']}d{overdue_str}")

    print(f"\nRecord: python lc.py review done <number> <confidence 1-5>")
    print("  1=forgot  2=hard  3=okay  4=good  5=easy")


def cmd_review_start(args):
    tracker = load_tracker()
    if not tracker["problems"]:
        print("No data. Run: python lc.py sync")
        return

    if args.all_problems:
        count = 0
        for pid, p in tracker["problems"].items():
            if p["finished"] and not p.get("review"):
                p["review"] = new_review()
                count += 1
        save_tracker(tracker)
        print(f"Started tracking {count} finished problems for review.")
        if count:
            print(f"First reviews due: {(today_date() + timedelta(days=1)).isoformat()}")
        return

    if not args.target:
        print("Usage: python lc.py review start <number>")
        print("   or: python lc.py review start --all")
        return

    pid = args.target
    if pid not in tracker["problems"]:
        print(f"Problem #{pid} not found in tracker.")
        return
    p = tracker["problems"][pid]
    if p.get("review"):
        print(f"#{pid} {p['title']} is already being tracked.")
        return
    p["review"] = new_review()
    save_tracker(tracker)
    print(f"Started tracking #{pid} {p['title']}.")
    print(f"First review due: {(today_date() + timedelta(days=1)).isoformat()}")


def cmd_review_done(args):
    tracker = load_tracker()
    pid = args.number
    confidence = args.confidence

    if confidence < 1 or confidence > 5:
        print("Confidence must be 1-5.")
        return

    if pid not in tracker["problems"]:
        print(f"Problem #{pid} not found.")
        return

    p = tracker["problems"][pid]
    if not p.get("review"):
        print(f"#{pid} is not being tracked. Run: python lc.py review start {pid}")
        return

    update_review(p["review"], confidence)
    save_tracker(tracker)

    r = p["review"]
    label = CONFIDENCE_LABELS.get(confidence, "")
    print(f"Recorded review for #{pid} {p['title']}")
    print(f"  Confidence: {confidence}/5 ({label})")
    print(f"  Next review: {r['next_review']} (in {r['interval_days']} days)")


# ─── Dashboard ─────────────────────────────────────────────────────────────────

def render_bar(done, total, width=20):
    if total == 0:
        return " " * width
    filled = round(done / total * width)
    return "#" * filled + "." * (width - filled)


def cmd_dash(args):
    tracker = load_tracker()
    if not tracker["problems"]:
        print("No data. Run: python lc.py sync")
        return

    problems = tracker["problems"]
    total = len(problems)
    finished = sum(1 for p in problems.values() if p["finished"])
    blind75 = [p for p in problems.values() if "Blind 75" in p.get("lists", [])]
    blind75_done = sum(1 for p in blind75 if p["finished"])

    easy_done = sum(1 for p in problems.values() if p["finished"] and p["difficulty"] == "Easy")
    med_done = sum(1 for p in problems.values() if p["finished"] and p["difficulty"] == "Medium")
    hard_done = sum(1 for p in problems.values() if p["finished"] and p["difficulty"] == "Hard")
    notes = sum(1 for p in problems.values() if p.get("note_file"))

    print()
    print("  LeetCode Progress Dashboard")
    print("  " + "=" * 58)
    print(f"  Total: {finished}/{total} ({finished*100//total}%)  |  "
          f"Blind 75: {blind75_done}/{len(blind75)}  |  Notes: {notes}")
    print(f"  Easy: {easy_done}  Medium: {med_done}  Hard: {hard_done}")
    print()

    # Category breakdown
    cat_stats = defaultdict(lambda: {"done": 0, "total": 0})
    for p in problems.values():
        cat = p.get("category", "Other")
        cat_stats[cat]["total"] += 1
        if p["finished"]:
            cat_stats[cat]["done"] += 1

    # Sort by phase order
    cat_order = []
    for cat_name, cat_info in tracker.get("categories", {}).items():
        cat_order.append((cat_info.get("phase", 99), cat_name))
    cat_order.sort()

    print("  Category Breakdown:")
    print("  " + "-" * 58)

    max_name_len = max(len(c) for _, c in cat_order) if cat_order else 20

    for _, cat_name in cat_order:
        s = cat_stats.get(cat_name, {"done": 0, "total": 0})
        bar = render_bar(s["done"], s["total"], 15)
        pct = s["done"] * 100 // s["total"] if s["total"] else 0
        marker = " *" if s["done"] == s["total"] and s["total"] > 0 else ""
        arrow = " <-- Next" if s["done"] == 0 and all(
            cat_stats.get(prev_cat, {}).get("done", 0) > 0
            for pp, prev_cat in cat_order
            if pp < _ and prev_cat in cat_stats
        ) else ""
        print(f"  {cat_name:<{max_name_len}}  {bar}  {s['done']:>2}/{s['total']:<2}  {pct:>3}%{marker}{arrow}")

    # Review stats
    print()
    due = 0
    overdue = 0
    upcoming_7d = 0
    confidences = []
    tracked = 0

    for p in problems.values():
        r = p.get("review")
        if not r:
            continue
        tracked += 1
        if r.get("confidence"):
            confidences.append(r["confidence"])
        if r.get("next_review"):
            nr = r["next_review"]
            if nr <= today_iso():
                due += 1
                if nr < today_iso():
                    overdue += 1
            elif nr <= (today_date() + timedelta(days=7)).isoformat():
                upcoming_7d += 1

    if tracked:
        avg_conf = sum(confidences) / len(confidences) if confidences else 0
        print(f"  Review: {due} due today | {overdue} overdue | "
              f"{upcoming_7d} upcoming (7d) | Tracking: {tracked}")
        if confidences:
            print(f"  Avg confidence: {avg_conf:.1f}/5")

        # Weakest categories (by avg confidence)
        cat_confs = defaultdict(list)
        for p in problems.values():
            r = p.get("review")
            if r and r.get("confidence"):
                cat_confs[p["category"]].append(r["confidence"])
        weak = sorted(cat_confs.items(), key=lambda x: sum(x[1])/len(x[1]))
        if weak:
            weakest = [(c, sum(v)/len(v)) for c, v in weak[:3] if sum(v)/len(v) < 4]
            if weakest:
                weak_str = ", ".join(f"{c} ({v:.1f})" for c, v in weakest)
                print(f"  Weakest: {weak_str}")
    else:
        print("  No problems tracked for review. Run: python lc.py review start --all")
    print()


# ─── Hint Generator ───────────────────────────────────────────────────────────

HINT_TEMPLATES = [
    # Level 1: Pattern
    """I'm working on LeetCode #{num} "{title}" ({difficulty}).
Without giving me the solution, what algorithmic PATTERN or technique
is commonly used for this type of problem? Just name the pattern and
explain in one sentence why it applies here.""",

    # Level 2: Approach
    """I'm working on LeetCode #{num} "{title}" ({difficulty}).
Category: {category}.{insight_line}
Without writing code, explain the HIGH-LEVEL APPROACH in 2-3 sentences.
What data structures should I use? What should I track?""",

    # Level 3: Key Insight
    """I'm working on LeetCode #{num} "{title}" ({difficulty}).
Category: {category}. I understand the general approach but I'm stuck.
What is the KEY INSIGHT or trick that makes this problem solvable?
Give me one critical observation, not the code.""",

    # Level 4: Pseudocode
    """I'm working on LeetCode #{num} "{title}" ({difficulty}).
Category: {category}. I understand the approach but can't translate
it to code. Please give me PSEUDOCODE (not Python) showing the
algorithm structure. Do NOT give the final solution.""",
]


def cmd_hint(args):
    tracker = load_tracker()
    pid = args.number

    if pid not in tracker["problems"]:
        print(f"Problem #{pid} not found. Run: python lc.py sync")
        return

    p = tracker["problems"][pid]
    note_data = parse_note_file(p.get("note_file"))

    insight_line = ""
    if note_data.get("key_insight"):
        insight_line = f"\nI already know this insight: \"{note_data['key_insight'][:100]}...\""
        insight_line += "\nGive me a DIFFERENT angle or deeper understanding."

    fmt = {
        "num": pid,
        "title": p["title"],
        "difficulty": p["difficulty"],
        "category": p["category"],
        "insight_line": insight_line,
    }

    if args.level:
        if args.level < 1 or args.level > 4:
            print("Level must be 1-4.")
            return
        levels = [args.level - 1]
    else:
        levels = range(4)

    level_names = ["Pattern Hint", "Approach Hint", "Key Insight", "Pseudocode"]

    print(f"\nProblem: #{pid} {p['title']} ({p['difficulty']}) — {p['category']}")
    print("Copy-paste into any AI chat:\n")

    for idx in levels:
        print(f"--- Level {idx+1}: {level_names[idx]} ---")
        print(HINT_TEMPLATES[idx].format(**fmt))
        print()


# ─── Note Command ─────────────────────────────────────────────────────────────

def cmd_note(args):
    tracker = load_tracker()
    pid = args.number

    if pid not in tracker["problems"]:
        print(f"Problem #{pid} not found. Run: python lc.py sync")
        return

    p = tracker["problems"][pid]
    note_file = p.get("note_file")

    if not note_file or not (NOTES_DIR / note_file).exists():
        print(f"No note found for #{pid} {p['title']}.")
        print(f"Create: \"{pid} - {p['title']}.md\"")
        return

    content = (NOTES_DIR / note_file).read_text(encoding="utf-8")
    print(content)


# ─── Concept Grouping ─────────────────────────────────────────────────────────

def cmd_group(args):
    tracker = load_tracker()
    if not tracker["problems"]:
        print("No data. Run: python lc.py sync")
        return

    if not args.name:
        # List all groups
        print("\nCategories (from roadmap):")
        cat_order = sorted(tracker.get("categories", {}).items(),
                           key=lambda x: x[1].get("phase", 99))
        for cat_name, cat_info in cat_order:
            done = sum(1 for p in tracker["problems"].values()
                       if p["category"] == cat_name and p["finished"])
            total = sum(1 for p in tracker["problems"].values()
                        if p["category"] == cat_name)
            print(f"  {cat_name} ({done}/{total})")

        if tracker.get("custom_groups"):
            print("\nCustom Groups:")
            for gname, gdata in tracker["custom_groups"].items():
                ids = ", ".join(f"#{n}" for n in gdata["problem_ids"])
                print(f"  {gname} ({ids})")
        print()
        return

    name = args.name

    # Try to match category
    for cat_name in tracker.get("categories", {}):
        if name.lower() in cat_name.lower():
            print(f"\n{cat_name} — {tracker['categories'][cat_name].get('description', '')}")
            cat_problems = [(pid, p) for pid, p in tracker["problems"].items()
                            if p["category"] == cat_name]
            cat_problems.sort(key=lambda x: int(x[0]))
            for pid, p in cat_problems:
                status = "[done]" if p["finished"] else "[    ]"
                note_str = ""
                if p.get("note_file"):
                    note_str = " — has note"
                print(f"  {status} #{pid:<4} {p['title']} ({p['difficulty']}){note_str}")
            print()
            return

    # Try custom group
    for gname, gdata in tracker.get("custom_groups", {}).items():
        if name.lower() in gname.lower():
            print(f"\n{gname}")
            if gdata.get("note_file"):
                print(f"  Note: {gdata['note_file']}")
            for pid in gdata["problem_ids"]:
                p = tracker["problems"].get(pid, {})
                status = "[done]" if p.get("finished") else "[    ]"
                print(f"  {status} #{pid} {p.get('title', '?')} ({p.get('difficulty', '?')})")
            print()
            return

    print(f"No group matching '{name}' found.")
    print("Use: python lc.py group   (to see all groups)")


def cmd_group_add(args):
    tracker = load_tracker()
    name = args.name
    nums = args.numbers

    # Validate problem numbers exist
    valid = []
    for n in nums:
        if n in tracker["problems"]:
            valid.append(n)
        else:
            print(f"Warning: #{n} not found in tracker, skipping.")

    if not valid:
        print("No valid problems to add.")
        return

    tracker["custom_groups"][name] = {
        "problem_ids": valid,
        "note_file": None,
    }
    save_tracker(tracker)

    ids = ", ".join(f"#{n}" for n in valid)
    print(f"Created group \"{name}\" with {ids}")


# ─── Git Automation ────────────────────────────────────────────────────────────

def git_run(*cmd, check=True):
    """Run a git command in the notes directory."""
    result = subprocess.run(
        ["git"] + list(cmd),
        cwd=str(NOTES_DIR),
        capture_output=True,
        text=True,
    )
    if check and result.returncode != 0:
        print(f"git error: {result.stderr.strip()}")
    return result


def cmd_git_init(args):
    tracker = load_tracker()

    # Check if already initialized
    if (NOTES_DIR / ".git").exists():
        print("Git repo already exists.")
        return

    git_run("init", check=True)

    # Create .gitignore
    gitignore = NOTES_DIR / ".gitignore"
    gitignore.write_text(
        ".obsidian/\n.claude/\n.DS_Store\n__pycache__/\n*.pyc\n",
        encoding="utf-8",
    )

    # Count finished problems
    n_finished = sum(1 for p in tracker["problems"].values() if p["finished"])

    git_run("add", ".gitignore")
    # Add all markdown files, lc.py, and tracker.json
    for f in NOTES_DIR.glob("*.md"):
        git_run("add", f.name, check=False)
    git_run("add", "lc.py", check=False)
    if TRACKER.exists():
        git_run("add", "tracker.json", check=False)

    git_run("commit", "-m", f"init: LeetCode practice notes ({n_finished} problems solved)")

    tracker["git"]["initialized"] = True
    save_tracker(tracker)
    print(f"Initialized git repo with initial commit ({n_finished} problems).")


def cmd_git_save(args):
    # Check if git repo exists
    if not (NOTES_DIR / ".git").exists():
        print("No git repo. Run: python lc.py git init")
        return

    # Check for changes
    result = git_run("status", "--porcelain")
    if not result.stdout.strip():
        print("Nothing to commit.")
        return

    # Parse changed files
    changed = result.stdout.strip().split("\n")
    new_notes = []
    modified_notes = []
    other_files = []

    tracker = load_tracker()

    for line in changed:
        status = line[:2].strip()
        filename = line[3:].strip().strip('"')

        if filename.endswith(".md"):
            # Try to find problem number
            m = re.match(r"^(\d+)\s*[-&]", filename)
            if m:
                pid = m.group(1)
                p = tracker["problems"].get(pid, {})
                info = f"#{pid} {p.get('title', filename)}"
                if p.get("category"):
                    info += f" ({p['category']})"
            else:
                info = filename

            if status in ("?", "A"):
                new_notes.append(info)
            else:
                modified_notes.append(info)
        else:
            other_files.append(filename)

    # Generate commit message
    parts = []
    if new_notes:
        parts.append("add: " + "; ".join(new_notes[:3]))
    if modified_notes:
        parts.append("update: " + "; ".join(modified_notes[:3]))
    if other_files and not parts:
        parts.append("update: tracker data")

    msg = " | ".join(parts) if parts else "update: LeetCode notes"

    # Stage and commit
    git_run("add", "-A")
    git_run("commit", "-m", msg)
    print(f"Committed: {msg}")

    if args.push:
        result = git_run("push", "origin", "HEAD")
        if result.returncode == 0:
            print("Pushed to remote.")
        else:
            print("Push failed. Set remote first: python lc.py git remote <url>")


def cmd_git_remote(args):
    url = args.url

    # Check if remote exists
    result = git_run("remote", check=False)
    if "origin" in (result.stdout or ""):
        git_run("remote", "set-url", "origin", url)
    else:
        git_run("remote", "add", "origin", url)

    tracker = load_tracker()
    tracker["git"]["remote_url"] = url
    save_tracker(tracker)
    print(f"Remote 'origin' set to: {url}")


# ─── CLI Entry Point ──────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="LeetCode Practice Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command")

    # sync
    subparsers.add_parser("sync", help="Parse roadmap & scan notes")

    # status
    subparsers.add_parser("status", help="One-line summary")

    # dash
    subparsers.add_parser("dash", help="Progress dashboard")

    # review
    review_parser = subparsers.add_parser("review", help="Review queue & tracking")
    review_sub = review_parser.add_subparsers(dest="review_action")

    start_parser = review_sub.add_parser("start", help="Start tracking a problem")
    start_parser.add_argument("target", nargs="?", default=None, help="Problem number")
    start_parser.add_argument("--all", action="store_true", dest="all_problems", help="Track all finished")

    done_parser = review_sub.add_parser("done", help="Record review result")
    done_parser.add_argument("number", help="Problem number")
    done_parser.add_argument("confidence", type=int, help="1-5 confidence rating")

    # hint
    hint_parser = subparsers.add_parser("hint", help="Generate hint prompts")
    hint_parser.add_argument("number", help="Problem number")
    hint_parser.add_argument("--level", type=int, help="Hint level 1-4")

    # note
    note_parser = subparsers.add_parser("note", help="Display problem note")
    note_parser.add_argument("number", help="Problem number")

    # group
    group_parser = subparsers.add_parser("group", help="Concept groups")
    group_parser.add_argument("group_args", nargs="*", help="[name] or: add <name> <nums...>")

    # git
    git_parser = subparsers.add_parser("git", help="Git automation")
    git_sub = git_parser.add_subparsers(dest="git_action")

    git_sub.add_parser("init", help="Initialize git repo")

    save_parser = git_sub.add_parser("save", help="Auto-commit changes")
    save_parser.add_argument("--push", action="store_true", help="Push after commit")
    save_parser.add_argument("--message", "-m", help="Custom commit message")

    remote_parser = git_sub.add_parser("remote", help="Set GitHub remote")
    remote_parser.add_argument("url", help="Remote URL")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "sync":
        cmd_sync(args)
    elif args.command == "status":
        cmd_status(args)
    elif args.command == "dash":
        cmd_dash(args)
    elif args.command == "review":
        if not hasattr(args, "review_action") or not args.review_action:
            cmd_review(args)
        elif args.review_action == "start":
            cmd_review_start(args)
        elif args.review_action == "done":
            cmd_review_done(args)
    elif args.command == "hint":
        cmd_hint(args)
    elif args.command == "note":
        cmd_note(args)
    elif args.command == "group":
        ga = args.group_args if args.group_args else []
        if ga and ga[0] == "add":
            if len(ga) < 3:
                print("Usage: python lc.py group add <name> <num1> <num2> ...")
                return
            # Create a namespace for group add
            class GroupAddArgs:
                name = ga[1]
                numbers = ga[2:]
            cmd_group_add(GroupAddArgs())
        else:
            class GroupArgs:
                name = " ".join(ga) if ga else None
            cmd_group(GroupArgs())
    elif args.command == "git":
        if not hasattr(args, "git_action") or not args.git_action:
            print("Usage: python lc.py git {init|save|remote}")
        elif args.git_action == "init":
            cmd_git_init(args)
        elif args.git_action == "save":
            cmd_git_save(args)
        elif args.git_action == "remote":
            cmd_git_remote(args)


if __name__ == "__main__":
    main()
