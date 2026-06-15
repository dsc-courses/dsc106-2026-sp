#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pandas",
#     "pillow",
#     "pymupdf",
#     "pyyaml",
# ]
# ///
"""Build the Spring 2026 project showcase data and thumbnails.

Usage:
    ./scripts/showcase_gradescope_export_to_site.py <gradescope_export_dir>
    ./scripts/showcase_gradescope_export_to_site.py <gradescope_export_dir> --score-csv <score_csv>

The export directory should contain submission_metadata.csv and
submission_<id>/ directories from Gradescope.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import fitz
import pandas as pd
import yaml
from PIL import Image, ImageOps


COL_TITLE = "Question 1 Response"
COL_PROJECT_URL = "Question 3 Response"
COL_VIDEO_URL = "Question 4 Response"
COL_SCREENSHOT = "Question 5.1 Response"
COL_VIDEO_PERMISSION = "Question 5.2 Response"
COL_SUBMISSION_ID = "Submission ID"
COL_STUDENT_NAME = "Name"
COL_TOTAL_SCORE = "Total Score"
COL_SCORE_SUBMISSION_ID = "Assignment Submission ID"
COL_SCORE = "Score"

THUMBNAIL_SIZE = (300, 200)
SUPPORTED_EXTENSIONS = {".gif", ".jpeg", ".jpg", ".pdf", ".png", ".webp"}

AWARDS_BY_URL = {
    "https://argsweet.github.io/delhi-air": "Best Project",
    "https://songsu-eight.github.io/warming-to-heat-risk": "Best Project",
    "https://colin-tran.github.io/dsc106-spr26-finalproject-sd_route_choice": "Best Project",
    "https://kmalva.github.io/hurricane-final_project": "Best Project",
    "https://kimichenn.github.io/dsc106-final-project": "Honorable Mention",
    "https://kyleduongg.github.io/umpiring": "Honorable Mention",
    "https://hannahhuangh.github.io/canyoulivethere": "Honorable Mention",
}


def has_response(value: Any) -> bool:
    if pd.isna(value):
        return False

    text = str(value).strip()
    return bool(text and text != "[]")


def clean_text(value: Any) -> str:
    if pd.isna(value):
        return ""

    return str(value).strip()


def normalize_url(url: str) -> str:
    return url.strip().rstrip("/").lower()


def award_for_url(url: str) -> str | None:
    return AWARDS_BY_URL.get(normalize_url(url))


def sort_key(project: dict[str, Any]) -> tuple[int, float]:
    award = project.get("award", "").lower()
    if "best project" in award:
        priority = 0
    elif "honorable mention" in award:
        priority = 1
    else:
        priority = 2

    score = project.get("_sort_total_score")
    return priority, -score if score is not None else float("inf")


def load_image(path: Path) -> Image.Image:
    if path.suffix.lower() == ".pdf":
        document = fitz.open(path)
        try:
            page = document.load_page(0)
            pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
            return Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
        finally:
            document.close()

    image = Image.open(path)
    image.seek(0)
    return image.copy()


def save_thumbnail(source_path: Path, output_path: Path) -> None:
    image = load_image(source_path)
    image = ImageOps.exif_transpose(image)

    if image.mode in ("RGBA", "LA") or (
        image.mode == "P" and "transparency" in image.info
    ):
        background = Image.new("RGB", image.size, "white")
        background.paste(image.convert("RGBA"), mask=image.convert("RGBA").split()[-1])
        image = background
    else:
        image = image.convert("RGB")

    thumbnail = ImageOps.contain(image, THUMBNAIL_SIZE, Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", THUMBNAIL_SIZE, "white")
    offset = (
        (THUMBNAIL_SIZE[0] - thumbnail.width) // 2,
        (THUMBNAIL_SIZE[1] - thumbnail.height) // 2,
    )
    canvas.paste(thumbnail, offset)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path)


def find_submission_file(export_dir: Path, submission_id: int) -> Path | None:
    submission_dir = export_dir / f"submission_{submission_id}"
    if not submission_dir.is_dir():
        return None

    for path in sorted(submission_dir.iterdir()):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            return path

    return None


def load_scores(score_csv_path: Path | None) -> dict[int, float]:
    if score_csv_path is None:
        return {}

    df = pd.read_csv(score_csv_path)
    scores: dict[int, float] = {}

    for _, row in df.iterrows():
        submission_id = pd.to_numeric(
            row.get(COL_SCORE_SUBMISSION_ID), errors="coerce"
        )
        score = pd.to_numeric(row.get(COL_SCORE), errors="coerce")
        if pd.isna(submission_id) or pd.isna(score):
            continue

        scores[int(submission_id)] = float(score)

    return scores


def build_projects(
    df: pd.DataFrame, scores_by_submission_id: dict[int, float]
) -> list[dict[str, Any]]:
    grouped_projects: dict[int, dict[str, Any]] = {}

    for _, row in df.iterrows():
        if not has_response(row[COL_SCREENSHOT]):
            continue

        submission_id = int(row[COL_SUBMISSION_ID])

        if submission_id not in grouped_projects:
            url = clean_text(row[COL_PROJECT_URL])
            score = scores_by_submission_id.get(submission_id)
            total_score = pd.to_numeric(row.get(COL_TOTAL_SCORE), errors="coerce")
            project: dict[str, Any] = {
                "title": clean_text(row[COL_TITLE]),
                "submission_id": submission_id,
                "url": url,
                "team": [],
                "_sort_total_score": None,
            }

            if score is not None:
                project["_sort_total_score"] = score
            elif not pd.isna(total_score):
                project["_sort_total_score"] = float(total_score)

            video_url = clean_text(row[COL_VIDEO_URL])
            if has_response(row[COL_VIDEO_PERMISSION]) and video_url:
                project["video"] = video_url

            award = award_for_url(url)
            if award:
                project["award"] = award

            grouped_projects[submission_id] = project

        student_name = clean_text(row[COL_STUDENT_NAME])
        if student_name and student_name not in grouped_projects[submission_id]["team"]:
            grouped_projects[submission_id]["team"].append(student_name)

    projects = list(grouped_projects.values())
    projects.sort(key=sort_key)

    for project in projects:
        project.pop("_sort_total_score", None)

    return projects


def write_projects(projects: list[dict[str, Any]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        yaml.dump(
            projects,
            f,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
        )


def write_thumbnails(
    projects: list[dict[str, Any]], export_dir: Path, thumbnail_dir: Path
) -> list[int]:
    missing_thumbnail_ids = []

    for project in projects:
        submission_id = int(project["submission_id"])
        source_path = find_submission_file(export_dir, submission_id)
        if source_path is None:
            missing_thumbnail_ids.append(submission_id)
            continue

        output_path = thumbnail_dir / str(submission_id) / "image.png"
        save_thumbnail(source_path, output_path)

    return missing_thumbnail_ids


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build showcase YAML and thumbnails from a Gradescope export."
    )
    parser.add_argument("export_dir", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("_data/projects.yml"),
        help="Path to write project YAML.",
    )
    parser.add_argument(
        "--thumbnails",
        type=Path,
        default=Path("assets/showcase-thumbnails"),
        help="Directory to write standardized thumbnails.",
    )
    parser.add_argument(
        "--score-csv",
        type=Path,
        help="Optional score CSV with Assignment Submission ID and Score columns.",
    )
    args = parser.parse_args()

    export_dir = args.export_dir.expanduser().resolve()
    metadata_path = export_dir / "submission_metadata.csv"
    if not metadata_path.is_file():
        raise FileNotFoundError(f"Missing metadata CSV: {metadata_path}")

    score_csv_path = args.score_csv.expanduser().resolve() if args.score_csv else None
    scores_by_submission_id = load_scores(score_csv_path)

    df = pd.read_csv(metadata_path)
    projects = build_projects(df, scores_by_submission_id)
    write_projects(projects, args.output)
    missing_thumbnail_ids = write_thumbnails(projects, export_dir, args.thumbnails)

    video_count = sum(1 for project in projects if "video" in project)
    award_count = sum(1 for project in projects if "award" in project)
    print(f"Wrote {len(projects)} projects to {args.output}")
    print(f"Wrote thumbnails to {args.thumbnails}")
    print(f"Included {video_count} video links and {award_count} award badges")
    if missing_thumbnail_ids:
        missing = ", ".join(str(submission_id) for submission_id in missing_thumbnail_ids)
        print(f"Missing thumbnails for submission IDs: {missing}")


if __name__ == "__main__":
    main()
