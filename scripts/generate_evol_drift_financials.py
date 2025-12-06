"""Generate EV0L drift financial projections in CSV and JSON formats.

The script recreates the data set provided by the user, appends a summary
row, writes CSV/JSON artifacts, and prints a readable table preview.
"""
ector,Job Types Created,Profit Sources,Estimated Profits (USD),Comment 🎮 EV0L Gaming (Meta Drift Gear),“2,400+ avatar stylists, beta testers, racers, gear installers”,“In-game drift tournaments, EV0L Cleats & Gear sales, Twitch-style views”,4800000,“Momentum visuals converted to fan betting & fashion revenue (ENFT-tied, 8-months)” 🏈 C@ntC0@CHTH@T Agency,“120 trainers, 15 NIL agents, 45 college liaisons”,“Draft value appreciation, endorsements, branded cleat drift replays”,1100000,Tom’s “Explosive Edge” + drifting clip monetization 🧠 MetaMindz™ Drift Curriculum (Neuro),“50 AI educators, 90 coders, 30 stylists”,Avatar clone motion study & revenue from physical-virtual drift mirroring,2600000,Training AI to mimic player drift paths; sold to schools & leagues 👟 EVOL Gear (Fashion Drift Line),“300 merch installers, 50 holographic tailors”,Sales from ‘DRIFT’ series wearables & movement-reactive smart clothing,1900000,Gear lights up & changes color when drifting detected 🎥 EVOL Studios / Smart Posters (Drift Edition),“80 animators, 24 visual FX leads”,Streaming of “Legendary Drift Moments” (ESPN-style edits),1700000,Views → ENFT resales + direct ad partnership (BlueLion Ink) 🚘 BLEUSprinters / AutoDrift Showcases,“40 car riggers, 25 drone operators”,Showcase monetization + drift sponsor overlays,880000,Cross-promotion with Formula-E-style events TOTAL,,,12980000,“Total estimated profits across listed sectors = $12,980,000” data/evol_drift_financials.json New +51 -0

[ { “Sector”: “🎮 EV0L Gaming (Meta Drift Gear)”, “Job Types Created”: “2,400+ avatar stylists, beta testers, racers, gear installers”, “Profit Sources”: “In-game drift tournaments, EV0L Cleats & Gear sales, Twitch-style views”, “Estimated Profits (USD)”: 4800000, “Comment”: “Momentum visuals converted to fan betting & fashion revenue (ENFT-tied, 8-months)” }, { “Sector”: “🏈 C@ntC0@CHTH@T Agency”, “Job Types Created”: “120 trainers, 15 NIL agents, 45 college liaisons”, “Profit Sources”: “Draft value appreciation, endorsements, branded cleat drift replays”, “Estimated Profits (USD)”: 1100000, “Comment”: “Tom’s “Explosive Edge” + drifting clip monetization” }, { “Sector”: “🧠 MetaMindz™ Drift Curriculum (Neuro)”, “Job Types Created”: “50 AI educators, 90 coders, 30 stylists”, “Profit Sources”: “Avatar clone motion study & revenue from physical-virtual drift mirroring”, “Estimated Profits (USD)”: 2600000, “Comment”: “Training AI to mimic player drift paths; sold to schools & leagues” }, { “Sector”: “👟 EVOL Gear (Fashion Drift Line)”, “Job Types Created”: “300 merch installers, 50 holographic tailors”, “Profit Sources”: “Sales from ‘DRIFT’ series wearables & movement-reactive smart clothing”, “Estimated Profits (USD)”: 1900000, “Comment”: “Gear lights up & changes color when drifting detected” }, { “Sector”: “🎥 EVOL Studios / Smart Posters (Drift Edition)”, “Job Types Created”: “80 animators, 24 visual FX leads”, “Profit Sources”: “Streaming of “Legendary Drift Moments” (ESPN-style edits)”, “Estimated Profits (USD)”: 1700000, “Comment”: “Views → ENFT resales + direct ad partnership (BlueLion Ink)” }, { “Sector”: “🚘 BLEUSprinters / AutoDrift Showcases”, “Job Types Created”: “40 car riggers, 25 drone operators”, “Profit Sources”: “Showcase monetization + drift sponsor overlays”, “Estimated Profits (USD)”: 880000, “Comment”: “Cross-promotion with Formula-E-style events” }, { “Sector”: “TOTAL”, “Job Types Created”: “”, “Profit Sources”: “”, “Estimated Profits (USD)”: 12980000, “Comment”: “Total estimated profits across listed sectors = $12,980,000” } ] scripts/generate_evol_drift_financials.py New +150 -0

“”“Generate EV0L drift financial projections in CSV and JSON formats.

The script recreates the data set provided by the user, appends a summary row, writes CSV/JSON artifacts, and prints a readable table preview. “”” from future import annotations

import csv import json from pathlib import Path from typing import Iterable, List, Tuple

DATA_ROWS = [ { “Sector”: “🎮 EV0L Gaming (Meta Drift Gear)”, “Job Types Created”: “2,400+ avatar stylists, beta testers, racers, gear installers”, “Profit Sources”: “In-game drift tournaments, EV0L Cleats & Gear sales, Twitch-style views”, “Estimated Profits (USD)”: 4_800_000, “Comment”: “Momentum visuals converted to fan betting & fashion revenue (ENFT-tied, 8-months)”, }, { “Sector”: “🏈 C@ntC0@CHTH@T Agency”, “Job Types Created”: “120 trainers, 15 NIL agents, 45 college liaisons”, “Profit Sources”: “Draft value appreciation, endorsements, branded cleat drift replays”, “Estimated Profits (USD)”: 1_100_000, “Comment”: “Tom’s “Explosive Edge” + drifting clip monetization”, }, { “Sector”: “🧠 MetaMindz™ Drift Curriculum (Neuro)”, “Job Types Created”: “50 AI educators, 90 coders, 30 stylists”, “Profit Sources”: “Avatar clone motion study & revenue from physical-virtual drift mirroring”, “Estimated Profits (USD)”: 2_600_000, “Comment”: “Training AI to mimic player drift paths; sold to schools & leagues”, }, { “Sector”: “👟 EVOL Gear (Fashion Drift Line)”, “Job Types Created”: “300 merch installers, 50 holographic tailors”, “Profit Sources”: “Sales from ‘DRIFT’ series wearables & movement-reactive smart clothing”, “Estimated Profits (USD)”: 1_900_000, “Comment”: “Gear lights up & changes color when drifting detected”, }, { “Sector”: “🎥 EVOL Studios / Smart Posters (Drift Edition)”, “Job Types Created”: “80 animators, 24 visual FX leads”, “Profit Sources”: “Streaming of “Legendary Drift Moments” (ESPN-style edits)”, “Estimated Profits (USD)”: 1_700_000, “Comment”: “Views → ENFT resales + direct ad partnership (BlueLion Ink)”, }, { “Sector”: “🚘 BLEUSprinters / AutoDrift Showcases”, “Job Types Created”: “40 car riggers, 25 drone operators”, “Profit Sources”: “Showcase monetization + drift sponsor overlays”, “Estimated Profits (USD)”: 880_000, “Comment”: “Cross-promotion with Formula-E-style events”, }, ]

FIELDNAMES = [ “Sector”, “Job Types Created”, “Profit Sources”, “Estimated Profits (USD)”, “Comment”, ]

def build_rows() -> Tuple[List[dict], int]: “”“Construct the financial projection dataset with a summary row.”””

rows = list(DATA_ROWS)
total = sum(row["Estimated Profits (USD)"] for row in rows)
summary_row = {
    "Sector": "TOTAL",
    "Job Types Created": "",
    "Profit Sources": "",
    "Estimated Profits (USD)": total,
    "Comment": f"Total estimated profits across listed sectors = ${total:,}",
}
rows.append(summary_row)
return rows, total


def write_csv(rows: Iterable[dict], path: Path) -> None: “”“Write the dataset to a CSV file.”””

with path.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
    writer.writeheader()
    writer.writerows(rows)


def write_json(rows: Iterable[dict], path: Path) -> None: “”“Write the dataset to a JSON file.”””

with path.open("w", encoding="utf-8") as handle:
    json.dump(list(rows), handle, ensure_ascii=False, indent=2)


def format_value(field: str, value) -> str: “”“Format a field for preview display.”””

if field == "Estimated Profits (USD)" and isinstance(value, (int, float)):
    return f"${value:,.0f}"
return str(value)


def print_preview(rows: Iterable[dict], csv_path: Path, json_path: Path, total: int) -> None: “”“Print a table preview and saved file paths.”””

formatted_rows = [
    {field: format_value(field, row.get(field, "")) for field in FIELDNAMES}
    for row in rows
]
column_widths = {
    field: max(len(field), max(len(r[field]) for r in formatted_rows))
    for field in FIELDNAMES
}

def render_row(row_dict: dict) -> str:
    return " | ".join(
        row_dict[field].ljust(column_widths[field])
        for field in FIELDNAMES
    )

print("Preview of EV0L Drift Financials:")
header = {field: field for field in FIELDNAMES}
print(render_row(header))
print("-+-".join("-" * column_widths[field] for field in FIELDNAMES))
for row in formatted_rows:
    print(render_row(row))

print("\nFiles saved:")
print(f"CSV -> {csv_path}")
print(f"JSON -> {json_path}")
print(f"\nTotal estimated profits (USD): ${total:,}")


if name == “main”: dataset, total_value = build_rows() output_dir = Path(file).resolve().parent.parent / “data” output_dir.mkdir(parents=True, exist_ok=True)

csv_output = output_dir / "evol_drift_financials.csv"
json_output = output_dir / "evol_drift_financials.json"

write_csv(dataset, csv_output)
write_json(dataset, json_output)
print_preview(dataset, csv_output, json_output, total_value)
        "Sector": "🎮 EV0L Gaming (Meta Drift Gear)",
        "Job Types Created": "2,400+ avatar stylists, beta testers, racers, gear installers",
        "Profit Sources": "In-game drift tournaments, EV0L Cleats & Gear sales, Twitch-style views",
        "Estimated Profits (USD)": 4_800_000,
        "Comment": "Momentum visuals converted to fan betting & fashion revenue (ENFT-tied, 8-months)",
    },
    {
        "Sector": "🏈 C@ntC0@CHTH@T Agency",
        "Job Types Created": "120 trainers, 15 NIL agents, 45 college liaisons",
        "Profit Sources": "Draft value appreciation, endorsements, branded cleat drift replays",
        "Estimated Profits (USD)": 1_100_000,
        "Comment": "Tom's \"Explosive Edge\" + drifting clip monetization",
    },
    {
        "Sector": "🧠 MetaMindz™ Drift Curriculum (Neuro)",
        "Job Types Created": "50 AI educators, 90 coders, 30 stylists",
        "Profit Sources": "Avatar clone motion study & revenue from physical-virtual drift mirroring",
        "Estimated Profits (USD)": 2_600_000,
        "Comment": "Training AI to mimic player drift paths; sold to schools & leagues",
    },
    {
        "Sector": "👟 EVOL Gear (Fashion Drift Line)",
        "Job Types Created": "300 merch installers, 50 holographic tailors",
        "Profit Sources": "Sales from 'DRIFT' series wearables & movement-reactive smart clothing",
        "Estimated Profits (USD)": 1_900_000,
        "Comment": "Gear lights up & changes color when drifting detected",
    },
    {
        "Sector": "🎥 EVOL Studios / Smart Posters (Drift Edition)",
        "Job Types Created": "80 animators, 24 visual FX leads",
        "Profit Sources": "Streaming of \"Legendary Drift Moments\" (ESPN-style edits)",
        "Estimated Profits (USD)": 1_700_000,
        "Comment": "Views → ENFT resales + direct ad partnership (BlueLion Ink)",
    },
    {
        "Sector": "🚘 BLEUSprinters / AutoDrift Showcases",
        "Job Types Created": "40 car riggers, 25 drone operators",
        "Profit Sources": "Showcase monetization + drift sponsor overlays",
        "Estimated Profits (USD)": 880_000,
        "Comment": "Cross-promotion with Formula-E-style events",
    },
]


FIELDNAMES = [
    "Sector",
    "Job Types Created",
    "Profit Sources",
    "Estimated Profits (USD)",
    "Comment",
]


def build_rows() -> Tuple[List[dict], int]:
    """Construct the financial projection dataset with a summary row."""

    rows = list(DATA_ROWS)
    total = sum(row["Estimated Profits (USD)"] for row in rows)
    summary_row = {
        "Sector": "TOTAL",
        "Job Types Created": "",
        "Profit Sources": "",
        "Estimated Profits (USD)": total,
        "Comment": f"Total estimated profits across listed sectors = ${total:,}",
    }
    rows.append(summary_row)
    return rows, total


def write_csv(rows: Iterable[dict], path: Path) -> None:
    """Write the dataset to a CSV file."""

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def write_json(rows: Iterable[dict], path: Path) -> None:
    """Write the dataset to a JSON file."""

    with path.open("w", encoding="utf-8") as handle:
        json.dump(list(rows), handle, ensure_ascii=False, indent=2)


def format_value(field: str, value) -> str:
    """Format a field for preview display."""

    if field == "Estimated Profits (USD)" and isinstance(value, (int, float)):
        return f"${value:,.0f}"
    return str(value)


def print_preview(rows: Iterable[dict], csv_path: Path, json_path: Path, total: int) -> None:
    """Print a table preview and saved file paths."""

    formatted_rows = [
        {field: format_value(field, row.get(field, "")) for field in FIELDNAMES}
        for row in rows
    ]
    column_widths = {
        field: max(len(field), max(len(r[field]) for r in formatted_rows))
        for field in FIELDNAMES
    }

    def render_row(row_dict: dict) -> str:
        return " | ".join(
            row_dict[field].ljust(column_widths[field])
            for field in FIELDNAMES
        )

    print("Preview of EV0L Drift Financials:")
    header = {field: field for field in FIELDNAMES}
    print(render_row(header))
    print("-+-".join("-" * column_widths[field] for field in FIELDNAMES))
    for row in formatted_rows:
        print(render_row(row))

    print("\nFiles saved:")
    print(f"CSV -> {csv_path}")
    print(f"JSON -> {json_path}")
    print(f"\nTotal estimated profits (USD): ${total:,}")


if __name__ == "__main__":
    dataset, total_value = build_rows()
    output_dir = Path(__file__).resolve().parent.parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_output = output_dir / "evol_drift_financials.csv"
    json_output = output_dir / "evol_drift_financials.json"

    write_csv(dataset, csv_output)
    write_json(dataset, json_output)
    print_preview(dataset, csv_output, json_output, total_value)
